# _*_ coding: utf-8 _*_
# 载入程序包
import pandas as pd
import jieba
from collections import Counter
import os
import re

# 获取当前脚本的路径
script_path = os.path.dirname(os.path.realpath(__file__))


# 读取数字化搜词词典
with open(os.path.join(script_path, "原关键词词典.txt"),'r',encoding='utf-8') as f:
    cidian = f.readlines()
# 计算文本个数
text_count = len(cidian)

#定义方法，获取文件名列表
def getFileList(path):
    """
    从path中读取文件列表参数
    path: str, 文件夹路径
    """
    filelist = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.isfile(os.path.join(root, file)):
                filelist.append(os.path.join(root, file))
    return filelist

# 定义方法，批量处理文件，计算指标
def get_data(path):
    filelist = getFileList(path)
    # 获取停用词列表
    stopfile = open(os.path.join(script_path, "stopwords.txt"), 'r', encoding='UTF-8').read()
    stopfile = stopfile.replace(" ","")
    stoplist = stopfile.split('n')
    #加载用户词典 即数字化词典
    jieba.load_userdict(os.path.join(script_path, "原关键词词典.txt"))

    datalist = []
    list = []
    start = '（'
    end = '-'
    for file in filelist:
        print("正在处理--{}".format(file))
        filename, extension = os.path.splitext(file)
        # 获取文件名
        filename1 = os.path.basename(filename)
        code = filename1[:6]
        # year = (file.split('-')[1]).split('.')[0]
        year = filename1.split('-')[1]
        # year = (filename1.split('：')[1]).split('年')[0]
        file=open(file,'r', encoding='utf-8').read()
        file = file[:file.index(start)] + file[file.index(end) + 1:].replace(end, "") # 去开头注释
        words = [x for x in jieba.cut(file) if len(x) >= 2 and x not in stoplist]
        keywords = [y.split() for y in cidian]
        keywords = [c[0] for c in keywords]

        # 将列表words转为特定的计数格式
        b = Counter(words)
        # 提取重点词汇的频次
        wordsfreq = [b[x] for x in keywords]
        totalfreq = sum(wordsfreq)
        # 所有词语的总数
        s = sum(b.values())
        # 计算比重
        weight = totalfreq/s

        filename_num = re.match(r"\d+", filename)

        data = [str(code)] + [year]+[totalfreq] + [weight]
        datalist.append(data)
        datadict = {
            'code': str(code),
            'year': year,
            '总计': totalfreq,
            '占比': weight
        }
        for i in range(0,text_count): # 238为关键词个数
            datadict[f'{keywords[i]}'] = wordsfreq[i]
        list.append(datadict)
    return list

# 定义方法，将列表数据写入csv文件
def write_csv(path):
    list= get_data(path)
    # 生成DataFrame格式数据
    csvfile = pd.DataFrame( list)
    # 写入csv文件，注意对中文乱码的处理
    csvfile.to_excel('数字化转型.xlsx', encoding="utf-8", index=False)


if __name__ == '__main__':
    path = '多文件夹txt'
    write_csv(path)

