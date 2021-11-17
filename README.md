XradScan自述文档

------

# XradScan

XradScan即是将xray和rad联动，启动xray监听端口，利用http-proxy将rad扫描带入xray，实现联动。

![img](/image.png)

# Who Use XradScan

那必须是渗透测试人员啦。

其实主要是为了方便批量进行漏扫，之前写过一个类似的简单脚本AutoXray`https://github.com/givemefivw/AutoXray`，同样是为了方便批量扫描。

# How It Works

其实我觉得这一项不必要写。

观察源码就可以看到，就是使用了os.system(我都没用subprocess)调用xray和rad工具执行命令。

啥？技术点？

那没有2333

# Usage

```JavaScript
____  ___                  .___
\   \/  /___________     __| _/
 \     /\_  __ \__  \   / __ |
 /     \ |  | \// __ \_/ /_/ |
/___/\  \|__|  (____  /\____ |
      \_/           \/      \/

                @Givemefivw

usage: XradScan.py [-h] [-f FILE]

Xrad Scan Help

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  Please set the target urlfile
```

很简单，只有一个参数，将目标网址写进txt文件里就可以开始扫描了。

![](./use.gif)

# Installation

```JavaScript
git clone 
cd XradScan
python3 XradScan.py -f url.txt
```

# Config

只需要将xray和rad放在同一目录下即可，注意两者的配置文件，有的网站默认不允许爬取，视情况修改配置文件。