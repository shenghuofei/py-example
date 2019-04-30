import pysnooper

'''
github: https://github.com/cool-RR/PySnooper
'''


@pysnooper.snoop()
def output():
    d = {"name": "asdfasf"}
    print(d)
    d['name'] = "123456"
    return d

output()
