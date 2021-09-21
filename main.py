# 参考 : https://qiita.com/nebula121/items/980bf87f215ea5c12083
import math
import numpy as np
import matplotlib.pyplot as plt

# 問題1の答え
randomArrayX = np.random.uniform(0.0, 1.0, 10**4)
randomArrayY = np.random.uniform(0.0, 1.0, 10**4)

insideCounter = 0

for x, y in zip(randomArrayX[:], randomArrayY[:]):
    if math.hypot(x, y) <= 1:
        insideCounter += 1
        plt.plot(x, y, 'x')

# 問題2の答え : insideCounter
print(insideCounter, randomArrayX.shape[0])

# 四分円の面積 / 第一象限四角形の面積 = [1/4 * (1 * 1) * pi(四分円)] / [1 * 1] = 1/4 * pi
# -> pi = 4 * 四分円の面積 / 第一象限四角形の面積
montePi = 4 * (insideCounter / randomArrayX.shape[0])
# 問題3の答え
print(montePi)

# 問題2でプロットして図に起こす場合にコメントアウトを外す。
# plt.show()
