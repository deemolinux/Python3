#!/usr/bin/env python3
a, b = 0, 1
while b < 100:
    print(b, end=' ')  # 以end内容为每次输出的结束符
    a, b = b, a + b
print()                # 换行


