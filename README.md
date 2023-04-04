# - 禁止商业用途Prohibited commercial use
# 简介
This is a word frequency statistics project with functions such as jieba word segmentation, stop words, removing comments at the beginning of the annual report (optional), and calculating keyword engagement letters, total and proportion
This is a Python word frequency statistics program that can customize dictionaries for txt text
1. Jieba participle jieba分词
2. Discontinued Words 停用词
3. Can remove annotations from annual report text 去除文本开头注释
4. Generate word frequency, total, and proportion 词频频数、总和及占比
5. Suitable for various word frequency statistics txt文本基本都能使用///
#自定义：
 若你想要自定义词典，则可将原关键词词典里的词全替换为你自己的词典，参考原来的格式，须相同。
 若你的年报名称为如下格式：000001-平安银行-2021，则在代码中修改year = filename1.split('-')[2]
 你的年报名称为如下格式：000001-2021-平安银行，则无需修改
 你的年报名称为如下格式：000001-平安银行：2021年年底报告，则在代码中修改
 将红框改为   year = (filename1.split('：')[1]).split('年')[0] 
 冒号英文还是中文，自行查看
 若你的年报开头没有注释，将以下一行代码前面加#号 注释掉即可
 #file = file[:file.index(start)] + file[file.index(end) + 1:].replace(end, "")
# Output excel
![结果预览](https://github.com/Ameaou/word-frequency-count/blob/main/output.png)
