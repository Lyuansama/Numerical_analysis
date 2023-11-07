# 第一次作业

## 理论分析

计算机的浮点系统在计算加法时，可能出现大数吃小数的情况，因此从大到小的计算方式误差应该大于从小到大的计算方式。

## 问题一

**问题要求**：按照从大到小的顺序进行计算。

**实现方法**：使用 Python 分别进行编程。函数的输入参数为下标 $N$，返回值为计算的结果。

由于 Python 中默认 `float` 类型数据使用双精度浮点数进行存储，因此需要引用 `numpy` 库中的 `float32` 以将数据的精度修改为单精度。

```python
  # from numpy import float32

  def large2small(n):
      result = float32(0) # 避免 result 为双精度浮点数
      for i in range(2, n + 1):
          result += float32(1 / (i ** 2 - 1))
      return result
```

## 问题二

**问题需求**：从小到大的顺序进行计算。

**实现方法**：与问题一类似，采用 Python 进行编程。

函数的输入值为 $N$，返回值为计算结果。

```python
def small2large(n):
    result = float32(0)
    for i in range(n, 1, -1):
        result += float32(1 / (i ** 2 - 1))
    return result
```

## 问题三

**问题需求**：使用问题一和问题二的程序，计算 $S_{10^2}$，$S_{10^4}$，$S_{10^6}$，与精确值进行比较，并指出有效位数。

**实现方法**：

设计了一个用于计算精确值的函数 `precise()`，该函数使用精确值的计算公式直接进行计算，内部数据使用双精度类型以提高计算的准确性。函数的传入参数为 $N$，返回值为精确的计算结果。

```python
def precise(n):
    precise_result = 0.5 * (1.5 - 1 / n - 1 / (n + 1))
    return precise_result
```

为了方便统计有效位数，设计了一个用于统计有效位数的函数 `get_valid_digit()`，该函数的传入参数为精确值和计算结果，返回值为有效位数。

```python
def get_valid_digit(precise_num, result_num):
    n = 0 # 第一个非零数字的权
    m = 0 # 精确数位的权
    e = abs(precise_num - result_num)

    # 如果小于系统最低精度，直接退出
    if e < sys.float_info.epsilon:
        print("误差过小，精确！")
        return -1

    precise_num = abs(precise_num)

    if precise_num > 1:
        while precise_num >= 10:
            n += 1
            precise_num /= 10
    else:
        while precise_num < 1:
            n -= 1
            precise_num *= 10

    m = n
    while e <= 0.5 * 10 ** (m - 1):
        m -= 1

    return n - m + 1
```

使用 for 循环，计算并输出结果

```python
s = [10 ** 2, 10 ** 4, 10 ** 6]
for N in Ns:
    print(f"N = {N}")
    print(f"large2small \t {large2small(N)} \t {get_valid_digit(precise(N), large2small(N))}")
    print(f"small2large \t {small2large(N)} \t {get_valid_digit(precise(N), small2large(N))}")
    print(f"precise \t {precise(N)}")
    print("-----------")
```

**实验结果**：

程序输出的内容如下所示：

```shell
N = 100
large2small      0.7400494813919067      7
small2large      0.7400495409965515      7
precise          0.740049504950495 
-----------
N = 10000
large2small      0.7498521208763123      4
small2large      0.7498999834060669      7
precise          0.7499000049995 
-----------
N = 1000000
large2small      0.7498521208763123      3
small2large      0.7499990463256836      7
precise          0.7499990000005
----------
```

有效位数

| n       | large2small | small2large |
|:------- |:----------- |:----------- |
| 100     | 7           | 7           |
| 10000   | 4           | 7           |
| 1000000 | 3           | 7           |

可以看到，从小到大的计算方式的有效位数要始终高于从大到小的计算方式。

## 结论

由于计算机浮点数的特性，从大到小的计算方式产生的误差要大于从小到大的计算方式。因此，当需要使用迭代的方法累计一串相差较大的数时，应该使用从小到大的计算方式，以减小误差。
