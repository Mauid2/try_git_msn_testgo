import pandas as pd
import openpyxl


shuju1 = pd.read_excel(r'G:\TPSHOP_data.xlsx')  # 'r'是转义字符，避免路径中的'\'被转译
# shuju1 = pd.read_excel('E:/2022Python/数据源.xlsx')  # 也可以不加'r'，但要变为'/'
# shuju1 = pd.read_excel('./数据源.xlsx')  # 相对路径
print("shuju1:\n",shuju1)
value = shuju1.iat[0, 0]
length=len(shuju1)  # 获取行数
print(value,length)

def test(shuju1):
    for i in range(length):
        for j in range(len(shuju1.columns)):
            def get_value(shuju1.iat[i,j]):
                return shuju1.iat[i,j]
