your_input = input("数字を入れて＞")

try:
    number = int(your_input)
    print(10/number)
except ValueError:
    print("文字が入りました")
except ZeroDivisionError:
    print("0は禁止")
except:
    print("エラーを確認してください")
