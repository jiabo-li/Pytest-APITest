import allure
import jsonpath
import pytest
import requests
from common.globalcontext import g_context
from pymysql import cursors
import pymysql

class keyword:
    def __init__(self):
        self.g_data = g_context()
    @allure.step("post request from url")
    def request_post_from_url(self,**kwargs):
        url = kwargs.get("URL",None)
        params = kwargs.get("PARAMS",None)
        data = kwargs.get("DATA",None)

        request_data = {
            "url":url,
            "params": params,
            "data":data
        }

        res = requests.post(**request_data)
        print(res.text)
        print("res json is ",res.json())
        self.g_data.set_dict("current_res",res)

    def request_get(self,**kwargs):
        res = requests.get(**kwargs)
        self.g_data.set_dict("current_res",res)

    @allure.step("extract json data")
    def ex_jsonData(self,**kwargs):
        exvalue = kwargs.get("EXVALUE",None)
        index = kwargs.get("INDEX",0)
        current_res = self.g_data.get_dict_by_key("current_res").json()
        if(not index):
            index = 0
        print("current result is :",current_res)
        ex_data = jsonpath.jsonpath(current_res,exvalue)[index]
        self.g_data.set_dict(kwargs["VARNAME"],ex_data)

    @allure.step("compare the result")
    def assert_text_comparators(self,**kwargs):
        comparator = {
            ">": lambda a, b: a > b,
            "<": lambda a, b: a < b,
            "==": lambda a, b: a == b,
        }
        if kwargs["OP_STR"] not in comparator:
            raise ValueError(f"not compare option:{kwargs['OP_STR']}")
        print(kwargs['VALUE'])
        current_value = self.g_data.get_dict_by_key(kwargs['VALUE'])
        print(current_value)
        if not comparator[kwargs['OP_STR']](current_value,kwargs['EXPECTED']):
            raise AttributeError(f"{kwargs['VALUE']} {kwargs['OP_STR']} {kwargs['EXPECTED']}")

    allure.step("Check result from sql")
    def ex_mysqlData(self, **kwargs):
        connect_params = {
                "user": 'api_test',
                "host": "shop-xo.hctestedu.com",
                "password": "Aa9999!",
                "port": 3306,
                "database": "shopxo_hctested",
                "cursorclass": cursors.DictCursor,
            }

        connection = pymysql.connect(**connect_params)
        cursor = connection.cursor()
        cursor.execute(kwargs['SQL'])


        res = cursor.fetchall()
        cursor.close()

        var_names = kwargs["VAR"].split(",")
        #print(var_names)

        for i, data in enumerate(res,start=1):
            print(f"get data from {data}")
            print("select name is :",data.get("nickname"))
            for j,value in enumerate(var_names):
                print(value)
                self.g_data.set_dict(f'{value}_{i}',data.get(var_names[j]))

        print(self.g_data.show_dict())




