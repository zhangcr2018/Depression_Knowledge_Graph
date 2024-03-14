该图谱的访问链接：
http://localhost:7474/browser/

其中，图谱数据是构建抑郁症知识图谱的数据，这些数据都是经过处理的，数据来源与两方面：
一是“39健康网”和“寻医问药网”的数据；
二是中国知网的数据。

buid_depressiongraph.py 是构成图谱的代码文件。需要的工具如下
py2neo                             4.3.0，
conda                              4.6.11，
jieba                              0.42.1，
Keras                              2.3.1，
numpy                              1.19.3，
pandas                             1.3.5，
pyahocorasick                      1.4.4，
PyMySQL                            1.0.2，
requests                           2.21.0，



据统计构建的知识图谱的实体规模为2595个，关系数量为2907个。
效果图如下

![image](https://github.com/zhangcr2018/Depression_Knowledge_Graph/assets/39765745/50fb18ce-9e91-4dd2-b013-aefd77dc563b)
![image](https://github.com/zhangcr2018/Depression_Knowledge_Graph/assets/39765745/cde25fad-babc-4838-bd9e-9c3052f88738)
![image](https://github.com/zhangcr2018/Depression_Knowledge_Graph/assets/39765745/b21a8e32-877b-45df-be54-f07c185ed21b)





