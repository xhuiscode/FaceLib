def bisection_search(f, left, right, epsilon):
    """
    使用二分法来求解函数 f 在区间 [left, right] 内的最小值，要求误差小于 epsilon。
    """
    while (right - left) > epsilon:
        # 计算区间的中点
        mid = (left + right) / 2
        # 计算函数在左右两端点和中点处的值
        f_left = f(left)
        f_right = f(right)
        f_mid = f(mid)
        # 判断最小值在左侧还是右侧
        if f_right - f_mid >= f_left - f_mid:
            right = mid
        else:
            left = mid
    # 返回区间的中点作为最小值的估计值
    return f((left + right) / 2)


def f(x):
    return x**2 - 4 * x + 5
# 求解函数 f 在区间 [0, 4] 内的最小值


result = bisection_search(f, 0, 4, 0.001)

# 输出结果
print("最小值：", result)

