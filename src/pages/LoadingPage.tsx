import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles } from 'lucide-react';

export const LoadingPage: React.FC = () => {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="min-h-screen bg-[#0F172A] flex flex-col items-center justify-center p-6 text-center space-y-8 relative overflow-hidden"
    >
      {/* Background gradient effects */}
      <div className="absolute top-[-10%] right-[-10%] w-80 h-80 bg-indigo-600/20 rounded-full blur-3xl" />
      <div className="absolute bottom-[-10%] left-[-10%] w-80 h-80 bg-purple-600/20 rounded-full blur-3xl" />

      <div className="relative z-10 flex flex-col items-center">
        <div className="relative w-24 h-24 mb-8 mx-auto">
          <motion.div
            animate={{ rotate: 360 }}
            transition={{ repeat: Infinity, duration: 2, ease: "linear" }}
            className="absolute inset-0 border-4 border-white/10 border-t-indigo-500 rounded-full"
          />
          <div className="absolute inset-0 flex items-center justify-center">
            <Sparkles className="text-indigo-500" size={32} />
          </div>
        </div>

        <div className="space-y-2 mb-8">
          <h2 className="text-2xl font-bold text-white">正在生成深度测评报告...</h2>
          <p className="text-gray-400">正在匹配职业模型与岗位数据</p>
        </div>

        <div className="w-full max-w-xs mx-auto">
          <div className="h-2 bg-white/10 rounded-full overflow-hidden">
            <motion.div
              initial={{ width: 0 }}
              animate={{ width: "100%" }}
              transition={{ duration: 1.5, ease: "easeInOut" }}
              className="h-full bg-indigo-600 shadow-[0_0_12px_rgba(99,102,241,0.6)]"
            />
          </div>
        </div>
      </div>
    </motion.div>
  );
};
