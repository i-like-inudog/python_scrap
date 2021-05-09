# https://qiita.com/yuu116atlab/items/154ac83c03de233bf9fb
# http://nekoya.github.io/blog/2014/06/04/python-module-injection/

import inspect
import re

def get_var_name(var, symboltable=None):
    for k,v in symboltable:
        if id(v) == id(var):
            return k

def p(x):
    code_context = inspect.stack()[-1].code_context[0]

    pattern = r'p\((.*)\)'
    var_name = re.match(pattern, code_context).groups()[0]

    # global_vars = caller.locales().items()

    # var_name = get_var_name(x, global_vars)
    print(var_name, ': ', x)

