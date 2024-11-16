from jinja2 import Template

def refresh(target,content):
    if target is None:
        return None
    return Template(str(target)).render(content)


def t_Refresh():
    target = {
        "name":"{{name}}",
        "token":"{{token}}"
    }

    context = {"name": "张三", "token": "3242343242343432432"}
    res = eval(refresh(target, context))

    print(res["token"])

t_Refresh()