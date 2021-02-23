
[^_^]:
  主标题
#PaddlePaddle飞浆领航团作业三分析

[^_^]:
  二级标题
## 2021年2月

[^_^]:
  三级级标题
  
### 一篇英语文章的词频分析
------开始------  

```
# 导入文章的语法
def get_artical(artical_path):
    with open(artical_path) as fr:
        data = fr.read()
    return data
text=get_artical('./artical.txt')
```
------处理字符数字换行与大小写问题------  
```
#处理大小写问题，将所有英语变为小写
text=text.lower() 
#运用re库仅提炼出文中的字母
import re
wordlist=re.findall('[a-z]{1,15}|[a-z]{1,15}\'[a-z]*',text)   #[a-z]{1,15}表示仅仅需要a-z并且长度在1-15的
```
------统计词频------  
```
#创建词典，将所有单词放入字典里面，并且次数设为0
newwordlist={}
for i in wordlist:  #将所有单词放入字典里面，并且次数设为0
    newwordlist[i]=0
    
#按字典中关键字，重新读取，累加次数
for i in wordlist:
    newwordlist[i]=newwordlist[i]+1
```
------按词频次数降序------ 
```
newwordlist1=sorted(newwordlist.items(),key= lambda x: x[1],reverse=True)
```
------按字典格式输出------ 
```
newwordlist2={}
for a in newwordlist1:
    newwordlist2[a[0]]=a[1]
print(newwordlist2)
```

课程地址：https://aistudio.baidu.com/aistudio/course/introduce/7073
[领航课程](https://aistudio.baidu.com/aistudio/course/introduce/7073)





附[MarkDown格式撰写技巧](https://www.jianshu.com/p/191d1e21f7ed)
