import os
import json
from py2neo import Graph,Node

class MedicalGraph:
    def __init__(self):
        cur_dir = '/'.join(os.path.abspath(__file__).split('/')[:-1])
        #print('1:',cur_dir)
        self.data_path = os.path.join(cur_dir, 'data/39.json')
        #print('2:',self.data_path)
        # self.g = Graph('http://localhost:7474/', auth=("neo4j", "zhang2022"))
        self.g = Graph(
           'http: // localhost: 7474 ',
            # host="127.0.0.1",  # neo4j 搭载服务器的ip地址，ifconfig可获取到
            # http_port=7474,  # neo4j 服务器监听的端口号
            user="neo4j",  # 数据库user name，如果没有更改过，应该是neo4j
            password="zhang2022")

    def read_nodes(self):
        #构建实体类型
        symptoms = []  # 症状
        typedepressionss=[] #疾病类型
        casedepressions=[]#抑郁症病因
        diseases=[]
        #  =[]#诊断内容
        drugs=[]#药品
        treatway=[]#治疗方法
        # ways=[]#小类
        nursepressions=[]#护理
        # carepressions=[]#保健
        foods=[]#食物
        #Thirdfloor=[]#第三层节点
        checks=[]#检查


        type_symptoms1=[] #早期症状
        type_symptoms2=[] #晚期症状
        type_symptoms3=[] #相关症状


#各节点相关信息
        disease_infos = [] #属性信息


#关系
        type_symptom=[] #症状类别
        typical_symptom = []  # 典型症状
        eary_symptom=[] #早期症状
        terminal_symptom=[]#晚期症状
        relevant_symptom=[]#相关症状
        big_symptom=[]#三大症状
        body_symptom=[] #躯体症状
        type_depression=[]#抑郁类型
        case_depression=[]#抑郁症病因
        com_depression=[]#并发症
        diag_depression=[]#诊断内容
        identify_depression=[]#鉴别对象
        comuse_drugs=[]#常用药物
        treat_way=[]#治疗方式
        # check_depression=[]#重点检查
        nurse_depression=[]#护理
        suit_nurse=[]#对症护理
        ordinary_nurse=[]#一般护理
        Daily_nurse=[]#日常护理
        care_type=[]#保健类型
        do_eat=[]#宜吃
        not_eat=[]#不宜吃
        recommend_food=[]#推荐食物
        include_with=[]#包括
        Check_item=[]#检查项目
        Pathogeness_item = []  # 发病机理






        count=0
        for data in open(self.data_path, encoding='utf-8'):
            #各节点信息
            disease_dict = {}
            disease_dict['别名']=''
            disease_dict['是否属于医保'] =''
            disease_dict['发病部位'] =''
            disease_dict['有无传染性'] =''
            disease_dict['建议就诊科室'] =''
            disease_dict['最佳就诊时间'] =''
            disease_dict['就诊时长'] =''
            disease_dict['治疗周期'] =''
            disease_dict['诊断标准'] =''
            disease_dict['抑郁症的判断方法'] =''
            disease_dict['抑郁症最危险的症状'] =''
            disease_dict['预防'] =''
            disease_dict['多发人群'] =''
            disease_dict['发病原因'] =''
            disease_dict['发病机制'] =''
            disease_dict['饮食禁忌'] = ''
            disease_dict['饮食适宜'] = ''
            disease_dict['忌吃食物'] = ''
            disease_dict['宜吃食物'] = ''
            disease_dict['药物治疗说明'] = ''
            disease_dict['抑郁症测量表'] = ''


            count+=1
            print(count)
            data_json = json.loads(data)
            disease = data_json['名称']
            disease_dict['名称'] = disease
            diseases.append(disease)
            disease_dict['简介'] =data_json['简介']
            if '别名' in data_json:
                disease_dict['别名'] = data_json['别名']
            if '抑郁症测量表' in data_json:
                disease_dict['抑郁症测量表'] = data_json['抑郁症测量表']
            if '治愈率' in data_json:
                disease_dict['治愈率'] = data_json['治愈率']
            if '治疗费用' in data_json:
                disease_dict['治疗费用'] = data_json['治疗费用']
            if '是否属于医保' in data_json:
                disease_dict['是否属于医保'] = data_json['是否属于医保']
            if '发病部位' in data_json:
                disease_dict['发病部位'] = data_json['发病部位']
            if '有无传染性' in data_json:
                disease_dict['有无传染性']=data_json['有无传染性']
            if '就诊科室' in data_json:
                disease_dict['就诊科室']=data_json['就诊科室']
            if '最佳就诊时间' in data_json:
                disease_dict['最佳就诊时间']=data_json['最佳就诊时间']
            if '就诊时长' in data_json:
                disease_dict['就诊时长'] = data_json['就诊时长']
            if '治疗周期' in data_json:
                disease_dict['治疗周期'] = data_json['治疗周期']
            if '诊断标准' in data_json:
                disease_dict['诊断标准'] = data_json['诊断标准']
            if '抑郁症的判断方法' in data_json:
                disease_dict['抑郁症的判断方法'] = data_json['抑郁症的判断方法']
            if '抑郁症最危险的症状' in data_json:
                disease_dict['抑郁症最危险的症状'] = data_json['抑郁症最危险的症状']
            if '预防' in data_json:
                disease_dict['预防']=data_json['预防']
            if '多发人群' in data_json:
                disease_dict['多发人群'] = data_json['多发人群']
            if '发病原因' in data_json:
                disease_dict['发病原因'] = data_json['发病原因']
            if '发病机制' in data_json:
                disease_dict['发病机制'] = data_json['发病机制']
            if '季节性情绪抑郁症状病因' in data_json:
                disease_dict['季节性情绪抑郁症状病因'] = data_json['季节性情绪抑郁症状病因']

            if '忌吃食物' in data_json:
                disease_dict['忌吃食物'] = data_json['忌吃食物']
            if '宜吃食物' in data_json:
                disease_dict['宜吃食物'] = data_json['宜吃食物']

            # 症状
            if '情绪低落' in data_json:
                disease_dict['情绪低落']=data_json['情绪低落']
            if '疑病性' in data_json:
                disease_dict['疑病性'] = data_json['疑病性']
            if '激越性' in data_json:
                disease_dict['激越性'] = data_json['激越性']
            if '隐匿性' in data_json:
                disease_dict['隐匿性'] = data_json['隐匿性']
            if "迟滞性"in data_json:
                disease_dict['迟滞性'] = data_json['迟滞性']
            if '妄想性' in data_json:
                disease_dict['妄想性'] = data_json['妄想性']
            if '抑郁症性假性痴呆' in data_json:
                disease_dict['抑郁症性假性痴呆'] = data_json['抑郁症性假性痴呆']
            if '自杀倾向' in data_json:
                disease_dict['自杀倾向'] = data_json['自杀倾向']
            if '季节性' in data_json:
                disease_dict['季节性'] = data_json['季节性']
            if '其他' in data_json:
                disease_dict['其他'] = data_json['其他']
            if '焦虑抑郁和激越的混合状态' in data_json:
                disease_dict['焦虑抑郁和激越的混合状态'] = data_json['焦虑抑郁和激越的混合状态']
            if '兴趣索然' in data_json:
                disease_dict['兴趣索然'] = data_json['兴趣索然']
            if "精力下降"in data_json:
                disease_dict['精力下降'] = data_json['精力下降']
            if '自我评价过低' in data_json:
                disease_dict['自我评价过低'] = data_json['自我评价过低']
            if '运动抑制' in data_json:
                disease_dict['运动抑制']=data_json['运动抑制']
            if '自杀观念行为' in data_json:
                disease_dict['自杀观念行为']=data_json['自杀观念行为']
            if '心境昼夜节律改变' in data_json:
                disease_dict['心境昼夜节律改变']=data_json['心境昼夜节律改变']
            if '心血管系统' in data_json:
                disease_dict['心血管系统'] = data_json['心血管系统']
            if '消化系统' in data_json:
                disease_dict['消化系统'] = data_json['消化系统']
            if '思维迟缓' in data_json:
                disease_dict['思维迟缓'] =data_json['思维迟缓']
            if '自主神经系统' in data_json:
                disease_dict['自主神经系统'] = data_json['自主神经系统']
            if '抑郁心境' in data_json:
                disease_dict['抑郁心境']=data_json['抑郁心境']
            if '抑郁症三大主要症状' in data_json:
                disease_dict['抑郁症三大主要症状']=data_json['抑郁症三大主要症状']
            if '意志活动减退' in data_json:
                disease_dict['意志活动减退']=data_json['意志活动减退']
            if '隐匿性抑郁症' in data_json:
                disease_dict['隐匿性抑郁症']=data_json['隐匿性抑郁症']
            if '其它躯体症状' in data_json:
                disease_dict['其它躯体症状'] = data_json['其它躯体症状']

            if '抑郁症心境不同' in data_json:
                disease_dict['抑郁症心境不同']=data_json['抑郁症心境不同']
            if '丧失兴趣' in data_json:
                disease_dict['丧失兴趣']=data_json['丧失兴趣']
            if '精力丧失' in data_json:
                disease_dict['精力丧失']=data_json['精力丧失']
            if '病人呈现显著持续普遍抑郁症' in data_json:
                disease_dict['病人呈显著持续普遍抑郁状态']=data_json['病人呈现显著持续普遍抑郁症']
            if '消极悲观' in data_json:
                disease_dict['消极悲观']=data_json['消极悲观']
            if '躯体或生物学症状' in data_json:
                disease_dict['躯体或生物学症状']=data_json['躯体或生物学症状']
            if '食欲不振体重减轻' in data_json:
                disease_dict['食欲不振体重减轻']=data_json['食欲不振体重减轻']
            if '性功能障碍' in data_json:
                disease_dict['性功能障碍']=data_json['性功能障碍']
            if '睡眠障碍' in data_json:
                disease_dict['睡眠障碍']=data_json['睡眠障碍']
            if '昼夜变化' in data_json:
                disease_dict['昼夜变化']=data_json['昼夜变化']

            if '情感方面' in data_json:
                disease_dict['情感方面'] = data_json['情感方面']
            if '思维方面' in data_json:
                disease_dict['思维方面'] = data_json['思维方面']
            if '行为异常' in data_json:
                disease_dict['行为异常']=data_json['行为异常']
            if '躯体症状' in data_json:
                disease_dict['躯体症状']=data_json['躯体症状']
            if '心境高涨' in data_json:
                disease_dict['心境高涨'] = data_json['心境高涨']
            if '思维奔逸' in data_json:
                disease_dict['思维奔逸'] = data_json['思维奔逸']
            if '活动增多' in data_json:
                disease_dict['活动增多']=data_json['活动增多']
            if '精神运动性兴奋' in data_json:
                disease_dict['精神运动性兴奋']=data_json['精神运动性兴奋']
            if '自我评价过高' in data_json:
                disease_dict['自我评价过高'] = data_json['自我评价过高']

            if '保持乐观愉快的情绪' in data_json:
                disease_dict['保持乐观愉快的情绪'] = data_json['保持乐观愉快的情绪']
            if '合理作息' in data_json:
                disease_dict['合理作息'] = data_json['合理作息']
            if '合理膳食' in data_json:
                disease_dict['合理膳食'] = data_json['合理膳食']

            if '偏头痛' in data_json:
                disease_dict['偏头痛'] = data_json['偏头痛']
            if '哮喘' in data_json:
                disease_dict['哮喘'] = data_json['哮喘']
            if '心血管疾病' in data_json:
                disease_dict['心血管疾病'] = data_json['心血管疾病']
            if '多发性硬化' in data_json:
                disease_dict['多发性硬化'] = data_json['多发性硬化']
            if '抑郁性神经症症状说明' in data_json:
                disease_dict['抑郁性神经症症状说明'] = data_json['抑郁性神经症症状说明']

            # 鉴别对象
            if '内源性抑郁症' in data_json:
                disease_dict['内源性抑郁症']=data_json['内源性抑郁症']
            if '继发性抑郁症' in data_json:
                disease_dict['继发性抑郁症'] = data_json['继发性抑郁症']
            if '抑郁症性假性痴呆' in data_json:
                disease_dict['抑郁症性假性痴呆'] = data_json['抑郁症性假性痴呆']
            if '焦虑症' in data_json:
                disease_dict['焦虑症'] = data_json['焦虑症']
            if '过度悲伤' in data_json:
                disease_dict['过度悲伤'] = data_json['过度悲伤']
            if '反应性抑郁症' in data_json:
                disease_dict['反应性抑郁症']=data_json['反应性抑郁症']
            if '以学习困难为特征的抑郁症' in data_json:
                disease_dict['以学习困难为特征的抑郁症']=data_json['以学习困难为特征的抑郁症']
            if '药物引起的继发性抑郁症' in data_json:
                disease_dict['药物引起的继发性抑郁症']=data_json['药物引起的继发性抑郁症']
            if '躯体疾病引起的继发性抑郁症' in data_json:
                disease_dict['躯体疾病引起的继发性抑郁症']=data_json['躯体疾病引起的继发性抑郁症']
            if '产后抑郁症' in data_json:
                disease_dict['产后抑郁症']=data_json['产后抑郁症']
            if '躯体疾病' in data_json:
                disease_dict['躯体疾病']=data_json['躯体疾病']
            if '五行音乐疗法' in data_json:
                disease_dict['五行音乐疗法']=data_json['五行音乐疗法']

            if '针刺疗法' in data_json:
                disease_dict['针刺疗法'] = data_json['针刺疗法']
            if '艾灸疗法' in data_json:
                disease_dict['艾灸疗法'] = data_json['艾灸疗法']
            if '耳穴法' in data_json:
                disease_dict['耳穴法'] = data_json['耳穴法']
            if '穴位注射法' in data_json:
                disease_dict['穴位注射法'] = data_json['穴位注射法']
            if '针药联合法' in data_json:
                disease_dict['针药联合法'] = data_json['针药联合法']
            if '产后抑郁症' in data_json:
                disease_dict['产后抑郁症'] = data_json['产后抑郁症']
            if '躯体疾病' in data_json:
                disease_dict['躯体疾病'] = data_json['躯体疾病']

            if '抑郁性神经症或心境恶劣障碍' in data_json:
                disease_dict['抑郁性神经症或心境恶劣障碍'] = data_json['抑郁性神经症或心境恶劣障碍']
            if '心因性抑郁症' in data_json:
                disease_dict['心因性抑郁症'] = data_json['心因性抑郁症']
            if '精神分裂症' in data_json:
                disease_dict['精神分裂症'] = data_json['精神分裂症']
            if '癫痫性病理心境恶劣' in data_json:
                disease_dict['癫痫性病理心境恶劣'] = data_json['癫痫性病理心境恶劣']

            if '狂躁躯体疾病' in data_json:
                disease_dict['狂躁躯体疾病'] = data_json['狂躁躯体疾病']
            if '药物' in data_json:
                disease_dict['药物'] = data_json['药物']
            if '抑郁躯体疾病' in data_json:
                disease_dict['抑郁躯体疾病'] = data_json['抑郁躯体疾病']
            if '神经系统疾病' in data_json:
                disease_dict['神经系统疾病'] = data_json['神经系统疾病']
            if '痴呆' in data_json:
                disease_dict['痴呆'] = data_json['痴呆']
            if '其他精神障碍' in data_json:
                disease_dict['其他精神障碍'] = data_json['其他精神障碍']

            if '神经衰弱' in data_json:
                disease_dict['神经衰弱'] = data_json['神经衰弱']
            if '中毒性精神病' in data_json:
                disease_dict['中毒性精神病'] = data_json['中毒性精神病']
            if '症状性精神病' in data_json:
                disease_dict['症状性精神病'] = data_json['症状性精神病']

            if '神经症性抑郁' in data_json:
                disease_dict['神经症性抑郁'] = data_json['神经症性抑郁']
            if '情感性精神障碍抑郁发作' in data_json:
                disease_dict['情感性精神障碍抑郁发作'] = data_json['情感性精神障碍抑郁发作']
            if '情感性精神障碍抑郁' in data_json:
                disease_dict['情感性精神障碍抑郁'] = data_json['情感性精神障碍抑郁']

            if '正念减压联合认知行为干预' in data_json:
                disease_dict['正念减压联合认知行为干预'] = data_json['正念减压联合认知行为干预']
            if '心理认知干预' in data_json:
                disease_dict['心理认知干预'] = data_json['心理认知干预']

            if '情绪宣泄支持' in data_json:
                disease_dict['情绪宣泄支持'] = data_json['情绪宣泄支持']
            if '丰富精神活动' in data_json:
                disease_dict['丰富精神活动'] = data_json['丰富精神活动']
            if '社会支持' in data_json:
                disease_dict['社会支持'] = data_json['社会支持']
            if '衔接支持' in data_json:
                disease_dict['衔接支持'] = data_json['衔接支持']
            if '定期随访' in data_json:
                disease_dict['定期随访'] = data_json['定期随访']

            # 病因
            if '遗传因素' in data_json:
                disease_dict['遗传因素']=data_json['遗传因素']
            if '去甲肾上腺素系统' in data_json:
                disease_dict['去甲肾上腺素系统']=data_json['去甲肾上腺素系统']
            if '羟色胺系统' in data_json:
                disease_dict['羟色胺系统']=data_json['羟色胺系统']
            if '多巴胺系统' in data_json:
                disease_dict['多巴胺系统'] = data_json['多巴胺系统']
            if '乙酰胆碱系统' in data_json:
                disease_dict['乙酰胆碱系统'] = data_json['乙酰胆碱系统']
            if '促肾上腺皮质激素系统' in data_json:
                disease_dict['促肾上腺皮质激素系统'] = data_json['促肾上腺皮质激素系统']
            if '生长激素系统' in data_json:
                disease_dict['生长激素系统'] = data_json['生长激素系统']
            if '促甲状腺激素系统' in data_json:
                disease_dict['促甲状腺激素系统'] = data_json['促甲状腺激素系统']
            if '生物节律变化' in data_json:
                disease_dict['生物节律变化'] = data_json['生物节律变化']
            if '脑组织结构改变' in data_json:
                disease_dict['脑组织结构改变'] = data_json['脑组织结构改变']
            if '遗传因素与APOE基因' in data_json:
                disease_dict['遗传因素与APOE基因'] = data_json['遗传因素与APOE基因']
            if '遗传因素与APOE基因' in data_json:
                disease_dict['遗传因素与APOE基因'] = data_json['遗传因素与APOE基因']
            if '心理社会因素' in data_json:
                disease_dict['心理社会因素'] = data_json['心理社会因素']
            if '神经生化因素' in data_json:
                disease_dict['神经生化因素'] = data_json['神经生化因素']
            if '体质因素' in data_json:
                disease_dict['体质因素']=data_json['体质因素']
            if '中枢神经介质的功能及代谢异常' in data_json:
                disease_dict['中枢神经介质的功能及代谢异常'] = data_json['中枢神经介质的功能及代谢异常']
            if '精神因素说明' in data_json:
                disease_dict['精神因素说明'] = data_json['精神因素说明']
            if '抑郁症并发症' in data_json:
                disease_dict['抑郁症并发症']=data_json['抑郁症并发症']
            if '体因性抑郁症' in data_json:
                disease_dict['体因性抑郁症'] = data_json['体因性抑郁症']
            if '轻性抑郁' in data_json:
                disease_dict['轻性抑郁'] = data_json['轻性抑郁']
            if '心因性和反应性抑郁症' in data_json:
                disease_dict['心因性和反应性抑郁症'] = data_json['心因性和反应性抑郁症']
            if '抑郁症鉴别排除标准' in data_json:
                disease_dict['抑郁症鉴别排除标准'] = data_json['抑郁症鉴别排除标准']
            if '情感性障碍因素' in data_json:
                disease_dict['情感性障碍因素'] = data_json['情感性障碍因素']

            if '双相情感障碍' in data_json:
                disease_dict['双相情感障碍'] = data_json['双相情感障碍']
            if '继发性抑郁障碍' in data_json:
                disease_dict['继发性抑郁障碍'] = data_json['继发性抑郁障碍']
            if '创伤后应激障碍' in data_json:
                disease_dict['创伤后应激障碍'] = data_json['创伤后应激障碍']

            if '思维障碍' in data_json:
                disease_dict['思维障碍'] = data_json['思维障碍']
            if '运动行为抑制' in data_json:
                disease_dict['运动行为抑制'] = data_json['运动行为抑制']
            if '认知功能障碍' in data_json:
                disease_dict['认知功能障碍'] = data_json['认知功能障碍']

            if '激素水平改变' in data_json:
                disease_dict['激素水平改变'] = data_json['激素水平改变']
            if '角色转变' in data_json:
                disease_dict['角色转变'] = data_json['角色转变']
            if '生活状态改变' in data_json:
                disease_dict['生活状态改变'] = data_json['生活状态改变']
            if '过于担忧' in data_json:
                disease_dict['过于担忧'] = data_json['过于担忧']

            if '经济因素' in data_json:
                disease_dict['经济因素'] = data_json['经济因素']
            if '家族因素' in data_json:
                disease_dict['家族因素'] = data_json['家族因素']
            if '其他因素' in data_json:
                disease_dict['其他因素'] = data_json['其他因素']


            if '神经内分泌' in data_json:
                disease_dict['神经内分泌'] = data_json['神经内分泌']
            if '神经免疫学' in data_json:
                disease_dict['神经免疫学'] = data_json['神经免疫学']
            if '睡眠与脑电' in data_json:
                disease_dict['睡眠与脑电'] = data_json['睡眠与脑电']
            if '脑影像学' in data_json:
                disease_dict['脑影像学'] = data_json['脑影像学']
            if '遗传学研究' in data_json:
                disease_dict['遗传学研究'] = data_json['遗传学研究']
            if '心理社会' in data_json:
                disease_dict['心理社会'] = data_json['心理社会']
            if '生物胺' in data_json:
                disease_dict['生物胺'] = data_json['生物胺']
            if '氨基酸肽类' in data_json:
                disease_dict['氨基酸肽类'] = data_json['氨基酸肽类']
            if '第二信使系统' in data_json:
                disease_dict['第二信使系统'] = data_json['第二信使系统']

            if '心理因素说明' in data_json:
                disease_dict['心理因素说明'] = data_json['心理因素说明']
            if '内分泌' in data_json:
                disease_dict['内分泌'] = data_json['内分泌']
            if '遗传' in data_json:
                disease_dict['遗传'] = data_json['遗传']

            if '年龄因素' in data_json:
                disease_dict['年龄因素'] = data_json['年龄因素']

            if '生物学因素' in data_json:
                disease_dict['生物学因素'] = data_json['生物学因素']
            if '病理心理因素' in data_json:
                disease_dict['病理心理因素'] = data_json['病理心理因素']
            if '社会心理因素' in data_json:
                disease_dict['社会心理因素'] = data_json['社会心理因素']

            if '神经递质学说' in data_json:
                disease_dict['神经递质学说'] = data_json['神经递质学说']
            if '神经回路学说' in data_json:
                disease_dict['神经回路学说'] = data_json['神经回路学说']

            if '生物学原因' in data_json:
                disease_dict['生物学原因'] = data_json['生物学原因']
            if '社会心理学假设' in data_json:
                disease_dict['社会心理学假设'] = data_json['社会心理学假设']

            #治疗方法
            if '西药治疗说明' in data_json:
                disease_dict['西药治疗说明']=data_json['西药治疗说明']
            if '药物选择' in data_json:
                disease_dict['药物选择'] = data_json['药物选择']
            if '双相抑郁和单相抑郁治疗方式' in data_json:
                disease_dict['双相抑郁和单相抑郁治疗方式'] = data_json['双相抑郁和单相抑郁治疗方式']
            if '疗程和剂量' in data_json:
                disease_dict['疗程和剂量'] = data_json['疗程和剂量']
            if '认知治疗' in data_json:
                disease_dict['认知治疗']=data_json['认知治疗']
            if '电痉挛疗法' in data_json:
                disease_dict['电痉挛疗法'] = data_json['电痉挛疗法']
            if '替代性疗法' in data_json:
                disease_dict['替代性疗法'] = data_json['替代性疗法']
            if '实验疗法' in data_json:
                disease_dict['实验疗法'] = data_json['实验疗法']
            if '女性荷尔蒙补充疗法HRT' in data_json:
                disease_dict['女性荷尔蒙补充疗法HRT'] = data_json['女性荷尔蒙补充疗法HRT']
            if '反射疗法' in data_json:
                disease_dict['反射疗法'] = data_json['反射疗法']
            if '运动疗法' in data_json:
                disease_dict['运动疗法'] = data_json['运动疗法']
            if '一般治疗' in data_json:
                disease_dict['一般治疗'] = data_json['一般治疗']
            if '药物治疗说明' in data_json:
                disease_dict['药物治疗说明'] = data_json['药物治疗说明']
            if '阿米替林' in data_json:
                disease_dict['阿米替林'] = data_json['阿米替林']
            if '电休克治疗' in data_json:
                disease_dict['电休克治疗'] = data_json['电休克治疗']
            if '物理治疗介绍' in data_json:
                disease_dict['物理治介绍'] = data_json['物理治疗介绍']
            if '教育' in data_json:
                disease_dict['教育'] = data_json['教育']
            if '其他治疗' in data_json:
                disease_dict['其他治疗'] = data_json['其他治疗']
            if '择优规范治疗' in data_json:
                disease_dict['择优规范治疗'] = data_json['择优规范治疗']
            if '康复治疗' in data_json:
                disease_dict['康复治疗'] = data_json['康复治疗']
            if '三环类抗抑郁药' in data_json:
                disease_dict['三环类抗抑郁药'] = data_json['三环类抗抑郁药']
            if '四环类抗抑郁剂' in data_json:
                disease_dict['四环类抗抑郁剂'] = data_json['四环类抗抑郁剂']
            if '单胺氧化酶抑制剂' in data_json:
                disease_dict['单胺氧化酶抑制剂'] = data_json['单胺氧化酶抑制剂']
            if '选择性羟色胺再摄取抑制剂' in data_json:
                disease_dict['选择性羟色胺再摄取抑制剂'] = data_json['选择性羟色胺再摄取抑制剂']
            if '其他新型抗抑郁药' in data_json:
                disease_dict['其他新型抗抑郁药'] = data_json['其他新型抗抑郁药']
            if '抗抑郁治疗的疗程' in data_json:
                disease_dict['抗抑郁治疗的疗程'] = data_json['抗抑郁治疗的疗程']
            if '行为治疗' in data_json:
                disease_dict['行为治疗'] = data_json['行为治疗']
            if '人际关系治疗' in data_json:
                disease_dict['人际关系治疗'] = data_json['人际关系治疗']
            if '各种胺代谢与修正胺假说' in data_json:
                disease_dict['各种胺代谢与修正胺假说'] = data_json['各种胺代谢与修正胺假说']
            if '团体心理治疗' in data_json:
                disease_dict['团体心理治疗'] = data_json['团体心理治疗']

            if '太阳浴治疗' in data_json:
                disease_dict['太阳浴治疗'] = data_json['太阳浴治疗']
            if '白色灯管治疗' in data_json:
                disease_dict['白色灯管治疗'] = data_json['白色灯管治疗']
            if '舍曲林联合重复经颅磁刺激治疗' in data_json:
                disease_dict['舍曲林联合重复经颅磁刺激治疗'] = data_json['舍曲林联合重复经颅磁刺激治疗']

            if '家人的理解和关心' in data_json:
                disease_dict['家人的理解和关心'] = data_json['家人的理解和关心']
            if '增强产妇的体质' in data_json:
                disease_dict['增强产妇的体质'] = data_json['增强产妇的体质']
            if '产前抑郁症心理治疗' in data_json:
                disease_dict['产前抑郁症心理治疗'] = data_json['产前抑郁症心理治疗']
            if '绝经抑郁症心理治疗' in data_json:
                disease_dict['绝经抑郁症心理治疗'] = data_json['绝经抑郁症心理治疗']

            if '扯下微笑的伪面具' in data_json:
                disease_dict['扯下微笑的伪面具'] = data_json['扯下微笑的伪面具']
            if '不要让不良情绪转化' in data_json:
                disease_dict['不要让不良情绪转化'] = data_json['不要让不良情绪转化']
            if '通过饮食缓解不适' in data_json:
                disease_dict['通过饮食缓解不适'] = data_json['通过饮食缓解不适']
            if '学点自我安慰和放松的技巧' in data_json:
                disease_dict['学点自我安慰和放松的技巧'] = data_json['学点自我安慰和放松的技巧']
            if '建立心理支持系统' in data_json:
                disease_dict['建立心理支持系统'] = data_json['建立心理支持系统']
            if '换一个角度看待生活和工作的关系' in data_json:
                disease_dict['换一个角度看待生活和工作的关系'] = data_json['换一个角度看待生活和工作的关系']

            if '健脾疏肝' in data_json:
                disease_dict['健脾疏肝'] = data_json['健脾疏肝']
            if '通督启神' in data_json:
                disease_dict['通督启神'] = data_json['通督启神']
            if '调神疏肝' in data_json:
                disease_dict['调神疏肝'] = data_json['调神疏肝']
            if '醒脑开窍' in data_json:
                disease_dict['醒脑开窍'] = data_json['醒脑开窍']
            if '头穴丛刺' in data_json:
                disease_dict['头穴丛刺'] = data_json['头穴丛刺']
            if '十三鬼穴' in data_json:
                disease_dict['十三鬼穴'] = data_json['十三鬼穴']
            if '针刺结合心理疗法' in data_json:
                disease_dict['针刺结合心理疗法'] = data_json['针刺结合心理疗法']
            if '针刺结合音乐疗法' in data_json:
                disease_dict['针刺结合音乐疗法'] = data_json['针刺结合音乐疗法']
            if '针刺结合推拿疗法' in data_json:
                disease_dict['针刺结合推拿疗法'] = data_json['针刺结合推拿疗法']
            if '针刺结合穴位注射疗法' in data_json:
                disease_dict['针刺结合穴位注射疗法'] = data_json['针刺结合穴位注射疗法']
            if '电针疗法' in data_json:
                disease_dict['电针疗法'] = data_json['电针疗法']
            if '针刺结合艾灸治疗法' in data_json:
                disease_dict['针刺结合艾灸治疗法'] = data_json['针刺结合艾灸治疗法']
            if '针刺结合耳穴疗法' in data_json:
                disease_dict['针刺结合耳穴疗法'] = data_json['针刺结合耳穴疗法']

            if '分娩过程中护理人员尽量在旁陪伴和指导' in data_json:
                disease_dict['分娩过程中护理人员尽量在旁陪伴和指导'] = data_json['分娩过程中护理人员尽量在旁陪伴和指导']
            if '产后给予一个安静舒适的环境' in data_json:
                disease_dict['产后给予一个安静舒适的环境'] = data_json['产后给予一个安静舒适的环境']
            if '对产妇的家庭成员进行心理卫生方面的宣教' in data_json:
                disease_dict['对产妇的家庭成员进行心理卫生方面的宣教'] = data_json['对产妇的家庭成员进行心理卫生方面的宣教']


            if '中药治疗说明' in data_json:
                disease_dict['中药治疗'] = data_json['中药治疗说明']
            if '肝气郁结者' in data_json:
                disease_dict['肝气郁结者'] = data_json['肝气郁结者']
            if '气郁化火上逆者' in data_json:
                disease_dict['气郁化火上逆者'] = data_json['气郁化火上逆者']
            if '痰气郁结者' in data_json:
                disease_dict['痰气郁结者'] = data_json['痰气郁结者']
            if '久郁伤神者' in data_json:
                disease_dict['久郁伤神者'] = data_json['久郁伤神者']
            if '阴虚火旺者' in data_json:
                disease_dict['阴虚火旺者'] = data_json['阴虚火旺者']
            if '肝气郁结型' in data_json:
                disease_dict['肝气郁结型'] = data_json['肝气郁结型']
            if '气郁化火型' in data_json:
                disease_dict['气郁化火型'] = data_json['气郁化火型']
            if '血行郁滞型' in data_json:
                disease_dict['血行郁滞型'] = data_json['血行郁滞型']
            if '痰气郁结型' in data_json:
                disease_dict['痰气郁结型'] = data_json['痰气郁结型']
            if '心阴亏虚型' in data_json:
                disease_dict['心阴亏虚型'] = data_json['心阴亏虚型']
            if '心脾两虚型' in data_json:
                disease_dict['心脾两虚型'] = data_json['心脾两虚型']
            if '肝肾阴虚型' in data_json:
                disease_dict['肝肾阴虚型'] = data_json['肝肾阴虚型']

            if '肝郁脾虚' in data_json:
                disease_dict['肝郁脾虚'] = data_json['肝郁脾虚']
            if '气滞血淤' in data_json:
                disease_dict['气滞血淤'] = data_json['气滞血淤']
            if '心脾两虚' in data_json:
                disease_dict['心脾两虚'] = data_json['心脾两虚']
            if '脾肾阳虚' in data_json:
                disease_dict['脾肾阳虚'] = data_json['脾肾阳虚']
            if '阴虚火旺' in data_json:
                disease_dict['阴虚火旺'] = data_json['阴虚火旺']


            if '痰热扰胆气滞扰心' in data_json:
                disease_dict['痰热扰胆气滞扰心'] = data_json['痰热扰胆气滞扰心']
            if '火内扰热陷心包' in data_json:
                disease_dict['火内扰热陷心包'] = data_json['火内扰热陷心包']
            if '火盛阴虚气血双虚' in data_json:
                disease_dict['火盛阴虚气血双虚'] = data_json['火盛阴虚气血双虚']
            if '火盛阴虚气血双虚' in data_json:
                disease_dict['火盛阴虚气血双虚'] = data_json['火盛阴虚气血双虚']
            if '抗精神病药治疗' in data_json:
                disease_dict['抗精神病药治疗'] = data_json['抗精神病药治疗']
            if '锂盐治疗' in data_json:
                disease_dict['锂盐治疗'] = data_json['锂盐治疗']

            if '抑郁性神经症心理治疗心理治疗' in data_json:
                disease_dict['抑郁性神经症心理治疗心理治疗'] = data_json['抑郁性神经症心理治疗心理治疗']
            if '产后抑郁症心理治疗' in data_json:
                disease_dict['产后抑郁症心理治疗'] = data_json['产后抑郁症心理治疗']
            if '成功后抑郁症心理治疗' in data_json:
                disease_dict['成功后抑郁症心理治疗'] = data_json['成功后抑郁症心理治疗']
            if '老年期抑郁症心理治疗' in data_json:
                disease_dict['老年期抑郁症心理治疗'] = data_json['老年期抑郁症心理治疗']


            if '常见问诊内容' in data_json:
                disease_dict['常见问诊内容']=data_json['常见问诊内容']
            if '颅脑CT检查' in data_json:
                disease_dict['颅脑CT检查'] = data_json['颅脑CT检查']
            if '脑氧代谢显像检查' in data_json:
                disease_dict['脑氧代谢显像检查'] = data_json['脑氧代谢显像检查']
            # 护理
            if '仔细观察病人情况' in data_json:
                disease_dict['仔细观察病人情况']=data_json['仔细观察病人情况']
            if '按医嘱要求确保病人不间断按量服制剂' in data_json:
                disease_dict['按医嘱要求确保病人不间断按量服制剂'] = data_json['按医嘱要求确保病人不间断按量服制剂']
            if '提高病人对外界变化的承受力' in data_json:
                disease_dict['提高病人对外界变化的承受力'] = data_json['提高病人对外界变化的承受力']
            if '防范病人可能出现的各种高危险行为' in data_json:
                disease_dict['防范病人可能出现的各种高危险行为'] = data_json['防范病人可能出现的各种高危险行为']
            if '家属注意自身心理健康状况' in data_json:
                disease_dict['家属注意自身心理健康状况'] = data_json['家属注意自身心理健康状况']
            if '及时送到医院就诊' in data_json:
                disease_dict['及时送到医院就诊'] = data_json['及时送到医院就诊']
            if '一般护理' in data_json:
                disease_dict['一般护理'] = data_json['一般护理']
            if '建立良好的治疗性人际关系' in data_json:
                disease_dict['建立良好的治疗性人际关系'] = data_json['建立良好的治疗性人际关系']
            if '安置患者住在护理人员易观察的大房间' in data_json:
                disease_dict['安置患者住在护理人员易观察的大房间'] = data_json['安置患者住在护理人员易观察的大房间']
            if '严格执行整体护理管理制度' in data_json:
                disease_dict['严格执行整体护理管理制度'] = data_json['严格执行整体护理管理制度']
            if '加强对病房设施的安全检查' in data_json:
                disease_dict['加强对病房设施的安全检查'] = data_json['加强对病房设施的安全检查']

            if '注意睡眠饮食和运动' in data_json:
                disease_dict['注意睡眠饮食和运动'] = data_json['注意睡眠饮食和运动']
            if '明确你的价值和目标' in data_json:
                disease_dict['明确你的价值和目标'] = data_json['明确你的价值和目标']
            if '将欢乐带入生活' in data_json:
                disease_dict['将欢乐带入生活'] = data_json['将欢乐带入生活']
            if '不要孤注一挪' in data_json:
                disease_dict['不要孤注一挪'] = data_json['不要孤注一挪']
            if '建立可靠的人际关系' in data_json:
                disease_dict['建立可靠的人际关系'] = data_json['建立可靠的人际关系']

            if '预防意外' in data_json:
                disease_dict['预防意外'] = data_json['预防意外']
            if '转移注意' in data_json:
                disease_dict['转移注意'] = data_json['转移注意']
            if '饮食禁忌' in data_json:
                disease_dict['饮食禁忌'] = data_json['饮食禁忌']
            if '饮食适宜' in data_json:
                disease_dict['饮食适宜'] = data_json['饮食适宜']
            if '生活照顾' in data_json:
                disease_dict['生活照顾'] = data_json['生活照顾']
            if '坚持服药' in data_json:
                disease_dict['坚持服药'] = data_json['坚持服药']
            if '心灵沟通' in data_json:
                disease_dict['心灵沟通'] = data_json['心灵沟通']

            if '遗传护理' in data_json:
                disease_dict['遗传护理'] = data_json['遗传护理']
            if '预防护理' in data_json:
                disease_dict['预防护理'] = data_json['预防护理']
            if '生活护理' in data_json:
                disease_dict['生活护理'] = data_json['生活护理']

            if '健康教育' in data_json:
                disease_dict['健康教育'] = data_json['健康教育']
            if '心理护理说明' in data_json:
                disease_dict['心理护理说明'] = data_json['心理护理说明']
            if '共情护理' in data_json:
                disease_dict['共情护理'] = data_json['共情护理']
            if '环境护理' in data_json:
                disease_dict['环境护理'] = data_json['环境护理']
            if '睡眠指导' in data_json:
                disease_dict['睡眠指导'] = data_json['睡眠指导']
            if '活动干预' in data_json:
                disease_dict['活动干预'] = data_json['活动干预']
            if '耳穴掀针' in data_json:
                disease_dict['耳穴掀针'] = data_json['耳穴掀针']
            #检查
            if '尿常规基本信息' in data_json:
                disease_dict['尿常规基本信息'] = data_json['尿常规基本信息']
            if '尿常规注意事项' in data_json:
                disease_dict['尿常规注意事项'] = data_json['尿常规注意事项']
            if '尿常规检查作用' in data_json:
                disease_dict['尿常规检查作用'] = data_json['尿常规检查作用']
            if '尿常规检查过程' in data_json:
                disease_dict['尿常规检查过程'] = data_json['尿常规检查过程']

            if '维生素B12基本信息' in data_json:
                disease_dict['维生素B12基本信息'] = data_json['维生素B12基本信息']
            if '维生素B12注意事项' in data_json:
                disease_dict['维生素B12注意事项'] = data_json['维生素B12注意事项']
            if '维生素B12检查作用' in data_json:
                disease_dict['维生素B12检查作用'] = data_json['维生素B12检查作用']
            if '维生素B12检查过程' in data_json:
                disease_dict['维生素B12检查过程'] = data_json['维生素B12检查过程']

            if '叶酸基本信息' in data_json:
                disease_dict['叶酸基本信息'] = data_json['叶酸基本信息']
            if '叶酸注意事项' in data_json:
                disease_dict['叶酸注意事项'] = data_json['叶酸注意事项']
            if '叶酸检查作用' in data_json:
                disease_dict['叶酸检查作用'] = data_json['叶酸检查作用']
            if '叶酸检查过程' in data_json:
                disease_dict['叶酸检查过程'] = data_json['叶酸检查过程']

            if '脑电图基本信息' in data_json:
                disease_dict['脑电图基本信息'] = data_json['脑电图基本信息']
            if '脑电图注意事项' in data_json:
                disease_dict['脑电图注意事项'] = data_json['脑电图注意事项']
            if '脑电图检查作用' in data_json:
                disease_dict['脑电图检查作用'] = data_json['脑电图检查作用']
            if '脑电图检查过程' in data_json:
                disease_dict['脑电图检查过程'] = data_json['脑电图检查过程']

            if '心电图基本信息' in data_json:
                disease_dict['心电图基本信息'] = data_json['心电图基本信息']
            if '心电图注意事项' in data_json:
                disease_dict['心电图注意事项'] = data_json['心电图注意事项']
            if '心电图检查作用' in data_json:
                disease_dict['心电图检查作用'] = data_json['脑电图检查作用']
            if '心电图检查过程' in data_json:
                disease_dict['心电图检查过程'] = data_json['心电图检查过程']

            if '性激素六项检查基本信息' in data_json:
                disease_dict['性激素六项检查基本信息'] = data_json['性激素六项检查基本信息']
            if '性激素六项检查注意事项' in data_json:
                disease_dict['性激素六项检查注意事项'] = data_json['性激素六项检查注意事项']
            if '性激素六项检查作用' in data_json:
                disease_dict['性激素六项检查作用'] = data_json['性激素六项检查作用']
            if '性激素六项检查过程' in data_json:
                disease_dict['性激素六项检查过程'] = data_json['性激素六项检查过程']

            if '血清T3T4抗体基本信息' in data_json:
                disease_dict['血清T3T4抗体基本信息'] = data_json['血清T3T4抗体基本信息']
            if '血清T3T4抗体注意事项' in data_json:
                disease_dict['血清T3T4抗体注意事项'] = data_json['血清T3T4抗体注意事项']
            if '血清T3T4抗体检查作用' in data_json:
                disease_dict['血清T3T4抗体检查作用'] = data_json['血清T3T4抗体检查作用']
            if '血清T3T4抗体检查过程' in data_json:
                disease_dict['血清T3T4抗体检查过程'] = data_json['血清T3T4抗体检查过程']

            if '脑脊液镁基本信息' in data_json:
                disease_dict['脑脊液镁基本信息'] = data_json['脑脊液镁基本信息']
            if '脑脊液镁注意事项' in data_json:
                disease_dict['脑脊液镁注意事项'] = data_json['脑脊液镁注意事项']
            if '脑脊液镁检查作用' in data_json:
                disease_dict['脑脊液镁检查作用'] = data_json['脑脊液镁检查作用']
            if '脑脊液镁检查过程' in data_json:
                disease_dict['脑脊液镁检查过程'] = data_json['脑脊液镁检查过程']

            if '促黄体生成素基本信息' in data_json:
                disease_dict['促黄体生成素基本信息'] = data_json['促黄体生成素基本信息']
            if '促黄体生成素注意事项' in data_json:
                disease_dict['促黄体生成素注意事项'] = data_json['促黄体生成素注意事项']
            if '促黄体生成素检查作用' in data_json:
                disease_dict['促黄体生成素检查作用'] = data_json['促黄体生成素检查作用']
            if '促黄体生成素检查过程' in data_json:
                disease_dict['促黄体生成素检查过程'] = data_json['促黄体生成素检查过程']

            if '多普勒超声心动图基本信息' in data_json:
                disease_dict['多普勒超声心动图基本信息'] = data_json['多普勒超声心动图基本信息']
            if '多普勒超声心动图注意事项' in data_json:
                disease_dict['多普勒超声心动图注意事项'] = data_json['多普勒超声心动图注意事项']
            if '多普勒超声心动图检查作用' in data_json:
                disease_dict['多普勒超声心动图检查作用'] = data_json['多普勒超声心动图检查作用']
            if '多普勒超声心动图检查过程' in data_json:
                disease_dict['多普勒超声心动图检查过程'] = data_json['多普勒超声心动图检查过程']

            if '健康体检基本信息' in data_json:
                disease_dict['健康体检基本信息'] = data_json['健康体检基本信息']
            if '健康体检注意事项' in data_json:
                disease_dict['健康体检注意事项'] = data_json['健康体检注意事项']
            if '健康体检检查作用' in data_json:
                disease_dict['健康体检检查作用'] = data_json['健康体检检查作用']
            if '健康体检检查过程' in data_json:
                disease_dict['健康体检检查过程'] = data_json['健康体检检查过程']

            if '颅脑CT检查基本信息' in data_json:
                disease_dict['颅脑CT检查基本信息'] = data_json['颅脑CT检查基本信息']
            if '颅脑CT检查注意事项' in data_json:
                disease_dict['颅脑CT检查注意事项'] = data_json['颅脑CT检查注意事项']
            if '颅脑CT检查作用' in data_json:
                disease_dict['颅脑CT检查作用'] = data_json['颅脑CT检查作用']
            if '颅脑CT检查过程' in data_json:
                disease_dict['颅脑CT检查过程'] = data_json['颅脑CT检查过程']

            if '神经系统检查基本信息' in data_json:
                disease_dict['神经系统检查基本信息'] = data_json['神经系统检查基本信息']
            if '神经系统检查注意事项' in data_json:
                disease_dict['神经系统检查注意事项'] = data_json['神经系统检查注意事项']
            if '神经系统检查作用' in data_json:
                disease_dict['神经系统检查作用'] = data_json['神经系统检查作用']
            if '神经系统检查过程' in data_json:
                disease_dict['神经系统检查过程'] = data_json['神经系统检查过程']

            if '地塞米松抑制试验基本信息' in data_json:
                disease_dict['地塞米松抑制试验基本信息'] = data_json['地塞米松抑制试验基本信息']
            if '地塞米松抑制试验注意事项' in data_json:
                disease_dict['地塞米松抑制试验注意事项'] = data_json['地塞米松抑制试验注意事项']
            if '地塞米松抑制试验作用' in data_json:
                disease_dict['地塞米松抑制试验作用'] = data_json['地塞米松抑制试验作用']
            if '地塞米松抑制试验过程' in data_json:
                disease_dict['地塞米松抑制试验过程'] = data_json['地塞米松抑制试验过程']

            if '血常规检查基本信息' in data_json:
                disease_dict['血常规基本检查信息'] = data_json['血常规检查基本信息']
            if '血常规检查注意事项' in data_json:
                disease_dict['血常规检查注意事项'] = data_json['血常规检查注意事项']
            if '血常规检查作用' in data_json:
                disease_dict['血常规检查作用'] = data_json['血常规检查作用']
            if '血常规检查过程' in data_json:
                disease_dict['血常规检查过程'] = data_json['血常规检查过程']

            if '肝功能检查基本信息' in data_json:
                disease_dict['肝功能检查基本信息'] = data_json['肝功能检查基本信息']
            if '肝功能检查注意事项' in data_json:
                disease_dict['肝功能检查注意事项'] = data_json['肝功能检查注意事项']
            if '肝功能检查作用' in data_json:
                disease_dict['肝功能检查作用'] = data_json['肝功能检查作用']
            if '肝功能检查过程' in data_json:
                disease_dict['肝功能检查过程'] = data_json['肝功能检查过程']

            #食疗保健
            if '养心安神粥' in data_json:
                disease_dict['养心安神粥'] = data_json['养心安神粥']
            if '远志枣仁粥' in data_json:
                disease_dict['远志枣仁粥'] = data_json['远志枣仁粥']
            if '首乌桑葚粥' in data_json:
                disease_dict['首乌桑葚粥'] = data_json['首乌桑葚粥']
            if '山药粥' in data_json:
                disease_dict['山药粥'] = data_json['山药粥']
            if '蒸百合枸杞' in data_json:
                disease_dict['蒸百合枸杞'] = data_json['蒸百合枸杞']
            if '莲子百合粥' in data_json:
                disease_dict['莲子百合粥'] = data_json['莲子百合粥']
            if '甘麦饮' in data_json:
                disease_dict['甘麦饮'] = data_json['甘麦饮']
            if '杞枣汤' in data_json:
                disease_dict['杞枣汤'] = data_json['杞枣汤']
            if '枸杞肉丝冬笋' in data_json:
                disease_dict['枸杞肉丝冬笋'] = data_json['枸杞肉丝冬笋']
            if '赤豆薏苡仁红枣粥' in data_json:
                disease_dict['赤豆薏苡仁红枣粥'] = data_json['赤豆薏苡仁红枣粥']

            if '猪肉苦瓜丝' in data_json:
                disease_dict['猪肉苦瓜丝'] = data_json['猪肉苦瓜丝']
            if '猪肉' in data_json:
                disease_dict['猪肉'] = data_json['猪肉']
            if '草鱼' in data_json:
                disease_dict['草鱼'] = data_json['草鱼']
            if '荔枝' in data_json:
                disease_dict['荔枝'] = data_json['荔枝']
            if '百合捞莲子' in data_json:
                disease_dict['百合捞莲子'] = data_json['百合捞莲子']
            if '杞叶炒猪心' in data_json:
                disease_dict['杞叶炒猪心'] = data_json['杞叶炒猪心']
            if '猪脑汤' in data_json:
                disease_dict['猪脑汤'] = data_json['猪脑汤']
            if '莲心大枣汤' in data_json:
                disease_dict['莲心大枣汤'] = data_json['莲心大枣汤']
            if '菖蒲炖猪心' in data_json:
                disease_dict['菖蒲炖猪心'] = data_json['菖蒲炖猪心']

            if '小炒虾仁' in data_json:
                disease_dict['小炒虾仁'] = data_json['小炒虾仁']
            if '香菇豆腐' in data_json:
                disease_dict['香菇豆腐'] = data_json['香菇豆腐']
            if '桃仁鸡丁' in data_json:
                disease_dict['桃仁鸡丁'] = data_json['桃仁鸡丁']

            if '螃蟹' in data_json:
                disease_dict['螃蟹'] = data_json['螃蟹']
            if '鳗鱼' in data_json:
                disease_dict['鳗鱼'] = data_json['鳗鱼']
            if '羊肉' in data_json:
                disease_dict['羊肉'] = data_json['羊肉']

            #宜吃
            if '深海鱼' in data_json:
                disease_dict['深海鱼'] = data_json['深海鱼']
            if '香蕉' in data_json:
                disease_dict['香蕉'] = data_json['香蕉']
            if '葡萄柚' in data_json:
                disease_dict['葡萄柚'] = data_json['葡萄柚']
            if '全麦面包' in data_json:
                disease_dict['全麦面包'] = data_json['全麦面包']
            if '菠菜' in data_json:
                disease_dict['菠菜'] = data_json['菠菜']
            if '樱桃' in data_json:
                disease_dict['樱桃'] = data_json['樱桃']
            if '大蒜' in data_json:
                disease_dict['大蒜'] = data_json['大蒜']
            if '南瓜' in data_json:
                disease_dict['南瓜'] = data_json['南瓜']
            if '低脂牛奶' in data_json:
                disease_dict['低脂牛奶'] = data_json['低脂牛奶']
            if '鸡肉' in data_json:
                disease_dict['鸡肉'] = data_json['鸡肉']

            if '镁' in data_json:
                disease_dict['镁'] = data_json['镁']
            if 'L-牛磺酸' in data_json:
                disease_dict['L-牛磺酸'] = data_json['L-牛磺酸']
            if 'L-酪胺酸' in data_json:
                disease_dict['L-酪胺酸'] = data_json['L-酪胺酸']
            if '不饱和脂肪酸' in data_json:
                disease_dict['不饱和脂肪酸'] = data_json['不饱和脂肪酸']
            if '维生素C' in data_json:
                disease_dict['维生素C'] = data_json['维生素C']
            if '锌' in data_json:
                disease_dict['锌'] = data_json['锌']
            if '猕猴桃' in data_json:
                disease_dict['猕猴桃'] = data_json['猕猴桃']
            if '木耳豆腐汤' in data_json:
                disease_dict['木耳豆腐汤'] = data_json['木耳豆腐汤']
            if '猪脑鸡蛋' in data_json:
                disease_dict['猪脑鸡蛋'] = data_json['猪脑鸡蛋']
            if '鸡腿菇' in data_json:
                disease_dict['鸡腿菇'] = data_json['鸡腿菇']
            if '腌酱菜' in data_json:
                disease_dict['腌酱菜'] = data_json['腌酱菜']
            if '糯米粥' in data_json:
                disease_dict['糯米粥'] = data_json['糯米粥']

            if '大白豆' in data_json:
                disease_dict['大白豆'] = data_json['大白豆']
            if '母鸡汤' in data_json:
                disease_dict['母鸡汤'] = data_json['母鸡汤']
            if '黄豆浆' in data_json:
                disease_dict['黄豆浆'] = data_json['黄豆浆']
            if '糖类' in data_json:
                disease_dict['糖类'] = data_json['糖类']
            if '蛋白质' in data_json:
                disease_dict['蛋白质'] = data_json['蛋白质']


            #不宜吃
            if '丁香' in data_json:
                disease_dict['丁香'] = data_json['丁香']
            if '酱油' in data_json:
                disease_dict['酱油'] = data_json['酱油']
            if '辣椒' in data_json:
                disease_dict['辣椒'] = data_json['辣椒']
            if '饮食禁忌' in data_json:
                disease_dict['饮食禁忌'] = data_json['饮食禁忌']
            if '饮食适宜' in data_json:
                disease_dict['饮食适宜'] = data_json['饮食适宜']
            if '咖啡' in data_json:
                disease_dict['咖啡'] = data_json['咖啡']
            if '猪血' in data_json:
                disease_dict['猪血'] = data_json['猪血']
            if '巧克力' in data_json:
                disease_dict['巧克力'] = data_json['巧克力']
            if '酒精等含兴奋元素' in data_json:
                disease_dict['酒精等含兴奋元素'] = data_json['酒精等含兴奋元素']


            if '症状类型' in data_json:
                symptoms+=data_json['症状类型']
                for symptom in data_json['症状类型']:
                    type_symptom.append([disease,symptom])

            if '典型症状' in data_json:
                symptoms += data_json['典型症状']
                for symptom in data_json['典型症状']:
                    typical_symptom.append([disease,symptom])

            if '早期症状' in data_json:
                symptoms+=data_json['早期症状']
                for symptom in data_json['早期症状']:
                    eary_symptom.append([symptoms[0],symptom])

            if '晚期症状' in data_json:
                symptoms+=data_json['晚期症状']
                for symptom in data_json['晚期症状']:
                    terminal_symptom.append([symptoms[1],symptom])

            if '相关症状' in data_json:
                symptoms+=data_json['相关症状']
                for symptom in data_json['相关症状']:
                    relevant_symptom.append([symptoms[2],symptom])

            if '情绪方面' in data_json:
                symptoms+=data_json['情绪方面']
                for symptom in data_json['情绪方面']:
                    include_with.append([symptoms[3],symptom])

            if '躯体方面' in data_json:
                symptoms+=data_json['躯体方面']
                for symptom in data_json['躯体方面']:
                    body_symptom.append([symptoms[4],symptom])

            if '行为方面' in data_json:
                symptoms+=data_json['行为方面']
                for symptom in data_json['行为方面']:
                    include_with.append([symptoms[5],symptom])

            if '生理方面' in data_json:
                symptoms+=data_json['生理方面']
                for symptom in data_json['生理方面']:
                    include_with.append([symptoms[6],symptom])

            if '三大症状'in data_json:
                symptoms+=data_json['三大症状']
                for symptom in data_json['三大症状']:
                    big_symptom.append([disease,symptom])

            if '抑郁状态' in data_json:
                symptoms += data_json['抑郁状态']
                for symptom in data_json['抑郁状态']:
                    include_with.append([symptoms[3], symptom])

            if '躁狂状态' in data_json:
                symptoms += data_json['躁狂状态']
                for symptom in data_json['躁狂状态']:
                    include_with.append([symptoms[4], symptom])

            if '抑郁症分类' in data_json:
                # typedepressionss+=data_json['抑郁症分类']
                diseases+=data_json['抑郁症分类']
                for types in data_json['抑郁症分类']:
                    type_depression.append([disease,types])

            if '抑郁症早期症状' in data_json:
                symptoms+=data_json['抑郁症早期症状']
                for symptom in data_json['抑郁症早期症状']:
                    eary_symptom.append([disease,symptom])

            if '病因' in data_json:
                casedepressions+=data_json['病因']
                for cases in data_json['病因']:
                    case_depression.append([disease,cases])

            if '生理因素' in data_json:
                casedepressions+=data_json['生理因素']
                for cases in data_json['生理因素']:
                    include_with.append([casedepressions[0],cases])

            if '精神因素' in data_json:
                casedepressions+=data_json['精神因素']
                for cases in data_json['精神因素']:
                    include_with.append([casedepressions[1],cases])

            if '心理因素' in data_json:
                casedepressions += data_json['心理因素']
                for cases in data_json['心理因素']:
                    include_with.append([casedepressions[2], cases])

            if '身体因素' in data_json:
                casedepressions += data_json['身体因素']
                for cases in data_json['身体因素']:
                    include_with.append([casedepressions[3], cases])

            if '外部因素' in data_json:
                casedepressions += data_json['外部因素']
                for cases in data_json['外部因素']:
                    include_with.append([casedepressions[4], cases])

            if '并发症' in data_json:
                symptoms+=data_json['并发症']
                for symptom in data_json['并发症']:
                    com_depression.append([disease,symptom])

            if '诊断内容' in data_json:
                typedepressionss+=data_json['诊断内容']
                for diags in data_json['诊断内容']:
                    diag_depression.append([disease,diags])

            if '鉴别对象' in data_json:
                typedepressionss+=data_json['鉴别对象']
                for inds in data_json['鉴别对象']:
                    identify_depression.append([disease,inds])

            if '常用药物' in data_json:
                drugs+=data_json['常用药物']
                for drug in data_json['常用药物']:
                    comuse_drugs.append([disease,drug])

            if '治疗方法' in data_json:
                treatway+=data_json['治疗方法']
                for way in data_json['治疗方法']:
                    treat_way.append([disease,way])

            if '中医治疗' in data_json:
                treatway+=data_json['中医治疗']
                for way in data_json['中医治疗']:
                    treat_way.append([treatway[0],way])

            if '西医治疗' in data_json:
                treatway+=data_json['西医治疗']
                for way in data_json['西医治疗']:
                    treat_way.append([treatway[1],way])

            if '物理治疗' in data_json:
                treatway += data_json['物理治疗']
                for way in data_json['物理治疗']:
                    include_with.append([treatway[2], way])

            if '运动治疗' in data_json:
                treatway += data_json['运动治疗']
                for way in data_json['运动治疗']:
                    include_with.append([treatway[3], way])

            if '心理治疗' in data_json:
                treatway += data_json['心理治疗']
                for way in data_json['心理治疗']:
                    include_with.append([treatway[4], way])

            if '药物治疗' in data_json:
                treatway += data_json['药物治疗']
                for way in data_json['药物治疗']:
                    include_with.append([treatway[5], way])

            # if '重点检查' in data_json:
            #     checks+=data_json['重点检查']
            #     for cont in data_json['重点检查']:
            #         check_depression.append([disease,cont])

            if '护理' in data_json:
                nursepressions+=data_json['护理']
                for nurse in data_json['护理']:
                    nurse_depression.append([disease,nurse])

            if '对症护理' in data_json:
                nursepressions+=data_json['对症护理']
                for nurse in data_json['对症护理']:
                    suit_nurse.append([nursepressions[0],nurse])

            if '日常护理' in data_json:
                nursepressions+=data_json['日常护理']
                for nurse in data_json['日常护理']:
                    Daily_nurse.append([nursepressions[2],nurse])

            if '睡眠护理' in data_json:
                nursepressions += data_json['睡眠护理']
                for nurse in data_json['睡眠护理']:
                    Daily_nurse.append([nursepressions[3], nurse])

            if '心理护理' in data_json:
                nursepressions += data_json['心理护理']
                for nurse in data_json['心理护理']:
                    Daily_nurse.append([nursepressions[4], nurse])

            if '营养物质' in data_json:
                foods += data_json['营养物质']
                for food in data_json['营养物质']:
                    do_eat.append([disease, food])

            if '叶酸营养' in data_json:
                foods += data_json['叶酸营养']
                for food in data_json['叶酸营养']:
                    include_with.append([foods[0], food])

            if '维生素B1营养' in data_json:
                foods += data_json['维生素B1营养']
                for food in data_json['维生素B1营养']:
                    include_with.append([foods[1], food])

            if '维生素B6营养' in data_json:
                foods += data_json['维生素B6营养']
                for food in data_json['维生素B6营养']:
                    include_with.append([foods[2], food])

            if '维生素B12营养' in data_json:
                foods += data_json['维生素B12营养']
                for food in data_json['维生素B12营养']:
                    include_with.append([foods[3], food])

            if '硒营养' in data_json:
                foods += data_json['硒营养']
                for food in data_json['硒营养']:
                    include_with.append([foods[4], food])

            if '氨基酸营养' in data_json:
                foods += data_json['氨基酸营养']
                for food in data_json['氨基酸营养']:
                    include_with.append([foods[5], food])

            if '脂肪酸营养' in data_json:
                foods += data_json['脂肪酸营养']
                for food in data_json['脂肪酸营养']:
                    include_with.append([foods[6], food])

            if '食疗护理' in data_json:
                foods+=data_json['食疗护理']
                for food in data_json['食疗护理']:
                    recommend_food.append([nursepressions[5],food])

            if '其他护理' in data_json:
                nursepressions += data_json['其他护理']
                for nurse in data_json['其他护理']:
                    Daily_nurse.append([nursepressions[6], nurse])

            if '食疗方' in data_json:
                foods+=data_json['食疗方']
                for food in data_json['食疗方']:
                    recommend_food.append([disease,food])

            if '宜吃' in data_json:
                foods+=data_json['宜吃']
                for food in data_json['宜吃']:
                   do_eat.append([disease,food])

            if '忌吃' in data_json:
                foods+=data_json['忌吃']
                for food in data_json['忌吃']:
                   not_eat.append([disease,food])

            if '检查' in data_json:
                checks+=data_json['检查']
                for check in data_json['检查']:
                   Check_item.append([disease,check])

            if "尿常规" in data_json:
                checks+=data_json["尿常规"]
                for check in data_json["尿常规"]:
                   include_with.append([checks[0],check])

            if '尿常规相关症状' in data_json:
                symptoms+=data_json['尿常规相关症状']
                for symptom in data_json['尿常规相关症状']:
                   include_with.append([checks[8],symptom])

            if '维生素B12' in data_json:
                checks += data_json['维生素B12']
                for check in data_json['维生素B12']:
                    include_with.append([checks[1], check])

            if '维生素B12相关症状' in data_json:
                symptoms += data_json['维生素B12相关症状']
                for symptom in data_json['维生素B12相关症状']:
                    include_with.append([checks[13], symptom])

            if '叶酸' in data_json:
                checks += data_json['叶酸']
                for check in data_json['叶酸']:
                    include_with.append([checks[2], check])

            if '叶酸相关症状' in data_json:
                symptoms += data_json['叶酸相关症状']
                for symptom in data_json['叶酸相关症状']:
                    include_with.append([checks[18], symptom])

            if '脑电图' in data_json:
                checks += data_json['脑电图']
                for check in data_json['脑电图']:
                    include_with.append([checks[3], check])

            if '脑电图相关症状' in data_json:
                symptoms += data_json['脑电图相关症状']
                for symptom in data_json['脑电图相关症状']:
                    include_with.append([checks[23], symptom])

            if '心电图' in data_json:
                checks += data_json['心电图']
                for check in data_json['心电图']:
                    include_with.append([checks[4], check])

            if '心电图相关症状' in data_json:
                symptoms += data_json['心电图相关症状']
                for symptom in data_json['心电图相关症状']:
                    include_with.append([checks[28], symptom])

            if '血清T3T4抗体' in data_json:
                checks += data_json['血清T3T4抗体']
                for check in data_json['血清T3T4抗体']:
                    include_with.append([checks[5], check])

            if '血清T3T4抗体相关症状' in data_json:
                symptoms += data_json['血清T3T4抗体相关症状']
                for symptom in data_json['血清T3T4抗体相关症状']:
                    include_with.append([checks[33], symptom])

            if '神经系统检查' in data_json:
                checks += data_json['神经系统检查']
                for check in data_json['神经系统检查']:
                    include_with.append([checks[42], check])

            if '神经系统检查相关症状' in data_json:
                symptoms += data_json['神经系统检查相关症状']
                for symptom in data_json['神经系统检查相关症状']:
                    include_with.append([checks[46], symptom])

            if '颅脑CT检查' in data_json:
                checks += data_json['颅脑CT检查']
                for check in data_json['颅脑CT检查']:
                    include_with.append([checks[43], check])

            if '颅脑CT检查相关症状' in data_json:
                symptoms += data_json['颅脑CT检查相关症状']
                for symptom in data_json['颅脑CT检查相关症状']:
                    include_with.append([checks[51], symptom])

            if '脑脊液镁' in data_json:
                checks += data_json['脑脊液镁']
                for check in data_json['脑脊液镁']:
                    include_with.append([checks[36], check])

            if '脑脊液镁相关症状' in data_json:
                symptoms += data_json['脑脊液镁相关症状']
                for symptom in data_json['脑脊液镁相关症状']:
                    include_with.append([checks[39], symptom])

            if '健康体检' in data_json:
                checks += data_json['健康体检']
                for check in data_json['健康体检']:
                    include_with.append([checks[54], check])

            if '健康体检相关症状' in data_json:
                symptoms += data_json['健康体检相关症状']
                for symptom in data_json['健康体检相关症状']:
                    include_with.append([checks[57], symptom])

            if '地塞米松抑制试验' in data_json:
                checks += data_json['地塞米松抑制试验']
                for check in data_json['地塞米松抑制试验']:
                    include_with.append([checks[61], check])

            if '地塞米松抑制试验相关症状' in data_json:
                symptoms += data_json['地塞米松抑制试验相关症状']
                for symptom in data_json['地塞米松抑制试验相关症状']:
                    include_with.append([checks[69], symptom])

            if '多普勒超声心动图' in data_json:
                checks += data_json['多普勒超声心动图']
                for check in data_json['多普勒超声心动图']:
                    include_with.append([checks[72], check])

            if '多普勒超声心动图相关症状' in data_json:
                symptoms += data_json['多普勒超声心动图相关症状']
                for symptom in data_json['多普勒超声心动图相关症状']:
                    include_with.append([checks[75], symptom])

            if '血常规' in data_json:
                checks += data_json['血常规']
                for check in data_json['血常规']:
                    include_with.append([checks[78], check])

            if '血常规检查相关症状' in data_json:
                symptoms += data_json['血常规检查相关症状']
                for symptom in data_json['血常规检查相关症状']:
                    include_with.append([checks[82], symptom])

            if '肝功能检查' in data_json:
                checks += data_json['肝功能检查']
                for check in data_json['肝功能检查']:
                    include_with.append([checks[79], check])

            if '肝功能检查相关症状' in data_json:
                symptoms += data_json['肝功能检查相关症状']
                for symptom in data_json['肝功能检查相关症状']:
                    include_with.append([checks[87], symptom])

            if '促黄体生成素' in data_json:
                checks += data_json['促黄体生成素']
                for check in data_json['促黄体生成素']:
                    include_with.append([checks[103], check])

            if '促黄体生成素相关症状' in data_json:
                symptoms += data_json['促黄体生成素相关症状']
                for symptom in data_json['促黄体生成素相关症状']:
                    include_with.append([checks[111], symptom])

            if '性激素六项检查' in data_json:
                checks += data_json['性激素六项检查']
                for check in data_json['性激素六项检查']:
                    include_with.append([checks[114], check])

            if '性激素六项检查相关症状' in data_json:
                symptoms += data_json['性激素六项检查相关症状']
                for symptom in data_json['性激素六项检查相关症状']:
                    include_with.append([checks[117], symptom])

            if '光照治疗' in data_json:
                treatway += data_json['光照治疗']
                for way in data_json['光照治疗']:
                    treat_way.append([treatway[2], way])

            if '自救处方' in data_json:
                treatway += data_json['自救处方']
                for way in data_json['自救处方']:
                    treat_way.append([treatway[4], way])

            if '心理精神治疗' in data_json:
                treatway += data_json['心理精神治疗']
                for way in data_json['心理精神治疗']:
                    treat_way.append([treatway[4], way])

            if '发病原理' in data_json:
                casedepressions+=data_json['发病原理']
                for cases in data_json['发病原理']:
                    Pathogeness_item.append([disease,cases])

            if '生物化学' in data_json:
                casedepressions += data_json['生物化学']
                for cases in data_json['生物化学']:
                    include_with.append([casedepressions[0], cases])

            if '自身因素' in data_json:
                casedepressions += data_json['自身因素']
                for cases in data_json['自身因素']:
                    include_with.append([casedepressions[3], cases])

            disease_infos.append(disease_dict)
            print(disease)
            print(checks)
            print('symptoms:',symptoms)
            print('symptoms长度:',len(symptoms))
            print('drugs:',drugs)
            print('drugs长度:', len(drugs))
            print('treatway:',treatway)
            print('treatway长度:', len(treatway))
            print('casedepressions:', casedepressions)
            print('casedepressions长度:', len(casedepressions))
            print('nursepressions:', casedepressions)
            print('nursepressions长度:', len(casedepressions))

            # print('set的症状:',set(symptoms))
            # print('开始症状:', symptoms)
        print('检查：',Check_item)
        print('治疗方式', treat_way)
        # print(include_with)
        return set(symptoms),set(typedepressionss),set(diseases),set(casedepressions),set(treatway),set(drugs),set(nursepressions),\
            set(foods),set(checks),disease_infos,type_symptom,eary_symptom,terminal_symptom,relevant_symptom,big_symptom, \
               body_symptom,type_depression,case_depression,com_depression,diag_depression,identify_depression,treat_way,comuse_drugs,\
               nurse_depression,suit_nurse,Daily_nurse,care_type,do_eat,not_eat,recommend_food,include_with,Check_item,Pathogeness_item,typical_symptom
    #创建节点
    def create_node(self, label, nodes,disease_dict):
        count = 0
        print(disease_dict)
        for node_name in nodes:
            node = Node(label, name=node_name)
            # if node['name'] == '情绪低落':
            #     node.update(情绪低落=disease_dict['情绪低落'], 抑郁症三大主要症状=disease_dict['抑郁症三大主要症状'])
            #
            # if node['name'] == '运动抑制':
            #     node.update(运动抑制=disease_dict['运动抑制'], 抑郁症三大主要症状=disease_dict['抑郁症三大主要症状'])
            #
            # if node['name'] == '思维迟缓':
            #     node.update(思维迟缓=disease_dict['思维迟缓'], 抑郁症三大主要症状=disease_dict['抑郁症三大主要症状'])
            #
            # if node['name'] == '抑郁心境':
            #     node.update(抑郁心境=disease_dict['抑郁心境'])
            #
            # if node['name'] == '意志活动减退':
            #     node.update(意志活动减退=disease_dict['意志活动减退'])
            #
            # if node['name'] == '躯体症状':
            #     node.update(躯体症状=disease_dict['躯体症状'])
            #
            # if node['name'] == '体因性抑郁症':
            #     node.update(体因性抑郁症=disease_dict['体因性抑郁症'])
            #
            # if node['name'] == '隐匿性抑郁症':
            #     node.update(隐匿性抑郁症=disease_dict['隐匿性抑郁症'])
            #
            # if node['name'] == '其它躯体症状':
            #     node.update(其它躯体症状=disease_dict['其它躯体症状'])
            #
            # if node['name'] == '抑郁症心境不同':
            #     node.update(抑郁症心境不同=disease_dict['抑郁症心境不同'])
            #
            # if node['name'] == '丧失兴趣':
            #     node.update(丧失兴趣=disease_dict['丧失兴趣'])
            #
            # if node['name'] == '精神丧失':
            #     node.update(精神丧失=disease_dict['精神丧失'])
            #
            # if node['name'] == '自我评价过低':
            #     node.update(自我评价过低=disease_dict['自我评价过低'])
            #
            # if node['name'] == '病人呈现显著持续普遍抑郁症':
            #     node.update(病人呈现显著持续普遍抑郁症=disease_dict['病人呈现显著持续普遍抑郁症'])
            #
            # if node['name'] == '消极悲观':
            #     node.update(消极悲观=disease_dict['消极悲观'])
            #
            # if node['name'] == '躯体或生物学症状':
            #     node.update(躯体或生物学症状=disease_dict['躯体或生物学症状'])
            #
            # if node['name'] == '食欲不振体重减轻':
            #     node.update(食欲不振体重减轻=disease_dict['食欲不振体重减轻'])
            #
            # if node['name'] == '性功能障碍':
            #     node.update(性功能障碍=disease_dict['性功能障碍'])
            #
            # if node['name'] == '睡眠障碍':
            #     node.update(睡眠障碍=disease_dict['睡眠障碍'])
            #
            # if node['name'] == '昼夜变化':
            #     node.update(昼夜变化=disease_dict['昼夜变化'])
            #
            # if node['name'] == '反应性抑郁症':
            #     node.update(反应性抑郁症=disease_dict['反应性抑郁症'])
            #
            # if node['name'] == '以学习困难为特征的抑郁症':
            #     node.update(以学习困难为特征的抑郁症=disease_dict['以学习困难为特征的抑郁症'])
            #
            # if node['name'] == '药物引起的继发性抑郁症':
            #     node.update(药物引起的继发性抑郁症=disease_dict['药物引起的继发性抑郁症'])
            #
            # if node['name'] == '躯体疾病引起的继发性抑郁症':
            #     node.update(躯体疾病引起的继发性抑郁症=disease_dict['躯体疾病引起的继发性抑郁症'])
            #
            # if node['name'] == '产后抑郁症':
            #     node.update(产后抑郁症=disease_dict['产后抑郁症'])
            #
            # if node['name'] == '躯体疾病':
            #     node.update(躯体疾病=disease_dict['躯体疾病'])
            #
            # if node['name'] == '遗传因素':
            #     node.update(遗传因素=disease_dict['遗传因素'])
            #
            # if node['name'] == '体质因素':
            #     node.update(体质因素=disease_dict['体质因素'])
            #
            # if node['name'] == '中枢神经介质的功能及代谢异常':
            #     node.update(中枢神经介质的功能及代谢异常=disease_dict['中枢神经介质的功能及代谢异常'])
            #
            # if node['name'] == '精神因素':
            #     node.update(精神因素=disease_dict['精神因素说明'])
            #
            # if node['name'] == '内源性抑郁症':
            #     node.update(内源性抑郁症=disease_dict['内源性抑郁症'])
            #
            # if node['name'] == '轻性抑郁':
            #     node.update(轻性抑郁=disease_dict['轻性抑郁'])
            #
            # if node['name'] == '心因性和反应性抑郁症':
            #     node.update(心因性和反应性抑郁症=disease_dict['心因性和反应性抑郁症'])
            #
            # # if node['name'] == '西药治疗':
            # #     node.update(西药治疗=disease_dict['西药治疗'])
            #
            # if node['name'] == '中药治疗':
            #     node.update(中药治疗=disease_dict['中药治疗'])
            #
            # if node['name'] == '疗程和剂量':
            #     node.update(疗程和剂量=disease_dict['疗程和剂量'])
            #
            # if node['name'] == '双相抑郁和单相抑郁治疗方式':
            #     node.update(双相抑郁和单相抑郁治疗方式=disease_dict['双相抑郁和单相抑郁治疗方式'])
            #
            # if node['name'] == '药物选择':
            #     node.update(药物选择=disease_dict['药物选择'])
            #
            # if node['name'] == '颅脑CT检查':
            #     node.update(颅脑CT检查=disease_dict['颅脑CT检查'])
            #
            # if node['name'] == '脑氧代谢显像检查':
            #     node.update(脑氧代谢显像检查=disease_dict['脑氧代谢显像检查'])
            #
            # if node['name'] == '认知治疗':
            #     node.update(认知治疗=disease_dict['认知治疗'])
            #
            # if node['name'] == '电痉挛疗法':
            #     node.update(电痉挛疗法=disease_dict['电痉挛疗法'])
            #
            # if node['name'] == '替代性疗法':
            #     node.update(替代性疗法=disease_dict['替代性疗法'])
            #
            # if node['name'] == '实验疗法':
            #     node.update(实验疗法=disease_dict['实验疗法'])
            #
            # if node['name'] == '女性荷尔蒙补充疗法HRT':
            #     node.update(女性荷尔蒙补充疗法HRT=disease_dict['女性荷尔蒙补充疗法HRT'])
            #
            # if node['name'] == '反射疗法':
            #     node.update(反射疗法=disease_dict['反射疗法'])
            #
            # if node['name'] == '运动疗法':
            #     node.update(运动疗法=disease_dict['运动疗法'])
            #
            # if node['name'] == '肝气郁结者':
            #     node.update(肝气郁结者=disease_dict['肝气郁结者'])
            #
            # if node['name'] == '气郁化火上逆者':
            #     node.update(气郁化火上逆者=disease_dict['气郁化火上逆者'])
            #
            # if node['name'] == '痰气郁结者':
            #     node.update(痰气郁结者=disease_dict['痰气郁结者'])
            #
            # if node['name'] == '久郁伤神者':
            #     node.update(久郁伤神者=disease_dict['久郁伤神者'])
            #
            # if node['name'] == '阴虚火旺者':
            #     node.update(阴虚火旺者=disease_dict['阴虚火旺者'])
            #
            # if node['name'] == '仔细观察病人情况':
            #     node.update(仔细观察病人情况=disease_dict['仔细观察病人情况'])
            #
            # if node['name'] == '按医嘱要求确保病人不间断按量服制剂':
            #     node.update(按医嘱要求确保病人不间断按量服制剂=disease_dict['按医嘱要求确保病人不间断按量服制剂'])
            #
            # if node['name'] == '提高病人对外界变化的承受力':
            #     node.update(提高病人对外界变化的承受力=disease_dict['提高病人对外界变化的承受力'])
            #
            # if node['name'] == '防范病人可能出现的各种高危险行为':
            #     node.update(防范病人可能出现的各种高危险行为=disease_dict['防范病人可能出现的各种高危险行为'])
            #
            # if node['name'] == '家属注意自身心理健康状况':
            #     node.update(家属注意自身心理健康状况=disease_dict['家属注意自身心理健康状况'])
            #
            # if node['name'] == '及时送到医院就诊':
            #     node.update(及时送到医院就诊=disease_dict['及时送到医院就诊'])
            #
            # if node['name'] == '一般护理':
            #     node.update(一般护理=disease_dict['一般护理'])
            #
            # if node['name'] == '建立良好的治疗性人际关系':
            #     node.update(建立良好的治疗性人际关系=disease_dict['建立良好的治疗性人际关系'])
            #
            # if node['name'] == '安置患者住在护理人员易观察的大房间':
            #     node.update(安置患者住在护理人员易观察的大房间=disease_dict['安置患者住在护理人员易观察的大房间'])
            #
            # if node['name'] == '严格执行整体护理管理制度':
            #     node.update(严格执行整体护理管理制度=disease_dict['严格执行整体护理管理制度'])
            #
            # if node['name'] == '加强对病房设施的安全检查':
            #     node.update(加强对病房设施的安全检查=disease_dict['加强对病房设施的安全检查'])
            #
            # if node['name'] == '注意睡眠饮食和运动':
            #     node.update(注意睡眠饮食和运动=disease_dict['注意睡眠饮食和运动'])
            #
            # if node['name'] == '明确你的价值和目标':
            #     node.update(明确你的价值和目标=disease_dict['明确你的价值和目标'])
            #
            # if node['name'] == '将欢乐带入生活':
            #     node.update(将欢乐带入生活=disease_dict['将欢乐带入生活'])
            #
            # if node['name'] == '不要孤注一挪':
            #     node.update(不要孤注一挪=disease_dict['不要孤注一挪'])
            #
            # if node['name'] == '建立可靠的人际关系':
            #     node.update(建立可靠的人际关系=disease_dict['建立可靠的人际关系'])
            #
            # if node['name'] == '养心安神粥':
            #     node.update(养心安神粥=disease_dict['养心安神粥'])
            #
            # if node['name'] == '远志枣仁粥':
            #     node.update(远志枣仁粥=disease_dict['远志枣仁粥'])
            #
            # if node['name'] == '首乌桑葚粥':
            #     node.update(首乌桑葚粥=disease_dict['首乌桑葚粥'])
            #
            # if node['name'] == '山药粥':
            #     node.update(山药粥=disease_dict['山药粥'])
            #
            # if node['name'] == '蒸百合枸杞':
            #     node.update(蒸百合枸杞=disease_dict['蒸百合枸杞'])
            #
            # if node['name'] == '莲子百合粥':
            #     node.update(莲子百合粥=disease_dict['莲子百合粥'])
            #
            # if node['name'] == '甘麦饮':
            #     node.update(甘麦饮=disease_dict['甘麦饮'])
            #
            # if node['name'] == '杞枣汤':
            #     node.update(杞枣汤=disease_dict['杞枣汤'])
            #
            # if node['name'] == '枸杞肉丝冬笋':
            #     node.update(枸杞肉丝冬笋=disease_dict['枸杞肉丝冬笋'])
            #
            # if node['name'] == '赤豆薏苡仁红枣粥':
            #     node.update(赤豆薏苡仁红枣粥=disease_dict['赤豆薏苡仁红枣粥'])
            #
            # if node['name'] == '深海鱼':
            #     node.update(深海鱼=disease_dict['深海鱼'])
            #
            # if node['name'] == '香蕉':
            #     node.update(香蕉=disease_dict['香蕉'])
            #
            # if node['name'] == '葡萄柚':
            #     node.update(葡萄柚=disease_dict['葡萄柚'])
            #
            # if node['name'] == '全麦面包':
            #     node.update(全麦面包=disease_dict['全麦面包'])
            #
            # if node['name'] == '菠菜':
            #     node.update(菠菜=disease_dict['菠菜'])
            #
            # if node['name'] == '樱桃':
            #     node.update(樱桃=disease_dict['樱桃'])
            #
            # if node['name'] == '大蒜':
            #     node.update(大蒜=disease_dict['大蒜'])
            #
            # if node['name'] == '南瓜':
            #     node.update(南瓜=disease_dict['南瓜'])
            #
            # if node['name'] == '低脂牛奶':
            #     node.update(低脂牛奶=disease_dict['低脂牛奶'])
            #
            # if node['name'] == '鸡肉':
            #     node.update(鸡肉=disease_dict['鸡肉'])
            # if node['name'] == '丁香':
            #     node.update(丁香=disease_dict['丁香'])
            # if node['name'] == '酱油':
            #     node.update(酱油=disease_dict['酱油'])
            # if node['name'] == '辣椒':
            #     node.update(辣椒=disease_dict['辣椒'])
            #
            # if node['name'] == '疑病性':
            #     node.update(疑病性=disease_dict['疑病性'])
            # if node['name'] == '激越性':
            #     node.update(激越性=disease_dict['激越性'])
            # if node['name'] == '隐匿性':
            #     node.update(隐匿性=disease_dict['隐匿性'])
            # if node['name'] == '迟滞性':
            #     node.update(迟滞性=disease_dict['迟滞性'])
            # if node['name'] == '妄想性':
            #     node.update(妄想性=disease_dict['妄想性'])
            # if node['name'] == '抑郁症性假性痴呆':
            #     node.update(抑郁症性假性痴呆=disease_dict['抑郁症性假性痴呆'])
            # if node['name'] == '自杀倾向':
            #     node.update(自杀倾向=disease_dict['自杀倾向'])
            # if node['name'] == '季节性':
            #     node.update(季节性=disease_dict['季节性'])
            # if node['name'] == '其他':
            #     node.update(其他=disease_dict['其他'])
            # if node['name'] == '焦虑抑郁和激越的混合状态':
            #     node.update(焦虑抑郁和激越的混合状态=disease_dict['焦虑抑郁和激越的混合状态'])
            # if node['name'] == '兴趣索然':
            #     node.update(兴趣索然=disease_dict['兴趣索然'])
            # if node['name'] == '精力下降':
            #     node.update(精力下降=disease_dict['精力下降'])
            # if node['name'] == '自杀观念行为':
            #     node.update(自杀观念行为=disease_dict['自杀观念行为'])
            # if node['name'] == '心境昼夜节律改变':
            #     node.update(心境昼夜节律改变=disease_dict['心境昼夜节律改变'])
            # if node['name'] == '躯体或生物学症状':
            #     node.update(躯体或生物学症状=disease_dict['躯体或生物学症状'])
            # if node['name'] == '心血管系统':
            #     node.update(心血管系统=disease_dict['心血管系统'])
            # if node['name'] == '消化系统':
            #     node.update(消化系统=disease_dict['消化系统'])
            # if node['name'] == '睡眠障碍':
            #     node.update(睡眠障碍=disease_dict['睡眠障碍'])
            # if node['name'] == '自主神经系统':
            #     node.update(自主神经系统=disease_dict['自主神经系统'])
            # if node['name'] == '心血管系统':
            #     node.update(心血管系统=disease_dict['心血管系统'])
            #
            # if node['name'] == '去甲肾上腺素系统':
            #     node.update(去甲肾上腺素系统=disease_dict['去甲肾上腺素系统'])
            # if node['name'] == '羟色胺系统':
            #     node.update(羟色胺系统=disease_dict['羟色胺系统'])
            # if node['name'] == '多巴胺系统':
            #     node.update(多巴胺系统=disease_dict['多巴胺系统'])
            # if node['name'] == '乙酰胆碱系统':
            #     node.update(乙酰胆碱系统=disease_dict['乙酰胆碱系统'])
            # if node['name'] == '促肾上腺皮质激素系统':
            #     node.update(促肾上腺皮质激素系统=disease_dict['促肾上腺皮质激素系统'])
            # if node['name'] == '生长激素系统':
            #     node.update(生长激素系统=disease_dict['生长激素系统'])
            # if node['name'] == '促甲状腺激素系统':
            #     node.update(促甲状腺激素系统=disease_dict['促甲状腺激素系统'])
            # if node['name'] == '各种胺代谢与修正胺假说':
            #     node.update(各种胺代谢与修正胺假说=disease_dict['各种胺代谢与修正胺假说'])
            # if node['name'] == '生物节律变化':
            #     node.update(生物节律变化=disease_dict['生物节律变化'])
            # if node['name'] == '脑组织结构改变':
            #     node.update(脑组织结构改变=disease_dict['脑组织结构改变'])
            # if node['name'] == '遗传因素与APOE基因':
            #     node.update(遗传因素与APOE基因=disease_dict['遗传因素与APOE基因'])
            # if node['name'] == '心理社会因素':
            #     node.update(心理社会因素=disease_dict['心理社会因素'])
            #
            # if node['name'] == '绝经抑郁症心理治疗':
            #     node.update(绝经抑郁症心理治疗=disease_dict['绝经抑郁症心理治疗'])

            # if node['name'] == '尿常规基本信息':
            #     node.update(尿常规基本信息=disease_dict['尿常规基本信息'])
            # if node['name'] == '尿常规注意事项':
            #     node.update(尿常规注意事项=disease_dict['尿常规注意事项'])
            # if node['name'] == '尿常规检查作用':
            #     node.update(尿常规检查作用=disease_dict['尿常规检查作用'])
            # if node['name'] == '尿常规检查过程':
            #     node.update(尿常规检查过程=disease_dict['尿常规检查过程'])
            # if node['name'] == '维生素B12基本信息':
            #     node.update(维生素B12基本信息=disease_dict['维生素B12基本信息'])
            # if node['name'] == '维生素B12注意事项':
            #     node.update(维生素B12注意事项=disease_dict['维生素B12注意事项'])
            # if node['name'] == '维生素B12检查作用':
            #     node.update(维生素B12检查作用=disease_dict['维生素B12检查作用'])
            # if node['name'] == '维生素B12检查过程':
            #     node.update(维生素B12检查过程=disease_dict['维生素B12检查过程'])
            # if node['name'] == '叶酸基本信息':
            #     node.update(叶酸基本信息=disease_dict['叶酸基本信息'])
            # if node['name'] == '叶酸注意事项':
            #     node.update(叶酸注意事项=disease_dict['叶酸注意事项'])
            # if node['name'] == '叶酸检查作用':
            #     node.update(叶酸检查作用=disease_dict['叶酸检查作用'])
            # if node['name'] == '叶酸检查过程':
            #     node.update(叶酸检查过程=disease_dict['叶酸检查过程'])
            # if node['name'] == '血清T3T4抗体基本信息':
            #     node.update(血清T3T4抗体基本信息=disease_dict['血清T3T4抗体基本信息'])
            # if node['name'] == '血清T3T4抗体注意事项':
            #     node.update(血清T3T4抗体注意事项=disease_dict['血清T3T4抗体注意事项'])
            # if node['name'] == '血清T3T4抗体检查作用':
            #     node.update(血清T3T4抗体检查作用=disease_dict['血清T3T4抗体检查作用'])
            # if node['name'] == '血清T3T4抗体检查过程':
            #     node.update(血清T3T4抗体检查过程=disease_dict['血清T3T4抗体检查过程'])
            # if node['name'] == '脑电图基本信息':
            #     node.update(脑电图基本信息=disease_dict['脑电图基本信息'])
            # if node['name'] == '脑电图注意事项':
            #     node.update(脑电图注意事项=disease_dict['脑电图注意事项'])
            # if node['name'] == '脑电图检查作用':
            #     node.update(脑电图检查作用=disease_dict['脑电图检查作用'])
            # if node['name'] == '脑电图检查过程':
            #     node.update(脑电图检查过程=disease_dict['脑电图检查过程'])
            # if node['name'] == '心电图基本信息':
            #     node.update(心电图基本信息=disease_dict['心电图基本信息'])
            # if node['name'] == '心电图注意事项':
            #     node.update(心电图注意事项=disease_dict['心电图注意事项'])
            # if node['name'] == '心电图检查作用':
            #     node.update(心电图检查作用=disease_dict['心电图检查作用'])
            # if node['name'] == '心电图检查过程':
            #     node.update(心电图检查过程=disease_dict['心电图检查过程'])

            # if node['name'] == '性激素六项检查基本信息':
            #     node.update(性激素六项检查基本信息=disease_dict['性激素六项检查基本信息'])
            # if node['name'] == '性激素六项检查注意事项':
            #     node.update(性激素六项检查注意事项=disease_dict['性激素六项检查注意事项'])
            # if node['name'] == '性激素六项检查作用':
            #     node.update(性激素六项检查作用=disease_dict['性激素六项检查作用'])
            # if node['name'] == '性激素六项检查过程':
            #     node.update(性激素六项检查过程=disease_dict['性激素六项检查过程'])

            # if node['name'] == '多普勒超声心动图基本信息':
            #     node.update(多普勒超声心动图基本信息=disease_dict['多普勒超声心动图基本信息'])
            # if node['name'] == '多普勒超声心动图注意事项':
            #     node.update(多普勒超声心动图注意事项=disease_dict['多普勒超声心动图注意事项'])
            # if node['name'] == '多普勒超声心动图检查作用':
            #     node.update(多普勒超声心动图检查作用=disease_dict['多普勒超声心动图检查作用'])
            # if node['name'] == '多普勒超声心动图检查过程':
            #     node.update(多普勒超声心动图检查过程=disease_dict['多普勒超声心动图检查过程'])
            #
            # if node['name'] == '继发性抑郁症':
            #     node.update(继发性抑郁症=disease_dict['继发性抑郁症'])
            # if node['name'] == '抑郁症性假性痴呆':
            #     node.update(抑郁症性假性痴呆=disease_dict['抑郁症性假性痴呆'])
            # if node['name'] == '焦虑症':
            #     node.update(焦虑症=disease_dict['焦虑症'])
            # if node['name'] == '过度悲伤':
            #     node.update(过度悲伤=disease_dict['过度悲伤'])
            #
            # if node['name'] == '一般治疗':
            #     node.update(一般治疗=disease_dict['一般治疗'])
            # if node['name'] == '电休克治疗':
            #     node.update(电休克治疗=disease_dict['电休克治疗'])
            # if node['name'] == '其他治疗':
            #     node.update(其他治疗=disease_dict['其他治疗'])
            # if node['name'] == '择优规范治疗':
            #     node.update(择优规范治疗=disease_dict['择优规范治疗'])
            # if node['name'] == '康复治疗':
            #     node.update(康复治疗=disease_dict['康复治疗'])
            # if node['name'] == '物理治疗':
            #     node.update(物理治疗=disease_dict['物理治疗介绍'])
            # if node['name'] == '药物治疗':
            #     node.update(药物治疗=disease_dict['药物治疗说明'])
            # if node['name'] == '阿米替林':
            #     node.update(阿米替林=disease_dict['阿米替林'])
            # if node['name'] == '三环类抗抑郁药':
            #     node.update(三环类抗抑郁药=disease_dict['三环类抗抑郁药'])
            # if node['name'] == '四环类抗抑郁剂':
            #     node.update(四环类抗抑郁剂=disease_dict['四环类抗抑郁剂'])
            # if node['name'] == '单胺氧化酶抑制剂':
            #     node.update(单胺氧化酶抑制剂=disease_dict['单胺氧化酶抑制剂'])
            # if node['name'] == '选择性羟色胺再摄取抑制剂':
            #     node.update(选择性羟色胺再摄取抑制剂=disease_dict['选择性羟色胺再摄取抑制剂'])
            # if node['name'] == '其他新型抗抑郁药':
            #     node.update(其他新型抗抑郁药=disease_dict['其他新型抗抑郁药'])
            # if node['name'] == '抗抑郁治疗的疗程':
            #     node.update(抗抑郁治疗的疗程=disease_dict['抗抑郁治疗的疗程'])
            # if node['name'] == '行为治疗':
            #     node.update(行为治疗=disease_dict['行为治疗'])
            # if node['name'] == '人际关系治疗':
            #     node.update(人际关系治疗=disease_dict['人际关系治疗'])
            # if node['name'] == '教育':
            #     node.update(教育=disease_dict['教育'])
            #
            # if node['name'] == '家人的理解和关心':
            #     node.update(家人的理解和关心=disease_dict['家人的理解和关心'])
            # if node['name'] == '增强产妇的体质':
            #     node.update(增强产妇的体质=disease_dict['增强产妇的体质'])


            # if node['name'] == '肝气郁结型':
            #     node.update(肝气郁结型=disease_dict['肝气郁结型'])
            # if node['name'] == '气郁化火型':
            #     node.update(气郁化火型=disease_dict['气郁化火型'])
            # if node['name'] == '血行郁滞型':
            #     node.update(血行郁滞型=disease_dict['血行郁滞型'])
            # if node['name'] == '痰气郁结型':
            #     node.update(痰气郁结型=disease_dict['痰气郁结型'])
            # if node['name'] == '心阴亏虚型':
            #     node.update(心阴亏虚型=disease_dict['心阴亏虚型'])
            # if node['name'] == '心脾两虚型':
            #     node.update(心脾两虚型=disease_dict['心脾两虚型'])
            # if node['name'] == '肝肾阴虚型':
            #     node.update(肝肾阴虚型=disease_dict['肝肾阴虚型'])
            #
            # if node['name'] == '肝郁脾虚':
            #     node.update(肝郁脾虚=disease_dict['肝郁脾虚'])
            # if node['name'] == '气滞血淤':
            #     node.update(气滞血淤=disease_dict['气滞血淤'])
            # if node['name'] == '心脾两虚':
            #     node.update(心脾两虚=disease_dict['心脾两虚'])
            # if node['name'] == '脾肾阳虚':
            #     node.update(脾肾阳虚=disease_dict['脾肾阳虚'])
            # if node['name'] == '阴虚火旺':
            #     node.update(阴虚火旺=disease_dict['阴虚火旺'])

            # if node['name'] == '预防意外':
            #     node.update(预防意外=disease_dict['预防意外'])
            # if node['name'] == '转移注意':
            #     node.update(转移注意=disease_dict['转移注意'])
            # if node['name'] == '饮食禁忌':
            #     node.update(饮食禁忌=disease_dict['饮食禁忌'])
            # if node['name'] == '饮食适宜':
            #     node.update(饮食适宜=disease_dict['饮食适宜'])
            # if node['name'] == '生活照顾':
            #     node.update(生活照顾=disease_dict['生活照顾'])
            # if node['name'] == '坚持服药':
            #     node.update(坚持服药=disease_dict['坚持服药'])
            # if node['name'] == '心灵沟通':
            #     node.update(心灵沟通=disease_dict['心灵沟通'])

            # if node['name'] == '抑郁性神经症或心境恶劣障碍':
            #     node.update(抑郁性神经症或心境恶劣障碍=disease_dict['抑郁性神经症或心境恶劣障碍'])
            # if node['name'] == '心因性抑郁症':
            #     node.update(心因性抑郁症=disease_dict['心因性抑郁症'])
            # if node['name'] == '癫痫性病理心境恶劣':
            #     node.update(癫痫性病理心境恶劣=disease_dict['癫痫性病理心境恶劣'])

            # if node['name'] == '情感性精神障碍抑郁':
            #     node.update(情感性精神障碍抑郁=disease_dict['情感性精神障碍抑郁'])

            # if node['name'] == '太阳浴治疗':
            #     node.update(太阳浴治疗=disease_dict['太阳浴治疗'])
            # if node['name'] == '白色灯管治疗':
            #     node.update(白色灯管治疗=disease_dict['白色灯管治疗'])

            # if node['name'] == '情感方面':
            #     node.update(情感方面=disease_dict['情感方面'])
            # if node['name'] == '思维方面':
            #     node.update(思维方面=disease_dict['思维方面'])
            # if node['name'] == '行为异常':
            #     node.update(行为异常=disease_dict['行为异常'])
            # if node['name'] == '躯体症状':
            #     node.update(躯体症状=disease_dict['躯体症状'])
            # if node['name'] == '心境高涨':
            #     node.update(心境高涨=disease_dict['心境高涨'])
            # if node['name'] == '思维奔逸':
            #     node.update(思维奔逸=disease_dict['思维奔逸'])
            # if node['name'] == '自我评价过高':
            #     node.update(自我评价过高=disease_dict['自我评价过高'])
            # if node['name'] == '精神运动性兴奋':
            #     node.update(精神运动性兴奋=disease_dict['精神运动性兴奋'])
            # if node['name'] == '行为异常':
            #     node.update(行为异常=disease_dict['行为异常'])
            # if node['name'] == '躯体症状':
            #     node.update(躯体症状=disease_dict['躯体症状'])
            # if node['name'] == '心境高涨':
            #     node.update(心境高涨=disease_dict['心境高涨'])
            # if node['name'] == '思维奔逸':
            #     node.update(思维奔逸=disease_dict['思维奔逸'])
            # if node['name'] == '神经生化因素':
            #     node.update(神经生化因素=disease_dict['神经生化因素'])
            # if node['name'] == '情感性障碍因素':
            #     node.update(情感性障碍因素=disease_dict['情感性障碍因素'])
            # if node['name'] == '舍曲林联合重复经颅磁刺激治疗':
            #     node.update(舍曲林联合重复经颅磁刺激治疗=disease_dict['舍曲林联合重复经颅磁刺激治疗'])
            # if node['name'] == '团体心理治疗':
            #     node.update(团体心理治疗=disease_dict['团体心理治疗'])

            # if node['name'] == '健脾疏肝':
            #     node.update(健脾疏肝=disease_dict['健脾疏肝'])
            # if node['name'] == '调神疏肝':
            #     node.update(调神疏肝=disease_dict['调神疏肝'])
            # if node['name'] == '通督启神':
            #     node.update(通督启神=disease_dict['通督启神'])
            # if node['name'] == '醒脑开窍':
            #     node.update(醒脑开窍=disease_dict['醒脑开窍'])
            # if node['name'] == '头穴丛刺':
            #     node.update(头穴丛刺=disease_dict['头穴丛刺'])
            # if node['name'] == '针刺结合心理疗法':
            #     node.update(针刺结合心理疗法=disease_dict['针刺结合心理疗法'])
            # if node['name'] == '针刺结合音乐疗法':
            #     node.update(针刺结合音乐疗法=disease_dict['针刺结合音乐疗法'])
            # if node['name'] == '针刺结合推拿疗法':
            #     node.update(针刺结合推拿疗法=disease_dict['针刺结合推拿疗法'])
            # if node['name'] == '针刺结合穴位注射疗法':
            #     node.update(针刺结合穴位注射疗法=disease_dict['针刺结合穴位注射疗法'])
            # if node['name'] == '电针疗法':
            #     node.update(电针疗法=disease_dict['电针疗法'])
            # if node['name'] == '针刺结合艾灸治疗法':
            #     node.update(针刺结合艾灸治疗法=disease_dict['针刺结合艾灸治疗法'])
            # if node['name'] == '针刺结合耳穴疗法':
            #     node.update(针刺结合耳穴疗法=disease_dict['针刺结合耳穴疗法'])

            # if node['name'] == '针刺疗法':
            #     node.update(针刺疗法=disease_dict['针刺疗法'])
            # if node['name'] == '艾灸疗法':
            #     node.update(艾灸疗法=disease_dict['艾灸疗法'])
            # if node['name'] == '耳穴法':
            #     node.update(耳穴法=disease_dict['耳穴法'])
            # if node['name'] == '穴位注射法':
            #     node.update(穴位注射法=disease_dict['穴位注射法'])
            # if node['name'] == '针药联合法':
            #     node.update(针药联合法=disease_dict['针药联合法'])

            # if node['name'] == '神经内分泌':
            #     node.update(神经内分泌=disease_dict['神经内分泌'])
            # if node['name'] == '神经免疫学':
            #     node.update(神经免疫学=disease_dict['神经免疫学'])
            # if node['name'] == '睡眠与脑电':
            #     node.update(睡眠与脑电=disease_dict['睡眠与脑电'])
            # if node['name'] == '脑影像学':
            #     node.update(脑影像学=disease_dict['脑影像学'])
            # if node['name'] == '心理社会':
            #     node.update(心理社会=disease_dict['心理社会'])
            # if node['name'] == '生物胺':
            #     node.update(生物胺=disease_dict['生物胺'])
            # if node['name'] == '氨基酸肽类':
            #     node.update(氨基酸肽类=disease_dict['氨基酸肽类'])
            # if node['name'] == '第二信使系统':
            #     node.update(第二信使系统=disease_dict['第二信使系统'])
            # if node['name'] == '遗传学研究':
            #     node.update(遗传学研究=disease_dict['遗传学研究'])

            # if node['name'] == '神经系统检查基本信息':
            #     node.update(神经系统检查基本信息=disease_dict['神经系统检查基本信息'])
            # if node['name'] == '神经系统检查注意事项':
            #     node.update(神经系统检查注意事项=disease_dict['神经系统检查注意事项'])
            # if node['name'] == '神经系统检查检查作用':
            #     node.update(神经系统检查作用=disease_dict['神经系统检查作用'])
            # if node['name'] == '神经系统检查过程':
            #     node.update(神经系统检查过程=disease_dict['神经系统检查过程'])
            # if node['name'] == '颅脑CT检查基本信息':
            #     node.update(颅脑CT检查基本信息=disease_dict['颅脑CT检查基本信息'])
            # if node['name'] == '颅脑CT检查注意事项':
            #     node.update(颅脑CT检查注意事项=disease_dict['颅脑CT检查注意事项'])
            # if node['name'] == '颅脑CT检查作用':
            #     node.update(颅脑CT检查作用=disease_dict['颅脑CT检查作用'])
            # if node['name'] == '颅脑CT检查过程':
            #     node.update(颅脑CT检查过程=disease_dict['颅脑CT检查过程'])

            # if node['name'] == '健康体检基本信息':
            #     node.update(健康体检基本信息=disease_dict['健康体检基本信息'])
            # if node['name'] == '健康体检注意事项':
            #     node.update(健康体检注意事项=disease_dict['健康体检注意事项'])
            # if node['name'] == '健康体检检查作用':
            #     node.update(健康体检作用=disease_dict['健康体检检查作用'])
            # if node['name'] == '健康体检检查过程':
            #     node.update(健康体检检查过程=disease_dict['健康体检检查过程'])

            # if node['name'] == '地塞米松抑制试验基本信息':
            #     node.update(地塞米松抑制试验基本信息=disease_dict['地塞米松抑制试验基本信息'])
            # if node['name'] == '地塞米松抑制试验注意事项':
            #     node.update(地塞米松抑制试验注意事项=disease_dict['地塞米松抑制试验注意事项'])
            # if node['name'] == '地塞米松抑制试验作用':
            #     node.update(地塞米松抑制试验作用=disease_dict['地塞米松抑制试验作用'])
            # if node['name'] == '地塞米松抑制试验过程':
            #     node.update(地塞米松抑制试验过程=disease_dict['地塞米松抑制试验过程'])

            # if node['name'] == '血常规检查基本信息':
            #     node.update(血常规检查基本信息=disease_dict['血常规检查基本信息'])
            # if node['name'] == '血常规检查注意事项':
            #     node.update(血常规检查注意事项=disease_dict['血常规检查注意事项'])
            # if node['name'] == '血常规检查作用':
            #     node.update(血常规检查作用=disease_dict['血常规检查作用'])
            # if node['name'] == '血常规检查过程':
            #     node.update(血常规检查过程=disease_dict['血常规检查过程'])

            # if node['name'] == '肝功能检查基本信息':
            #     node.update(肝功能检查基本信息=disease_dict['肝功能检查基本信息'])
            # if node['name'] == '肝功能检查注意事项':
            #     node.update(肝功能检查注意事项=disease_dict['肝功能检查注意事项'])
            # if node['name'] == '肝功能检查作用':
            #     node.update(肝功能检查作用=disease_dict['肝功能检查作用'])
            # if node['name'] == '肝功能检查过程':
            #     node.update(肝功能检查过程=disease_dict['肝功能检查过程'])

            # if node['name'] == '促黄体生成素基本信息':
            #     node.update(促黄体生成素基本信息=disease_dict['促黄体生成素基本信息'])
            # if node['name'] == '促黄体生成素注意事项':
            #     node.update(促黄体生成素注意事项=disease_dict['促黄体生成素注意事项'])
            # if node['name'] == '促黄体生成素检查作用':
            #     node.update(促黄体生成素检查作用=disease_dict['促黄体生成素检查作用'])
            # if node['name'] == '促黄体生成素检查过程':
            #     node.update(促黄体生成素检查过程=disease_dict['促黄体生成素检查过程'])

            # if node['name'] == '狂躁躯体疾病':
            #     node.update(狂躁躯体疾病=disease_dict['狂躁躯体疾病'])
            # if node['name'] == '药物':
            #     node.update(药物=disease_dict['药物'])
            # if node['name'] == '抑郁躯体疾病':
            #     node.update(抑郁躯体疾病=disease_dict['抑郁躯体疾病'])
            # if node['name'] == '颅脑CT检查作用':
            #     node.update(神经系统疾病=disease_dict['神经系统疾病'])
            # if node['name'] == '痴呆':
            #     node.update(痴呆=disease_dict['痴呆'])
            # if node['name'] == '其他精神障碍':
            #     node.update(其他精神障碍=disease_dict['其他精神障碍'])

            # if node['name'] == '痰热扰胆气滞扰心':
            #     node.update(痰热扰胆气滞扰心=disease_dict['痰热扰胆气滞扰心'])
            # if node['name'] == '火内扰热陷心包':
            #     node.update(火内扰热陷心包=disease_dict['火内扰热陷心包'])
            # if node['name'] == '火盛阴虚气血双虚':
            #     node.update(火盛阴虚气血双虚=disease_dict['火盛阴虚气血双虚'])
            # if node['name'] == '火盛阴虚气血双虚':
            #     node.update(火盛阴虚气血双虚=disease_dict['火盛阴虚气血双虚'])
            # if node['name'] == '抗精神病药治疗':
            #     node.update(抗精神病药治疗=disease_dict['抗精神病药治疗'])
            # if node['name'] == '锂盐治疗':
            #     node.update(锂盐治疗=disease_dict['锂盐治疗'])
            # if node['name'] == '抑郁性神经症症状说明':
            #     node.update(抑郁性神经症症状说明=disease_dict['抑郁性神经症症状说明'])

            # if node['name'] == '遗传护理':
            #     node.update(遗传护理=disease_dict['遗传护理'])
            # if node['name'] == '生活护理':
            #     node.update(生活护理=disease_dict['生活护理'])
            # if node['name'] == '预防护理':
            #     node.update(预防护理=disease_dict['预防护理'])
            # if node['name'] == '偏头痛':
            #     node.update(偏头痛=disease_dict['偏头痛'])
            # if node['name'] == '哮喘':
            #     node.update(哮喘=disease_dict['哮喘'])
            # if node['name'] == '心血管疾病':
            #     node.update(心血管疾病=disease_dict['心血管疾病'])
            # if node['name'] == '多发性硬化':
            #     node.update(多发性硬化=disease_dict['多发性硬化'])

            # if node['name'] == '中毒性精神病':
            #     node.update(中毒性精神病=disease_dict['中毒性精神病'])
            # if node['name'] == '症状性精神病':
            #     node.update(症状性精神病=disease_dict['症状性精神病'])
            # if node['name'] == '神经衰弱':
            #     node.update(神经衰弱=disease_dict['神经衰弱'])

            # if node['name'] == '抑郁性神经症心理治疗心理治疗':
            #     node.update(抑郁性神经症心理治疗心理治疗=disease_dict['抑郁性神经症心理治疗心理治疗'])
            # if node['name'] == '成功后抑郁症心理治疗':
            #     node.update(成功后抑郁症心理治疗=disease_dict['成功后抑郁症心理治疗疗'])

            # if node['name'] == '心血管疾病':
            #     node.update(心血管疾病=disease_dict['心血管疾病'])
            # if node['name'] == '多发性硬化':
            #     node.update(多发性硬化=disease_dict['多发性硬化'])

            # if node['name'] == '镁':
            #     node.update(镁=disease_dict['镁'])
            # if node['name'] == 'L-牛磺酸':
            #     node.update(L-牛磺酸=disease_dict['L-牛磺酸'])
            # if node['name'] == 'L-酪胺酸':
            #     node.update(L-酪胺酸=disease_dict['L-酪胺酸'])
            # if node['name'] == '不饱和脂肪酸':
            #     node.update(不饱和脂肪酸=disease_dict['不饱和脂肪酸'])
            # if node['name'] == '维生素C':
            #     node.update(维生素C=disease_dict['维生素C'])
            # if node['name'] == '锌':
            #     node.update(锌=disease_dict['锌'])
            # if node['name'] == '猕猴桃':
            #     node.update(猕猴桃=disease_dict['猕猴桃'])
            # if node['name'] == '麦苗茶':
            #     node.update(麦苗茶=disease_dict['麦苗茶'])
            # if node['name'] == '木耳豆腐汤':
            #     node.update(木耳豆腐汤=disease_dict['木耳豆腐汤'])
            # if node['name'] == '猪脑鸡蛋':
            #     node.update(猪脑鸡蛋=disease_dict['猪脑鸡蛋'])
            # if node['name'] == '鸡腿菇':
            #     node.update(鸡腿菇=disease_dict['鸡腿菇'])
            # if node['name'] == '腌酱菜':
            #     node.update(腌酱菜=disease_dict['腌酱菜'])
            # if node['name'] == '糯米粥':
            #     node.update(糯米粥=disease_dict['糯米粥'])
            # if node['name'] == '咖啡':
            #     node.update(咖啡=disease_dict['咖啡'])
            # if node['name'] == '猪血':
            #     node.update(猪血=disease_dict['猪血'])
            # if node['name'] == '巧克力':
            #     node.update(巧克力=disease_dict['巧克力'])
            # if node['name'] == '酒精等含兴奋元素':
            #     node.update(酒精等含兴奋元素=disease_dict['酒精等含兴奋元素'])

            # if node['name'] == '猪肉苦瓜丝':
            #     node.update(猪肉苦瓜丝=disease_dict['猪肉苦瓜丝'])
            # if node['name'] == '猪肉':
            #     node.update(猪肉=disease_dict['猪肉'])
            # if node['name'] == '草鱼':
            #     node.update(草鱼=disease_dict['草鱼'])
            # if node['name'] == '百合捞莲子':
            #     node.update(百合捞莲子=disease_dict['百合捞莲子'])
            # if node['name'] == '杞叶炒猪心':
            #     node.update(杞叶炒猪心=disease_dict['杞叶炒猪心'])
            # if node['name'] == '莲心大枣汤':
            #     node.update(莲心大枣汤=disease_dict['莲心大枣汤'])
            # if node['name'] == '菖蒲炖猪心':
            #     node.update(菖蒲炖猪心=disease_dict['菖蒲炖猪心'])

            # if node['name'] == '小炒虾仁':
            #     node.update(小炒虾仁=disease_dict['小炒虾仁'])
            # if node['name'] == '香菇豆腐':
            #     node.update(香菇豆腐=disease_dict['香菇豆腐'])
            # if node['name'] == '桃仁鸡丁':
            #     node.update(桃仁鸡丁=disease_dict['桃仁鸡丁'])

            # if node['name'] == '螃蟹':
            #     node.update(螃蟹=disease_dict['螃蟹'])
            # if node['name'] == '鳗鱼':
            #     node.update(鳗鱼=disease_dict['鳗鱼'])
            # if node['name'] == '羊肉':
            #     node.update(羊肉=disease_dict['羊肉'])

            # if node['name'] == '大白豆':
            #     node.update(大白豆=disease_dict['大白豆'])
            # if node['name'] == '母鸡汤':
            #     node.update(母鸡汤=disease_dict['母鸡汤'])
            # if node['name'] == '黄豆浆':
            #     node.update(黄豆浆=disease_dict['黄豆浆'])
            # if node['name'] == '糖类':
            #     node.update(糖类=disease_dict['糖类'])
            # if node['name'] == '蛋白质':
            #     node.update(蛋白质=disease_dict['蛋白质'])

            # if node['name'] == '海参':
            #     node.update(海参=disease_dict['海参'])
            # if node['name'] == '鱿鱼':
            #     node.update(鱿鱼=disease_dict['鱿鱼'])
            # if node['name'] == '鱼翅':
            #     node.update(鱼翅=disease_dict['鱼翅'])

            # if node['name'] == '扯下微笑的伪面具':
            #     node.update(扯下微笑的伪面具=disease_dict['扯下微笑的伪面具'])
            # if node['name'] == '不要让不良情绪转化':
            #     node.update(不要让不良情绪转化=disease_dict['不要让不良情绪转化子'])
            # if node['name'] == '通过饮食缓解不适':
            #     node.update(通过饮食缓解不适=disease_dict['通过饮食缓解不适'])
            # if node['name'] == '学点自我安慰和放松的技巧':
            #     node.update(学点自我安慰和放松的技巧=disease_dict['学点自我安慰和放松的技巧'])
            # if node['name'] == '建立心理支持系统':
            #     node.update(建立心理支持系统=disease_dict['建立心理支持系统'])
            # if node['name'] == '换一个角度看待生活和工作的关系':
            #     node.update(换一个角度看待生活和工作的关系=disease_dict['换一个角度看待生活和工作的关系'])

            # if node['name'] == '心理因素':
            #     node.update(心理因素=disease_dict['心理因素说明'])
            # if node['name'] == '内分泌':
            #     node.update(内分泌=disease_dict['内分泌'])
            # if node['name'] == '遗传':
            #     node.update(遗传=disease_dict['遗传'])

            # if node['name'] == '神经递质学说':
            #     node.update(神经递质学说=disease_dict['神经递质学说'])
            # if node['name'] == '神经回路学说':
            #     node.update(神经回路学说=disease_dict['神经回路学说'])

            # if node['name'] == '双相情感障碍':
            #     node.update(双相情感障碍=disease_dict['双相情感障碍'])
            # if node['name'] == '继发性抑郁障碍':
            #     node.update(继发性抑郁障碍=disease_dict['继发性抑郁障碍'])
            # if node['name'] == '创伤后应激障碍':
            #     node.update(创伤后应激障碍=disease_dict['创伤后应激障碍'])

            # if node['name'] == '思维障碍':
            #     node.update(思维障碍=disease_dict['思维障碍'])
            # if node['name'] == '运动行为抑制':
            #     node.update(运动行为抑制=disease_dict['运动行为抑制'])
            # if node['name'] == '认知功能障碍':
            #     node.update(认知功能障碍=disease_dict['认知功能障碍'])

            # if node['name'] == '激素水平改变':
            #     node.update(激素水平改变=disease_dict['激素水平改变'])
            # if node['name'] == '角色转变':
            #     node.update(角色转变=disease_dict['角色转变'])
            # if node['name'] == '生活状态改变':
            #     node.update(生活状态改变=disease_dict['生活状态改变'])
            # if node['name'] == '认知功能障碍':
            #     node.update(认知功能障碍=disease_dict['认知功能障碍'])
            # if node['name'] == '过于担忧':
            #     node.update(过于担忧=disease_dict['过于担忧'])

            # if node['name'] == '经济因素':
            #     node.update(经济因素=disease_dict['经济因素'])
            # if node['name'] == '家族因素':
            #     node.update(家族因素=disease_dict['家族因素'])
            # if node['name'] == '其他因素':
            #     node.update(其他因素=disease_dict['其他因素'])
            # if node['name'] == '年龄因素':
            #     node.update(年龄因素=disease_dict['年龄因素'])

            # if node['name'] == '生物学原因':
            #     node.update(生物学原因=disease_dict['生物学原因'])
            # if node['name'] == '社会心理学假设':
            #     node.update(社会心理学假设=disease_dict['社会心理学假设'])

            # if node['name'] == '生物学因素':
            #     node.update(生物学因素=disease_dict['生物学因素'])
            # if node['name'] == '病理心理因素':
            #     node.update(病理心理因素=disease_dict['病理心理因素'])
            # if node['name'] == '社会心理因素':
            #     node.update(社会心理因素=disease_dict['社会心理因素'])
            # if node['name'] == '老年期抑郁症心理治疗':
            #     node.update(老年期抑郁症心理治疗=disease_dict['老年期抑郁症心理治疗'])

            # if node['name'] == '保持乐观愉快的情绪':
            #     node.update(保持乐观愉快的情绪=disease_dict['保持乐观愉快的情绪'])
            # if node['name'] == '合理作息':
            #     node.update(合理作息=disease_dict['合理作息'])
            # if node['name'] == '合理膳食':
            #     node.update(合理膳食=disease_dict['合理膳食'])

            # if node['name'] == '神经症性抑郁':
            #     node.update(神经症性抑郁=disease_dict['神经症性抑郁'])
            # if node['name'] == '情感性精神障碍抑郁发作':
            #     node.update(情感性精神障碍抑郁发作=disease_dict['情感性精神障碍抑郁发作'])
            # if node['name'] == '精神分裂症':
            #     node.update(精神分裂症=disease_dict['精神分裂症'])

            # if node['name'] == '分娩过程中护理人员尽量在旁陪伴和指导':
            #     node.update(分娩过程中护理人员尽量在旁陪伴和指导=disease_dict['分娩过程中护理人员尽量在旁陪伴和指导'])
            # if node['name'] == '产后给予一个安静舒适的环境':
            #     node.update(产后给予一个安静舒适的环境=disease_dict['产后给予一个安静舒适的环境'])
            # if node['name'] == '对产妇的家庭成员进行心理卫生方面的宣教':
            #     node.update(对产妇的家庭成员进行心理卫生方面的宣教=disease_dict['对产妇的家庭成员进行心理卫生方面的宣教'])

            # if node['name'] == '耳穴掀针':
            #     node.update(耳穴掀针=disease_dict['耳穴掀针'])
            # if node['name'] == '活动干预':
            #     node.update(活动干预=disease_dict['活动干预'])
            # if node['name'] == '睡眠指导':
            #     node.update(睡眠指导=disease_dict['睡眠指导'])
            # if node['name'] == '环境护理':
            #     node.update(环境护理=disease_dict['环境护理'])
            # if node['name'] == '共情护理':
            #     node.update(共情护理=disease_dict['共情护理'])
            # if node['name'] == '心理护理':
            #     node.update(心理护理=disease_dict['心理护理说明'])
            # if node['name'] == '健康教育':
            #     node.update(健康教育=disease_dict['健康教育'])

            # if node['name'] == '五行音乐疗法':
            #     node.update(五行音乐疗法=disease_dict['五行音乐疗法'])
            # if node['name'] == '正念减压联合认知行为干预':
            #     node.update(正念减压联合认知行为干预=disease_dict['正念减压联合认知行为干预'])
            # if node['name'] == '心理认知干预':
            #     node.update(心理认知干预=disease_dict['心理认知干预'])

            # if node['name'] == '情绪宣泄支持':
            #     node.update(情绪宣泄支持=disease_dict['情绪宣泄支持'])
            # if node['name'] == '家庭支持':
            #     node.update(家庭支持=disease_dict['家庭支持'])
            # if node['name'] == '社会支持':
            #     node.update(社会支持=disease_dict['社会支持'])
            # if node['name'] == '衔接支持':
            #     node.update(衔接支持=disease_dict['衔接支持'])
            # if node['name'] == '丰富精神活动':
            #     node.update(丰富精神活动=disease_dict['丰富精神活动'])
            # if node['name'] == '定期随访':
            #     node.update(定期随访=disease_dict['定期随访'])

            self.g.create(node)
            count += 1
            print(count, len(nodes))
        return
    #创建抑郁症节点的属性
    def create_diseases_nodes(self, disease_infos):
        count = 0
        for disease_dict in disease_infos:
            node = Node("抑郁症", name=disease_dict['名称'], 简介=disease_dict['简介'],是否属于医保=disease_dict['是否属于医保'],
                        抑郁症预防=disease_dict['预防'],发病部位=disease_dict['发病部位'],有无传染性=disease_dict['有无传染性'],
                        建议就诊科室=disease_dict['建议就诊科室'],最佳就诊时间=disease_dict['最佳就诊时间'],就诊时长=disease_dict['就诊时长'],
                        诊断标准=disease_dict['诊断标准'],抑郁症的判断方法=disease_dict['抑郁症的判断方法'],
                        抑郁症最危险的症状=disease_dict['抑郁症最危险的症状'],别名=disease_dict['别名'],饮食禁忌=disease_dict['饮食禁忌'],
                        饮食适宜=disease_dict['饮食适宜'],药物治疗说明=disease_dict['药物治疗说明'],抑郁症测量表=disease_dict['抑郁症测量表'])
            self.g.create(node)
            count += 1
            print(count)
        return
# # #创建节点属性
#     def node_info(self,node,disease_dict):
#         count=0
#         print(disease_dict)
#         for node_name in node:
#             node = Node(name=node_name)
#
#
#
#         return

    def create_graphnodes(self):
        symptoms,typedepressionss,Disease,Casedepressions,treatway,drugs,nursepressions,foods,checks,disease_infos,type_symptom,eary_symptom,\
        terminal_symptom,relevant_symptom,big_symptom,body_symptom, type_depression,case_depression,com_depression,diag_depression,identify_depression,treat_way,\
        comuse_drugs,nurse_depression,suit_nurse,Daily_nurse,care_type,do_eat,not_eat,recommend_food,include_with,Check_item,Pathogeness_item,typical_symptom= self.read_nodes()
        self.create_diseases_nodes(disease_infos)
        disease_dict = {}
        c=1
        for disease_dic in disease_infos:
            c+=1
            disease_dict.update(disease_dic)
        self.create_node('症状', symptoms,disease_dic)
        print(len(symptoms))
        self.create_node('疾病', typedepressionss,disease_dic)
        print(len(typedepressionss))
        self.create_node('病因', Casedepressions,disease_dic)
        print(len(Casedepressions))
        # self.create_node('诊断内容', discontent,disease_dic)
        # print(len(discontent))
        self.create_node('药物', drugs,disease_dic)
        print(len(drugs))
        self.create_node('治疗方法',treatway,disease_dic)
        print(len(treatway))
        # self.create_node('小类', ways,disease_dic)
        # print(len(ways))
        self.create_node('护理', nursepressions,disease_dic)
        print(len(nursepressions))
        # self.create_node('保健', carepressions,disease_dic)
        # print(len(carepressions))
        self.create_node('食物', foods,disease_dic)
        print(len(foods))
        # self.create_node('杂类',Thirdfloor, disease_dic)
        # print(len(Thirdfloor))
        self.create_node('检查', checks, disease_dic)
        print(len(checks))
        # nodes=symptoms.union(typedepressionss).union(Casedepressions).union(discontent).union(drugs).union(treatway).union(ways).union(nursepressions).union(foods).union(Thirdfloor).union(checks)
        # self.node_info(nodes,disease_dict)
        # print("构建节点属性")


        # self.create_node('早期症状', type_symptoms1)
        # print(len(symptoms))
        # self.create_node('晚期症状', type_symptoms2)
        # print(len(typedepressions))
        # self.create_node('相关症状', type_symptoms3)
        # print(len(symptoms))
        # print('症状集合：',symptoms)
        # self.create_pnodes('症状集合', symptoms[3],emotion_infos)
        return

    #创建实体关系边
    def create_graphrels(self):
        symptoms, typedepressions,Disease, Casedepressions,treatway,drugs,nursepressions,foods,checks,disease_infos, type_symptom, eary_symptom, terminal_symptom, relevant_symptom, big_symptom, \
        body_symptom, type_depression,case_depression,com_depression,diag_depression,identify_depression,treat_way,comuse_drugs, \
        nurse_depression, suit_nurse,Daily_nurse,care_type,do_eat,not_eat,recommend_food,include_with,Check_item,Pathogeness_item,typical_symptom = self.read_nodes()
        self.create_relationship('抑郁症', '症状', type_symptom, '症状类型', '症状类型')
        self.create_relationship('症状', '症状', include_with, '包括', '包括')
        self.create_relationship('症状', '症状',  eary_symptom, '早期症状', '早期症状')
        self.create_relationship('抑郁症', '症状', typical_symptom, '典型症状', '典型症状')
        self.create_relationship('症状', '症状', terminal_symptom, '晚期症状', '晚期症状')
        self.create_relationship('症状', '症状', relevant_symptom, '相关症状', '相关症状')
        self.create_relationship('抑郁症', '症状', big_symptom, '三大症状', '三大症状')
        self.create_relationship('症状', '症状', body_symptom, '躯体症状', '躯体症状')

        self.create_relationship('抑郁症', '抑郁症',type_depression, '抑郁症类型', '抑郁症类型')

        self.create_relationship('抑郁症', '疾病', diag_depression, '诊断', '检查内容')
        self.create_relationship('抑郁症', '疾病', identify_depression, '鉴别对象', '鉴别对象')
        self.create_relationship('抑郁症', '药物', comuse_drugs, '常用药物', '常用')

        self.create_relationship('抑郁症', '病因', case_depression, '病因', '病因')
        self.create_relationship('病因', '病因', include_with, '包括', '包括')
        self.create_relationship('抑郁症', '病因', Pathogeness_item, '发病原理', '发病原理')
        self.create_relationship('抑郁症', '症状', com_depression, '并发症', '并发症')

        self.create_relationship('抑郁症', '治疗方法', treat_way, '治疗方法', '治疗方法')
        self.create_relationship('治疗方法', '治疗方法', treat_way, '治疗方法', '治疗方法')
        self.create_relationship('治疗方法', '症状', treat_way, '包括', '包括')
        self.create_relationship('治疗方法', '药物', include_with, '包括', '包括')
        self.create_relationship('治疗方法', '治疗方法', include_with, '包括', '包括')

        self.create_relationship('抑郁症', '检查', Check_item, '检查项目', '检查')
        self.create_relationship('检查', '检查', include_with, '包括', '包括')
        self.create_relationship('检查', '症状', include_with, '包括', '包括')

        self.create_relationship('抑郁症', '护理', nurse_depression, '护理类型', '护理类型')
        self.create_relationship('护理', '护理', suit_nurse, '对症护理', '对症护理')
        self.create_relationship('护理', '护理', Daily_nurse, '日常护理', '日常护理')
        self.create_relationship('护理', '护理', include_with, '包括', '包括')
        self.create_relationship('护理', '食物', recommend_food, '食疗推荐', '食疗推荐')

        self.create_relationship('食物', '食物', include_with, '包括', '包括')
        self.create_relationship('抑郁症', '食物', do_eat, '宜吃', '宜吃')
        self.create_relationship('抑郁症', '食物', not_eat, '忌吃', '忌吃')
        self.create_relationship('抑郁症', '食物', recommend_food, '食疗推荐', '食疗推荐')


    '''创建实体关联边'''
    def create_relationship(self, start_node, end_node, edges, rel_type, rel_name):
        count = 0
        # 去重处理
        set_edges = []
        for edge in edges:
            set_edges.append('###'.join(edge))
        all = len(set(set_edges))
        for edge in set(set_edges):
            edge = edge.split('###')
            p = edge[0]
            q = edge[1]
            query = "match(p:%s),(q:%s) where p.name='%s'and q.name='%s' create (p)-[rel:%s{name:'%s'}]->(q)" % (
                start_node, end_node, p, q, rel_type, rel_name)
            try:
                self.g.run(query)
                count += 1
                print(rel_type, count, all)
            except Exception as e:
                print(e)
        return

    '''导出数据'''

    def export_data(self):
        symptoms, typedepressions, Disease, Casedepressions, treatway, drugs, nursepressions, foods, checks, disease_infos, type_symptom, eary_symptom, terminal_symptom, relevant_symptom, big_symptom, \
        body_symptom, type_depression, case_depression, com_depression, diag_depression, identify_depression, treat_way, comuse_drugs,\
        nurse_depression, suit_nurse, Daily_nurse, care_type, do_eat, not_eat, recommend_food, include_with, Check_item, Pathogeness_item, typical_symptom = self.read_nodes()

        f_type = open('feature_words/types.txt', 'w+',encoding='utf-8')
        f_symptom = open('feature_words/symptom.txt', 'w+',encoding='utf-8')
        f_disease = open('feature_words/disease.txt', 'w+',encoding='utf-8')
        f_case =open('feature_words/case.txt', 'w+',encoding='utf-8')
        f_content=open('feature_words/content.txt', 'w+',encoding='utf-8')
        f_treatway = open('feature_words/treatway.txt', 'w+',encoding='utf-8')
        f_drugs = open('feature_words/drugs.txt', 'w+',encoding='utf-8')
        # f_ways = open('feature_words/ways.txt', 'w+',encoding='utf-8')
        f_nursepressions = open('feature_words/nursepressions.txt', 'w+',encoding='utf-8')
        # f_carepressions = open('feature_words/carepressions.txt', 'w+',encoding='utf-8')
        f_foods = open('feature_words/foods.txt', 'w+',encoding='utf-8')
        # f_Thirdfloor=open('feature_words/thirdfloor.txt', 'w+',encoding='utf-8')
        f_check = open('feature_words/check.txt', 'w+', encoding='utf-8')



        f_type.write('\n'.join(list(typedepressions)))
        f_symptom.write('\n'.join(list(symptoms)))
        f_disease.write('\n'.join(list(Disease)))
        f_case.write('\n'.join(list(Casedepressions)))
        # f_content.write('\n'.join(list(discontent)))
        f_treatway.write('\n'.join(list(treatway)))
        f_drugs.write('\n'.join(list(drugs)))
        # f_ways.write('\n'.join(list(ways)))
        f_nursepressions.write('\n'.join(list(nursepressions)))
        # f_carepressions.write('\n'.join(list(carepressions)))
        f_foods.write('\n'.join(list(foods)))
        # f_Thirdfloor.write('\n'.join(list(Thirdfloor)))
        f_check.write('\n'.join(list(checks)))

        f_type.close()
        f_symptom.close()
        f_disease.close()
        f_case.close()
        # f_content.close()
        f_treatway.close()
        f_drugs.close()
        # f_ways.close()
        f_nursepressions.close()
        # f_carepressions.close()
        f_foods.close()
        # f_Thirdfloor.close()
        f_check.close()

        print('特征提取成功！')

        return

if __name__ == '__main__':
    handler = MedicalGraph()
    print("step1:导入图谱节点中")
    handler.create_graphnodes()
    print("step2:导入图谱边中")
    handler.create_graphrels()
    handler.export_data()






