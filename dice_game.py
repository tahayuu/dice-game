# dice_game.py
import random

# 名前を入力
name = input("What is your name?\n> ")
print(f"Hello, {name}!")

# サイコロを振る
print("Rolling the dice...")
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

# サイコロの出目を表示
print(f"Die 1: {die1}")
print(f"Die 2: {die2}")
print(f"Total value: {total}")

# 勝ち負けの判定
if total > 7:
    print(f"{name} won!")
else:
    print(f"{name} lost!")
