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

+ 单行最好不超过80个字符，但可读性是最高前提！
+ 

### 二、 最佳实践


#### 1 has_key()将被淘汰
    
    if name in my_dict: √

    if my_dict.haskey("name"):  △

同样，用`in`和`not in`而不是`__contains__`来检查是否包含某元素，如

    >>> "ild" in "Children" # True

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

也就是说一个object可以==空但非空，这不是我们想要的。

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
    a[:3] + a[4:] # 去掉第四个
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
    1. `sys.path[0]`在交互式（在command line里面输入python或者ipython等进入的模式，没有当前文件）模式下为空字符串`""`；如果是通过`python xxx.py`运行的，那么`sys.path[0]`置为`xxx.py`所在目录
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
    import other
    from . import a2
    from .subA import sa1

    # 隐式相对引入，就是没有.视角是从当前module来看的, 即a1.py。 【该方式Python3将不可使用】
    import other
    import a2
    import subA.sa1

注意的是，相对引用的顶级package/（top-level package，相对引用最高可以到达的但不包含的目录）是由入口脚本，在这里就是`start.py`决定的，也就是说`a1.py`中的相对引用最高可以到达的是`start.py`所在位置，而非`test/`，因此`a1.py`对`start.py`周围文件的信息是感知不到的，或者说`test/`这个package底下有其他什么文件是不知道的。

因此当你试图使用`from .. import other`将会失败提示`ValueError: attempted relative import beyond top-level package`。告诉你试图从`start.py`这个**top-level**的上层`test/`去引用一些东西，但`a1.py`不认识`test/`导致失败。

所以相似的例子：**任何直接运行**的脚本（入口脚本）都无法引用父文件夹中的文件。 错误原因与上面一样，被直接运行的脚本**决定**了最高路径，从而**决定**了可以引用的包的路径。 如果试图从`sa1.py`中`from .. import a1`同样会报`ValueError: attempted relative import beyond top-level package`

##### 1.5 总结

结合上面所有内容，总结如下：

1.  直接运行的脚本要有`if __name__ == "__main__":`
2.  尽量使用绝对路径。如果一定要使用相对引用，使用显式而非隐式
3.  尽量不要从父文件夹引用文件，如果要用，使用绝对路径
4.  不要使用重名的module或package

#### 2 中文编码问题

##### 2.1 编码基础

首先电脑天然不储存字符的，只储存`1`和`0`。再来看以下几个概念

+ 字符（character）：`I`,`爱`,`あ`
+ 码位（code point）：一个长度不一定的十六进制整数值，用于表示某一个字符，比如0061是代表`a`。怎么规定哪个字符是由哪个整数代表，并不统一。unicode只是其中一种方案但却是最主流的方案。
+ Unicode编码或者说Unicode标准：用一张表记录了几乎所有**字符**和**码位**之间映射关系的标准
+ Unicode字符串（string）：一系列的遵循unicode标准的**字符**， 因为**字符**用**码位**表示，所以本质是一系列的**码位**，更本质的是一系列的**16进制整数**，更本质我一系列**2进制**数，但存在内存中是以**bytes（8位2进制4个字节）**存在的。

**Unicode其实只规定了这个字符和码位的对应的编码，但并没有规定如何传输和保存这个编码**， `ASCII`，`Latin-1`，`UTF-8`，`UTF-16`，`GBK`等都可以认为是规定了如何传输和保存这种编码关系的格式

##### 2.2 UTF-8

UTF-xx和Unicode之间的关系，通过UTF的全称就能知道

UTF全称Unicode Transmission Format，**Unicode的传输格式**，意思是传输的时候我们要进行压缩，不然Unicode string全长空间太长了（一个字符4个bytes）浪费传输带宽。这个压缩的过程就叫encode编码，反之decode解码。

                             encode
        字符串       ---------------------->     字节串
    unicode string  <-----code points----->   UTF-8 string
    （unicode类型）  <----------------------   （str类型）
                             decode

UTF-8就是用8位1个字节用于编码，但是具体一个“code point用多少个8位/字节”是不一定的，可以是1个字节，也可以是2,3,4个字节，因此同时具备扩展性和可伸缩性，是一种可变长编码，比全长的4个字节要好多了吧。

UTF-8具体这样决定：

1. 当code point的值<128（0x80）时，那就用code point这个整数值本身
2. 当code point的值>=128 (0x80)时，那就变成2、3、4个字节来表示，每个字节范围是128~255(0x80~0xff)

我们和ASCII来进行对比, ASCII也是用8位1个字节用于编码的，但是**只能使用1位表示一个字节**，因此它最大只支持code point < 128的字符。 UTF-8则可以表示全部，另一个显而易见的好处是UTF-8是向后兼容的，用**ASCII进行编码的文本天然也是UTF-8文本**


##### 2.3 Python2和Unicode、str

在Python中对于字符串和字节串的区分很让人困惑！`basestring`的子类有两个，
一种是`str`，一种是`unicode`。简单理解的话，`unicode`表达的是**文本**是code points的序列，是真正的“字符串”；`str`是bytes串字节串，是二进制的序列。见上面的图。

还有个蛋疼的地方是，unicode string在python2中的默认编码并不是UTF-8而是ASCII码。所以你经常会发现以下错误：

    >>> s = Unicode("你")
    UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0:
    ordinal not in range(128)

注意这句话：`can't decode`， 因为什么呢？因为`你`的code point显然是超过128的，`Unicode("你")`实际上是一个decode的过程，是把字符串“
解压”为unicode string，而默认的decoder是ASCII，ASCII只能处理128以内的，所以出错了。

你可以指定用于decode用的编码`unicode("你", encoding="utf-8")或者unicode("你", "utf-8")`就不会出错。Python支持几乎所有常见编码。

Unicode string也是basestring，因此可以使用各种`find()`，`replace()`，`upper()`的方法。 但是这些参数如果是字符串的话，也必须是code point值小于128的，因为这里还是会隐式地进行一次ASCII码式的decode。

另外一个最重要的也是最常用的unicode方法是`.encode([encoding], [errors='strict'])`，就是encode编码嘛。比如说

    >>> u"你abc".encode("utf-8")
    >>> '\xe4\xbd\xa0abc'  # "你"用三个字节来表示，"abc"小于128，原封不动
    
    >>> u"你abc".encode("ascii")
    UnicodeEncodeError: 'ascii' codec can't encode character u'\uf4u0' in
    position 0: ordinal not in range(128)

成功encode之后，字符串的类型将由`unicode`变成`str`，或者准确的说是从**字符串**变成了**字节串**。自然也有反过程`.decode([encoding], [errors='strict'])`.

    >>> "你", type("你")
    >>> ('\xe4\xbd\xa0', str)
    >>> "你".decode("utf8"), type("你".decode("utf8"))
    >>> (u'\u4f60', unicode) 

##### 2.3 Python2字符串处理建议

##### 读写io流场景

Python2处理文件时，应该把python当做一个水池，水池进口处文件全部转成unicode--->在水池
中始终保持unicode处理，出口处再转成目标编码。

---
    # 假设读取的文件是utf8编码的
    with open("myfile.txt", "rb") as f:
        text = f.read().decode("utf8")

    # 写
    with open("output.txt", "rb") as f:
        f.write(text.encode("utf8"))

同样地，读取序列化时，也要解码再编码

    content = '{"名字":　"小明"}' # str类型, 如果是unicode的话就不用考虑解码问题了
    mydict = json.loads(content, encoding="latin-1")  # 如不指定encoding，将使用utf-8解码

    mydict[u"年龄"] = 18 # 注意用unicode来暂存字符串
    return json.dumps(mydict, ensure_ascii=False)

这里解释一下为什么要用这个参数`ensure_ascii=False`:

> If ensure_ascii is true (the default), all non-ASCII characters in the output are escaped with \uXXXX sequences, and the result is a str instance consisting of ASCII characters only. If ensure_ascii is false, some chunks written to fp may be unicode instances. This usually happens because the input contains unicode strings or the encoding parameter is used. Unless fp.write() explicitly understands unicode (as in codecs.getwriter()) this is likely to cause an error.

> 当ensure_ascii为true(默认值)时，所有非ASCII字符比如中文，会变成结果字符串里的\uXXXX， 保证了返回值是一个只包含ASCII字符的str实例。当ensure_ascii为false时，有些情况下会变成unicode实例。当输入值里面包含了unicode，strings或者是encoding参数被赋了值就会返回一个unicode。除非fp.write()显式得知了unicode(比如说通过codecs.getwriter()获取)，这种方式容易产生错误

为什么会有这个值且为什么默认为**保证**返回一个ascii字符的str实例呢？其实主要是为了保证`json.dump`这个函数正常工作，因为python的默认encoder是ascii码，在正常的`with open`中使用`write`函数也就会使用`ascii`来编码，如果dump的obj中含有非ascii的字符就会导致编码失败。 （p.s.在最新的Python3.7中，默认编码才变成了utf-8）

##### 在.py文件中使用非ascii字符

所有的.py文件打开文件第一行都是 `# -*- coding: utf-8 -*-`

它的含义是让python解释器在读取当前.py文件中时可以“理解”非ascii字符从而保证了.py文件中可以使用非ascii字符，而并非**使得当前默认的编码变成utf-8**

所以即便这样声明，也不能保证你在`f.write(output)`这样的操作不会因为编码问题失败。

具体是如何生效的，可以想象.py文件本身也是一段text，即便是现在的编辑器或者IDE都能以utf-8保存.py文件，但是它从硬盘中读取出来运行的时候也是要按照一定编码的，python默认编码是ascii，如果不显式的指定utf8的话，那自然会导致ascii编码不认识.py中超过code points超过128的字符，执行失败。`# -*- coding: utf-8 -*-`就是告诉解释器，要用utf-8读取执行。

##### 建议不要使用`import sys; reload(sys); sys.setdefaultencoding("utf8")`

> This allows you to switch from the default ASCII to other encodings such as UTF-8, which the Python runtime will use whenever it has to decode a string buffer to unicode.

> 这个（命令）可以让你从默认的ASCII编码转变为其他编码比如说utf8，使得python解释器能够在无论何时你需要把string buffer转化成unicode时使用该编码。

有无数理由建议你不要这么做，但总结起来就是：

1. 这并不是一种末端用户（end-user）代码，也就是说没事儿不要操作底层
2. python3开始严格区分了bytes和string（下面会讨论）这个命令将不可用

在python2中，乖乖地使用unicode并在I/O时使用`decode("utf8")`和`encode("utf8")`

##### 2.4 Python3的字符处理

Python3把string和bytes彻底分开，string字符串就只有一种，类型名叫`str`形如`my_str = "我爱you"`, 二进制bytes（由unicode encode而来）另外一种类型`bytes`形式b`abc`(聪明的你肯定会知道bytes类型只支持ascii字符)

                             encode
        字符串       ---------------------->     字节串
    unicode string  <-----code points----->    二进制string
      （str类型）    <----------------------   （bytes类型）
                             decode

所以在python3中不用使用`u"我"`这样的表达了

同时在python2中，`"我爱{}".format("你")`和`u"我爱{}".format(u"你")`都是可用的，但是在python3中，`b"ab{}".format(b"c")`直接就不给用了

#### 3 静态/类变量， 静态/类方法

一个例子说明白

    class Test(object):
        s_var = 0
        def __init__(self):
            self.name = "Mike"

        @staticmethod
        def s_func():
            print "hello"

        @classmethod
        def c_func(cls):
            return cls.s_var

        @classmethod
        def wrong_c_func():
            pass

Python其实区分**静态变量**, **类变量**，他们都是一种表示被所有类的所有实例所共享的变量，写在类中且不在函数体内的变量都是这样的变量，统一叫**类变量**，与之相对的，`self.name`是实例变量，`@staticmethod`装饰器修饰的是静态方法，`@classmethod`自然就是类方法。

这两者的区别就是，被`@classmethod`所修饰的方法在被调用时，无论形参里面有没有给参数，都默认会把自己所处的类的当做参数传进去， 方便使用类的其他能力

因此，用不到类作为参数的方法，比如说公共的方法，就可以定义为静态方法，甚至可以丢到类外面（至于要不要丢到类外面，就要看你逻辑上是怎么组织这些函数和类的了）。而要用到这个cls参数的，就用类方法

下面例子也可以直观地体验两者差别

    >>> Test.c_func()
    >>> 0
    >>> Test.wrong_c_func()
    >>> TypeError: wrong_c_func() takes no arguments (1 given) # 默认传进来的参数，Test

### 4 一些python的特性

#### 4.1 更强大的列表解析式

zip操作：
    
      "display": [
    {
      "label": "地域",
      "type": "string",
      "value": "diyu1-ss(zm_vdc_project)"
    },
    {
      "label": "名称",
      "type": "string",
      "value": "ecs-1bfd"
    },
    {
      "label": "可用分区",
      "type": "string",
      "value": "kvm.type2"
    },
    {
      "label": "规格",
      "type": "string",
      "value": "sp002"
    },
    {
      "label": "镜像",
      "type": "string",
      "value": "cirros_kvm"
    }


    labels = [u"地域", u"名称", u"可用分区", u"规格", u"镜像"]
    values = [u"diyu1-ss(zm_vdc_project)", "ecs-1bfd", "kvm.type2", "sp002", "cirros_kvm"]

    display = [{
        "label": l,
        "type": "string",
        "value": v
    } for l, v in zip(labels, values)]

一行快排：

    def quicksort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i >pivot]
            return quicksort(less) + [pivot] + quicksort(greater)

    def q_sort(l):
        return l if len(l) < 2 else q_sort([el for el in l[1:] if el <= l[0]]) + [l[0]] + q_sort([el for el in l[1:] if el <= l[0]])


#### 4.2 函数编程

函数编程的奥义就是怎么想的就怎么做

简单的例子，把列表中的int全部变成string
    
    # java    
    List<Integer> oldList = ...
    
    List<String> newList = new ArrayList<String>(oldList.size()) 
    
    for (Integer myInt : oldList) { 
        newList.add(String.valueOf(myInt)); 
    }

    # Python
    new_list = map(str, old_list)

    # 不谋而合的guava
    import com.google.common.collect.Lists;
    import com.google.common.base.Functions

    List<Integer> integers = Arrays.asList(1, 2, 3, 4);
    List<String> strings = Lists.transform(integers, Functions.toStringFunction());

    # lambda
    # 按value的大小顺序打印key
    for key, value in sorted(my_dict.items(), key=lambda x: x[1]):
        print key

#### 4.3 迭代器，生成器

<p align="center">
  <img src="./imgs/迭代器生成器.webp">
</p>

##### 迭代器(iterator)

通俗易懂地讲，迭代器就是允许你进行遍历其集合中所有元素的object，外在表象是如此，内在是只要实现了`__next()__`方法的类的object都叫迭代器，但还有其他方法实现（比如生成器）

##### 可迭代（iterable形容词），可迭代对象（iterables名词）

可以通过iter(自己)来返回一个迭代器的类都叫可迭代的，因此除了实现`__next__`以外你还得实现`__iter__`函数用于返回一个迭代器。

数据结构set就是可迭代对象（iterables）, 可以通过iter(set对象)来获取它的迭代器（iterator）

    a_set = {1， 2， 3}
    a_iterator = iter(a_set) # type(a_iterator) = iterator

所以一个简单的iterable类就这么设计,

    class Series(object):
        def __init__(self, low, high):
            self.current = low
            self.high = high

        def __iter__(self): # 在Python2中这个函数叫iter
            return self

        def __next__(self): # 在Python2中这个函数叫next
            if self.current > self.high:
                raise StopIteration
            else:
                self.current += 1
                return self.current - 1

    n_list = Series(1,10)    
    print(list(n_list))

##### 容器（Container）

这可不是docker的容器，有数据值的并支持通过`in`或`not in`来某个元素是否存在它的内部中的对象都可以叫做容器。 如何实现`in`, `not in`查询元素存在呢？实现`__contains__`函数，例如

     class Player():

        def __init__(self, name):
            self.name = name

        def __contains__(self, substring):
            if substring in self.name:
                return True
            else:
                return False

    obj1 = Player("Sam")
    print ('am' in obj1)    ----> True
    print ('ami' in obj1)   ----> False

##### 生成器（Generator）

生成器其实是迭代器的另一种实现方式，而且更省空间，更简便。

    def series_generator(low, high):
        while low <= high:
           yield low # break, 这里就是
           low += 1

    n_list = []
    for num in series_generator(1,10):
        n_list.append(num)

    print(n_list)
    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

`yield`关键字提供两个功能

1. return 相同的功能，返回一个low
2. **暂停**（而非停止）函数执行，**跳出**（而非退出）函数，**保存上下文**

当`for ... in`试图遍历生成器时，会进入到生成器内部从头往下执行，直到找到yield，第一次执行到yield处时，返回当前的low并跳出；然后使用完返回的low之后又一次进入生成器内部，但是这一次不是从头开始执行了，而是从刚才跳出的地方下一行开始继续执行。

这样一个简单的`yield`就完成了迭代器，而且，虽然`series_generator(1, 10)`表现得像个列表，可以从里面源源不断地拿出数字来，但每次拿出的数字都不是提前生成好的，而是当场计算后吐出来的。这意味着如果用生成器替代含有大量数据（并且可按照一定规则计算算出来的）容器时，可以节省大量空间。 

比如：

    import sys
    
    l_10 = [x for x in range(10)]
    g_10 = series_generator(0, 9)
    print sys.getsizeof(l_10), sys.getsizeof(g_10) # 100, 40

    l_100000 = [x for x in range(100000)]
    g_100000 = series_generator(0, 99999)
    sys.getsizeof(l_100000), sys.getsizeof(g_100000) # 412236, 40

3.3以上版本，甚至支持生成器解析式，
    
    (x for x in range(10) if x % 2 == 0) # 返回生成器
    [x for x in range(10) if x % 2 == 0] # 返回

##### 协程和asyncio, await

Python3.5开始引入的关键字级别的协程特性，可以非常简单地实现使用协程来实现异步IO操作

至于协程是什么，我理解是通过保存函数上下文来实现的语言级别的多任务能力。
