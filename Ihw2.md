###### 图灵为什么要证明停机问题, 其证明方法和数学原理是什么
停机问题在图灵之前当然不叫停机问题，作为引起第三次数学危机的悖论之一，这个问题曾以“罗素悖论”的形式引发数学界的动荡。

人们认为这个悖论的证明，可以解决面临的矛盾。

然而，“计算机科学之父”，图灵提出了停机问题的证明，这表明悖论就是悖论，的确任何一个形式系统都是不完备的！图灵机（理论上），其实本就是为图灵证明停机问题而生。

**计算机语言化的图灵证明表示如下**
>证明: 反证法
>
>(1). 假定存在这样一个算法 f
>
>boolean f(program, input)

>   if ( program halt on input) return true

>    else return false

>(2). 构造 程序 g
>
>boolean g(program)

>    if f(program, program) == true

>        loop forever

>        return false

>    else 

>        return true

>(3). 调用 g(g) 结果出现悖论
