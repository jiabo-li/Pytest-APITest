# This is a sample Python script.
import os

import requests
import jsonpath
import pymysql
import pytest


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def get_indx():
    url = "http://shop-xo.hctestedu.com?s=api/index/index"
    param = {"application": "app", "application_client_type": "weixin"}
    res = requests.get(url=url,params=param)
    print(res.text)

def login_user():
    url = "http://shop-xo.hctestedu.com/index.php?s=/api/user/login"
    public_data = {"application": "app", "application_client_type": "weixin"}
    data = {"accounts": "15251870288", "pwd": "Fox110110", "type": "username"}
    res = requests.post(url=url,params=public_data,data=data)

    print(type(res))
    print(res.headers)
    print(res.request.headers)
    #inputdata = json.dump(res.text)
    token = jsonpath.jsonpath(res.json(), '$..token')[0]
    get_msg_url ="http://shop-xo.hctestedu.com/index.php?s=api/message/index"
    public_data = {"application": "app", "application_client_type": "weixin","token":token}
    data = {"page":1}
    res = requests.post(url=get_msg_url,params=public_data,data=data)
    print(res.text)
    msg = jsonpath.jsonpath(res.json(),'$.data')[0]
    print(msg)

    add_cart_url ="http://shop-xo.hctestedu.com/index.php?s=api/cart/save"
    data = {
        "goods_id": "2",
        "spec": [
        {
        "type": "套餐",
        "value": "套餐二"
        },
        {
        "type": "颜色",
        "value": "银色"
        },
        {
        "type": "容量",
        "value": "64G"
        }
        ],
        "stock": 2
    }
    res = requests.post(url=add_cart_url, params=public_data, data=data)
    print(res.text)

    get_cart_url ="http://shop-xo.hctestedu.com/index.php?s=api/cart/index"

    res = requests.post(url=get_cart_url, params=public_data)
    print(res.text)


def get_userinfor_fromdb(sqlstring,expected):
    connect_params = {
        "user":'api_test',
        "host": "shop-xo.hctestedu.com",
        "password":"Aa9999!",
        "port":3306,
        "database":"shopxo_hctested"
    }
    conn = pymysql.connect(**connect_params)
    cursor = conn.cursor()
    #sqlstring = "select username,id from sxo_user where username = '15251870288'"
    cursor.execute(sqlstring)
    res = cursor.fetchall()
    print(res)
    cursor.close()
    #assert res[0] == expected
    #
    for i ,data in enumerate(res,start=0):
        print(data)

    #print(res[0])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    py_args = [
        "-s","-v","--capture=sys",
        "./core/apirun.py",
        "--clean-alluredir",
        "--alluredir=allure-results"

    ]
    print("run pytest with: ",py_args)
    pytest.main(py_args)
    os.system("allure generate -c -o allure-report")
    from allure_combine import combine_allure
    combine_allure("./allure-report")
