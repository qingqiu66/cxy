#pylint:disable=E0602
from datetime import datetime
#密码登录程序
user=input('请输入用户名：')
password=input('请输入密码：')
if user == 'admin' and password == 'admin':
	print('登录成功')
	print('你好,',user,'欢迎登录!')
else:
	print('登录失败(密码或用户名错误)')
	quit()
	
#功能菜单
def show_menu():
    print("\n===== 功能菜单 =====")
    print("1. 查看当前时间")
    print("2. 计算两个数的和")
    print('3. 计算两个数的差')
    print('4. 计算两个数的积')
    print('5. 计算两个数的商')
    print("8. 退出程序")
    print("================")

def get_current_time():
    #获取当前时间

    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def add_two_numbers():
    #计算两个数的和
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        print(f"{num1} + {num2} = {num1 + num2}")
    except ValueError:
        print("输入无效，请输入数字！")
def reduce_two_numbers():
    #计算两个数的差
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        print(f"{num1} - {num2} = {num1 - num2}")
    except ValueError:
        print("输入无效，请输入数字！")
def x_two_numbers():
    #计算两个数的积
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        print(f"{num1} * {num2} = {num1 * num2}")
    except ValueError:
        print("输入无效，请输入数字！")
def except_two_numbers():
    #计算两个数的商
    try:
        num1 = float(input("请输入第一个数: "))
        num2 = float(input("请输入第二个数: "))
        print(f"{num1} / {num2} = {num1 / num2}")
    except ValueError:
        print("输入无效，请输入数字！")

def main():
    #主程序
    while True:
        show_menu()  # 显示菜单
        choice = input("请输入您的选择: ")  # 获取输入内容

        if choice == "1":
            get_current_time()  # 查看当前时间
        elif choice == "2":
            add_two_numbers()  # 计算两个数的和
        elif choice == "3":
            reduce_two_numbers()  # 计算两个数的差
        elif choice == "4":
            x_two_numbers()  # 计算两个数的积
        elif choice == "5":
            except_two_numbers()  # 计算两个数的商
        elif choice == "6":
            print("退出程序，再见！")
            break  # 退出循环
        else:
            print("无效的选择，请输入正确的选项")

if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    sk-b3c112383b4242658340594b9c2999a1