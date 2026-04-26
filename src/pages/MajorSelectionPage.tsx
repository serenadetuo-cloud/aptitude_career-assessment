import React from 'react';
import { motion } from 'framer-motion';
import { useAssessmentStore } from '../store/assessmentStore';
import { MajorTag } from '../types';

const MAJOR_OPTIONS: { value: MajorTag; label: string; icon: string }[] = [
  { value: 'major_medical', label: '医学', icon: '🏥' },
  { value: 'major_cs', label: '计算机', icon: '💻' },
  { value: 'major_engineering', label: '工程', icon: '⚙️' },
  { value: 'major_business', label: '商科', icon: '💼' },
  { value: 'major_art', label: '艺术', icon: '🎨' },
  { value: 'major_education', label: '教育', icon: '📚' },
  { value: 'major_science', label: '理科', icon: '🔬' },
  { value: 'major_liberal_arts', label: '文科', icon: '📖' },
  { value: 'major_open', label: '法学', icon: '⚖️' },
];

export const MajorSelectionPage: React.FC = () => {
  const [selected, setSelected] = React.useState<MajorTag[]>([]);
  const selectMajors = useAssessmentStore((state) => state.selectMajors);

  const toggleMajor = (major: MajorTag) => {
    setSelected((prev) =>
      prev.includes(major) ? prev.filter((m) => m !== major) : [...prev, major]
    );
  };

  const handleNext = () => {
    // 允许跳过专业选择,如果没选则传空数组
    selectMajors(selected);
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="min-h-screen bg-[#0F172A] flex flex-col justify-between p-4 py-8 relative overflow-hidden"
    >
      {/* Background gradient effects */}
      <div className="absolute top-[-10%] right-[-10%] w-80 h-80 bg-indigo-600/20 rounded-full blur-3xl" />
      <div className="absolute bottom-[-10%] left-[-10%] w-80 h-80 bg-purple-600/20 rounded-full blur-3xl" />

      <div className="z-10 max-w-2xl w-full mx-auto">
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-center mb-4 md:mb-8"
        >
          <div className="inline-flex items-center gap-1.5 px-2.5 py-1 md:px-4 md:py-2 bg-white/5 border border-white/10 rounded-full text-indigo-400 text-[9px] md:text-xs font-bold tracking-widest uppercase backdrop-blur-sm mb-2 md:mb-6">
            <span className="w-1 h-1 md:w-2 md:h-2 rounded-full bg-indigo-500 animate-pulse" />
            职向力测评
          </div>
          <h1 className="text-xl md:text-4xl font-black text-white mb-1.5 md:mb-4 tracking-tight">
            你的专业背景是?
          </h1>
          <p className="text-gray-400 text-xs md:text-lg">可多选,也可以直接开始探索更多可能性</p>
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="bg-white/5 backdrop-blur-md rounded-[20px] md:rounded-[32px] p-3 md:p-8 border border-white/10 shadow-2xl"
        >
          <div className="grid grid-cols-3 gap-2 md:gap-4 mb-3 md:mb-8">
            {MAJOR_OPTIONS.map((option, index) => (
              <motion.button
                key={option.value}
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ delay: 0.4 + index * 0.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => toggleMajor(option.value)}
                className={`p-2 md:p-6 rounded-[12px] md:rounded-[24px] border-2 transition-all ${
                  selected.includes(option.value)
                    ? 'border-indigo-400 bg-indigo-500/40 shadow-lg shadow-indigo-500/30 scale-[1.02]'
                    : 'border-white/10 bg-white/5 hover:border-white/20'
                }`}
              >
                <div className="text-xl md:text-4xl mb-0.5 md:mb-2">{option.icon}</div>
                <div className="text-[10px] md:text-sm font-bold text-white">{option.label}</div>
              </motion.button>
            ))}
          </div>

          <motion.button
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.8 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleNext}
            className="w-full py-3 md:py-5 rounded-[16px] md:rounded-[24px] font-bold text-sm md:text-lg transition-all bg-indigo-600 text-white hover:bg-indigo-700 shadow-xl shadow-indigo-600/30"
          >
            {selected.length > 0 ? `开始测评 (已选 ${selected.length} 项)` : '探索更多可能性,直接开始'}
          </motion.button>
          {selected.length === 0 && (
            <p className="text-center text-[9px] md:text-xs text-gray-500 mt-1.5 md:mt-3">
              适合专业不在列表/不想从事对口专业的同学
            </p>
          )}
        </motion.div>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="text-center text-xs md:text-sm text-gray-500 mt-3 md:mt-6"
        >
          已有 12,482 位同学完成测评，好评率 98%
        </motion.p>
      </div>
    </motion.div>
  );
};
