# 聊天机器人

用 chatterbot 框架搭建的包含问答和调教功能的机器人。注意要使用 python3，python2不支持中文。

## 安装

```sh
pip install chatterbot
```
## 初始化数据库

```sh
python init_chatbot.py
```
当前目录下有生成 db.sqlite3 就成功了

## 启动

```sh
FLASK_APP=server.py python -m flask run
```

然后就可以在浏览器打开以下地址：localhost:5000
