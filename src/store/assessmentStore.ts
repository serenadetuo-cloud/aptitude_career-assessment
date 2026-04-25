import { create } from 'zustand';
import {
  Question,
  UserAnswer,
  MajorTag,
  AssessmentResult,
} from '../types';
import { AssessmentEngine } from '../engine/AssessmentEngine';

interface AssessmentState {
  // 数据
  engine: AssessmentEngine;
  questions: Question[];

  // 用户状态
  currentStep: 'major' | 'questions' | 'loading' | 'result';
  currentQuestionIndex: number;
  userMajors: MajorTag[];
  userAnswers: UserAnswer[];

  // 结果
  result: AssessmentResult | null;

  // 操作
  initialize: () => Promise<void>;
  selectMajors: (majors: MajorTag[]) => void;
  answerQuestion: (questionId: number, optionId: string) => void;
  setCurrentQuestionIndex: (index: number) => void;
  calculateResult: () => void;
  reset: () => void;
}

export const useAssessmentStore = create<AssessmentState>((set, get) => ({
  engine: new AssessmentEngine(),
  questions: [],
  currentStep: 'major',
  currentQuestionIndex: 0,
  userMajors: [],
  userAnswers: [],
  result: null,

  initialize: async () => {
    const { engine } = get();
    await engine.loadData();
    const questions = engine.getQuestions().filter((q) => q.questionId > 0);
    set({ questions });
  },

  selectMajors: (majors: MajorTag[]) => {
    const { engine } = get();
    // 根据用户选择的专业重新过滤题目
    const questions = engine.getQuestions(majors).filter((q) => q.questionId > 0);
    set({ userMajors: majors, questions, currentStep: 'questions' });
  },

  answerQuestion: (questionId: number, optionId: string) => {
    const { userAnswers, currentQuestionIndex, questions } = get();

    const newAnswers = [...userAnswers, { questionId, optionId }];
    set({ userAnswers: newAnswers });

    if (currentQuestionIndex < questions.length - 1) {
      set({ currentQuestionIndex: currentQuestionIndex + 1 });
    } else {
      get().calculateResult();
    }
  },

  setCurrentQuestionIndex: (index: number) => {
    set({ currentQuestionIndex: index });
  },

  calculateResult: () => {
    set({ currentStep: 'loading' });

    const { engine, userAnswers, userMajors } = get();

    setTimeout(() => {
      const dimensionScores = engine.calculateScores(userAnswers, userMajors);
      const topJobs = engine.matchJobs(dimensionScores, userMajors, 3);
      const resultType = engine.matchResultType(dimensionScores, topJobs);

      set({
        result: {
          userMajors,
          dimensionScores,
          topJobs,
          resultType,
        },
        currentStep: 'result',
      });
    }, 1500);
  },

  reset: () => {
    set({
      currentStep: 'major',
      currentQuestionIndex: 0,
      userMajors: [],
      userAnswers: [],
      result: null,
    });
  },
}));
