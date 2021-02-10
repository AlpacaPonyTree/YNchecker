from YNchecker import YNchecker

answer = YNchecker("本当によろしいですか？(Y/N)")
if answer:
    print("はい")
else:
    print("いいえ")
