import numpy as np
from tqdm import tqdm

# 数据标准化
def normalize_MinMax(features):
    """
    只接受一个参数-->ndarray
    返回一个标准化后的数组
    """
    return (features - np.min(features)) / (np.max(features) - np.min(features))


def normalize_0Min(features):
    """
    标准差
    """
    return (features - np.mean(features)) / np.std(features)


def normalize(features):
    return features / np.max(features)


# 数据拆分

def data_split(features, labels, ratio=0.25, shuffle=False):
    """
    接受三个参数
    features和labels
    数据分割的比例: 默认是0.25
    返回-> (x_train,y_train),(x_test,y_test)
    """
    if shuffle == True:
        features, labels = (data_shuffle_v2(features, labels))

    samples = features.shape[0]
    rng = int(samples * (1 - ratio))
    x_train = features[:rng]
    y_train = labels[:rng]
    x_test = features[rng:]
    y_test = labels[rng:]
    print("Part1: {} {}".format(x_train.shape, y_train.shape))
    print("Part2: {} {}".format(x_test.shape, y_test.shape))

    return (x_train, y_train), (x_test, y_test)


# 打乱数据集
def data_shuffle(features, labels):
    """
    input: features, labels(ndarray)
    return: shuffled features, shuffled labels
    效率太慢了
    """
    features, labels = np.array(features), np.array(labels)

    x_shape = features.shape
    y_shape = labels.shape
    new_features = np.array([])
    new_labels = np.array([])
    new_order = np.arange(x_shape[0])
    np.random.shuffle(new_order)
    for i in tqdm(range(x_shape[0])):
        new_features = np.append(new_features, features[new_order[i]])
        new_labels = np.append(new_labels, labels[new_order[i]])

    return new_features.reshape(x_shape), new_labels.reshape(y_shape)


def data_shuffle_v2(features, labels):
    """
    input: features, labels(ndarray)
    return: shuffled features, shuffled labels
    效率显著提升
    """
    features, labels = np.array(features), np.array(labels)

    x_shape = features.shape
    y_shape = labels.shape
    # 将label 和 Features zip起来
    zipped = np.array(list(zip(features,labels)))
    np.random.shuffle(zipped)
    new_features = np.array([x[0] for x in zipped])
    new_labels = np.array([x[1] for x in zipped])
    

    return new_features.reshape(x_shape), new_labels.reshape(y_shape)

def one_hot(labels):
    """
    把以index为label的转换为one-hot格式
    参数: labels
    return一个ndArray
    """
    if type(labels) != type(np.array([])):
        labels = np.array(labels)

    result = np.array([])
    class_num = len(set(labels.copy()))
    temp = np.identity(class_num)
    for i in range(labels.shape[0]):
        result = np.append(result, temp[labels[i]])
    result = result.reshape(-1, class_num)
    return result
