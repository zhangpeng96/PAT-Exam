# 【7-2】教超冠军卷（20分）

> 作者: 陈越
> 单位: 浙江大学
> 时间限制: 400 ms
> 内存限制: 64 MB
> 代码长度限制: 16 KB

“教育超市”是拼题A系统的一个衍生产品，发布了各种试卷和练习供用户选购。在试卷列表中，系统不仅列出了每份试卷的单价，还显示了当前的购买人次。本题就请你根据这些信息找出教育超市所有试卷中的销量（即购买人次）冠军和销售额冠军。

### 输入格式：

输入首先在第一行中给出一个正整数N（$\leqslant 10^4$），随后N行，每行给出一份卷子的独特ID（由小写字母和数字组成的、长度不超过8位的字符串）、单价（为不超过100的正整数）和购买人次（为不超过$10^6$的非负整数）。

### 输出格式：

在第一行中输出销量冠军的ID及其销量，第二行中输出销售额冠军的ID及其销售额。同行输出间以一个空格分隔。题目保证冠军是唯一的，不存在并列。

### 输入样例：

```
4
zju007 39 10
pku2019 9 332
pat2018 95 79
qdu106 19 38
```

### 输出样例：

```
pku2019 332
pat2018 7505
```
