from math import log 
import operator 
import re 
fileName='iris.txt'
def fileToDataSet(fileName): 
# 此方法功能是:从文件中读取样本集数据,样本数据的格式为:数据以空白字符分割,最后一列为类标签      
# 参数: 
# fileName:存放样本集数据的文件路径      
# 返回值: 
# dataSet:样本集数据组成的二维数组 
  file=open(fileName, mode='r') 
  lines=file.readlines() 
  dataSet=[] 
  index=0
  p=re.compile(r"\s+") 
  for line in lines: 
    line=p.split(line.strip()) 
    dataSet.append(line) 
    index+=1
  return dataSet 
def calculateShannonEntropy(dataSet): 
# 此方法功能是:计算样本集数据类别的信息熵,样本数据的格式为二维数组     
# 参数: 
# dataSet:样本集数据组成的二维数组     
# 返回值: 
# shannonEntropy:样本集数据类别的信息熵 
  dataCount=len(dataSet) 
  classCountDic={} 
  for data in dataSet: 
    label=data[-1] 
    if label not in classCountDic.keys(): 
      classCountDic[label]=0
    classCountDic[label]+=1
  shannonEntropy=0.0
  for key in classCountDic: 
    prob=float(classCountDic[key])/dataCount 
    shannonEntropy-=prob*log(prob,2) 
  return shannonEntropy 
def splitDataSet(dataSet,axis,value): 
# 此方法功能是:对样本集数据按照某一特征进行分割,使得分割后的数据集中该特征的值全部等于同一个值,并且将分割后的数据中该特征列去除   
# 参数: 
# dataSet:待分割的样本集数据,二维数组 
# axis:特征所在样本集数据列中的位置 
# value:样本集数据分割后该特征的值         
# 返回值: 
# splitedDataSet:按照所在位置为axis的特征进行分割,并且该特征值为value的样本集数据的子集 
  splitedDataSet=[] 
  for data in dataSet: 
    if data[axis]==value: 
      splitedData=data[:axis] 
      splitedData.extend(data[axis+1:]) 
      splitedDataSet.append(splitedData) 
  return splitedDataSet 
def chooseBestFeatureToSlipt(dataSet): 
# 此方法功能是:分别计算整个样本集数据的信息熵与按照各个特征分割后的数据集的信息熵之差,得到使差值最大的分割方案,得到该分割方案的特征     
# 参数: 
#  dataSet:待分割的样本集数据,二维数组         
# 返回值: 
#bestFeature:按照分割前后信息熵差值最大的分割方案得到的特征，返回此特征所在样本集数据列中的位置 
  bestFeature=-1
  dataSetShannonEntropy=calculateShannonEntropy(dataSet) 
  infoGain=0
  featureCount=len(dataSet[0])-1
  for i in range(featureCount): 
    featureList=[example[i] for example in dataSet] 
    featureSet=set(featureList) 
    splitedDataSetShannonEntropy=0
    for feature in featureSet: 
      splitedDataSet=splitDataSet(dataSet,i,feature) 
      splitedDataSetShannonEntropy+=float(len(splitedDataSet))/len(dataSet)*calculateShannonEntropy(splitedDataSet) 
    if dataSetShannonEntropy-splitedDataSetShannonEntropy>infoGain: 
      infoGain=dataSetShannonEntropy-splitedDataSetShannonEntropy 
      bestFeature=i 
  return bestFeature
def majorityClass(classList): 
# 此方法功能是:从类别列表中得到个数最多的类别 
# 参数: 
# classList:类别列表,一维数组 
# 返回值: 
# 类别列表中个数最多的类别 
  classCountDic={} 
  for label in classList: 
    if label not in classCountDic.keys():
      classCountDic[label]=0
    classCountDic[label]+=1
  classCountDic=sorted(classCountDic.item(),key=operator.itemgetter(1),reverse=True) 
  return classCountDic[0][0]
def createTree(dataSet,features): 
# 此方法功能是:根据训练样本集数据创建对分类最有效的决策树 
# 参数: 
# dataSet:训练样本集数据,二维数组 
# features:与训练样本集数据中各列的特征值相对应的特征名称集合,一维数组    
# 返回值: 
#tree:根据训练样本集数据所创建的，对分类最有效的决策树 
  subFeatures=features[:] 
  classList=[example[-1] for example in dataSet] 
  if classList.count(classList[0])==len(classList): 
    return classList[0] 
  if len(dataSet[0])==1: 
    return majorityClass(classList) 
  bestFeature=chooseBestFeatureToSlipt(dataSet) 
  label=subFeatures[bestFeature] 
  tree={label:{}} 
  del(subFeatures[bestFeature]) 
  featureList=[example[bestFeature] for example in dataSet] 
  featureSet=set(featureList) 
  for feature in featureSet: 
    splitedDataSet=splitDataSet(dataSet,bestFeature,feature) 
    tree[label][feature]=createTree(splitedDataSet, subFeatures) 
  return tree
def classify(inX,tree,features): 
# 此方法功能是:根据创建好的决策树,对特定的数据进行分类 
# 参数: 
# inX:待分类的数据,特征值向量,一维数组 
# tree:根据决策树算法创建好的最有效的决策树 
# features:与训练样本集数据中各列的特征值相对应的特征名称集合,一维数组       
# 返回值: 
# label:待分类的数据通过决策树分类之后的类别 
  feature=list(tree.keys())[0] 
  featureIndex=features.index(feature) 
  secondTree=tree[feature][inX[featureIndex]] 
  if type(secondTree).__name__=="dict": 
    label=classify(inX,secondTree,features) 
  else: 
    label=secondTree 
  return label