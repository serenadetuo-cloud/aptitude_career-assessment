import React, { useRef, useState, useMemo } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAssessmentStore } from '../store/assessmentStore';
import { Radar, RadarChart, PolarGrid, PolarAngleAxis, ResponsiveContainer } from 'recharts';
import { Dimension } from '../types';
import { ChevronRight, Download, MessageCircle, Star, CheckCircle2, Lightbulb, Trophy } from 'lucide-react';
import { toJpeg } from 'html-to-image';

// @ts-ignore - Recharts type compatibility issue
const Chart = RadarChart as any;

const DIMENSION_LABELS: Record<Dimension, string> = {
  商业服务: '商业服务',
  医疗健康: '医疗健康',
  教育培训: '教育培训',
  文化艺术: '文化艺术',
  工程制造: '工程制造',
  公共服务: '公共服务',
  科研创新: '科研创新',
  自主创业: '自主创业',
};

export const ResultPage: React.FC = () => {
  const { result, engine, reset } = useAssessmentStore();
  const [expandedJob, setExpandedJob] = useState<number | null>(null);
  const [posterImage, setPosterImage] = useState<string | null>(null);
  const [isGenerating, setIsGenerating] = useState(false);
  const [showWechatModal, setShowWechatModal] = useState(false);
  const reportRef = useRef<HTMLDivElement>(null);

  // 随机选择1位前辈（遍历所有推荐岗位,找到第一个有有效mentor的）
  const randomMentor = useMemo(() => {
    if (!result || !result.topJobs || result.topJobs.length === 0) return null;

    // 遍历所有推荐岗位,找到第一个有mentor的
    for (const jobMatch of result.topJobs) {
      const allMentors = engine.getMentorsByIds(jobMatch.job.mentorIds);
      if (allMentors && allMentors.length > 0) {
        return allMentors[Math.floor(Math.random() * allMentors.length)];
      }
    }

    return null;
  }, [result, engine]);

  if (!result) return null;

  const resultTypeObj = engine.getResultTypeObject(result.dimensionScores, result.topJobs);
  const typicalProfile = resultTypeObj?.typicalProfile || '';
  const coreTraits = resultTypeObj?.coreTraits || [];

  // 使用动态生成的内容,而不是从resultTypeObj读取
  const strengths = engine.generateDynamicStrengths(result.dimensionScores, result.topJobs);
  const weaknesses = engine.generateDynamicWeaknesses(result.dimensionScores, result.topJobs);
  const actionPlan = engine.generateDynamicActionPlan(result.dimensionScores, result.topJobs);
  const cta = engine.generateDynamicCTA(result.dimensionScores, result.topJobs);

  const radarData = Object.entries(result.dimensionScores).map(([dimension, score]) => ({
    dimension: DIMENSION_LABELS[dimension as Dimension],
    score,
    fullMark: 100,
  }));

  const sortedDimensions = Object.entries(result.dimensionScores)
    .sort(([, a], [, b]) => b - a)
    .slice(0, 3);

  const maxScore = Math.max(...Object.values(result.dimensionScores));
  const minScore = Math.min(...Object.values(result.dimensionScores));
  const percentile = Math.min(95, Math.round(50 + (maxScore / 100) * 45));

  // 生成雷达图总结
  const generateRadarSummary = () => {
    const top3 = sortedDimensions.map(([dim]) => DIMENSION_LABELS[dim as Dimension]);
    const scoreRange = maxScore - minScore;

    if (scoreRange < 20) {
      return `你的各维度发展较为均衡，整体得分在 ${minScore}-${maxScore} 分之间`;
    } else if (maxScore >= 80 && sortedDimensions.length >= 2 && sortedDimensions[1][1] >= 80) {
      // 多个维度都很高(80+)
      const highScoreDimensions = sortedDimensions.filter(([, score]) => score >= 80);
      if (highScoreDimensions.length >= 3) {
        return `你在 ${highScoreDimensions.slice(0, 3).map(([dim]) => DIMENSION_LABELS[dim as Dimension]).join('、')} 等多个维度表现优异，得分均在 80 分以上，展现出综合发展潜力`;
      } else {
        return `你在 ${highScoreDimensions.map(([dim]) => DIMENSION_LABELS[dim as Dimension]).join('、')} 维度表现突出，得分分别为 ${highScoreDimensions.map(([, score]) => score).join('、')} 分`;
      }
    } else if (maxScore >= 80) {
      return `你在 ${top3[0]} 维度表现突出（${maxScore}分），展现出专家级潜力`;
    } else {
      return `你在 ${top3.slice(0, 2).join('、')} 维度表现较强，得分分别为 ${sortedDimensions[0][1]}、${sortedDimensions[1][1]} 分`;
    }
  };

  const handleDownloadImage = async () => {
    if (!reportRef.current) return;
    setIsGenerating(true);

    // 添加导出模式的CSS类
    reportRef.current.classList.add('export-mode');

    try {
      // 等待CSS生效
      await new Promise(resolve => setTimeout(resolve, 100));

      const dataUrl = await toJpeg(reportRef.current, {
        quality: 0.9,
        backgroundColor: '#0F172A',
        pixelRatio: 2,
      });
      setPosterImage(dataUrl);
    } catch (e) {
      console.error('生成海报失败', e);
      alert('生成海报失败，建议直接截图保存');
    } finally {
      // 移除CSS类
      if (reportRef.current) {
        reportRef.current.classList.remove('export-mode');
      }
      setIsGenerating(false);
    }
  };

  // 第一个推荐岗位
  const topJob = result.topJobs[0];
  const whyFitTop = topJob ? engine.generateWhyFit(topJob.job, result.dimensionScores) : '';

  return (
    <motion.div
      initial={{ opacity: 0, x: 20 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -20 }}
      className="min-h-screen bg-[#0F172A] pb-24"
    >
      <div ref={reportRef} className="bg-gradient-to-br from-indigo-900/40 via-purple-900/20 to-[#0F172A] relative overflow-hidden">
        {/* Dark Header */}
        <div className="relative px-6 pt-12 pb-16 flex flex-col items-center">
          {/* Background effects */}
          <div className="absolute top-20 right-[-10%] w-72 h-72 bg-indigo-600/30 rounded-full blur-[100px]" />
          <div className="absolute top-40 left-[-10%] w-72 h-72 bg-purple-600/20 rounded-full blur-[100px]" />

          {/* Header Info */}
          <div className="w-full max-w-2xl mx-auto flex justify-between items-center mb-12 relative z-10">
            <div className="text-white">
              <p className="text-[10px] font-black tracking-widest text-indigo-400 uppercase mb-1">Career Navigator</p>
              <div className="flex items-center gap-1.5 font-black text-xs text-white">
                <span className="w-2.5 h-2.5 rounded-full bg-indigo-500 animate-pulse shadow-[0_0_8px_rgba(99,102,241,0.8)]" />
                深层评估完成
              </div>
            </div>
            <div className="text-white/30 text-[10px] font-mono text-right">
              #2026_REPORT<br />
              IDX: {Math.random().toString(36).substring(7).toUpperCase()}
            </div>
          </div>

          {/* Avatar & Type */}
          <div className="relative mb-8 group z-10">
            <motion.div
              initial={{ scale: 0.8, rotate: -5 }}
              animate={{ scale: 1, rotate: 0 }}
              className="w-48 h-48 rounded-[40px] overflow-hidden border-4 border-white/10 shadow-2xl bg-gradient-to-br from-indigo-500 to-purple-600 flex items-center justify-center text-6xl"
            >
              🎯
            </motion.div>
            <div className="absolute -bottom-4 -right-10 bg-indigo-600 text-white px-5 py-3 rounded-[20px] shadow-xl z-20 font-black text-sm rotate-6 whitespace-nowrap border border-white/20">
              核心契合度 {percentile}%
            </div>
          </div>

          <div className="text-center space-y-4 mb-10 mt-6 relative z-10 px-4 max-w-2xl mx-auto">
            <motion.h2
              initial={{ y: 20, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ delay: 0.2 }}
              className="text-4xl font-black text-white tracking-tighter"
            >
              {result.resultType}
            </motion.h2>
            {typicalProfile && (
              <motion.p
                initial={{ y: 20, opacity: 0 }}
                animate={{ y: 0, opacity: 1 }}
                transition={{ delay: 0.3 }}
                className="text-base text-white/80 leading-relaxed max-w-xl mx-auto"
              >
                {typicalProfile}
              </motion.p>
            )}
          </div>

          {coreTraits.length > 0 && (
            <div className="flex flex-wrap justify-center gap-2.5 mb-14 px-6 relative z-10 max-w-2xl mx-auto">
              {coreTraits.map((trait: string, idx: number) => (
                <span key={idx} className="px-5 py-2.5 bg-white/5 border border-white/10 rounded-full text-white/90 text-xs font-bold tracking-widest uppercase backdrop-blur-md">
                  #{trait}
                </span>
              ))}
            </div>
          )}

          {/* Radar Chart */}
          <div className="w-full max-w-2xl mx-auto bg-white/5 backdrop-blur-md rounded-[40px] p-8 border border-white/10 mb-8 relative z-10">
            <div className="text-center mb-6">
              <h3 className="font-black text-[11px] text-gray-400 uppercase tracking-[0.2em] mb-3">核心潜力维度分布</h3>
              <div className="h-1.5 w-12 bg-indigo-500 mx-auto rounded-full" />
            </div>

            <div className="h-[300px] w-full">
              <ResponsiveContainer width="100%" height="100%">
                <Chart data={radarData}>
                  <PolarGrid stroke="#334155" />
                  {/* @ts-ignore */}
                  <PolarAngleAxis
                    dataKey="dimension"
                    tick={({ payload, x, y, textAnchor, index }: any) => {
                      const yPos = typeof y === 'number' ? y : 0;
                      return (
                        <g>
                          <text x={x} y={yPos} textAnchor={textAnchor} fill="#94A3B8" fontSize={10} fontWeight={900}>
                            {payload.value}
                          </text>
                          <text x={x} y={yPos + 12} textAnchor={textAnchor} fill="#6366F1" fontSize={9} fontWeight={900}>
                            {radarData[index].score} pts
                          </text>
                        </g>
                      );
                    }}
                  />
                  <Radar
                    name="得分"
                    dataKey="score"
                    stroke="#6366F1"
                    fill="#6366F1"
                    fillOpacity={0.2}
                    strokeWidth={3}
                  />
                </Chart>
              </ResponsiveContainer>
            </div>

            <div className="mt-6 text-center px-4">
              <p className="text-sm text-white/70 leading-relaxed">
                {generateRadarSummary()}
              </p>
            </div>
          </div>

          {/* Celebrity */}
          {randomMentor && (
            <div className="w-full max-w-2xl mx-auto bg-gradient-to-br from-indigo-600 to-purple-600 rounded-[40px] p-8 text-white relative overflow-hidden shadow-lg shadow-indigo-600/30 z-10 mb-8">
              <div className="absolute top-[-20%] right-[-10%] w-48 h-48 bg-white/20 rounded-full blur-3xl" />
              <div className="absolute bottom-[-10%] left-[-10%] w-32 h-32 bg-purple-500/30 rounded-full blur-2xl" />

              <div className="relative z-10">
                <div className="text-center mb-10">
                  <h3 className="text-3xl font-black text-white mb-2">你的职场前辈</h3>
                  <div className="text-xs text-white/50 uppercase tracking-widest">CAREER PREDECESSOR</div>
                </div>

                <div>
                  <div className="flex flex-col items-center gap-4 mb-6">
                    <div className="w-32 h-32 rounded-full overflow-hidden border-4 border-white/30 shrink-0 bg-white/10 shadow-xl">
                      <div className="w-full h-full bg-gradient-to-br from-indigo-400 to-purple-500 flex items-center justify-center text-5xl">
                        👤
                      </div>
                    </div>
                    <div className="text-center">
                      <h4 className="text-2xl font-black text-white mb-2">{randomMentor.name}</h4>
                      <p className="text-base text-white/80 font-bold">{randomMentor.title}</p>
                    </div>
                  </div>

                  <div className="bg-white/10 backdrop-blur-sm rounded-[24px] p-6 mb-4">
                    <p className="text-base leading-relaxed text-white/95 italic">
                      "{randomMentor.quote}"
                    </p>
                    <p className="text-sm text-white/70 text-right mt-3">
                      —— {randomMentor.name}{randomMentor.englishName ? ` (${randomMentor.englishName})` : ''}
                    </p>
                  </div>

                  <div className="mb-4">
                    <p className="text-sm text-white/90 leading-relaxed">{randomMentor.story}</p>
                  </div>

                  <div>
                    <div className="text-xs font-black text-white/60 uppercase tracking-wider mb-3">核心能力</div>
                    <div className="flex flex-wrap gap-2">
                      {randomMentor.coreAbilities.map((ability, i) => (
                        <span key={i} className="px-4 py-2 bg-white/20 backdrop-blur-sm rounded-full text-sm font-bold text-white border border-white/30">
                          {ability}
                        </span>
                      ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Main Content */}
        <div className="relative z-10 px-6 pt-12 pb-8 max-w-2xl mx-auto">
          {/* Job Recommendations */}
          <div className="mb-12">
            <div className="flex items-center gap-3 mb-8 bg-white/5 py-3 px-5 rounded-2xl border border-white/10">
              <div className="w-10 h-10 rounded-2xl bg-indigo-600/20 flex items-center justify-center text-indigo-400 border border-indigo-500/30">
                <Trophy size={20} />
              </div>
              <h3 className="text-[22px] font-black text-white">
                <span className="hide-in-export">TOP 3 推荐职业方向</span>
                <span className="show-in-export hidden">最推荐的职业方向</span>
              </h3>
            </div>

            <div className="space-y-6">
              {result.topJobs.slice(0, 3).map((jobMatch, i) => {
                const isExpanded = expandedJob === i;
                const whyFit = engine.generateWhyFit(jobMatch.job, result.dimensionScores);

                return (
                  <motion.div
                    key={jobMatch.job.jobId}
                    onClick={() => setExpandedJob(isExpanded ? null : i)}
                    className={`bg-white/5 backdrop-blur-md rounded-[28px] border border-white/10 cursor-pointer hover:border-indigo-500/50 transition-all ${i > 0 ? 'hide-in-export' : ''}`}
                    data-job-index={i}
                  >
                    <div className="flex items-center justify-between p-6">
                      <div className="flex items-center gap-5">
                        <div className="text-xs font-black text-gray-600">0{i + 1}</div>
                        <div>
                          <div className="font-black text-[17px] text-white">{jobMatch.job.jobName}</div>
                          <div className="flex items-center gap-3 mt-1.5">
                            <div className="flex gap-0.5">
                              {Array.from({ length: 5 }).map((_, s) => (
                                <Star key={s} size={10} fill={s < 4 ? '#6366F1' : 'none'} stroke={s < 4 ? '#6366F1' : '#475569'} />
                              ))}
                            </div>
                            <span className="text-[10px] font-black text-indigo-400 tracking-wider uppercase">匹配度 {jobMatch.matchScore}%</span>
                          </div>
                        </div>
                      </div>
                      <div className={`w-10 h-10 rounded-full bg-white/5 flex items-center justify-center text-gray-400 transition-all ${isExpanded ? 'bg-indigo-600 text-white rotate-90' : ''}`}>
                        <ChevronRight size={16} />
                      </div>
                    </div>

                    <AnimatePresence>
                      {isExpanded && (
                        <motion.div
                          initial={{ height: 0, opacity: 0 }}
                          animate={{ height: 'auto', opacity: 1 }}
                          exit={{ height: 0, opacity: 0 }}
                          className="overflow-hidden job-details"
                        >
                          <div className="px-6 pb-6 space-y-4">
                            <div className="text-[13.5px] text-gray-300 leading-relaxed">
                              <span className="font-black text-white block mb-1.5">岗位速写</span>
                              {jobMatch.job.jobDescription}
                            </div>
                            {/* 只在有具体内容时显示"典型的一天"，过滤掉通用模板 */}
                            {jobMatch.job.typicalDay.length > 0 &&
                             !jobMatch.job.typicalDay.some((activity: any) =>
                               typeof activity === 'string' && activity.includes('查看工作安排，处理优先事项')
                             ) && (
                              <div className="text-[13.5px] text-indigo-300 leading-relaxed bg-indigo-600/10 p-5 rounded-[20px] border border-indigo-500/20">
                                <span className="font-black text-indigo-400 block mb-1.5">典型的一天</span>
                                {jobMatch.job.typicalDay.map((activity, idx) => (
                                  <div key={idx} className="text-xs mb-1">• {activity.time} {activity.activity}</div>
                                ))}
                              </div>
                            )}
                            <div className="text-[13.5px] text-purple-300 leading-relaxed bg-purple-600/10 p-5 rounded-[20px] border border-purple-500/20">
                              <span className="font-black text-purple-400 block mb-1.5">为什么适合你</span>
                              {whyFit}
                            </div>

                            {/* 职业发展路径与薪资 */}
                            <div className="text-[13.5px] text-gray-300">
                              <span className="font-black text-white block mb-3">职业发展路径与薪资</span>
                              <div className="grid grid-cols-3 gap-3">
                                {[
                                  {
                                    stage: jobMatch.job.careerPath.junior,
                                    label: '初级阶段',
                                    salary: jobMatch.job.salaryRange.freshGraduate
                                  },
                                  {
                                    stage: jobMatch.job.careerPath.mid,
                                    label: '中级阶段',
                                    salary: jobMatch.job.salaryRange.experienced_3y
                                  },
                                  {
                                    stage: jobMatch.job.careerPath.senior,
                                    label: '高级阶段',
                                    salary: jobMatch.job.salaryRange.experienced_5y
                                  }
                                ].map((item, idx) => {
                                  const salaryData = Object.values(item.salary)[0] as any;
                                  const minYear = Math.round(salaryData.min / 10000);
                                  const maxYear = Math.round(salaryData.max / 10000);
                                  const minMonth = Math.round(salaryData.min / 12 / 1000);
                                  const maxMonth = Math.round(salaryData.max / 12 / 1000);

                                  return (
                                    <div key={idx} className="bg-white/5 p-4 rounded-xl border border-white/10">
                                      <div className="font-bold text-white text-sm mb-2">{item.label}</div>
                                      <div className="text-xs text-gray-400 mb-2">{item.stage.duration}</div>
                                      <div className="text-xs text-gray-300 mb-3">
                                        {item.stage.positions.join(' / ')}
                                      </div>
                                      <div className="text-xs text-indigo-400 font-semibold border-t border-white/10 pt-3">
                                        <div>月薪：{minMonth}-{maxMonth}k</div>
                                        <div>年薪：{minYear}-{maxYear}万</div>
                                      </div>
                                    </div>
                                  );
                                })}
                              </div>
                            </div>
                          </div>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </motion.div>
                );
              })}
            </div>
          </div>

          {/* Pros */}
          <div className="mb-12 hide-in-export">
            <div className="flex items-center gap-3 mb-6 bg-white/5 py-3 px-5 rounded-2xl border border-white/10">
              <div className="w-10 h-10 rounded-2xl bg-emerald-600/20 flex items-center justify-center text-emerald-400 border border-emerald-500/30">
                <CheckCircle2 size={20} />
              </div>
              <h3 className="text-[22px] font-black text-white">你的职业优势</h3>
            </div>
            <div className="space-y-4">
              {strengths.length > 0 ? strengths.map((strength: any, i: number) => (
                <div key={i} className="bg-emerald-600/10 rounded-[28px] p-6 border border-emerald-500/20">
                  <div className="font-black text-white mb-1.5 text-[15px]">优势 {i + 1}：{strength.title}</div>
                  <div className="text-[13px] text-gray-300 leading-relaxed mb-3">{strength.description}</div>
                  {strength.example && (
                    <>
                      <div className="text-[10px] font-black text-emerald-400 uppercase tracking-wider mb-2">场景举例</div>
                      <div className="text-[12px] text-gray-400 leading-relaxed">{strength.example}</div>
                    </>
                  )}
                </div>
              )) : (
                <div className="bg-emerald-600/10 rounded-[28px] p-6 border border-emerald-500/20">
                  <div className="text-[13px] text-emerald-300/80 leading-relaxed">根据你的测评结果，我们正在为你生成个性化的职业优势分析...</div>
                </div>
              )}
            </div>
          </div>

          {/* Cons */}
          <div className="mb-12 hide-in-export">
            <div className="flex items-center gap-3 mb-6 bg-white/5 py-3 px-5 rounded-2xl border border-white/10">
              <div className="w-10 h-10 rounded-2xl bg-amber-600/20 flex items-center justify-center text-amber-400 border border-amber-500/30">
                <Lightbulb size={20} />
              </div>
              <h3 className="text-[22px] font-black text-white">需要注意的短板</h3>
            </div>
            <div className="space-y-4">
              {weaknesses.length > 0 ? weaknesses.map((weakness: any, i: number) => (
                <div key={i} className="bg-white/5 rounded-[28px] p-6 border border-white/10">
                  <div className="font-black text-amber-400 mb-2 text-[15px]">短板 {i + 1}：{weakness.title}</div>
                  <div className="text-[13px] text-gray-300 leading-relaxed mb-4">{weakness.description}</div>
                  {weakness.improvements && weakness.improvements.length > 0 && (
                    <>
                      <div className="text-[10px] font-black text-amber-400 uppercase tracking-wider mb-2">如何改进</div>
                      <div className="text-[12px] text-gray-400">
                        {weakness.improvements.map((improvement: string, idx: number) => (
                          <div key={idx}>• {improvement}</div>
                        ))}
                      </div>
                    </>
                  )}
                </div>
              )) : (
                <div className="bg-white/5 rounded-[28px] p-6 border border-white/10">
                  <div className="text-[13px] text-gray-300 leading-relaxed">根据你的测评结果，我们正在为你生成个性化的短板分析...</div>
                </div>
              )}
            </div>
          </div>

          {/* Action Plan */}
          <div className="mb-12 hide-in-export">
            <div className="flex items-center gap-3 mb-6 bg-white/5 py-3 px-5 rounded-2xl border border-white/10">
              <div className="w-10 h-10 rounded-2xl bg-indigo-600 flex items-center justify-center text-white">
                <Trophy size={20} />
              </div>
              <h3 className="text-[22px] font-black text-white">你的求职行动计划</h3>
            </div>
            <div className="space-y-8">
              {actionPlan.shortTerm && actionPlan.shortTerm.length > 0 && (
                <div>
                  <div className="px-4 py-1.5 bg-indigo-600 text-white rounded-full text-xs font-black mb-4 inline-block">近期（1-3个月）</div>
                  <div className="space-y-3">
                    {actionPlan.shortTerm.map((item: any, idx: number) => (
                      <div key={idx} className="bg-white/5 rounded-[20px] p-5 border border-white/10">
                        <h4 className="font-black text-white mb-2">{idx + 1}. {item.step}</h4>
                        <div className="text-sm text-gray-300 whitespace-pre-line">{item.details}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {actionPlan.midTerm && actionPlan.midTerm.length > 0 && (
                <div>
                  <div className="px-4 py-1.5 bg-purple-600 text-white rounded-full text-xs font-black mb-4 inline-block">中期（3-6个月）</div>
                  <div className="space-y-3">
                    {actionPlan.midTerm.map((item: any, idx: number) => (
                      <div key={idx} className="bg-white/5 rounded-[20px] p-5 border border-white/10">
                        <h4 className="font-black text-white mb-2">{actionPlan.shortTerm.length + idx + 1}. {item.step}</h4>
                        <div className="text-sm text-gray-300 whitespace-pre-line">{item.details}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
              {(!actionPlan.shortTerm || actionPlan.shortTerm.length === 0) && (!actionPlan.midTerm || actionPlan.midTerm.length === 0) && (
                <div className="bg-white/5 rounded-[20px] p-5 border border-white/10">
                  <div className="text-sm text-gray-300">根据你的测评结果，我们正在为你生成个性化的求职行动计划...</div>
                </div>
              )}
            </div>
          </div>

          {/* CTA */}
          {cta && (
            <div className="bg-gradient-to-br from-indigo-600 to-purple-600 rounded-[40px] p-10 text-white relative overflow-hidden hide-in-export">
              <div className="absolute top-0 right-0 w-40 h-40 bg-white/10 rounded-full blur-[50px]" />
              <div className="relative z-10">
                <h3 className="text-2xl font-black mb-6">你可能正在纠结：</h3>
                <div className="text-left space-y-2 mb-8 text-white/90">
                  {cta.concerns.map((concern: string, idx: number) => (
                    <div key={idx}>• {concern}</div>
                  ))}
                </div>

                <h3 className="text-xl font-black mb-4">我们能帮你：</h3>
                <div className="text-left space-y-2 mb-6 text-white/90 text-sm">
                  <div>👉 添加职业规划师微信，免费领取：</div>
                  {cta.benefits.map((benefit: string, idx: number) => (
                    <div key={idx} className="ml-6">• {benefit}</div>
                  ))}
                </div>

                <div className="bg-white p-3 rounded-[24px] w-32 h-32 mx-auto mt-6">
                  <img
                    src="/images/wechat-qr.jpg"
                    alt="微信二维码"
                    className="w-full h-full object-cover rounded-xl"
                  />
                </div>
                <p className="text-white/70 text-xs mt-3">扫码添加职业规划师微信</p>
              </div>
            </div>
          )}

          {/* QR Code Section - Only show in export - Taobao style bottom bar */}
          <div className="hidden show-in-export mt-8">
            <div className="relative bg-white rounded-[24px] p-6 shadow-lg">
              <div className="flex items-center justify-between gap-4">
                <div className="flex-1">
                  <p className="text-base font-black text-gray-900 mb-1">发现你的职业可能性</p>
                  <p className="text-sm text-gray-600">扫码开始职向力测评</p>
                </div>
                <div className="flex-shrink-0">
                  <img
                    src={`https://api.qrserver.com/v1/create-qr-code/?size=100x100&data=${encodeURIComponent(typeof window !== 'undefined' ? window.location.origin : 'https://example.com')}`}
                    alt="测评二维码"
                    className="w-20 h-20 rounded-lg"
                    crossOrigin="anonymous"
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Actions */}
      <div className="px-6 py-6 max-w-2xl mx-auto">
        <button
          onClick={reset}
          className="w-full bg-white/5 border border-white/10 py-4 rounded-[24px] font-bold text-white hover:bg-white/10 transition-all mb-4"
        >
          重新测评
        </button>
      </div>

      {/* Fixed Bottom Bar */}
      <div className="fixed bottom-0 left-0 right-0 p-4 bg-[#0F172A]/90 backdrop-blur-2xl border-t border-white/10 flex gap-3 z-50 max-w-2xl mx-auto">
        <button
          onClick={handleDownloadImage}
          disabled={isGenerating}
          className="flex-shrink-0 w-16 h-16 flex items-center justify-center bg-white/5 rounded-[20px] text-white hover:bg-white/10 transition-colors border border-white/10 disabled:opacity-50"
        >
          <Download size={24} />
        </button>
        <button
          onClick={() => setShowWechatModal(true)}
          className="flex-1 bg-indigo-600 text-white rounded-[20px] font-black text-sm uppercase flex items-center justify-center gap-2 shadow-xl shadow-indigo-600/30 hover:bg-indigo-700 transition-all"
        >
          <MessageCircle size={18} />
          1v1 深度求职规划
        </button>
      </div>

      {/* Image Preview Modal */}
      {posterImage && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[100] bg-black/90 flex flex-col items-center justify-center p-6 backdrop-blur-sm"
          onClick={() => setPosterImage(null)}
        >
          <p className="text-white font-bold mb-4 flex items-center gap-2">
            <Download size={20} />
            长按图片保存
          </p>
          <div className="relative w-full max-w-sm max-h-[75vh] overflow-y-auto rounded-xl shadow-2xl scrollbar-hide" onClick={e => e.stopPropagation()}>
            <img src={posterImage} alt="测评海报" className="w-full h-auto rounded-xl" />
          </div>
          <button
            className="mt-6 px-8 py-3 bg-white/20 text-white rounded-full font-bold backdrop-blur-md hover:bg-white/30 transition"
            onClick={() => setPosterImage(null)}
          >
            关闭预览
          </button>
        </motion.div>
      )}

      {/* WeChat QR Code Modal */}
      {showWechatModal && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-[100] bg-black/90 flex items-center justify-center p-6 backdrop-blur-sm"
          onClick={() => setShowWechatModal(false)}
        >
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            exit={{ scale: 0.9, opacity: 0 }}
            className="bg-gradient-to-br from-indigo-900/90 to-purple-900/90 backdrop-blur-xl rounded-[32px] p-8 max-w-sm w-full border border-white/20 shadow-2xl"
            onClick={e => e.stopPropagation()}
          >
            <div className="text-center">
              <h3 className="text-2xl font-black text-white mb-3">1v1 深度求职规划</h3>
              <p className="text-sm text-white/70 mb-6">添加职业规划师微信，获取专属求职指导</p>

              <div className="bg-white p-4 rounded-[24px] mb-6">
                <img
                  src="/images/IMG_0429.JPG"
                  alt="微信二维码"
                  className="w-full h-auto rounded-xl"
                  onError={(e) => {
                    e.currentTarget.style.display = 'none';
                    const parent = e.currentTarget.parentElement;
                    if (parent) {
                      parent.innerHTML = '<div class="w-full h-64 flex items-center justify-center text-gray-500 text-sm">二维码加载失败</div>';
                    }
                  }}
                />
              </div>

              <p className="text-xs text-white/60 mb-6">扫码添加微信，开启你的职业规划之旅</p>

              <button
                className="w-full py-3 bg-white/20 text-white rounded-[20px] font-bold backdrop-blur-md hover:bg-white/30 transition"
                onClick={() => setShowWechatModal(false)}
              >
                关闭
              </button>
            </div>
          </motion.div>
        </motion.div>
      )}
    </motion.div>
  );
};
