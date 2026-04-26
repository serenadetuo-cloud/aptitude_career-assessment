import {
  Question,
  Job,
  UserAnswer,
  DimensionScores,
  Dimension,
  JobMatch,
  MajorTag,
  CareerMentor,
} from '../types';

export class AssessmentEngine {
  private questions: Question[] = [];
  private jobs: Job[] = [];
  private mentors: Map<string, CareerMentor> = new Map();
  private resultTypes: any[] = [];

  async loadData() {
    const baseUrl = process.env.PUBLIC_URL || '';
    const [questionsRes, jobsRes, mentorsRes, resultTypesRes] = await Promise.all([
      fetch(`${baseUrl}/data/questions.json`),
      fetch(`${baseUrl}/data/jobs-database.json`),
      fetch(`${baseUrl}/data/career-mentors.json`),
      fetch(`${baseUrl}/data/result-types.json`),
    ]);

    const questionsData = await questionsRes.json();
    const jobsData = await jobsRes.json();
    const mentorsData = await mentorsRes.json();
    const resultTypesData = await resultTypesRes.json();

    this.questions = questionsData.questions;
    this.jobs = jobsData.jobs;
    this.resultTypes = resultTypesData.resultTypes;

    // 构建前辈 Map
    Object.values(mentorsData.categories).forEach((category: any) => {
      category.mentors.forEach((mentor: CareerMentor) => {
        this.mentors.set(mentor.mentorId, mentor);
      });
    });
  }

  calculateScores(answers: UserAnswer[], userMajors: MajorTag[] = []): DimensionScores {
    const generalScores: DimensionScores = {
      商业服务: 0,
      健康服务: 0,
      教育培训: 0,
      文化艺术: 0,
      工程制造: 0,
      公共服务: 0,
      科研创新: 0,
      自主创业: 0,
    };

    const majorScores: DimensionScores = {
      商业服务: 0,
      健康服务: 0,
      教育培训: 0,
      文化艺术: 0,
      工程制造: 0,
      公共服务: 0,
      科研创新: 0,
      自主创业: 0,
    };

    // 分离通用题和专业定向题的得分
    answers.forEach((answer) => {
      const question = this.questions.find((q) => q.questionId === answer.questionId);
      if (!question) return;

      const isMajorQuestion = question.requiredMajors && question.requiredMajors.length > 0;
      const targetScores = isMajorQuestion ? majorScores : generalScores;

      // 处理李克特量表题
      if (question.questionType === 'likert_scale') {
        try {
          const likertAnswers = JSON.parse(answer.optionId) as Record<string, string>;
          question.statements?.forEach((statement) => {
            const score = likertAnswers[statement.statementId];
            if (score && statement.scoring[score]) {
              Object.entries(statement.scoring[score]).forEach(([dimension, points]) => {
                if (dimension in targetScores) {
                  targetScores[dimension as Dimension] += points;
                }
              });
            }
          });
        } catch (e) {
          console.error('Failed to parse likert scale answer:', e);
        }
      } else {
        // 处理普通单选题
        const option = question.options?.find((opt) => opt.optionId === answer.optionId);
        if (!option) return;

        Object.entries(option.scoring).forEach(([dimension, points]) => {
          if (dimension in targetScores) {
            targetScores[dimension as Dimension] += points;
          }
        });
      }
    });

    // 分别归一化通用题和专业定向题
    const normalizedGeneral = this.normalizeScores(generalScores);
    const normalizedMajor = this.normalizeScores(majorScores);

    // 合并分数:通用题占主导(80%),专业定向题作为校准(20%)
    const combined: DimensionScores = {} as DimensionScores;
    Object.keys(normalizedGeneral).forEach((dim) => {
      const dimension = dim as Dimension;
      const generalScore = normalizedGeneral[dimension];
      const majorScore = normalizedMajor[dimension];

      // 如果用户做了专业定向题,则混合分数;否则只用通用题分数
      if (majorScore > 0) {
        combined[dimension] = Math.round(generalScore * 0.8 + majorScore * 0.2);
      } else {
        combined[dimension] = generalScore;
      }
    });

    // 应用专业加权
    return this.applyMajorWeighting(combined, userMajors);
  }

  private normalizeScores(scores: DimensionScores): DimensionScores {
    const maxScore = Math.max(...Object.values(scores));
    if (maxScore === 0) return scores;

    const normalized: DimensionScores = {} as DimensionScores;
    Object.entries(scores).forEach(([dim, score]) => {
      normalized[dim as Dimension] = Math.round((score / maxScore) * 100);
    });

    return normalized;
  }

  private applyMajorWeighting(scores: DimensionScores, userMajors: MajorTag[]): DimensionScores {
    const weightedScores = { ...scores };

    userMajors.forEach((major) => {
      switch (major) {
        case 'major_medical':
          // 医学专业：轻微提升健康服务维度,但不强制
          if (scores['健康服务'] > 50) {
            weightedScores['健康服务'] = Math.min(100, Math.round(scores['健康服务'] * 1.15));
          }
          break;

        case 'major_cs':
          // 计算机专业：轻微提升科研创新维度
          if (scores['科研创新'] > 50) {
            weightedScores['科研创新'] = Math.min(100, Math.round(scores['科研创新'] * 1.15));
          }
          break;

        case 'major_engineering':
          // 工程专业：轻微提升工程制造维度
          if (scores['工程制造'] > 50) {
            weightedScores['工程制造'] = Math.min(100, Math.round(scores['工程制造'] * 1.15));
          }
          break;

        case 'major_business':
          // 商科专业：轻微提升商业服务维度
          if (scores['商业服务'] > 50) {
            weightedScores['商业服务'] = Math.min(100, Math.round(scores['商业服务'] * 1.15));
          }
          break;

        case 'major_art':
          // 艺术专业：轻微提升文化艺术维度
          if (scores['文化艺术'] > 50) {
            weightedScores['文化艺术'] = Math.min(100, Math.round(scores['文化艺术'] * 1.15));
          }
          break;

        case 'major_education':
          // 教育专业：轻微提升教育培训维度
          if (scores['教育培训'] > 50) {
            weightedScores['教育培训'] = Math.min(100, Math.round(scores['教育培训'] * 1.15));
          }
          break;

        case 'major_science':
          // 理工科专业：轻微提升科研创新维度
          if (scores['科研创新'] > 50) {
            weightedScores['科研创新'] = Math.min(100, Math.round(scores['科研创新'] * 1.3));
          }
          break;

        case 'major_liberal_arts':
          // 文科专业：强化文化艺术维度
          if (scores['文化艺术'] > 35) {
            weightedScores['文化艺术'] = Math.min(100, Math.round(scores['文化艺术'] * 1.2));
          }
          break;
      }
    });

    return weightedScores;
  }

  matchJobs(
    scores: DimensionScores,
    userMajors: MajorTag[],
    limit: number = 3
  ): JobMatch[] {
    const matches: JobMatch[] = [];

    // 专业标签映射: 岗位数据用的是简写,需要转换
    const majorMapping: Record<string, MajorTag> = {
      'medical': 'major_medical',
      'cs': 'major_cs',
      'engineering': 'major_engineering',
      'business': 'major_business',
      'art': 'major_art',
      'education': 'major_education',
      'science': 'major_science',
      'liberal_arts': 'major_liberal_arts'
    };

    this.jobs.forEach((job) => {
      // 检查专业门槛 - medium和high都需要检查
      if ((job.professionalBarrier === 'high' || job.professionalBarrier === 'medium') &&
          job.requiredMajors.length > 0) {
        // 将岗位的requiredMajors转换为标准格式
        const normalizedJobMajors = job.requiredMajors.map(m => majorMapping[m] || m);
        const hasRequiredMajor = normalizedJobMajors.some((major) =>
          userMajors.includes(major as MajorTag)
        );
        if (!hasRequiredMajor) {
          // 用户没有该岗位要求的专业,跳过
          return;
        }
      }

      // 计算匹配分数
      let matchScore = 0;
      let totalWeight = 0;

      Object.entries(job.dimensionRequirements).forEach(([dimension, req]) => {
        const userScore = scores[dimension as Dimension] || 0;
        const weight = req.weight;
        totalWeight += weight;

        if (userScore >= req.targetScore) {
          // 达到目标分数,给满分
          matchScore += 100 * weight;
        } else if (userScore >= req.minThreshold) {
          // 在最低阈值和目标分数之间,线性插值
          const ratio =
            (userScore - req.minThreshold) / (req.targetScore - req.minThreshold);
          matchScore += ratio * 100 * weight;
        } else {
          // 低于最低阈值,给较低的基础分(降低到15%),避免推荐不合适的岗位
          const ratio = userScore / req.minThreshold;
          matchScore += ratio * 15 * weight;
        }
      });

      if (totalWeight > 0) {
        const finalScore = matchScore / totalWeight;
        matches.push({
          job,
          matchScore: Math.round(finalScore),
        });
      }
    });

    // 按分数排序并返回前N个，确保一定有结果
    const sorted = matches.sort((a, b) => b.matchScore - a.matchScore);
    return sorted.slice(0, Math.min(limit, sorted.length));
  }

  getMentorsByIds(mentorIds: string[]): CareerMentor[] {
    return mentorIds
      .map((id) => this.mentors.get(id))
      .filter((mentor): mentor is CareerMentor => mentor !== undefined);
  }

  getQuestions(userMajors: MajorTag[] = []): Question[] {
    // 过滤题目:只返回通用题目 + 用户专业匹配的题目
    return this.questions.filter(q => {
      // Q0是专业选择题,总是显示
      if (q.questionId === 0) return true;

      // 如果题目没有requiredMajors字段,说明是通用题目,显示
      if (!('requiredMajors' in q) || !q.requiredMajors || q.requiredMajors.length === 0) {
        return true;
      }

      // 如果题目有requiredMajors,检查用户是否选了对应专业
      return q.requiredMajors.some((major: string) => userMajors.includes(major as MajorTag));
    });
  }

  generateWhyFit(job: Job, scores: DimensionScores): string {
    let text = job.whyFitTemplate;

    Object.entries(scores).forEach(([dimension, score]) => {
      const placeholder = `{${dimension}}`;
      if (text.includes(placeholder)) {
        text = text.replace(new RegExp(placeholder.replace(/[{}]/g, '\\$&'), 'g'), dimension);
      }

      const scorePlaceholder = `{${dimension}得分}`;
      if (text.includes(scorePlaceholder)) {
        text = text.replace(
          new RegExp(scorePlaceholder.replace(/[{}]/g, '\\$&'), 'g'),
          score.toString()
        );
      }
    });

    return text;
  }

  matchResultType(scores: DimensionScores, topJobs: JobMatch[]): string {
    const resultType = this.getResultTypeObject(scores, topJobs);
    return resultType?.typeName || Object.entries(scores).sort(([, a], [, b]) => b - a)[0][0];
  }

  getResultTypeObject(scores: DimensionScores, topJobs: JobMatch[]): any {
    if (!topJobs || topJobs.length === 0) {
      const sortedScores = Object.entries(scores).sort(([, a], [, b]) => b - a);
      const topDimension = sortedScores[0][0];
      return this.resultTypes.find((t: any) => t.category === topDimension);
    }

    const jobCategories = topJobs.map(match => match.job.category);
    const categoryCount: Record<string, number> = {};
    jobCategories.forEach(cat => {
      categoryCount[cat] = (categoryCount[cat] || 0) + 1;
    });

    const sortedCategories = Object.entries(categoryCount).sort(([, a], [, b]) => b - a);
    const dominantCategory = sortedCategories[0][0];
    const dominantCount = sortedCategories[0][1];

    if (sortedCategories.length >= 2 && dominantCount === 1) {
      const balancedType = this.resultTypes.find((t: any) => t.matchingConditions.balanced);
      if (balancedType) return balancedType;
    }

    const categoryScore = scores[dominantCategory as Dimension] || 0;
    if (categoryScore >= 80) {
      const specialistType = this.resultTypes.find((t: any) => {
        const conditions = t.matchingConditions;
        return conditions[dominantCategory] && conditions[dominantCategory].min === 80;
      });
      if (specialistType) return specialistType;
    }

    return this.resultTypes.find((t: any) => t.category === dominantCategory) ||
           this.resultTypes.find((t: any) => t.category === Object.entries(scores).sort(([, a], [, b]) => b - a)[0][0]);
  }

  generateDynamicStrengths(scores: DimensionScores, topJobs: JobMatch[]): any[] {
    const sortedDimensions = Object.entries(scores).sort(([, a], [, b]) => b - a);
    const topDimension = sortedDimensions[0];
    const secondDimension = sortedDimensions[1];

    // 根据最高分维度和推荐岗位生成第一个优势
    const firstStrength = this.generateJobSpecificStrength(topDimension, topJobs);

    // 根据第二高分维度生成第二个优势
    const secondStrength = this.generateSecondaryStrength(secondDimension, topJobs);

    return [firstStrength, secondStrength];
  }

  private generateJobSpecificStrength(topDimension: [string, number], topJobs: JobMatch[]): any {
    const [dimension, score] = topDimension;
    const jobNames = topJobs.map(j => j.job.jobName);
    const primaryCategory = topJobs[0]?.job?.category || dimension;

    // 优先根据岗位类型判断,避免维度错配导致的描述不匹配
    // 体制内岗位(警察/消防/公务员)
    if (jobNames.some(j => j.includes('警察') || j.includes('消防') || j.includes('公务员'))) {
      return {
        title: '责任心强，原则性强',
        description: `你的${dimension}能力得分${score}分，适合${jobNames[0]}这类需要强烈责任感和原则性的岗位。`,
        example: `在${jobNames[0]}工作中，你会严格遵守规章制度，公正执法。比如处理一个案件时，你会严格按照法律程序，确保每个环节都有据可查，既保护当事人权益，也维护法律权威。这种原则性和责任感是${jobNames[0]}岗位的核心要求。`
      };
    }

    // 健康服务岗位
    if (jobNames.some(j => j.includes('医生') || j.includes('护士') || j.includes('药剂') || j.includes('医师'))) {
      return {
        title: '专业严谨，注重循证',
        description: `你的${dimension}能力得分${score}分，展现出${jobNames[0]}岗位所需的专业素养和严谨态度。`,
        example: `在临床工作中，你不会凭感觉做判断。比如遇到一个症状，你会系统地问诊：什么时候开始的？有什么诱因？伴随症状是什么？然后结合检查结果和文献证据，给出诊断和治疗方案。这种循证思维确保每个决策都有依据，最大程度保障患者安全。`
      };
    }

    // 教师岗位
    if (jobNames.some(j => j.includes('教师') || j.includes('教育'))) {
      return {
        title: '善于引导和启发，而不是灌输',
        description: `你的${dimension}能力得分${score}分，非常适合${jobNames[0]}这类需要传递知识和培养能力的岗位。`,
        example: `在教学中，你不会照本宣科。比如讲一个复杂概念时，你会先问学生"你们觉得这个是什么意思？"通过提问引导他们思考，再用生活中的例子类比，最后总结核心要点。这种苏格拉底式的教学法让学生真正理解知识，而不是死记硬背。`
      };
    }

    // 根据维度、岗位类别和具体岗位名称生成针对性的优势描述
    // 商业服务维度 - 产品/运营类岗位(增加多样化变体)
    if (dimension === '商业服务' && primaryCategory === '商业服务' && jobNames.some(j => j.includes('产品') || j.includes('运营'))) {
      const variants = [
        {
          title: '产品思维强，能洞察用户需求',
          description: `你的商业服务能力得分${score}分，特别适合${jobNames[0]}这类需要理解用户和业务的岗位。`,
          example: `在做${jobNames[0]}相关工作时，你不会只关注表面需求。比如用户说"我想要一个搜索功能"，你会追问：为什么需要搜索？要找什么？现在怎么找的？通过深挖真实场景，你能设计出真正解决问题的方案，而不是堆砌功能。`
        },
        {
          title: '数据敏感度高，善于用数据驱动决策',
          description: `你的商业服务能力得分${score}分，在${jobNames[0]}这类需要量化分析的岗位上会很有优势。`,
          example: `在做${jobNames[0]}相关工作时，你不会凭直觉拍脑袋。比如要优化一个功能，你会先看数据：用户在哪个环节流失？停留时长多少？转化率如何？然后提出假设、设计AB测试、分析结果，用数据验证每个决策。这种严谨的方法论能大幅降低试错成本。`
        },
        {
          title: '全局观强，能平衡多方诉求',
          description: `你的商业服务能力得分${score}分，特别适合${jobNames[0]}这类需要协调资源的岗位。`,
          example: `在做${jobNames[0]}相关工作时，你不会只站在自己角度思考。比如推进一个项目，你会同时考虑：用户要什么？技术能实现吗？商业价值在哪？老板关注什么指标？然后找到各方都能接受的平衡点，推动项目落地。`
        }
      ];
      return variants[Math.floor(score) % variants.length];
    }

    // 商业服务维度 - 销售/商务类岗位(增加多样化变体)
    if (dimension === '商业服务' && primaryCategory === '商业服务' && jobNames.some(j => j.includes('销售') || j.includes('商务') || j.includes('客户'))) {
      const variants = [
        {
          title: '沟通能力强，善于建立信任',
          description: `你的商业服务能力得分${score}分，在${jobNames[0]}这类需要对外沟通的岗位上会很有优势。`,
          example: `在和客户沟通时，你不会急于推销产品，而是先建立信任。比如初次见面，你会花时间了解对方的业务痛点、决策流程、预算情况，找到双方的共同利益点，再提出针对性的解决方案。这种"先理解，再建议"的方式让客户觉得你是在帮他解决问题，而不是单纯卖东西。`
        },
        {
          title: '抗压能力强，目标导向明确',
          description: `你的商业服务能力得分${score}分，非常适合${jobNames[0]}这类需要持续突破的岗位。`,
          example: `在做${jobNames[0]}相关工作时，你不会因为几次拒绝就放弃。比如一个客户说"暂时不需要"，你会分析：是真的不需要，还是时机不对？预算不够还是决策链太长？然后调整策略，持续跟进。这种韧性让你能在高压环境下持续出业绩。`
        },
        {
          title: '同理心强，能快速建立rapport',
          description: `你的商业服务能力得分${score}分，在${jobNames[0]}这类需要人际互动的岗位上会很出彩。`,
          example: `在和客户交流时，你能快速捕捉对方的情绪和关注点。比如客户说话犹豫，你会察觉到他可能有顾虑，主动问"您是不是担心XX？"这种敏锐的洞察力让客户觉得被理解，更愿意敞开心扉，加速成交。`
        }
      ];
      return variants[Math.floor(score) % variants.length];
    }

    if (dimension === '教育培训') {
      return {
        title: '善于引导和启发，而不是灌输',
        description: `你的教育培训能力得分${score}分，非常适合${jobNames[0]}这类需要传递知识和培养能力的岗位。`,
        example: `在教学或培训中，你不会照本宣科。比如讲一个复杂概念时，你会先问学生"你们觉得这个是什么意思？"通过提问引导他们思考，再用生活中的例子类比，最后总结核心要点。这种苏格拉底式的教学法让学生真正理解知识，而不是死记硬背。`
      };
    }

    if (dimension === '健康服务') {
      return {
        title: '专业严谨，注重循证',
        description: `你的健康服务能力得分${score}分，展现出${jobNames[0]}岗位所需的专业素养和严谨态度。`,
        example: `在临床或健康管理工作中，你不会凭感觉做判断。比如遇到一个症状，你会系统地问诊：什么时候开始的？有什么诱因？伴随症状是什么？然后结合检查结果和文献证据，给出诊断和治疗方案。这种循证思维确保每个决策都有依据，最大程度保障患者安全。`
      };
    }

    if (dimension === '文化艺术') {
      return {
        title: '创意思维活跃，善于视觉表达',
        description: `你的文化艺术能力得分${score}分，在${jobNames[0]}这类需要创意和审美的岗位上会很出彩。`,
        example: `在做${jobNames[0]}相关工作时，你不会简单模仿。比如设计一个品牌视觉，你会先研究品牌调性、目标用户、使用场景，然后从色彩心理学、构图原理、文化符号等多个维度思考，最终呈现出既美观又有内涵的作品。`
      };
    }

    if (dimension === '工程制造') {
      return {
        title: '动手能力强，善于解决技术问题',
        description: `你的工程制造能力得分${score}分，非常适合${jobNames[0]}这类需要技术实现的岗位。`,
        example: `在做${jobNames[0]}相关工作时，你不会遇到问题就放弃。比如调试一个复杂系统，你会系统地排查：先复现问题，再隔离变量，然后逐个模块测试，最后定位根因并修复。这种结构化的问题解决能力让你能攻克各种技术难题。`
      };
    }

    if (dimension === '科研创新') {
      return {
        title: '逻辑思维强，善于深度钻研',
        description: `你的科研创新能力得分${score}分，在${jobNames[0]}这类需要研究和创新的岗位上会很有优势。`,
        example: `在做${jobNames[0]}相关工作时，你不会浅尝辄止。比如研究一个新算法，你会深入理解数学原理、推导公式、分析复杂度，然后动手实现并在真实数据上验证效果。这种"理论+实践"的闭环让你能真正掌握技术本质。`
      };
    }

    // 公共服务维度 - 其他公共服务岗位(体制内岗位已在前面处理)
    if (dimension === '公共服务') {
      return {
        title: '责任心强，善于协调多方利益',
        description: `你的公共服务能力得分${score}分，适合${jobNames[0]}这类需要服务意识和协调能力的岗位。`,
        example: `在做${jobNames[0]}相关工作时，你会站在更高的视角思考。比如处理一个公共事务，你不会只考虑效率，还会权衡公平性、可持续性、社会影响。你会主动倾听不同群体的声音，寻找各方都能接受的解决方案。`
      };
    }

    // 默认通用描述
    return {
      title: `${dimension}能力突出`,
      description: `你的${dimension}能力得分${score}分，在${jobNames[0]}岗位上会很有优势。`,
      example: `在${jobNames[0]}相关工作中，你能够快速理解业务需求，并提出有价值的解决方案。`
    };
  }

  private generateSecondaryStrength(secondDimension: [string, number], topJobs: JobMatch[]): any {
    const [dimension, score] = secondDimension;
    const jobNames = topJobs.map(j => j.job.jobName).join('、');

    // 第二优势强调"复合能力"
    return {
      title: `复合能力：${dimension}为你加分`,
      description: `你的${dimension}能力得分${score}分，这让你在${jobNames}等岗位上比单一能力的候选人更有竞争力。`,
      example: `很多人只擅长一个领域，但你同时具备${dimension}能力。比如在实际工作中，这意味着你不仅能完成本职工作，还能跨领域协作。这种"T型人才"的特质在团队中非常稀缺和宝贵。`
    };
  }

  generateDynamicWeaknesses(scores: DimensionScores, topJobs: JobMatch[]): any[] {
    const jobNames = topJobs.map(j => j.job.jobName);
    void jobNames;

    const weaknesses = [];

    // 分析推荐岗位的维度要求 vs 用户得分,找出gap
    const jobDimensionGaps = this.analyzeJobDimensionGaps(topJobs, scores);

    if (jobDimensionGaps.length > 0) {
      const biggestGap = jobDimensionGaps[0];
      weaknesses.push({
        title: `${biggestGap.dimension}能力需要加强`,
        description: `${jobNames[0]}岗位对${biggestGap.dimension}能力要求较高(目标${biggestGap.targetScore}分),但你目前得分${biggestGap.userScore}分,还有提升空间。`,
        improvements: this.generateSpecificImprovements(biggestGap.dimension, jobNames[0])
      });
    }

    // 第二个短板:根据岗位特点个性化生成
    const secondWeakness = this.generateSecondWeakness(jobNames[0]);
    if (secondWeakness) {
      weaknesses.push(secondWeakness);
    }

    return weaknesses;
  }

  private generateSecondWeakness(jobName: string): any | null {
    // 体制内/考试类岗位 - 短板是考试准备
    const examBasedJobs = ['公务员', '警察', '消防员', '医生', '护士', '教师'];
    if (examBasedJobs.some(j => jobName.includes(j))) {
      return {
        title: `应试能力和备考经验不足`,
        description: `${jobName}岗位需要通过严格的考试选拔,但你可能还没有系统的备考经验和应试技巧。`,
        improvements: [
          `了解考试大纲和题型,购买官方教材和历年真题,制定3-6个月的备考计划`,
          `加入备考社群或报班,获取最新考试资讯和高效学习方法`,
          `每天至少投入3-4小时备考,做题+总结错题+模拟考试,形成应试节奏`
        ]
      };
    }

    // 学术研究类岗位 - 短板是科研训练
    const researchJobs = ['科研人员', '研究员', '算法研究', '数据科学家'];
    if (researchJobs.some(j => jobName.includes(j))) {
      return {
        title: `科研方法论和论文写作经验不足`,
        description: `${jobName}岗位需要扎实的科研训练,但你可能还缺少系统的研究方法和学术写作能力。`,
        improvements: [
          `阅读该领域的顶级论文,学习研究者如何提出问题、设计实验、分析结果`,
          `尝试复现一篇论文的实验,或参与导师/实验室的科研项目,体验完整的研究流程`,
          `学习学术写作规范,练习撰写文献综述和研究报告`
        ]
      };
    }

    // 创意/艺术类岗位 - 短板是作品集
    const creativeJobs = ['设计师', '插画师', '摄影师', '视频制作', '编剧', '导演', '演员', '音乐人'];
    if (creativeJobs.some(j => jobName.includes(j))) {
      return {
        title: `作品集数量和质量需要提升`,
        description: `${jobName}岗位主要看作品说话,但你可能还没有足够多、足够好的作品来展示你的能力和风格。`,
        improvements: [
          `确定你的创作方向和风格定位,专注一个细分领域持续输出`,
          `每周完成1-2个作品,在小红书、B站等平台持续发布,积累粉丝和曝光`,
          `主动向行业前辈请教,获得反馈并快速迭代,提升作品质量`
        ]
      };
    }

    // 技术/工程类岗位 - 短板是项目经验
    const techJobs = ['工程师', '开发', '程序员', '架构师', '技术'];
    if (techJobs.some(j => jobName.includes(j))) {
      return {
        title: `缺少完整的项目开发经验`,
        description: `${jobName}岗位需要实际的项目经验,但你可能还没有独立完成过完整的开发项目。`,
        improvements: [
          `做1-2个个人项目:从需求分析到设计、开发、测试、部署,走完全流程`,
          `参与开源项目或实习,学习团队协作、代码规范、版本管理等工程实践`,
          `在GitHub上展示你的代码,写好README和技术文档,形成可展示的作品集`
        ]
      };
    }

    // 商业/管理类岗位 - 短板是商业sense
    const businessJobs = ['产品', '运营', '市场', '销售', '商务', '管理', '咨询'];
    if (businessJobs.some(j => jobName.includes(j))) {
      return {
        title: `商业敏感度和行业理解不够深入`,
        description: `${jobName}岗位需要对商业逻辑和行业动态有敏锐的洞察,但你可能还缺少这方面的积累。`,
        improvements: [
          `关注${jobName}领域的行业报告、案例分析、大厂动态,建立商业sense`,
          `分析3-5个成功产品/公司,拆解他们的商业模式、增长策略、竞争优势`,
          `尝试做一个小项目(哪怕是校园创业),实践从0到1的完整商业流程`
        ]
      };
    }

    // 默认:实战经验(适用于其他岗位)
    return {
      title: `${jobName}领域的实战经验较少`,
      description: `虽然你的能力测评结果不错,但可能还缺少${jobName}岗位所需的实际项目经验和行业理解。`,
      improvements: [
        `寻找${jobName}相关的实习机会,即使是短期实习也能快速积累经验`,
        `做1-2个${jobName}相关的个人项目,完整走一遍工作流程,形成可展示的作品`,
        `关注${jobName}领域的优秀案例,分析他们是如何解决问题的,学习实战思路`
      ]
    };
  }

  private analyzeJobDimensionGaps(topJobs: JobMatch[], scores: DimensionScores): Array<{dimension: string, targetScore: number, userScore: number, gap: number}> {
    const gaps: Array<{dimension: string, targetScore: number, userScore: number, gap: number}> = [];

    // 分析第一个推荐岗位的维度要求
    const firstJob = topJobs[0]?.job;
    if (!firstJob) return gaps;

    Object.entries(firstJob.dimensionRequirements).forEach(([dimension, req]) => {
      const userScore = scores[dimension as Dimension] || 0;
      const targetScore = req.targetScore;
      const gap = targetScore - userScore;

      if (gap > 10) {  // 只关注差距>10分的维度
        gaps.push({
          dimension,
          targetScore,
          userScore,
          gap
        });
      }
    });

    return gaps.sort((a, b) => b.gap - a.gap);
  }

  private generateSpecificImprovements(dimension: string, jobName: string): string[] {
    const improvementMap: Record<string, string[]> = {
      '商业服务': [
        `分析3-5个${jobName}领域的成功案例,拆解他们的商业模式和增长策略`,
        `关注行业报告和大厂动态(36氪、人人都是产品经理),建立商业sense`,
        `尝试做一个校园小项目:比如帮社团做活动策划、帮小店做线上推广,实践商业思维`
      ],
      '健康服务': [
        `通过B站、知乎、丁香园等平台学习医学基础知识和临床思维`,
        `关注健康服务领域的前沿进展,阅读科普文章和行业报告`,
        `争取医院见习机会(跟诊、观摩),或参与健康科普、义诊等志愿活动`
      ],
      '教育培训': [
        `通过B站、知乎学习教育心理学基础(如何激发学习动机、如何设计教学环节)`,
        `尝试做家教或线上辅导,实践"如何把知识讲清楚",积累教学经验`,
        `观摩优秀教师的公开课(B站、学而思等平台),学习他们的教学设计和互动技巧`
      ],
      '文化艺术': [
        `通过B站、优设网学习设计基础:色彩、构图、排版、视觉心理学`,
        `每天做小练习:临摹优秀作品、用不同风格表达同一主题,训练创意思维`,
        `在小红书、站酷等平台发布作品,获取反馈并快速迭代`
      ],
      '工程制造': [
        `通过GitHub、技术博客学习${jobName}的核心技术,边学边做小项目`,
        `参与开源项目或技术社区(如掘金、V2EX),学习工程实践和代码规范`,
        `做1-2个完整项目:从需求到上线,形成可展示的作品集`
      ],
      '科研创新': [
        `通过Coursera、B站系统学习${jobName}领域的理论基础,理解核心原理`,
        `阅读该领域的经典论文和综述,学习研究者的思维方式`,
        `尝试复现一篇论文的实验,或参与导师/实验室的科研项目`
      ],
      '公共服务': [
        `通过公开课、书籍了解公共政策和社会治理的基本逻辑`,
        `参与志愿服务或公益项目(社区服务、支教、环保活动),积累实践经验`,
        `关注社会热点,思考不同群体的诉求和解决方案`
      ],
      '自主创业': [
        `通过播客、公众号学习创业方法论(精益创业、商业模式画布、MVP验证)`,
        `尝试做一个校园小项目:摆摊、代购、活动策划,体验从0到1的过程`,
        `多和创业者交流(校友、学长学姐),了解真实的挑战和经验`
      ]
    };

    return improvementMap[dimension] || [
      `系统学习${dimension}领域的核心知识和技能`,
      `寻找${dimension}相关的实践机会,在实战中提升能力`,
      `向${dimension}领域的优秀从业者学习,了解行业最佳实践`
    ];
  }

  private getRealisticJobSearchTimeline(jobName: string): string {
    // 医疗岗位 - 需要考证+规培,周期很长
    const medicalJobs = ['临床医生', '外科医生', '儿科医生', '精神科医生', '口腔医生', '护士', '护士长'];
    if (medicalJobs.some(j => jobName.includes(j))) {
      return '目标:6-12个月内通过资格考试并找到规培/实习岗位(医疗岗位周期较长,需要耐心)';
    }

    // 教师/公务员 - 需要考试,有固定招考周期
    const examJobs = ['教师', '公务员', '警察', '消防员'];
    if (examJobs.some(j => jobName.includes(j))) {
      return '目标:关注每年的招考公告(通常3-6月、9-11月),提前3-6个月备考';
    }

    // 金融/咨询 - 竞争激烈,周期较长
    const competitiveJobs = ['投资', '咨询', '券商', '基金', '四大'];
    if (competitiveJobs.some(j => jobName.includes(j))) {
      return '目标:4-6个月内拿到offer(这些岗位竞争激烈,需要充分准备)';
    }

    // 创意/自由职业 - 看作品集,不是传统求职
    const creativeJobs = ['设计师', '插画师', '摄影师', '视频制作', '自由撰稿人'];
    if (creativeJobs.some(j => jobName.includes(j))) {
      return '目标:3-6个月内接到第一批付费项目(创意类岗位看作品,不是传统投简历)';
    }

    // 技术岗位 - 相对标准化,周期适中
    const techJobs = ['工程师', '开发', '程序员', '算法'];
    if (techJobs.some(j => jobName.includes(j))) {
      return '目标:2-3个月内拿到实习offer(技术岗位相对标准化,准备充分可以较快拿到机会)';
    }

    // 商业岗位 - 周期适中
    const businessJobs = ['产品', '运营', '市场', '销售'];
    if (businessJobs.some(j => jobName.includes(j))) {
      return '目标:2-4个月内拿到实习offer(商业岗位看综合能力,需要一定时间积累)';
    }

    // 默认:3个月
    return '目标:3个月内拿到实习offer';
  }

  generateDynamicActionPlan(scores: DimensionScores, topJobs: JobMatch[]): any {
    const jobNames = topJobs.map(j => j.job.jobName);
    const firstJob = topJobs[0]?.job;
    const primaryCategory = firstJob?.category || '目标';

    const gaps = this.analyzeJobDimensionGaps(topJobs, scores);
    const hasSignificantGap = gaps.length > 0 && gaps[0].gap > 15;

    // 根据推荐岗位判断求职路径类型
    const creativeFreelanceJobs = ['演员', '插画师', '自由撰稿人', '独立设计师', '摄影师', '视频博主', '自媒体创作者', '独立音乐人', '自由翻译', '配音演员', '舞蹈演员', '漫画家', '独立游戏开发者'];
    const entrepreneurshipJobs = ['创业者', '自由职业者', '独立咨询师', '电商创业者', '工作室创始人'];
    const examBasedJobs = {
      medical: ['临床医生', '外科医生', '儿科医生', '精神科医生', '口腔医生', '护士', '护士长', '药剂师', '临床药师', '影像科医生', '医学检验师'],
      teacher: ['中小学教师', '大学教师', '英语教师', '对外汉语教师', '音乐教师', '美术教师', '幼儿教师'],
      civilService: ['公务员', '事业单位工作人员', '警察', '消防员']
    };

    // 检查推荐岗位类型
    const hasCreativeFreelance = jobNames.some(name => creativeFreelanceJobs.includes(name));
    const hasEntrepreneurship = jobNames.some(name => entrepreneurshipJobs.includes(name)) || primaryCategory === '自主创业';
    const hasMedical = jobNames.some(name => examBasedJobs.medical.includes(name));
    const hasTeacher = jobNames.some(name => examBasedJobs.teacher.includes(name));
    const hasCivilService = jobNames.some(name => examBasedJobs.civilService.includes(name));

    // 考试/考编路径(医生、教师、公务员)
    if (hasMedical || hasTeacher || hasCivilService) {
      let examType = '';
      let examName = '';
      let jobType = '';

      if (hasMedical) {
        examType = '执业资格考试';
        examName = '医师资格考试/护士执业资格考试';
        jobType = jobNames.find(name => examBasedJobs.medical.includes(name)) || '医疗岗位';
      } else if (hasTeacher) {
        examType = '教师资格证考试';
        examName = '教师资格证考试(笔试+面试)';
        jobType = jobNames.find(name => examBasedJobs.teacher.includes(name)) || '教师岗位';
      } else {
        examType = '公务员/事业编考试';
        examName = '国考/省考/事业单位联考';
        jobType = jobNames.find(name => examBasedJobs.civilService.includes(name)) || '公务员';
      }

      return {
        shortTerm: [
          {
            step: `准备${examType}`,
            details: `目标:通过${examName},获得从业资格\n\n具体行动:\n- 了解考试时间、报名条件、考试科目和题型\n- 购买官方教材和历年真题,制定3-6个月的备考计划\n- ${hasMedical ? '重点复习医学基础知识、临床技能、法律法规' : hasTeacher ? '重点复习综合素质、教育知识与能力、学科知识' : '重点复习行测、申论,了解时事政治'}\n- 加入备考群或报班,获取最新考试资讯和学习资源\n- 每天至少投入3-4小时备考,做题+总结错题`
          },
          {
            step: hasSignificantGap ? `补齐专业短板:${gaps[0].dimension}` : '提升专业能力',
            details: hasSignificantGap
              ? `${jobType}需要${gaps[0].dimension}能力,这是你目前的短板\n\n具体行动:\n${this.generateSpecificImprovements(gaps[0].dimension, jobType).map(imp => `- ${imp}`).join('\n')}`
              : `系统提升${jobType}的核心能力\n\n具体行动:\n- ${hasMedical ? '通过实习、见习积累临床经验,熟悉医疗流程' : hasTeacher ? '通过家教、支教、助教积累教学经验,练习授课技巧' : '关注时事政治,提升公文写作和材料分析能力'}\n- 向在职人员请教工作内容和职业发展路径\n- 阅读行业相关书籍和案例,建立专业知识体系`
          },
          {
            step: '了解招聘信息和岗位要求',
            details: `目标:明确目标单位和岗位,做好针对性准备\n\n具体行动:\n- ${hasMedical ? '关注各大医院的招聘公告(官网、医疗人才网)' : hasTeacher ? '关注教育局、学校官网的教师招聘公告' : '关注国家公务员局、各省人社厅的招考公告'}\n- 研究目标岗位的专业要求、学历要求、工作地点\n- ${hasCivilService ? '了解岗位的报考比例和往年分数线,评估竞争难度' : '了解单位的待遇、发展空间、工作强度'}\n- 提前准备好学历证明、资格证书等材料`
          }
        ],
        midTerm: [
          {
            step: `通过${examType}并参加招聘`,
            details: `目标:拿到资格证书,通过单位招聘\n\n具体行动:\n- 考前冲刺:做模拟题、背重点、调整作息\n- 考试当天:提前到场、带齐证件、保持冷静\n- ${hasMedical ? '通过考试后,关注医院招聘,准备简历和面试' : hasTeacher ? '拿到教师资格证后,参加教师招聘考试(笔试+面试+试讲)' : '通过笔试后,准备面试:了解岗位职责,练习结构化面试'}\n- ${hasCivilService ? '面试技巧:STAR法则回答问题,展现政治素养和应变能力' : '面试/试讲技巧:展现专业能力、沟通能力、职业素养'}`
          },
          {
            step: '入职后快速适应',
            details: `目标:顺利度过试用期,站稳脚跟\n\n具体行动:\n- ${hasMedical ? '虚心向老医生学习,熟悉科室流程和规范' : hasTeacher ? '向老教师请教教学方法,快速熟悉教材和学生' : '熟悉单位规章制度,学习公文写作和办事流程'}\n- 保持谦虚态度,多做事少抱怨,建立良好人际关系\n- ${hasMedical ? '持续学习医学新知识,考虑规培、进修、职称晋升' : hasTeacher ? '参加教研活动,提升教学水平,争取评优评先' : '关注政策文件,提升业务能力,争取转正定级'}\n- 平衡工作和生活,${hasMedical || hasTeacher ? '避免职业倦怠' : '适应体制内工作节奏'}`
          }
        ]
      };
    }

    // 创意自由职业者路径(作品集驱动)
    if (hasCreativeFreelance) {
      const creativeJob = jobNames.find(name => creativeFreelanceJobs.includes(name)) || jobNames[0];
      const isArtPerformance = ['演员', '主持人', '配音演员', '舞蹈演员', '独立音乐人'].includes(creativeJob);

      return {
        shortTerm: [
          {
            step: '建立作品集',
            details: `目标:积累3-5个高质量作品,展示你的风格和能力\n\n具体行动:\n- 确定你的创作方向和风格定位,不要什么都做,专注一个细分领域\n- 每周完成1个作品:${isArtPerformance ? '可以是短视频、片段表演、翻唱作品' : '可以是个人项目、模拟商业项目、重新设计经典案例'}\n- 在小红书、B站、微博等平台持续发布作品,积累粉丝和曝光\n- 主动向行业前辈请教,获得反馈并快速迭代`
          },
          {
            step: hasSignificantGap ? `补齐创作短板:${gaps[0].dimension}` : '提升专业技能',
            details: hasSignificantGap
              ? `${creativeJob}需要${gaps[0].dimension}能力,这是你目前的短板\n\n具体行动:\n${this.generateSpecificImprovements(gaps[0].dimension, creativeJob).map(imp => `- ${imp}`).join('\n')}`
              : `系统提升${creativeJob}的核心技能\n\n具体行动:\n- 找到该领域的顶尖创作者,分析他们的作品和创作方法\n- 通过在线课程、工作坊、大师班系统学习\n- 每天至少投入2-3小时刻意练习,保持创作手感`
          },
          {
            step: '建立个人品牌',
            details: `目标:让潜在客户/粉丝能找到你并记住你\n\n具体行动:\n- 搭建个人网站或作品集页面(可以用Notion、小红书主页、个人公众号)\n- 在社交媒体保持活跃:分享创作过程、行业观察、个人思考\n- 参加行业活动、比赛、展览,扩大人脉和曝光\n- 主动联系小型项目或客户,积累商业案例和口碑`
          }
        ],
        midTerm: [
          {
            step: '获取第一批付费客户/项目',
            details: `目标:在3-6个月内接到第一批商业项目\n\n具体行动:\n- 在自由职业平台(猪八戒、站酷、Upwork)注册并投标项目\n- 主动联系可能需要${creativeJob}服务的小企业、工作室、品牌\n- 前期可以适当降低报价,优先积累案例和好评\n- 每个项目都要争取客户推荐和作品授权,形成口碑传播`
          },
          {
            step: '建立稳定收入来源',
            details: `目标:从零散接单到稳定收入\n\n具体行动:\n- 争取长期合作客户:月度服务、年度合作,稳定现金流\n- 探索多元变现:${isArtPerformance ? '商演、代言、课程、付费社群' : '项目外包、付费教程、素材售卖、会员订阅'}\n- 提高单价:随着作品质量和知名度提升,逐步调整报价\n- 控制接单节奏:不要为了赚钱接太多项目,保证作品质量和个人品牌`
          }
        ]
      };
    }

    // 创业路径
    if (hasEntrepreneurship) {
      return {
        shortTerm: [
          {
            step: '验证创业想法',
            details: `目标:用最小成本验证你的创业方向是否可行\n\n具体行动:\n- 明确你想解决什么问题,目标用户是谁,他们愿意为此付费吗\n- 做用户访谈:找10-20个潜在用户深度聊,了解他们的真实痛点和支付意愿\n- 分析竞品:看看市场上有没有类似产品,他们做得怎么样,你的差异化在哪\n- 用最简单的方式做MVP(最小可行产品):可以是落地页+问卷,可以是手工服务,先验证需求再做产品`
          },
          {
            step: hasSignificantGap ? `补齐创业短板:${gaps[0].dimension}` : '学习创业方法论',
            details: hasSignificantGap
              ? `创业需要${gaps[0].dimension}能力,这是你目前的短板(当前${gaps[0].userScore}分)\n\n具体行动:\n${this.generateSpecificImprovements(gaps[0].dimension, '创业者').map(imp => `- ${imp}`).join('\n')}`
              : `系统学习创业的底层逻辑和方法\n\n具体行动:\n- 阅读《精益创业》《从0到1》等经典创业书籍\n- 学习商业模式画布、用户增长、产品迭代等实战方法\n- 关注成功创业者的分享(播客、公众号、视频),学习他们的思维方式`
          },
          {
            step: '组建初始团队或找到合伙人',
            details: `创业很难一个人完成,需要找到互补的伙伴\n\n具体行动:\n- 评估自己的能力短板:技术、产品、运营、销售,你缺哪块\n- 在校友、同学、前同事中寻找潜在合伙人,优先找能力互补且价值观一致的人\n- 如果暂时找不到合伙人,可以先外包或兼职合作,但要尽快补齐核心能力`
          }
        ],
        midTerm: [
          {
            step: '启动项目并快速迭代',
            details: `目标:在3-6个月内做出第一版产品并获得初始用户\n\n具体行动:\n- 开发MVP:功能极简,只做核心价值,快速上线\n- 找到种子用户:可以是身边朋友、社群、冷启动渠道,先服务好10-100个用户\n- 快速迭代:每周收集用户反馈,优化产品,验证商业模式\n- 记录关键数据:用户增长、留存率、付费转化,用数据指导决策`
          },
          {
            step: '探索商业化路径',
            details: `验证产品价值后,开始思考如何赚钱\n\n具体行动:\n- 测试定价策略:可以先免费积累用户,再推付费版;也可以直接收费验证支付意愿\n- 尝试不同变现方式:订阅制、一次性付费、广告、佣金,看哪种最适合你的产品\n- 如果短期不赚钱,考虑融资:准备BP(商业计划书),找天使投资人或加速器\n- 控制成本:创业初期现金流最重要,能省则省,把钱花在刀刃上`
          }
        ]
      };
    }

    return {
      shortTerm: [
        {
          step: '明确目标岗位并深入研究',
          details: `锁定岗位:${jobNames.join('、')}\n\n具体行动:\n- 在招聘网站(Boss直聘、拉勾)搜索这些岗位,看20-30个真实JD,提取高频关键词\n- 找到3-5个目标公司,研究他们对这个岗位的具体要求和工作内容\n- 加入${primaryCategory}相关的社群(知识星球、微信群),向在职人员请教`
        },
        {
          step: hasSignificantGap ? `补齐核心短板:${gaps[0].dimension}` : '提升核心技能',
          details: hasSignificantGap
            ? `你在${gaps[0].dimension}方面还有提升空间(当前${gaps[0].userScore}分,目标${gaps[0].targetScore}分)\n\n具体行动:\n${this.generateSpecificImprovements(gaps[0].dimension, jobNames[0]).map(imp => `- ${imp}`).join('\n')}`
            : `学习${jobNames[0]}岗位的核心技能和工具\n\n具体行动:\n- 找到该岗位的技能图谱,列出必备技能清单\n- 通过在线课程、书籍、实战项目系统学习\n- 每周至少投入10小时,持续3个月`
        },
        {
          step: '积累可展示的项目经验',
          details: `目标:完成1-2个${jobNames[0]}相关的项目,形成作品集\n\n具体行动:\n- 如果能找到实习,优先实习(即使是远程/兼职)\n- 如果暂时没有实习,做个人项目:模仿真实业务场景,完整走一遍工作流程\n- 记录项目过程:遇到什么问题、如何解决、最终效果如何,形成案例故事`
        }
      ],
      midTerm: [
        {
          step: '打磨求职材料',
          details: `简历:\n- 用STAR法则描述项目经验(Situation-Task-Action-Result)\n- 突出与${jobNames[0]}岗位相关的技能和成果\n- 量化成果:不要说"提升了用户体验",要说"通过XX优化,用户留存率提升15%"\n\n作品集:\n- 整理2-3个最能展示能力的项目案例\n- 每个案例包括:背景、目标、方案、成果、反思\n\n面试准备:\n- 准备${jobNames[0]}岗位的常见面试题(去牛客网、LeetCode搜索)\n- 找朋友或学长做模拟面试,提前适应面试节奏`
        },
        {
          step: '开始投递并持续优化',
          details: `投递策略:\n- 第一周:投递5-10家公司,测试简历和面试表现\n- 根据反馈优化:如果简历通过率低,改简历;如果面试挂了,复盘问题\n- 优先投递有实习转正机会的岗位,争取留用\n\n时间规划:\n- ${this.getRealisticJobSearchTimeline(jobNames[0])}\n- 如果超过预期时间还没有面试机会,说明简历或投递策略有问题,及时调整`
        }
      ]
    };
  }

  generateDynamicCTA(scores: DimensionScores, topJobs: JobMatch[]): any {
    const jobNames = topJobs.map(j => j.job.jobName);
    const firstJob = topJobs[0]?.job;
    const primaryCategory = firstJob?.category || '目标';

    // 分析用户的短板
    const gaps = this.analyzeJobDimensionGaps(topJobs, scores);
    const hasSignificantGap = gaps.length > 0 && gaps[0].gap > 15;

    // 分析分数分布特征
    const sortedDimensions = Object.entries(scores).sort(([, a], [, b]) => b - a);
    const maxScore = sortedDimensions[0][1];
    const minScore = sortedDimensions[sortedDimensions.length - 1][1];
    const scoreRange = maxScore - minScore;
    const isBalanced = scoreRange < 20;
    const hasMultipleHighScores = sortedDimensions.filter(([, score]) => score >= 80).length >= 2;

    // 根据用户情况生成困惑点
    const concerns: string[] = [];

    // 困惑1: 根据岗位和短板生成
    if (hasSignificantGap) {
      concerns.push(`${jobNames[0]}要求${gaps[0].dimension}能力强,但我这方面经验不足,能胜任吗?`);
    } else if (jobNames.length >= 2) {
      concerns.push(`${jobNames[0]}和${jobNames[1]}都挺适合我的,但不知道该选哪个?`);
    } else {
      concerns.push(`${jobNames[0]}这个方向适合我吗?未来发展空间怎么样?`);
    }

    // 困惑2: 根据分数分布特征生成
    if (isBalanced) {
      concerns.push(`我的能力比较均衡,没有特别突出的方向,会不会不够有竞争力?`);
    } else if (hasMultipleHighScores) {
      concerns.push(`我在${sortedDimensions.slice(0, 2).map(([dim]) => dim).join('和')}都有优势,是专注一个还是发展复合能力?`);
    } else {
      concerns.push(`除了${jobNames[0]},我还能做什么?要不要多准备几个备选方向?`);
    }

    // 困惑3: 实战经验相关
    if (firstJob?.professionalBarrier === 'high') {
      concerns.push(`${jobNames[0]}专业门槛高,我现在开始准备还来得及吗?需要考证吗?`);
    } else {
      concerns.push(`0经验怎么进入${primaryCategory}行业?实习难找吗?`);
    }

    // 生成我们能提供的价值
    const benefits: string[] = [
      `《${primaryCategory}求职指南》(含简历模板、面试题库、行业分析)`,
      `${jobNames[0]}岗位的详细JD解读和技能图谱`,
      `1对1职业规划咨询:帮你分析优劣势,制定3-6个月求职计划`
    ];

    // 如果有显著短板,增加针对性资料
    if (hasSignificantGap) {
      benefits.push(`${gaps[0].dimension}能力提升资料包(课程推荐+学习路径)`);
    }

    return {
      concerns,
      benefits
    };
  }
}
