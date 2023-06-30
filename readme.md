
pikpak 是一个 新加坡 的网盘，可以帮你在服务端下载torrent, http文件。

## 安装
直接clone。

## 使用
包括了两个可以使用的文件: `list-file.py`和`pik-shell.py`

### 一个简单的交互 `pik-shell.py`
```
#source venv-pikpak/bin/activate
python3 pik-shell.py
```
然后，可以输入一些命令做交互。如： help, exit, cd , ls, download, fetch 等。


### 列出文件 `list-file.py`
```
#source venv-pikpak/bin/activate
python list-file.py [json配置文件]
```
如
```
python3 list-file.py leon.json
```
在首次时，会提示你输入用户名和密码。成功登录后，会将登录信息保存到`leon.json`中。再次使用时，就不需要输入用户名和密码了。

## 说明
[GitHub](https://github.com/Quan666/PikPakAPI) 上有一个 pikpak api 的python 实现
。本程序将它clone到目录 `pikpak/` 下。
也可以使用`pip`安装
```
pip install pikpakapi
```

直接使用 `pikpak/` 可能需要`request`
```
pip install requests
```

## 文件
1. `client.py`
这是创建client的文件

2. `list-file.py`
列出帐号下的文件，并且可以生成下载的URL

