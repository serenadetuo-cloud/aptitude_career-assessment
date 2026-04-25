import React from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAssessmentStore } from '../store/assessmentStore';
import { ChevronLeft, Shield } from 'lucide-react';
import { LikertScaleQuestion } from '../components/LikertScaleQuestion';

export const QuestionPage: React.FC = () => {
  const { questions, currentQuestionIndex, answerQuestion, setCurrentQuestionIndex } = useAssessmentStore();
  const currentQuestion = questions[currentQuestionIndex];

  if (!currentQuestion) return null;

  const progress = ((currentQuestionIndex + 1) / questions.length) * 100;

  const handlePrevious = () => {
    if (currentQuestionIndex > 0) {
      setCurrentQuestionIndex(currentQuestionIndex - 1);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -20 }}
      className="min-h-screen bg-[#0F172A] p-4 pt-10 flex flex-col relative overflow-hidden"
    >
      {/* Background gradient effects */}
      <div className="absolute top-[-10%] right-[-10%] w-80 h-80 bg-indigo-600/10 rounded-full blur-3xl" />
      <div className="absolute bottom-[-10%] left-[-10%] w-80 h-80 bg-purple-600/10 rounded-full blur-3xl" />

      <div className="max-w-lg mx-auto w-full z-10">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-between mb-4">
            <button
              onClick={handlePrevious}
              className={`w-10 h-10 rounded-full flex items-center justify-center transition-all ${
                currentQuestionIndex > 0
                  ? 'bg-white/10 text-white hover:bg-white/20 border border-white/10'
                  : 'opacity-0 cursor-default'
              }`}
            >
              <ChevronLeft size={20} />
            </button>
            <div className="flex-1 px-8">
              <div className="w-full h-2 bg-white/10 rounded-full overflow-hidden">
                <motion.div
                  initial={{ width: 0 }}
                  animate={{ width: `${progress}%` }}
                  className="h-full bg-indigo-600 shadow-[0_0_12px_rgba(99,102,241,0.6)]"
                />
              </div>
            </div>
            <div className="w-10 text-[10px] font-black text-indigo-400">
              {currentQuestionIndex + 1}/{questions.length}
            </div>
          </div>
          <h2 className="text-xl font-black text-white">核心能力矩阵测评</h2>
          <p className="text-xs text-gray-400 mt-1">请快速根据直觉完成以下题项</p>
        </div>

        {/* Question Card */}
        <div className="flex-1 flex flex-col justify-center pb-24">
          <AnimatePresence mode="wait">
            <motion.div
              key={currentQuestion.questionId}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: -20 }}
              className="bg-white/5 backdrop-blur-md rounded-[32px] p-8 border border-white/10 shadow-2xl"
            >
              <div className="flex items-start gap-4 mb-8">
                <span className="flex-shrink-0 w-8 h-8 rounded-xl bg-indigo-600/20 text-indigo-400 flex items-center justify-center text-xs font-black border border-indigo-500/30">
                  {currentQuestionIndex + 1}
                </span>
                <h3 className="text-lg font-bold text-white leading-tight">
                  {currentQuestion.questionText}
                </h3>
              </div>

              {currentQuestion.questionType === 'likert_scale' ? (
                <LikertScaleQuestion
                  question={currentQuestion}
                  onAnswer={(answers) => {
                    // 李克特量表题一次性提交所有陈述的答案
                    answerQuestion(currentQuestion.questionId, JSON.stringify(answers));
                  }}
                />
              ) : (
                <div className="grid grid-cols-1 gap-3">
                  {currentQuestion.options?.map((opt) => (
                    <motion.button
                      key={`${currentQuestion.questionId}-${opt.optionId}`}
                      whileTap={{ scale: 0.98 }}
                      onClick={() => answerQuestion(currentQuestion.questionId, opt.optionId)}
                      className="group w-full text-left px-6 py-4 rounded-[20px] text-sm font-bold transition-all border flex justify-between items-center bg-white/5 text-gray-300 border-white/10 hover:bg-indigo-600/20 hover:text-white hover:border-indigo-500/50"
                    >
                      <span>{opt.optionText}</span>
                      <div className="w-5 h-5 rounded-full border-2 flex items-center justify-center transition-all border-white/20 group-hover:border-indigo-400">
                        <div className="w-0 h-0 group-hover:w-2.5 group-hover:h-2.5 bg-indigo-400 rounded-full transition-all" />
                      </div>
                    </motion.button>
                  ))}
                </div>
              )}
            </motion.div>
          </AnimatePresence>
        </div>

        {/* Fixed Privacy Notice */}
        <div className="fixed bottom-8 left-0 right-0 text-center text-xs text-gray-500 flex items-center justify-center gap-1 z-50 pointer-events-none">
          <Shield size={14} />
          隐私受保护，仅用于结果生成
        </div>
      </div>
    </motion.div>
  );
};
