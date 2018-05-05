# -*- coding: utf-8 -*-
__author__ = 'zhihua_oba'
import operator
from numpy import *
from math import log
#文件读取
def file2matrix(filename, attribute_num): #传入参数：文件名，属性个数
 fr = open(filename)
 arrayOLines = fr.readlines()
 numberOfLines = len(arrayOLines) #统计数据集行数（样本个数）
 dataMat = zeros((numberOfLines, attribute_num))
 classLabelVector = [] #分类标签
 index = 0
 for line in arrayOLines:
  line = line.strip() #strip() 删除字符串中的'\n'
  listFromLine = line.split() #将一个字符串分裂成多个字符串组成的列表，不带参数时以空格进行分割，当代参数时，以该参数进行分割
  dataMat[index, : ] = listFromLine[0:attribute_num] #读取数据对象属性值
  classLabelVector.append(listFromLine[-1]) #读取分类信息
  index += 1
 dataSet = [] #数组转化成列表
 index = 0
 for index in range(0, numberOfLines):
  temp = list(dataMat[index, :])
  temp.append(classLabelVector[index])
  dataSet.append(temp)
 return dataSet
#划分数据集
def splitDataSet(dataSet, axis, value):
 retDataSet = []
 for featvec in dataSet: #每行
  if featvec[axis] == value: #每行中第axis个元素和value相等 #删除对应的元素，并将此行，加入到rerDataSet
   reducedFeatVec = featvec[:axis]
   reducedFeatVec.extend(featvec[axis+1:])
   retDataSet.append(reducedFeatVec)
 return retDataSet
#计算香农熵 #计算数据集的香农熵 == 计算数据集类标签的香农熵
def calcShannonEnt(dataSet):
 numEntries = len(dataSet) #数据集样本点个数
 labelCounts = {} #类标签
 for featVec in dataSet: #统计数据集类标签的个数，字典形式
  currentLabel = featVec[-1]
  if currentLabel not in labelCounts.keys():
   labelCounts[currentLabel] = 0
  labelCounts[currentLabel] += 1
 shannonEnt = 0.0
 for key in labelCounts:
  prob = float(labelCounts[key])/numEntries
  shannonEnt -= prob * log(prob, 2)
 return shannonEnt
#根据香农熵，选择最优的划分方式 #根据某一属性划分后，类标签香农熵越低，效果越好
def chooseBestFeatureToSplit(dataSet):
 baseEntropy = calcShannonEnt(dataSet) #计算数据集的香农熵
 numFeatures = len(dataSet[0])-1
 bestInfoGain = 0.0 #最大信息增益
 bestFeature = 0 #最优特征
 for i in range(0, numFeatures):
  featList = [example[i] for example in dataSet] #所有子列表（每行）的第i个元素，组成一个新的列表
  uniqueVals = set(featList)
  newEntorpy = 0.0
  for value in uniqueVals: #数据集根据第i个属性进行划分，计算划分后数据集的香农熵
   subDataSet = splitDataSet(dataSet, i, value)
   prob = len(subDataSet)/float(len(dataSet))
   newEntorpy += prob*calcShannonEnt(subDataSet)
  infoGain = baseEntropy-newEntorpy #划分后的数据集，香农熵越小越好，即信息增益越大越好
  if(infoGain > bestInfoGain):
   bestInfoGain = infoGain
   bestFeature = i
 return bestFeature
#如果数据集已经处理了所有属性，但叶子结点中类标签依然不是唯一的，此时需要决定如何定义该叶子结点。这种情况下，采用多数表决方法，对该叶子结点进行分类
def majorityCnt(classList): #传入参数：叶子结点中的类标签
 classCount = {}
 for vote in classList:
  if vote not in classCount.keys():
   classCount[vote] = 0
   classCount[vote] += 1
 sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
 return sortedClassCount[0][0]
#创建树
def createTree(dataSet, labels): #传入参数：数据集，属性标签（属性标签作用：在输出结果时，决策树的构建更加清晰）
 classList = [example[-1] for example in dataSet] #数据集样本的类标签
 if classList.count(classList[0]) == len(classList): #如果数据集样本属于同一类，说明该叶子结点划分完毕
  return classList[0]
 if len(dataSet[0]) == 1: #如果数据集样本只有一列（该列是类标签），说明所有属性都划分完毕，则根据多数表决方法，对该叶子结点进行分类
  return majorityCnt(classList)
 bestFeat = chooseBestFeatureToSplit(dataSet) #根据香农熵，选择最优的划分方式
 bestFeatLabel = labels[bestFeat] #记录该属性标签
 myTree = {bestFeatLabel:{}} #树
 del(labels[bestFeat]) #在属性标签中删除该属性
 #根据最优属性构建树
 featValues = [example[bestFeat] for example in dataSet]
 uniqueVals = set(featValues)
 for value in uniqueVals:
  subLabels = labels[:]
  subDataSet = splitDataSet(dataSet, bestFeat, value)
  myTree[bestFeatLabel][value] = createTree(subDataSet, subLabels)
 return myTree
#测试算法：使用决策树，对待分类样本进行分类
def classify(inputTree, featLabels, testVec): #传入参数：决策树，属性标签，待分类样本
 firstStr = inputTree.keys()[0] #树根代表的属性
 secondDict = inputTree[firstStr]
 featIndex = featLabels.index(firstStr) #树根代表的属性，所在属性标签中的位置，即第几个属性
 for key in secondDict.keys():
  if testVec[featIndex] == key:
   if type(secondDict[key]).__name__ == 'dict':
    classLabel = classify(secondDict[key], featLabels, testVec)
   else:
    classLabel = secondDict[key]
 return classLabel
def main():
 dataSet = file2matrix('test_sample.txt', 4)
 labels = ['attr01', 'attr02', 'attr03', 'attr04']
 labelsForCreateTree = labels[:]
 Tree = createTree(dataSet, labelsForCreateTree )
 testvec = [2, 3, 2, 3]
 print classify(Tree, labels, testvec)
if __name__ == '__main__':
  main()