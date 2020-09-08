#!/usr/bin/env python
# -*- coding:utf-8 -*-
import base64

def get_header(user, token):
    sign = "{}:{}".format(user, token)
    headers = {"Authorization": "Basic " + base64.b64encode(sign).decode("utf-8")}
    return headers

print(get_header('xxx', 'xxx-xxx-xxx-xxx-xxx'))
