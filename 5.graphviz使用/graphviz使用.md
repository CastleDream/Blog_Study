想在vscode中使用graphviz绘制流程图，其实很简单。

# 1. 安装
确保电脑上安装了graphviz，
+ 首先要先安装[homebrew](https://brew.sh/index_zh-cn),就是在命令行输入命令   
    ```
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    ```

+ 然后开始安装graphviz。**brew install graphviz**（然后速度也比较慢。。。 还会下载一些graphviz的依赖包，要等一会，差不多一个小时半小时吧，网速差的话。安完了之后有一些提示文字）
+ 然后直接下面，就好了 也不用pip install graphviz了
    ```
    pip install pydot
    ```

---
在vscode中
+ 只需要安装**插件Graphviz（dot） language support for Visual Studio Code**（另外，为了预览效果更好，可以安装**Graphviz Preview**）
+ 直接新建.dot文件，输入以下代码（仅作为示例），就可以在预览中看到一个简易的流程图了：
    ```
    digraph first{
    a[lable="这是a" shape="diamond"];
    b[lable="这是b" shape="box"];
    c;
    d;
    a -> b[lable="边"];
    b -> c;
    d -> c;}
    ```
+ 以上部分参考 https://blog.csdn.net/qq_38295511/article/details/97555223

# 2. 教程
主要是参考官方文档进行一些简单基础的使用：[graphviz官方文档](http://www.graphviz.org/documentation/)

## 2.1. The dot language
1. 关键词**node, edge, graph, digraph（directed graph有向图）, subgraph（子图）和strict**都是不区分大小写的。此外，指针值（A->B,也就是表示节点的东西，可以允许其不是关键字，因为这些字符串也可能在别的地方被用作一般的标识符，解析器可以接受任何标识符）。
2. 流程图中所有对象都有自己唯一的id（可以指定，可以不指定，不要求必须指定，[ID] 可选）。
    一个ID（也就是一个对象名字），可以是以下内容
    + 由任意字母（a-zA-Z），下换线，或者数字，不以数字开头构成的字符串
    + 以下划线开头的数字
    + 任意双引号括起来的字符串，可以包括转义符
    + HTML字符串（也就是<>括起来的）
    （PS：一个ID就是一个字符串，第一种情况其实是为了简单省略了引号，如果是想使用关键字作为ID值，例如 graph，则需要加上引号，即”graph“）
3. 边表示（edge-op） 有向图中，使用”->“表示边；向图中，使用”--“表示边
4. 注释（comment），dot语言支持C++样式的注释，即：/* */和//。此外，使用‘#’开头的行会被C预处理器作为一个行输出，（例如：# 34 表示行 34 )会被丢弃.）
5. 分号，逗号，空格。分号和逗号有助于提高可读性，但不是必需的。 另外，可以在终端之间插入任意数量的空格。
6. **子图和簇**（Subgraphs and Clusters）子图在graphviz中有三个作用：
    1. 子图可以用于表明图的结构，表明哪些节点和边应该在一起。这是子图最基本的作用，表明图组件的明确语义信息。其也可以为边的定义提供方便，edge定义语句运行edge操作符左右都有子图，一个边是从边操作符左侧的每个节点到边操作符的右侧的每个节点，如下面的定义：A -> {B C} 等价于 A -> B A -> C。可以看看 {AB CD} -> {E F} 这个的效果
    2. 子图可以为设置属性提供上下文环境。比如：可以定义该子图中所有节点颜色为蓝色。以下例子：
    subgraph { 
    rank = same; A; B; C; 
    }  
    （该匿名子图表示A B C三个节点应该位于图中的同一级别）
    3. 由特定图引擎决定的图的布局。如果子图的名字以cluster开头，则graphviz会将这个子图视为一个特殊的簇子图。在支持的情况下，布局引擎会将属于同一簇的节点布局到一起，同时保证整个簇绘制在边界矩形中。请注意，无论好坏，簇子图都不是DOT语言的一部分，而仅仅是某些布局引擎所遵循的语法约定。
7. **词汇和语义注释**（Lexical and Semantic Notes）
    + 一个图必须定义为digraph（有向图）或者graph（无向图）。从语义来说，这表明节点之间的边是否有方向；从词汇上来说，一个有向图必须使用'->'定义边，而无向图必须使用'--'；在操作上，该区别用于定义不同的默认渲染属性。 例如，默认情况下，将使用指向头节点的箭头来绘制有向图的边缘。对于普通图形，默认情况下绘制的边缘没有任何箭头。
    + 图也可以描述为严格（**strict**）。 这禁止创建多边缘，即，对于有向图和无向图，相连的两个节点之间最多只能有一个边。 随后使用相同两个节点的edge语句将使用先前定义的边缘节点标识该edge，并应用edge语句中给定的任何属性。 例如
    ```
        strict graph { 
        a -- b
        a -- b
        b -- a [color=blue]
        } 
    ```
    上述语句其实只创建了一条蓝色的边
    + 另外，如果在节点，边或者图定义语句中定义了一个默认属性，或者当一个属性没有与特定的点或者边关联时，其后定义的任何类型合适的对象都会继承这个属性，直到那个默认属性被指定新值。针对默认属性之前定义的对象，一旦默认属性进行了定义，会有一个空白属性绑定到该对象的属性上。
    + 尤其需要注意的是，子图在定义时会继承父图的属性设置。这一属性很有用，比如：可以对根图定义一种字体，则所有子图都会使用这种字体。不过对于某些属性，这一继承特性就不尽如人意了。如果将一个label属性绑定到根图上，继承这个属性到所有子图上可能就不是我们所想要的结果。与其将图属性列在顶层的图中，在子图中重置这些属性，还不如直接在需要使用该属性的子图中进行定义，而不是在顶层的图中进行定义。
    + 如果一个边属于一个簇，则其端点属于该簇。因此，有时一个边也可以影响布局，因为簇有时是递归布局的。
    + 子图和簇有一些限制。①目前，图和子图使用相同的命名空间，因此，每个子图必须有不一样的名字。②虽然节点可以属于任意数量的子图，但是当将簇视为节点和边的子集时，我们认为簇形成了一种严格的层次结构。
8. **字符编码（Character encodings）**
+ dot语言最少支持ascii字符集，带引号的字符串（普通的字符串和类似HTML的），也可以包含非ascii字符。在大多数情况下，这些字符串是无解释的，他们仅仅作为特有的标识符或者以不变的方式传递的值（不需要进行说明）。而labels便签则是必须要显示的，为此，软件需要计算文本的大小并确定何时的字形，因此需要明确所使用的编码集。
+ DOT默认使用utf-8字符集，也接受Latin1 (ISO-8859-1) 字符集，输入的图可以使用charset属性来指定字符集。对于使用其它字符集的图，通常可以使用像iconv这样的程序将字符集进行转换。
## 2.2. Command-line Invocation命令行调用
所有graphviz命令调用形式都是类似的：
```
cmd [ flags ] [ input files ]
```
如果没有给出input files，则从stdin中进行读取。
1. **Flags**
    + -Gname[=value] 设置图属性，默认 value=true
    + -Nname[=value] 设置默认节点属性，默认value=true
    ……
详细说明，https://graphviz.gitlab.io/_pages/doc/info/command.html
2. **Environment Variables**
详细说明网页同上。
## 2.3 Output Formats输出格式
在命令行中使用 -T来标志。例如： 
```
dot first.dot -Tpng -o first.png
```
其中 -Tpng 中png表明输出格式。详见[Output Formats](https://graphviz.gitlab.io/_pages/doc/info/output.html)

支持常见的如：.bmp, .eps, .gif, .jpg, .jpeg, .pdf, .png, .ps, .svg, .tiff等。
## 2.4 Node, Edge and Graph Attributes
所有的graphviz属性都是使用名称-值这样的键值对进行定义，例如，要设置一个叫abc的节点的填充色，使用：
```
abc [fillcolor = red]
```
类似的，如果想设置一个边的箭头样式，可以使用：
```
abc -> def [arrowhead = diamond]
```
注意，有些属性，arrowhead和arrowtail对于无向图而言是无意义的。[这一页](https://graphviz.gitlab.io/_pages/doc/info/attrs.html)给出的表格中，注意：E, N, G, S和C分别表示边，节点，根图，子图和簇子图。

以下仅介绍常见的一些属性：
+ _background 背景色。xdot格式的字符串，指定任意背景。 在渲染期间，首先按照bgcolor属性中的描述填充画布。 然后，如果定义了_background，则在画布上执行字符串中描述的图形操作。
+ dir 设置边的箭头的类型，默认forward(directed)，none(undirected)，也可以设置为both或者back（箭头末端）
+ arrowhead 箭头前端的样式。常见的箭头样式有:[箭头样式](https://graphviz.gitlab.io/_pages/doc/info/attrs.html#k:arrowType)
+ arrowsize 箭头尺寸的倍数
+ arrowtail 箭头末端的样式（只有当dir=back或者both时才有效）
+ bgcolor 绑定在根图上，这个颜色会作为整个画布的背景色。当为群集属性时，它用作群集的    初始背景。如果群集具有填充样式，则群集的fillcolor将覆盖背景色。
   如果该值为colorList，则使用渐变填充。默认情况下，使用线性填充；设置style = radial将导致径向填充。目前，仅使用两种颜色。如果缺少第二种颜色（在冒号之后），则使用默认颜色。
   对于某些输出格式，例如PostScript，除非显式设置了bgcolor，否则不会对根图进行填充。但是，对于位图格式，需要将位初始化为某种格式，因此默认情况下，画布以白色填充。这意味着，如果位图输出包含在其他文档中，则将设置位图边界框中的所有位，从而覆盖页面上已经存在的任何颜色或图形。如果不需要这种效果，并且您只想设置在绘制图形时显式分配的位，请设置bgcolor =“ transparent”。
+ center 如果其值为true, 则绘画结果在输出画布的中央，默认值是false
+ color 用于图的颜色，而不用于文本。对于边而言，其值可以是一个单一的颜色或者是一个颜色列表。对于后者，如果颜色列表没有给出分数，则使用平行线条绘制，并按照给定的顺序使用颜色列表中的每种颜色绘制一条线。（正向箭头，如果有，使用颜色列表中第一个颜色，反向箭头，如果有，使用第二个）。这支持绘制相对边的常见情况，但使用平行样条线而不是单独布线的多边。 如果使用任何分数，则按顺序绘制颜色，每种颜色大致指定为其指定的边缘分数。例如：
    ```
    digraph G {
        a -> b [dir=both color="red:blue"]
        c -> d [dir=none color="green:red;0.25:blue"]
    }
    ```
    则c->d的那个线大约有25%的长度是蓝色。
+ fontcolor 文字颜色
+ decorate 装饰。如果为true，则通过2段多段线将边缘标签附加到边缘，在标签下划线，然后移至最接近样条线的点。（如果不是比较复杂的图，这个属性看不出来太大不同）。
+ fontname 控制字体的，很大程度上取决于输出格式，对于像PostScript或者SVG这样的非位图输出，则取决于展示或者打印时字体的可用性。因此，最好使用常见可得的字体，比如**Times-Roman，Helvetica或者Courier**。此外，字体名称的解析方式还取决于处理字体名称解析的基底层库，如果Graphviz是使用fontconfig库构建的，则将使用后者来搜索字体。有关如何解析名称以及可用字体的信息，请参见命令fc-list，fc-match和其他fontconfig命令。其他系统可能会提供自己的字体包，例如Quartz for OSX。

    如果Graphviz不是使用高级字体库构建的，则fontname将被视为Type 1或True Type字体文件的名称。 如果指定fontname = schlbk，则该工具将在fontpath属性指定的目录之一中查找名为schlbk.ttf或schlbk.pfa或schlbk.pfb的文件。 查找确实支持各种通用字体别名。
+ fontsize 控制字体大小，每英寸72个点，72 points per inch
+ fontpath 字体路径 如果Graphviz不是使用fontconfig库构建的，则libgd用于搜索位图字体的目录列表。 如果未设置fontpath，则检查环境变量DOTFONTPATH。 如果未设置，则检查GDFONTPATH。 如果未设置，libgd将使用其内置的字体路径。 请注意，fontpath是根图的属性。
+ id 为图中的每一个对象提供独一无二的id名称
+ image 给出包含要在节点内显示的图像的文件的名称。图像文件必须采用公认的格式之一，通常为JPEG，PNG，GIF，BMP，SVG或Postscript，并且能够转换为所需的输出格式。
该文件必须包含图像大小信息。对于位图格式，这通常很简单。对于PostScript，文件必须包含以%% BoundingBox开头的行：后跟四个整数，指定图像边框的左下x和y坐标以及右上x和y坐标，坐标以磅为单位。 SVG图像文件必须包含width和height属性，通常作为svg元素的一部分。这些值的格式应为浮点数，后跟可选的单位，例如width =“ 76pt”。公认的单位分别为px，pc，pt，cm和mm，分别表示英寸，像素，皮卡，点，厘米和毫米。默认单位是磅。
    与shapefile属性不同，图像被视为节点内容，而不是整个节点。特别地，图像可以包含在任何形状的节点中，而不仅仅是矩形
+ 配套的有 imagepath（图像路径）imagepos（图像位置） imagescale（图像与节点大小关系控制 自适应 放大 缩小等）
+ label 附加到对象的文本标签。 如果节点的形状是记录的，则标签可以具有描述记录布局的特殊格式。请注意，节点的默认标签为“ \ N”，因此该节点的名称或ID成为其标签。 从技术上讲，节点的名称可以是HTML字符串，但这并不意味着该节点的标签将被解释为类似HTML的标签。 这是因为节点的实际标签是普通字符串，将由存储在节点名称中的原始字节替换。 要获得类似HTML的标签，label属性值本身必须是HTML字符串。**如果一个节点没有label，则显示的文本就是该节点变量的名称，否则显示label中的内容**

## 2.5. 节点形状
https://graphviz.gitlab.io/_pages/doc/info/shapes.html
box 矩形	polygon 多边形	ellipse	oval 椭圆形等 
也可以绘制更复杂的图形嵌套图形的结构。

## 2.6 箭头形状
https://graphviz.gitlab.io/_pages/doc/info/arrows.html

## 2.7 颜色
https://graphviz.gitlab.io/_pages/doc/info/colors.html

# 3. 具体使用实例
主要参考：
[1] [程序员如何更好的表达自己的想法- Graphviz:关系图脚本绘制工具](https://stidio.github.io/2017/07/how_do_programmer_express_yourself_better-graphviz/)
[2] [Graphviz - Graph Visualization Software](https://graphviz.gitlab.io/gallery/)
[3] [Graphviz-example](https://graphviz.readthedocs.io/en/stable/examples.html)








