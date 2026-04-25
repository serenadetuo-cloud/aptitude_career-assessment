import React, { useState } from 'react';
import { motion } from 'framer-motion';
import { Question } from '../types';

interface LikertScaleQuestionProps {
  question: Question;
  onAnswer: (answers: Record<string, string>) => void;
}

export const LikertScaleQuestion: React.FC<LikertScaleQuestionProps> = ({ question, onAnswer }) => {
  const [answers, setAnswers] = useState<Record<string, string>>({});

  const handleScoreSelect = (statementId: string, score: string) => {
    const newAnswers = { ...answers, [statementId]: score };
    setAnswers(newAnswers);

    // 如果所有陈述都已打分,自动提交
    if (question.statements && Object.keys(newAnswers).length === question.statements.length) {
      setTimeout(() => onAnswer(newAnswers), 300);
    }
  };

  const allAnswered = question.statements && Object.keys(answers).length === question.statements.length;

  return (
    <div className="space-y-6">
      <div className="text-xs text-gray-400 text-center mb-4">
        1=非常不符合 → 5=非常符合
      </div>

      {question.statements?.map((statement, index) => (
        <motion.div
          key={statement.statementId}
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.1 }}
          className="bg-white/5 rounded-2xl p-5 border border-white/10"
        >
          <p className="text-sm text-gray-300 mb-4">{statement.statementText}</p>

          <div className="flex justify-between gap-2">
            {[1, 2, 3, 4, 5].map((score) => (
              <button
                key={score}
                onClick={() => handleScoreSelect(statement.statementId, score.toString())}
                className={`flex-1 h-12 rounded-xl text-sm font-bold transition-all ${
                  answers[statement.statementId] === score.toString()
                    ? 'bg-indigo-600 text-white border-2 border-indigo-400 shadow-lg shadow-indigo-600/30'
                    : 'bg-white/5 text-gray-400 border border-white/10 hover:bg-white/10 hover:text-white'
                }`}
              >
                {score}
              </button>
            ))}
          </div>
        </motion.div>
      ))}

      {allAnswered && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="text-center text-xs text-indigo-400 font-bold"
        >
          ✓ 已完成,正在跳转...
        </motion.div>
      )}
    </div>
  );
};
