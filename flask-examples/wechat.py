# -*- coding: utf-8 -*-


import hashlib

from flask import Flask, request
app = Flask(__name__)


@app.route('/weixin', methods=['GET', 'POST'])
def weixin():
    if len(request.args) > 3:
        token = "can1you2guess3me"
        signature = request.args["signature"]
        timestamp = request.args["timestamp"]
        nonce = request.args["nonce"]
        echostr = request.args["echostr"]

        newstr = "".join(sorted([token, timestamp, nonce])).encode('UTF-8')
        sha1str = hashlib.sha1(newstr)
        hashcode = sha1str.hexdigest()
        if signature == hashcode:
            return echostr
        else:
            return "认证失败，不是微信服务器的请求！"
    else:
        return "你请求的方法是：" + request.method


if __name__ == "__main__":
    # 必须80端口，微信要求
    app.run()
