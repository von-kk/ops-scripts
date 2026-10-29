"""
对比实验：把自测题里答错的 6 个点，跑出来给你看。

运行：python3 对比实验.py
每段前面有【实验 N】，对应复习手册第六节的题号。
"""

import subprocess
import sys

LINE = "=" * 60


# ============================================================
# 实验 3：缩进 4 格 vs 顶格，Python 到底理解成什么不同
# ============================================================
print(LINE)
print("【实验 3】缩进 4 格 vs 顶格")
print(LINE)

print("--- A：print 缩进了 → 在循环里，执行 3 次 ---")
for i in [1, 2, 3]:
    print("    这是循环内的一句，i =", i)

print()
print("--- B：print 顶格 → 在循环外，只执行 1 次 ---")
for i in [1, 2, 3]:
    print("    （循环体只做了一件事）", i)
print("    这句在循环外，所以只执行 1 次，此时 i =", i)

print()
print(">>> 结论：缩进 = 归属。缩进的属于上面的循环/判断，顶格的不属于。")
print()


# ============================================================
# 实验 4：\n 到底是一个字符还是两个？
# ============================================================
print(LINE)
print("【实验 4】\\n 是一个字符")
print(LINE)

s = "abc\n"
print("s = 'abc\\n'")
print("  len(s) =", len(s), "  ← 是 4 不是 5，说明 \\n 只占 1 个字符")
print("  repr(s) =", repr(s), "  ← repr 让它显形")
print("  直接 print(s) 长这样：")
print(s + "下一行（我本来就在下面）")

print()
print("  用 strip() 之后：")
s2 = s.strip()
print("  len(s2) =", len(s2))
print("  repr(s2) =", repr(s2))

print()
print(">>> 结论：\\n 是 1 个字符（换行符）。repr() 让它显形，strip() 把它剥掉。")
print()


# ============================================================
# 实验 6：= 和 == 的区别
# ============================================================
print(LINE)
print("【实验 6】= 是赋值，== 是比较")
print(LINE)

up = 1
print("up =", up)
print("  up == 1  的结果是：", up == 1, "  ← 这是一个提问，答案是 True/False")
print("  up == 0  的结果是：", up == 0)
print()
up = 5
print("  执行 up = 5 之后，up 变成：", up, "  ← 这是赋值，把 5 放进 up")

print()
print(">>> 结论：== 问「等于吗」，回答 True/False；= 说「放进去」。")
print(">>> 如果你写成  if up = 1:  Python 会直接报 SyntaxError，不让你在 if 里赋值。")
print()


# ============================================================
# 实验 7：不加 capture_output 会怎样
# ============================================================
print(LINE)
print("【实验 7】capture_output=True：输出到底去哪了")
print(LINE)

print("--- 不加 capture_output：下面这行 ping 的输出会直接冲到屏幕上 ---")
sys.stdout.flush()
subprocess.run(["ping", "-c", "1", "-W", "1000", "127.0.0.1"])
print("--- 上面那段 PING 输出，不是我 print 的，是 ping 自己打的 ---")

print()
sys.stdout.flush()
r = subprocess.run(["ping", "-c", "1", "-W", "1000", "127.0.0.1"])
print("加了但没捕获时，result.stdout 是什么：", r.stdout)
print("  ← 是 None，因为输出跑到屏幕上去了，程序里拿不到")

print()
print(">>> 结论：不加 capture_output，输出跑到屏幕，程序抓不到；")
print(">>>       加了之后，输出存进 result.stdout，程序才能处理它（判断、写文件、发邮件）。")
print()


# ============================================================
# 实验 8：text=True 的作用
# ============================================================
print(LINE)
print("【实验 8】text=True：字节串 vs 字符串")
print(LINE)

r1 = subprocess.run(
    ["ping", "-c", "1", "-W", "1000", "127.0.0.1"],
    capture_output=True
)
print("--- 不加 text=True ---")
print("  类型：", type(r1.stdout))
print("  内容前 50 字节：", r1.stdout[:50])
print("  ← 前面有个 b'，这是 bytes（字节串），不是普通文字")

print()
r2 = subprocess.run(
    ["ping", "-c", "1", "-W", "1000", "127.0.0.1"],
    capture_output=True,
    text=True
)
print("--- 加了 text=True ---")
print("  类型：", type(r2.stdout))
print("  内容前 50 字符：", repr(r2.stdout[:50]))
print("  ← 没有 b' 了，是可以直接做文字处理（查找、切分、strip）的字符串")

print()
print(">>> 结论：text=True 把字节串解码成字符串。不加的话，.strip() 之类全用不了。")
print()


# ============================================================
# 实验 10：print(up + 1) vs up += 1
# ============================================================
print(LINE)
print("【实验 10】print(up + 1) 和 up += 1 的区别")
print(LINE)

print("--- A：只打印 up + 1（演示你昨天写错的那种） ---")
up = 0
for i in [1, 2, 3]:
    print("    打印 up + 1 =", up + 1, "  但 up 本身还是", up)
print("  循环结束后 up =", up, "  ← 从头到尾都是 0")

print()
print("--- B：用 up += 1 ---")
up = 0
for i in [1, 2, 3]:
    up += 1
    print("    执行 up += 1 之后，up =", up)
print("  循环结束后 up =", up, "  ← 真的加上了")

print()
print(">>> 结论：up + 1 只是算了一下就扔了；up += 1 会把结果存回 up。")
print()


print(LINE)
print("全部实验结束。哪一段还是没看懂，就带着它的编号来问。")
print(LINE)
