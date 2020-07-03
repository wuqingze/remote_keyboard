### 键盘监听代码

```
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import socket
import sys
from pynput import keyboard
from pynput.keyboard import Key, KeyCode
key_stack = []
def on_press(key):
    msg = '{0}'.format(key)
    print(msg)
    #print("'\x02'" == msg)
    print(r"'\x02'" == msg)
    if "'q'" == msg:
        1/0
def on_release(key):
    pass

while True:
    with keyboard.Listener(
        on_press = on_press,
        on_release = on_release) as listener:
        listener.join()
```

在python中不需要转义表示字符`str=r"..."`表示即可
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
'<186>':;
'<222>':'
'<188>':,
'<190>':.
'<191>':/
```

### 几个比较特殊的字符

* i:'\t'
* j:'\n'
* m:'\r'

关于键位映射，得到的是无引号字符，所以需要在普通键位上也需要将引号去掉为好
