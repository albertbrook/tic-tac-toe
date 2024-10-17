﻿# 井字棋
极大极小值算法（minimax）和alpha-beta剪枝算法实现对战
## 部分过程
![](images/demo1.jpg)
## 演示
X or O?o<br>
012<br>
345<br>
678<br>
--------------------<br>
X = 1<br>
0X2<br>
345<br>
678<br>
--------------------<br>
O = 3<br>
0X2<br>
O45<br>
678<br>
--------------------<br>
X = 4<br>
0X2<br>
OX5<br>
678<br>
--------------------<br>
O = 7<br>
0X2<br>
OX5<br>
6O8<br>
--------------------<br>
X = 2<br>
0XX<br>
OX5<br>
6O8<br>
--------------------<br>
O = 0<br>
OXX<br>
OX5<br>
6O8<br>
--------------------<br>
X = 6<br>
OXX<br>
OX5<br>
XO8<br>
--------------------<br>
X win