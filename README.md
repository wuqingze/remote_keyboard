### 介绍
---

如果你存在使用两台机子的场景，比如一台Linux的机子一台Windows的机子，或者一台主机一台笔记本，
当你需要从一台机子切换到另一台机子进行键盘输入时，那么常见的操作是你的手需要从一个键盘移动
到另一个键盘，如果此时手指不需要离开键盘就能切换机器进行输入，那么这样是不是很方便呢。

基于以上的场景，本项目提供了远程键盘的功能，你可以通过快捷键的方式从一台机子切换到另一台机子
进行键盘操作。开发这个项目的背景是我有台ThinkPad的键盘坏掉了，但是不想就此放弃掉ThinkPad，
所以开发了一个远程键盘，通过别的机子操控我键盘坏掉的ThinkPad，哈哈哈。

### 环境
---
* java
* python

### quick start
---
被控制的电脑
```
1. 进入server_project目录
2. python py_server.py
3. ./start_server.sh 
```

控制的电脑(用来键盘输入的电脑）
```
1. 进入client_project目录
2. java JavaClient
3. python py_client.py
```

功能快捷键
```
1. 切换机器进行键盘输入 ctrl+.
2. 退出远程键盘  ctrl+q
3. xxx
```

### 在没有允许的环境的电脑上运行
---
一般情况下，用户的机器上没有python和Java环境(当然本项目的初衷是为了解决程序员开发过程中不同机子
输入切换的问题，程序员的机器默认存在Java和python环境),所以我打包了exe文件放在release中。
* 被控制电脑运行keyboard_server.exe
* 进行键盘输入的电脑运行keyboard_client.exe
