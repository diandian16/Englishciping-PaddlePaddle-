#!/usr/bin/env python
# coding: utf-8

# # Lesson 3 大作业
# 
# ## 作业内容
# 
# 统计英语6级试题中所有单词的词频，并返回一个如下样式的字典
# 
# {'and':100,'abandon':5}
# 
# 英语6级试题的文件路径`./artical.txt`
# 
# Tip: 读取文件的方法
# 
# ```python
# def get_artical(artical_path):
#     with open(artical_path) as fr:
#         data = fr.read()
#     return data
# 
# get_artical('./artical.txt')
# ```
# 
# **处理要求**
# * (a) '\n'是换行符 需要删除
# * (b) 标点符号需要处理
# ```python
# ['.', ',', '!', '?', ';', '\'', '\"', '/', '-', '(', ')']
# ```
# * (c) 阿拉伯数字需要处理
# ```python
# ['1','2','3','4','5','6','7','8','9','0'] 
# ```
# * (d) 注意大小写
# 一些单词由于在句首，首字母大写了。需要把所有的单词转成小写
# ```python
# 'String'.lower()
# ```
# * (e) **高分项**
# 
# 通过自己查找资料学习正则表达式，并在代码中使用(re模块)
# 
# 可参考资料：https://docs.python.org/3.7/library/re.html
# 

# In[ ]:


# 请根据处理要求下面区域完成代码的编写。
def get_artical(artical_path):
    with open(artical_path) as fr:
        data = fr.read()
    return data

# get_artical()为自定义函数，可用于读取指定位置的试题内容。
# get_artical('./artical.txt')


# 请点击[此处](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576)查看本环境基本用法.  <br>
# Please click [here ](https://ai.baidu.com/docs#/AIStudio_Project_Notebook/a38e5576) for more detailed instructions. 

# In[1]:


import re

# 请根据处理要求下面区域完成代码的编写。
def get_artical(artical_path):
    with open(artical_path) as fr:
        data = fr.read()
    return data

# get_artical()为自定义函数，可用于读取指定位置的试题内容。
text=get_artical('./artical.txt')
#print(text)
text=text.lower() 
#print(text)
wordlist=re.findall('[A-Za-z]{1,15}|[A-Za-z]{1,15}\'[A-Za-z]*',text)
newwordlist={}
for i in wordlist:  #将所有单词放入字典里面，并且次数设为0
    newwordlist[i]=0
for i in wordlist:
    newwordlist[i]=newwordlist[i]+1   #重新读取，累加次数
#print(newwordlist)
#排个降序
#print('来排个序看看','*'*100)
newwordlist1=sorted(newwordlist.items(),key= lambda x: x[1],reverse=True)
#print(newwordlist1)
newwordlist2={}
for a in newwordlist1:
    newwordlist2[a[0]]=a[1]
print(newwordlist2)




# In[ ]:




