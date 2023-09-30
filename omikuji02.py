import random

# 中吉を追加
omikuji = ["大吉", "吉", "凶" , "中吉"] 

idx = random.randint(0,len(omikuji)-1)

print(f"今日の運勢は... {omikuji[idx]}")