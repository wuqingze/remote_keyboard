### 问题1
java rmi远程调用参数输出错误

#### 解决方法
直接打印看看，不做字符串格式化
#### 原因
是字符串String.format的原因

### 问题2
socket close问题 代码bug


thinkpad的 b,n, ^键位坏掉了，可以替换成home,end,delete键勉强先用着

现在遇到的问题是

为了加快进度，现在先不理睬快捷键的问题，先把程序调通先，从前台到后台

还有keycode的问题，如果我的想法是对的话，那么可能会省下很多力气

现在先验证下想法

现在验证的结果是ctrl键位加正常字符键位时，直接press并不能发挥他们组合的效果，所以现在的出路
是将ctrl之后的x码转成字符，但又存在一个问题，ctrl+i, 或者ctrl+m出来的str都是\t的形式，
这一定程度上决定了这两个快捷键hotkey是不能够实现的了。不过好在实际使用中我目前还没有碰到
过使用ctrl+i或者ctrl+m的快捷键的情况。还有一个问题ctrl+char的大小要不要跳过i和m两个字符？
要验证下才知道。验证下来的，顺序是递增的，没有跳过i,m,因为存在重复值，做映射有点困难啊。
看开了，反正这些快捷键都用不到，全部映射到ctrl+m好了。

现在的工作是将ctrl快捷键做一个映射,映射表如下
```
A:'\x01'
B:'\x02'
C:'\x03'
D:'\x04'
E:'\x05'
F:'\x06'
G:'\x07'
H:'\x08'
I:'\x09'
J:'\x0a'
K:'\x0b'
L:'\x0c'
M:'\x0d'
N:'\x0e'
O:'\x0f'
P:'\x10'
Q:'\x11'
R:'\x12'
S:'\x13'
T:'\x14'
U:'\x15'
V:'\x16'
W:'\x17'
X:'\x18'
Y:'\x19'
Z:'\x1a'
[:'\x1b'
\:'\x1c'
]:'\x1d'
^:'\x1e'
_:'\x1f'
`:'\x20'
```

### Bilibili
<iframe src="//player.bilibili.com/player.html?aid=668703765&bvid=BV15a4y1e7Kw&cid=207194579&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" style="width:100%;height:500px"> </iframe>


### 键盘映射
```
'\0x1':A
'\0x2':B
'\0x3':C
'\0x4':D
'\0x5':E
'\0x6':F
'\0x7':G
'\0x8':H
'\0x9':I
'\0xa':J
'\0xb':K
'\0xc':L
'\0xd':M
'\0xe':N
'\0xf':O
'\0x10':P
'\0x11':Q
'\0x12':R
'\0x13':S
'\0x14':T
'\0x15':U
'\0x16':V
'\0x17':W
'\0x18':X
'\0x19':Y
'\0x1a':Z
'\0x1b':[
'\0x1c':\
'\0x1d':]
'\0x1e':^
'\0x1f':_
'\0x20':`
'\0x21':a
'\0x22':b
'\0x23':c
'\0x24':d
'\0x25':e
'\0x26':f
'\0x27':g
'\0x28':h
'\0x29':i
'\0x2a':j
'\0x2b':k
'\0x2c':l
'\0x2d':m
'\0x2e':n
'\0x2f':o
'\0x30':p
'\0x31':q
'\0x32':r
'\0x33':s
'\0x34':t
'\0x35':u
'\0x36':v
'\0x37':w
'\0x38':x
'\0x39':y
'\0x3a':z
```

### 映射2
```
'\x01':a
'\x02':b
'\x03':c
'\x04':d
'\x05':e
'\x06':f
'\x07':g
'\x08':h
'\x09':i
'\x0a':j
'\x0b':k
'\x0c':l
'\x0d':m
'\x0e':n
'\x0f':o
'\x10':p
'\x11':q
'\x12':r
'\x13':s
'\x14':t
'\x15':u
'\x16':v
'\x17':w
'\x18':x
'\x19':y
'\x1a':z
'\x1b':[
'\x1c':\
'\x1d':]
'\x1e':^
'\x1f':_
'\x20':`
```

### 如何在python中不需要转义表示字符
`str=r"..."`表示即可

