### 打包python项目实例 [官方文档](https://packaging.python.org/tutorials/packaging-projects/)
#### 打包
1. 创建项目目录(如mymod)
2. 在项目目录(mymod)下新建项目源码目录(如mymod)
3. 在项目源码目录(mymod)下创建__init__.py及源码文件(如mymod.py)
4. 在项目目录下创建setup.py(setup.cfg如需要的话)
5. 在项目目录下执行python setup.py sdist 进行打包
#### 安装
1. 在项目目录下执行python setup.py install
#### 引用时注意事项
1. 引用时要明确包中的文件,直接import包名不行
    如要使用print_info函数需要
    ```
    from mymod import mymod
    mymod.print_info()
    ```
2. 如果要import包名,并在dir(包名) 中显示包含的模块，需要在__init__.py中添加相关信息
