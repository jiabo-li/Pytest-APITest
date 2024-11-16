import ast
import json

from common.keyworks import keyword
from common.yamlparse import yamlparser
import pytest
import allure

g_cases = ["a","b","c"]
file_path = f"d:/apipractis/TestCases"
def getcases():
    g_cases = ["a", "b", "c","d","e","f"]
    print(g_cases)
    return g_cases
def get_all_cases():
    ympaser = yamlparser()
    ympaser.get_all_tasks(file_path)
    print(ympaser.g_tasks)
    return ympaser.g_tasks


class Test_apiruner:
    g_cases = get_all_cases()
    @pytest.mark.parametrize("caseinfo", g_cases)
    def test_run_case(self,caseinfo):
        print("test run case")
        print(caseinfo)
        des = caseinfo["desc"]
        steps = caseinfo["steps"]
        allure.dynamic.title(des)
        keyworks = keyword()
        for step in steps:
            for key,values in step.items():
                step_name = key
                key_function = values['KEY']
                params = values

            with allure.step(step_name):
                try:
                    keyfunc = keyworks.__getattribute__(key_function)
                except AttributeError as e:
                    print("Can't find the keyword",e)
                keyfunc(**params)





