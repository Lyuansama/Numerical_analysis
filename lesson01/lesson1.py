from numpy import float32
import sys

def small2large(n):
    result = float32(0)
    for i in range(n, 1, -1):
        result += float32(1 / (i ** 2 - 1))
    return result


def large2small(n):
    result = float32(0)
    for i in range(2, n + 1):
        result += float32(1 / (i ** 2 - 1))
    return result


def precise(n):
    precise_result = 0.5 * (1.5 - 1 / n - 1 / (n + 1))
    return precise_result

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


Ns = [10 ** 2, 10 ** 4, 10 ** 6]
for N in Ns:
    print(f"N = {N}")
    print(f"large2small \t {large2small(N)} \t {get_valid_digit(precise(N), large2small(N))}")
    print(f"small2large \t {small2large(N)} \t {get_valid_digit(precise(N), small2large(N))}")
    print(f"precise \t {precise(N)} ")
    print("-----------")