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
      className="min-h-screen bg-[#0F172A] flex items-center justify-center p-4 relative overflow-hidden"
    >
      {/* Background gradient effects */}
      <div className="absolute top-[-10%] right-[-10%] w-80 h-80 bg-indigo-600/20 rounded-full blur-3xl" />
      <div className="absolute bottom-[-10%] left-[-10%] w-80 h-80 bg-purple-600/20 rounded-full blur-3xl" />

      <div className="z-10 max-w-2xl w-full">
        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.2 }}
          className="text-center mb-8"
        >
          <div className="inline-flex items-center gap-2 px-4 py-2 bg-white/5 border border-white/10 rounded-full text-indigo-400 text-xs font-bold tracking-widest uppercase backdrop-blur-sm mb-6">
            <span className="w-2 h-2 rounded-full bg-indigo-500 animate-pulse" />
            职向力测评
          </div>
          <h1 className="text-4xl font-black text-white mb-4 tracking-tight">
            你的专业背景是?
          </h1>
          <p className="text-gray-400 text-lg">可多选,也可以直接开始探索更多可能性</p>
        </motion.div>

        <motion.div
          initial={{ y: 20, opacity: 0 }}
          animate={{ y: 0, opacity: 1 }}
          transition={{ delay: 0.3 }}
          className="bg-white/5 backdrop-blur-md rounded-[32px] p-8 border border-white/10 shadow-2xl"
        >
          <div className="grid grid-cols-3 gap-4 mb-8">
            {MAJOR_OPTIONS.map((option, index) => (
              <motion.button
                key={option.value}
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                transition={{ delay: 0.4 + index * 0.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={() => toggleMajor(option.value)}
                className={`p-6 rounded-[24px] border-2 transition-all ${
                  selected.includes(option.value)
                    ? 'border-indigo-500 bg-indigo-500/20 shadow-lg shadow-indigo-500/20'
                    : 'border-white/10 bg-white/5 hover:border-indigo-500/50 hover:bg-white/10'
                }`}
              >
                <div className="text-4xl mb-2">{option.icon}</div>
                <div className="text-sm font-bold text-white">{option.label}</div>
              </motion.button>
            ))}
          </div>

          <motion.button
            initial={{ y: 20, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ delay: 0.8 }}
            whileTap={{ scale: 0.95 }}
            onClick={handleNext}
            className="w-full py-5 rounded-[24px] font-bold text-lg transition-all bg-indigo-600 text-white hover:bg-indigo-700 shadow-xl shadow-indigo-600/30"
          >
            {selected.length > 0 ? `开始测评 (已选 ${selected.length} 项)` : '探索更多可能性,直接开始'}
          </motion.button>
          {selected.length === 0 && (
            <p className="text-center text-xs text-gray-500 mt-3">
              适合专业不在列表/不想从事对口专业的同学
            </p>
          )}
        </motion.div>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          className="text-center text-xs text-gray-500 mt-6"
        >
          已有 12,482 位同学完成测评，好评率 98%
        </motion.p>
      </div>
    </motion.div>
  );
};
