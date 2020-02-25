from collections import defaultdict
from vector import distance, vector_and, vector_or, vector_mean
from functools import reduce
from random import sample
import datetime
from collections import Counter
import time
g_dataSet = {}
g_testSet = {}
g_dataSet_modify = {}

def read_digit(fp):
    bits = fp.read(32*33).replace('\n','')
    if bits == '':
        return -1, -1
    vec = list(map(int,bits))
    label = int(fp.readline())
    return label, vec

def load_data():
    global g_dataSet
    global g_dataSet_modify
    global g_testDataSet
    g_dataSet = defaultdict(list)
    g_dataSet_modify = defaultdict(list)
    g_testDataSet = defaultdict(list)
    with open('digit-training.txt') as fp:
        while True:
            l,v = read_digit(fp)
            if l == -1:
                break
            g_dataSet[l].append(v)
            g_dataSet_modify[l].append(v)

def show_info():
    #show training
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Beginning of Training @ {}'.format(date))
    print('-' * 40)
    print('Training Info'.center(40))
    for i in range (40):
        print('-',end='')
    print()
    total_sample = 0
    for d,v in sorted(g_dataSet.items()):
        print(' ' * 15 + '{} = '.format(d) +'{}'.format(len(v)).center(3))
        total_sample = total_sample + len(v)
    print('-' * 40)
    print('   Total Sample = {}'.format(total_sample))
    print('-' * 40)

def show_info_test():
    print('-' * 40)
    print('Testing Info'.center(37))
    print('-' * 40)
    total_rate = 0
    total_sample = 0
    total_Correct = 0
    for d,v in sorted(g_testDataSet.items()):
        print(' ' * 10 + '{} = '.format(d) +'{}'.format(len(v)-g_testSet[d]).center(3) 
                + '  {},  '.format(g_testSet[d]).center(7) + '%d%%'%((len(v) - int(g_testSet[d])) * 100 / len(v)))
        total_sample = total_sample + len(v)
        total_Correct = total_Correct + (len(v) - int(g_testSet[d]))
        total_rate = total_rate + ((len(v) - int(g_testSet[d])) * 100 / len(v))
    print('-' * 40)
    print('     Average = ' + '%.2f%%'%((total_Correct / total_sample) * 100))
    print('     Correct/Total = {}/{}'.format(total_Correct,total_sample))
    print('-' * 40)
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print('Ending of Training @ {}'.format(date))


def predict(p_vec):
    knn=[]
    for d,vectors in g_dataSet_modify.items():
        cnt = 0
        for v in vectors:
            dist = distance(v, p_vec)
            if dist > 15:
                cnt = cnt + 1
                if cnt > 2:
                    break
            knn.append((dist, d))
    knn.sort()
    nearest = knn[:9]
    nearest_data = []
    for i in nearest:
        nearest_data.append(i[1])
    c = Counter(nearest_data)
    for i in c.most_common(1):
        nearest_number = i[0]
    return nearest_number

def data_mean():
    for d, vectors in g_dataSet.items():
        for g in range (35):
            s = sample(g_dataSet_modify[d],3)
            v = vector_mean(s)
            g_dataSet_modify[d].append(v)
            g_dataSet[d].append(v)
        g_dataSet_modify[d] = g_dataSet_modify[d][-35:]
        g_dataSet[d] = g_dataSet[d][-35:]
        for i in range(2, len(g_dataSet[d])):
            distance_1 = distance(g_dataSet[d][i], g_dataSet[d][i - 1])
            distance_2 = distance(g_dataSet[d][i], g_dataSet[d][i - 2])
            if distance_1 > 8 and distance_2 > 8:
                g_dataSet_modify[d].remove(g_dataSet[d][i])
    return g_dataSet_modify

def test():
    global g_testSet
    g_testSet = defaultdict(int)
    with open('digit-testing.txt') as tp:
        while True:
            tl, p_vec = read_digit(tp)
            if tl == -1:
                break
            else:
                if predict(p_vec) != tl:
                    g_testSet[tl] = g_testSet[tl] + 1
            g_testDataSet[tl].append(p_vec)
    return g_testSet

def predict_last():
    print('-' * 40)
    print('My prediction')
    with open('digit-predict.txt') as pp:
        while True:
            pl, p_vec = read_digit(pp)
            if pl == -1:
                break
            else:
                print(predict(p_vec))

def main():
    load_data()
    show_info()
    data_mean()
    test()
    show_info_test()
    predict_last()
main()