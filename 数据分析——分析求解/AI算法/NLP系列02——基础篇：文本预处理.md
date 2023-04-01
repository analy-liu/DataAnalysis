# NLP系列02——基础篇：文本预处理

为什么要进行文本预处理？  
因为处理后机器才可以将文本转变为变量，且构成序列数据（sequence)

## 分句分标记（token)

将文本信息分成以下形式

```
[
    ["Hello","world],# 英文词token
    ["l","e","a","r","n"],# 英文字token
    ["学习","自然语言处理"], # 中文词token
    ["学”,"习"] # 中文字token
]
```

token可以是词（word）或者字（char）

英文分词较为简单，词与词之间有空格，中文较为复杂，但目前有中文分词工具（[结巴](https://github.com/TaurusTiger/jieba)）可以直接使用

## 构建词汇映射表（vocabulary)

为什么要做映射？因为字符串训练起来很慢  
怎么做？将token映射到一个从0开始表示的数字索引（index）中

1. 常用规则

\<unk> 表示未知token，通常下标记为0  
尖括号常用于表示一个特殊的token，比如句子开始句子结尾

2. 实现代码

包导入
```python
import collections
import re
from d21 import torch as d21
```
读取文件
```python
# 按行读取文件
def read_data(path):
   with open (path,'r') as f:
       lines = f.readlines()
   # 简单预处理
   return [re.sub('[^A-Za-z]+'," ",line).strip().lower() for line in lines]
```
将文本序列拆分成token
```python
def tokenize(lines,token='word'):
    if token == 'word':
        return [line.split() for line in lines]
    elif token == 'char':
        return [list(line) for line in lines]
    else:
        print('错误：位置令牌类型：'+token)
```
vocabulary生成
```python
class Vocab:
    """文本词汇表"""
    def __init__(self,tokens=None,min_freq=0,reserved_tokens=None):
        if tokens is None:
            tokens = []
        if reserved_tokens if None:
            reserved_tokens = []
        # 统计词出现次数
        if len(tokens) == 0 or isintance(tokens[0],list):
            tokens = [token for line in tokens for token]
        counter = collections.Counter(tokens)
        # 对词按出现频次构造list
        self.token_freqs = sorted(counter.items(),key=lambda x:x[1],reverse=True)
        self.unk = 0
        uniq_tokens = ['<unk>']+reserved_tokens
        uniq_tokens += [
            token for token,freq in self.token_freqs 
            if freq >= min_freq and token not in uniq_tokens
        ]
        # 生成互相查询的文件
        self.idx_to_token = []
        self.token_to_idx = dict()
        # 
        for token in uniq_tokens:
            self.idx_to_token.append(token)
            self.token_to_idx[token] = len(self.idx_to_token)
    def __len__(self):
        return len(self.idx_to_token)
    
    def __getitem__(self,tokens):
        if not isinstance(tokens,(list,tuple)):
            return self.token_to_idx.get(tokens, self.unk)
        return [self.__getitem__(token) for token in tokens]
    
    def to_tokens(self,indices):
        if not isinstanc(indices,(list,tuple)):
            return self.idx_to_token[indices]
        return [self.idx_to_token[index] for index in indices]
```
打包
```python
def load_corpus_path(path,max_tokens=-1):
    lines = read_data(path)
    tokens = tokenize(lines,"char")
    vocab = Vocab(tokens)
    corpus = [vocab[token] for line in tokens for token in line]# 返回的是所有词对应的index
    if max_tokens > 0:
        corpus = corpus[:max_tokens]
    return corpus, vocab
```