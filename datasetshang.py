def cal_entropy(data,feature):
    """
    计算熵的函数
    输入：数据集的某一个feature
    输出：数据集这个feature的熵
    """
    data_size = len(data)
    # 创建一个用来储存计数的字典
    count = {}
    # 找出这个特征的所有取值的列表
    feature_value = set(data[feature])
    # 下面开始遍历，并且记录每个类别出现的次数
    for f in feature_value:
        # 如果某个feature中的类别重复出现，则计数值+1
        # 如果某个feature中的类别第一次出现，则设置初始值为0       
	    if f in count.keys():
		    count[f] += 1 
		else:
		    count[f] = 0
    # 计数完成之后，开始计算概率和熵
    ent_sum = 0
    for key in count:
        # 某个类别出现的概率
        prob = count[key]/data_size
        # 计算这个类别的熵
        ent = -prob*np.log(prob,2)
        ent_sum += ent
    return ent