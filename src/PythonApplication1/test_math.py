import math

# 激活函数
def activate_function(distance):
    return 0.5 + math.atan(distance) / math.pi


def calculate_score(weight, distance):

    # 计算激活函数值
    activated_value = 0.5 + math.atan(distance) / math.pi

    # 计算最终得分
    score = weight * activated_value
    return score

# 计算得分1
score1 = calculate_score(0.8, 0.9999999)
score2 = calculate_score(0.3, 7.7350235)
score = score1 + score2
print("最终得分1:", score)

# 计算得分2
score1 = calculate_score(0.8, 0.53189427)
score2 = calculate_score(0.3, 6.3179684)
score = score1 + score2
print("最终得分2:", score)

# 计算得分3
score1 = calculate_score(0.8, 0.45735544)
score2 = calculate_score(0.3, 5.3983445)
score = score1 + score2
print("最终得分3:", score)

# 计算得分4
score1 = calculate_score(0.8, 0.38964748)
score2 = calculate_score(0.3, 6.272743)
score = score1 + score2
print("最终得分4:", score)