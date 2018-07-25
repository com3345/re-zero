# Python代码技巧和割接经验中的分享

兼容Python2.7以上版本

## Python基本

首先Python有个应该坚持的总体格式原则，叫[PEP8](https://www.python.org/dev/peps/pep-0008/)标准，具体的标题叫Style Guide for Python Code规定了应该遵循的代码风格。

### 一、格式

格式说不重要也不重要, 说重要还挺重要的。格式关乎可读性。格式不对可能导致脚本失败。

#### 1 缩进

Python使用4个空格缩进，在编辑器中编辑代码时要注意是否设置了自动将tab转化为4个空格

#### 2 空格使用

各种符号后面都应该用空格

    name = "xiangxiao" √
    name= "xiangxiao" ×

    list = [1, 2, 3] √
    list = [1,2, 3]  ×

但是在写 函数调用时的关键字参数 或 函数定义时的默认参数 时 不应有空格

    # 注意name，age后面，紧跟了参数
    def get_name_and_age(name="xiao", age=10)    √
        pass

    def get_name_and_age(name = "xiao", age = 10) ×
        pass

#### 3 驼峰 or 下划线使用

    # Java是通过驼峰来增加可读性的
    # Python推荐用下划线来增加可读性
    def my_function():  √
    # is better than
    def myFunction():   △

#### 4 下滑线`_`号和`__`的使用

`_`有多种用法，但是最主要的用法是区分变量和方法是否私有

    class Girl(object): 
        name = "HuangYinQi"
        _age = 30
        __password = "woshixiaoxiannv"

        def get_name():
            return name

        def get_birth_year():
            return 2018 - _get_age()

        def _get_age():
            return _age

        def __get_password():
            return __password

Python没有protect这个属性，也不用priavte来控制变量访问，只通过前面添加双下划线`__`来指定私有变量或方法，通过在方法或者变量名前添加下划线来获得以下行为：

+ 没有下划线开头的方法和变量可以从类外直接访问，实例变量通过【实例名.变量名】访问，类变量（静态变量）通过【类名.变量名】访问。方法亦然。
+ 以单`_`开头的方法和变量的是同样可以从外界直接访问，访问方法相同
+ 以双`__`开头的方法和变量**不能**从外界直接访问，但是可以**间接访问**：

---
    print Girl.__password
    AttributeError: class Girl has no attribute '__password'
    print Girl._Girl__password
    woshixiaoxiannv

实际上，Python的私有变量并不是真的私有，只是将`__password`的前面添加了类名`_`Girl来避免子类的变量覆盖掉父类的相同的变量名，而非防止外界刻意地访问，虽然这个机制导致了不能直接通过变量名来访问，如果你非要访问，可以使用以上的方法，即:【`类名._类名__变量名`】来访问类“私有”变量；【`实例名._类名__变量名`】来访问实例“私有”变量。方法亦然。

但是机制上是这样的，并不代表我们不应该在语法层面通过加下划线来“昭告”别人和“暗示”自己，这些变量和方法是不是要暴露出去。因此个人习惯于：

+ 无下划线开头，代表公有，彻底暴露出去
+ 单下划线开头，代表仅供类内部其他函数使用的，不想暴露出去的，
+ 双下划线开头，完全不想暴露的

#### 5 其他

+ 单行最好不超过80个字符，但可读性是最高前提！例
+ 

### 二、 最佳实践


#### 1 has_key()将被淘汰
    
    if name in my_dict: √

    if my_dict.haskey("name"):  △

#### 2 字符串拼接
    my_num = ''.join(("1", "2", "3"))  √
    # is faster than
    my_num = "1" + "2" + "3"           △

#### 3 字符串格式化

    "My name is {}, I am {} years old".format("xiangxiao", 18)
    # Or
    "My name is {0}, I am {1} years old".format("xiangxiao", 18)
    # Or
    "My name is {name}, I am {age} years old".format(name="xiangxiao", age=18)

    # is better Than

    "My name is %s, I am %d years old" % ("XiangXiao", 18)  △

    还可以通过在花括号内添加【:格式符】指定格式：
    print("Sammy ate {0:.1f} percent of a pizza!".format(75.765367))
    print("{:*^20s}".format("Sammy"))

#### 4 `is None` 和 `== None`

`is`类似于比较地址, `==`比较值

    lst = [1, 2, 3]
    lst == lst[:]  # True
    lst is lst[:]  # False， Python重新分配了空间给列表的切片

> PEP8： Comparisons to singletons like None should always be done with is or is not, never the equality operators.

为什么？因为`==`可以在python中可以通过被重载，

如，

    class Negator(object):
        def __eq__(self,other):
            return not other

    thing = Negator()
    print thing == None    # True
    print thing is None    # False

也就是说一个object可以==空但非空，这不是我们想要的。例子

#### 5 `is None` 和 `not value`

    print "" is None # False
    print not ""     # True
    print not None   # True

`is None`仅判空，`not value`在value为None或""、[]等“空或者看起来空”的情况都覆盖。

因此可以择机使用

    if value:   # 当value不为空且不为""、[]等看起来空的值时

    if not value: # 当value位空或不为""、[]等看起来空的值时

#### 6 `try except`不要裸抛

try catch语句在python中是以以下形式呈现, `[]`为可选的。

    try:
        # block 1
    except [异常类型 as e]:
        # block 2, 发生异常时， 执行此处
    [else]:
        # block 3, 当block 1被顺利执行完没有捕捉到异常, 执行此处
    [finally]:
        # block 4, 当1——>2或1——>3执行完，必定执行此处哪怕在1,2,3中有raise，sys.exit等中断操作


其中`except`后要指定异常类型，不要直接抛，如果所有异常都想捕获在一个异常处理block里，那就`except Exception`

### 三、 Pythonic

像写英文一样写python，怎么想的就怎么做

比如说

    for number in number_list:
    而不是
    for i in range(0, len(number_list)):
        number = number_list[i]

    if x is not None
    而不是
    if not x.equals(None)

等等，

#### 1 列表解释式

列表解释式表达能力很强，很简洁，关键是体现了python理念，怎么想的就怎么做

例如，把列表中的每个大于0的元素都平方后塞到一个新列表中

计算机思绪是：

1. 我先要遍历列表，
2. 在遍历的过程中取出每一个值，
3. 判断是否大于0，
4. 对于大于0的数进行平方，
5. 然后塞到新列表中

人类的思绪或者说英语的思绪则应该是**我新的列表的元素值是旧列表非负元素平方**。这句话中最重要的就是元素值平方。

    num = [1, -2, 3, -4, 5]
    new_list = [x**2 for x in num if x > 0]

正如英语中，最重要的话往往放在最前面，于是有`x**2`；定语从句放在后面：解释*哪样的x*呢？哦，x > 0的那些x

<p align="center">
  <img src="./imgs/列表解析式.jpg">
</p>

#### 2 `_`的另外作用

`_`可以做方法名`def _():`；也可以做变量名`_ = 3`。但是一般不直接使用，而只在一些约定俗成的场景下使用，其中最常用的是当做*废弃变量*

    def get_name_and_age():
        return self.name, self.age

    # Python支持函数返回不止一个返回值，通过把几个值包装为一个tuple实现
    # 当使用这个函数却只用到其中一个值时，可以用_代表废弃的那个

    _, her_age = get_name_and_age()

#### 3 `*`的作用

`*`有除了可以表示乘法以外还有以下作用

`*`可用于解包（unpack），把一个sequence/collection解包成位置参数。
`**`同样是解包，但把字典解包成关键字参数

    def query_ecs_endpoint(self):
        return self.host, self.port

    query_image_detail_url = 'https://{0}:{1}/v2/images'.format(*query_ecs_endpoint())

    def get_server_info(self):
        return {"tenant_id": self.project_id, "server_id": self.ecs_id}

    query_ecs_detail_url = 'https://{}:{}/v2.1/{tenant_id}/servers/{server_id}'.format(*query_ecs_endpoint, **get_server_info())

既然向方法传递参数时可以用`*`和`**`，那么岂不是方法定义时也能接受`*`, `**`参数

    def sum(*values, **options):
        s = 0
        for i in values:
            s = s + i
        if options.get("neg") is True:
            s = -s
        return s

    s = sum(1,2,3, neg=True)  # -6
    s = sum(1,2,3, neg=False) # 6
    s = sum(1,2,3)            # 6


最后，`**`可表示平方`2 ** 3 = 8`
 
#### 4 enumerate关键字

    for server_id in server_id_list: # 很帅很Pythonic但是如果我要序号信息怎么办？即一般循环中的i参数

    for (i, server_id) in enumerate(server_id_list):
        logging.info("开始处理第{}台服务器：{}".format(i, server_id)
    # output:
        开始处理第0台服务器:471a-451b....
        开始处理第1台服务器:1asz-9952....

有点奇怪？
加个参数

    for (i, server_id) in enumerate(server_id_list, 1):

你懂我意思吧？

#### 5 列表切片

切片好顶赞，基础语法 `[start:end:step]`
列表是有序号的
    
    # 正着数：
      0    1    2    3
    ["a", "b", "c", "d"]
     -4    -3   -2   -1
    # 倒着数

所以有例子
    
    # 翻转列表
    a = ["a", "b", "c", "d"]
    b = a[::-1] # 省略start和end就表示从-1到-4, step=-1, 所以从-1开始减到-4, b = ["d", "c", "b", "a"]
    
    # 偶序数值
    b = a[::2]
    # b = ["a", "c"]

    a[-1] # 取最后一个值
    a[-2:] # 取最后俩
    a[:-3] # 去掉最后仨
    等等

### 三、常见迷思

#### 1 script, module, package

**script**和**module**本质没有区别都是可以被执行的一段代码，

但是**script**一般指直接可以自运行的比如通过添加`if __name__ == "__main__"`代码来达到自运行
    
    # test.py
    def foo():
        print "I am your father"

    if __name__ == "__main__":
        foo()

    # 通过python 脚本名执行
    ~> python test.py
    ~> I am your father

而**module**可以理解为用`import`导入的library代码文件，不**应该**被完整执行。

##### 1.1 `if __name__ == "__main__"`的作用

至于`if __name__ == "__main__"`做一个判断的原因就是用来区分，当前执行的代码文件究竟是**script**还是**module**

首先`__name__`可以是一个py文件的名字，test.py的`__name__`是`test`

因为Python会把在命令行用`python 文件名.py`来执行的入口文件的`__name__`值设置为`"__main__"`以区分【直接被执行的文件】和【在被执行的文件中被`import`进来的文件】，直接被执行的文件会被视为主程序。

这样有什么好处呢？如果你有一个文件既可以直接执行，又可以作为**module**被`import`到另外一个文件被另一个文件使用自己的某些方法或者类，比如`my_module.py`

    # my_module.py
    class bar():
        def say_hi():
            print "{}'s name is {}".format(__file__, __name__）

    if __name__ == "__main__":
        b = bar()
        b.say_hi()

    
    # 在test.py中引用my_module中的类
    from my_module import bar

    def foo():
        print "{}'s name is {}".format(__file__, __name__）

    if __name__ == "__main__":
        foo()
        test_b = bar()
        test_b.say_hi()

则执行`python test.py`，将并不会执行my_module.py文件中的`b = bar();b.say_hi()`部分，输出将会是：
    
    ~> python test.py
    ~> test.py's name is __main__
       my_module.py's name is my_module


##### 1.2 package和`__init__.py`

同一个文件夹下其他module可以直接用import来引用，但是不同的文件夹的其他module怎么import呢？这就涉及到**package**的管理.


**package**是python提供的构建namespace的功能，任何包含`__init__.py`文件的文件夹都被视作**package**. (p.s.在大于3.3的版本中，所有文件夹都被认为是package，可以不额外放置一个`__init__.py`文件)

##### 1.3 `import`使用方法

    import <package> [as xxx]
    import <module>  [as xxx]
    from <package> import <module or subpackage or object> [as xxx]
    from <module> import <object> [as xxx]

其中`[as xxx]`是可选项，意思是给**module**或**package**取个别名。

> 当一个**module**被`import`，python会执行**module**的所有语句；当一个**package**被`import`，实际上是**package**所包含`__init__.py`被`import`了，`__init__.py`内的语句将会被全部执行。

并且，`import`是通过搜索`sys.path`这个列表来查找被`import`的**module**或**package**（实际上package也可以看做一个module，以下不做特殊说明时，用module指代module和package）。搜索顺序是：

1. [Python标准库](https://docs.python.org/2/library/)里的**module**(比如`math`, `os`)
2. `sys.path`里包含所有路径里的**module**
    1. `sys.path[0]`在交互式（在command line里面输入python或者ipython等进入的模式，没有当前文件）模式下为空字符串`""`；如果是通过`python xxx.py`运行的，那么`sys.path[0]`置为`xxx.py`
    2. `sys.path`里还包含`PYTHONPATH`环境变量
    3. 一些默认的位置

可通过以下方式查看

    import sys
    print sys.path

    # output:
    [
        "",
        "C:\\Python36\\Scripts\\ipython.exe",
        "c:\\python36\\python36.zip",
        "c:\\python36\\DLLs",
        "c:\\python36\\lib",
        "c:\\python36",
        "c:\\python36\\lib\\site-packages",
        "c:\\python36\\lib\\site-packages\\openpyxl-2.5.2-py3.6.egg",
        "c:\\python36\\lib\\site-packages\\pip-8.1.2-py3.6.egg",
        "c:\\python36\\lib\\site-packages\\IPython\\extensions",
        "C:\\Users\\x00442516\\.ipython"
    ]

所以，如果当你的模块名字和他人写的模块名字或者系统模块名字重名时，会出现奇怪的覆盖问题。因此**尽量不要使用重名**

##### 1.4 相对和绝对引入

写`import aaa.bbb`时，这个`aaa.bbb`的路径根据【相对于谁来说的】可以分成三种引入

1. 绝对引入（**absolute import**）：从项目根目录到需要被`import`的**module**的完整路径
2. 显式相对引入（**explicit relative import**）： 从当前**module**到目标**module**。形式是`from .<module/package> import X`，其中`.<module/package>`表示当前目录的其他模块，`..`两个点表示上层目录，依次类推
3. 隐式相对引入（**implicit relative import**）：只有当前模块的路径被加入到`sys.path`中才可以使用。

例子，

<p align="center">
  <img src="./imgs/目录.png">
</p>

在`a1.py`中如果我们想引入**父目录**中的`other.py`, **相同目录**中的`a2.py`, **子目录**中的`sa1.py`的话，三种方式分别为：

    # 绝对引入，视角是从根目录来看的，即test/
    import other
    import packA.a2
    import packA.subA.sa1

    # 显式相对引入，视角是从当前module来看的，即a1.py
    
