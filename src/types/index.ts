// 专业背景
export type MajorTag =
  | 'major_medical'
  | 'major_cs'
  | 'major_engineering'
  | 'major_business'
  | 'major_art'
  | 'major_education'
  | 'major_science'
  | 'major_liberal_arts'
  | 'major_open';

// 行业维度
export type Dimension =
  | '商业服务'
  | '医疗健康'
  | '教育培训'
  | '文化艺术'
  | '工程制造'
  | '公共服务'
  | '科研创新'
  | '自主创业';

// 题目选项
export interface QuestionOption {
  optionId: string;
  optionText: string;
  scoring: Record<Dimension, number>;
  majorTag?: MajorTag;
}

// 李克特量表陈述
export interface LikertStatement {
  statementId: string;
  statementText: string;
  scoring: Record<string, Record<Dimension, number>>; // "1" -> {维度: 分数}
}

// 题目
export interface Question {
  questionId: number;
  questionCategory?: string;
  questionText: string;
  questionType: 'single_choice' | 'multiple_choice' | 'likert_scale';
  options?: QuestionOption[];
  statements?: LikertStatement[]; // 李克特量表题使用
  requiredMajors?: string[];  // 专业定向题目需要的专业
}

// 维度得分
export type DimensionScores = Record<Dimension, number>;

// 岗位维度要求
export interface DimensionRequirement {
  weight: number;
  minThreshold: number;
  targetScore: number;
  importance: 'critical' | 'high' | 'medium' | 'low';
}

// 职业发展路径
export interface CareerPath {
  junior: {
    title: string;
    positions: string[];
    duration: string;
  };
  mid: {
    title: string;
    positions: string[];
    duration: string;
  };
  senior: {
    title: string;
    positions: string[];
    duration: string;
  };
}

// 薪资范围
export interface SalaryRange {
  freshGraduate: Record<string, { min: number; max: number; description: string; note?: string }>;
  experienced_3y: Record<string, { min: number; max: number; description: string; note?: string }>;
  experienced_5y: Record<string, { min: number; max: number; description: string; note?: string }>;
}

// 典型一天
export interface TypicalDayActivity {
  time: string;
  activity: string;
}

// 岗位
export interface Job {
  jobId: string;
  jobName: string;
  industry: Dimension;
  category: string;
  professionalBarrier: 'none' | 'low' | 'medium' | 'high';
  requiredMajors: MajorTag[];
  dimensionRequirements: Record<Dimension, DimensionRequirement>;
  mentorIds: string[];
  jobDescription: string;
  typicalDay: TypicalDayActivity[];
  whyFitTemplate: string;
  careerPath: CareerPath;
  salaryRange: SalaryRange;
}

// 职场前辈
export interface CareerMentor {
  mentorId: string;
  name: string;
  englishName?: string;
  avatar: string;
  title: string;
  quote: string;
  story: string;
  coreAbilities: string[];
  applicableJobs: string[];
}

// 岗位匹配结果
export interface JobMatch {
  job: Job;
  matchScore: number;
}

// 用户答题记录
export interface UserAnswer {
  questionId: number;
  optionId: string;
}

// 测评结果
export interface AssessmentResult {
  userMajors: MajorTag[];
  dimensionScores: DimensionScores;
  topJobs: JobMatch[];
  resultType: string;
}
