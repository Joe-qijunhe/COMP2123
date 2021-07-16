Problem 5

get stuck vertex 是出度为0，入度为n - 1的点。在matrix中，如果存在get stuck vertex i，i 这一行必须全是0，且i 这一列必须全是1（除了 (i, i) 这个点）。算法是：

从左上角开始

-   如果在对角线，就往右边走
-   如果碰到0，就往右边走。如果碰到1，就往下走。

这是因为如果碰到1了，说明这行肯定不是get stuck，检查下一行。如果遇到0，就继续往右检查。

最后检查出来的那行和列来判断get stuck vertex存不存在。