import requests
import pandas as pd
import matplotlib.pyplot as plt

access_token = "eyJzaWduX3RpbWUiOiIyMDI1LTA3LTIxIDExOjMzOjQyIn0=.eyJ1aWQiOiIxMTQwODMyNjEiLCJ1c2VyIjp7ImFjY291bnQiOiJ6cXNiMDYwIiwiYXV0aFVzZXJJbmZvIjp7IkVleGNlbFBheWVycyI6IjE3MzU5NTUyMzgwMDAifSwiY29kZUNTSSI6W10sImNvZGVaekF1dGgiOltdLCJoYXNBSVByZWRpY3QiOmZhbHNlLCJoYXNBSVRhbGsiOmZhbHNlLCJoYXNDSUNDIjpmYWxzZSwiaGFzQ1NJIjpmYWxzZSwiaGFzRXZlbnREcml2ZSI6ZmFsc2UsImhhc0ZUU0UiOmZhbHNlLCJoYXNGYXN0IjpmYWxzZSwiaGFzRnVuZFZhbHVhdGlvbiI6ZmFsc2UsImhhc0hLIjp0cnVlLCJoYXNMTUUiOmZhbHNlLCJoYXNMZXZlbDIiOmZhbHNlLCJoYXNSZWFsQ01FIjpmYWxzZSwiaGFzVHJhbnNmZXIiOmZhbHNlLCJoYXNVUyI6ZmFsc2UsImhhc1VTQUluZGV4IjpmYWxzZSwiaGFzVVNERUJUIjpmYWxzZSwibWFya2V0QXV0aCI6eyJEQ0UiOmZhbHNlfSwibWF4T25MaW5lIjoxLCJub0Rpc2siOmZhbHNlLCJwcm9kdWN0VHlwZSI6IlNVUEVSQ09NTUFORFBST0RVQ1QiLCJyZWZyZXNoVG9rZW5FeHBpcmVkVGltZSI6IjIwMjYtMDEtMDQgMDk6NDc6MTgiLCJzZXNzc2lvbiI6IjNmMGRjNDFlYmIwNTQ5MDczOWMxMDFhMzRjMmU1OTJmIiwic2lkSW5mbyI6ezY0OiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDE6IjEwMSIsMjoiMSIsNjc6IjEwMTExMTExMTExMTExMTExMTExMTExMSIsMzoiMSIsNjk6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDU6IjEiLDY6IjEiLDcxOiIxMTExMTExMTExMTExMTExMTExMTExMDAiLDc6IjExMTExMTExMTExIiw4OiIwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSIsMTM4OiIxMTExMTExMTExMTExMTExMTExMTExMTExIiwxMzk6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDE0MDoiMTExMTExMTExMTExMTExMTExMTExMTExMSIsMTQxOiIxMTExMTExMTExMTExMTExMTExMTExMTExIiwxNDI6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDE0MzoiMTEiLDgwOiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDgxOiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDgyOiIxMTExMTExMTExMTExMTExMTExMTAxMTAiLDgzOiIxMTExMTExMTExMTExMTExMTEwMDAwMDAiLDg1OiIwMTExMTExMTExMTExMTExMTExMTExMTEiLDg3OiIxMTExMTExMTAwMTExMTEwMTExMTExMTEiLDg5OiIxMTExMTExMTAxMTAxMDAwMDAwMDExMTEiLDkwOiIxMTExMTAxMTExMTExMTExMTAwMDExMTExMCIsOTM6IjExMTExMTExMTExMTExMTExMDAwMDExMTEiLDk0OiIxMTExMTExMTExMTExMTExMTExMTExMTExIiw5NjoiMTExMTExMTExMTExMTExMTExMTExMTExMSIsOTk6IjEwMCIsMTAwOiIxMTExMDExMTExMTExMTExMTEwIiwxMDI6IjEiLDQ0OiIxMSIsMTA5OiIxIiw1MzoiMTExMTExMTExMTExMTExMTExMTExMTExIiw1NDoiMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLDU3OiIwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMCIsNjI6IjExMTExMTExMTExMTExMTExMTExMTExMSIsNjM6IjExMTExMTExMTExMTExMTExMTExMTExMSJ9LCJ0cmFuc0F1dGgiOmZhbHNlLCJ1aWQiOiIxMTQwODMyNjEiLCJ1c2VyVHlwZSI6IkZSRUVJQUwiLCJ3aWZpbmRMaW1pdE1hcCI6e319fQ==.8DAA52AF252B8FE7ABBA8E5E8FE0B998AF38582C32D169AFA3C6F5DE6C3817A9"

url = "https://ft.10jqka.com.cn/api/v1/capital_flow"
headers = {
    "Content-Type": "application/json",
    "access_token": access_token
}
payload = {
    "codes": "600183.SH",
    "startdate": "2024-01-01",
    "enddate": "2025-07-21",
    "frequency": "D"  # 日线
}

res = requests.post(url, headers=headers, json=payload)
data = res.json()

if 'tables' in data and data['tables']:
    table = data['tables'][0]
    df = pd.DataFrame(table['table'])
    df['date'] = pd.to_datetime(table['time'])
    df.set_index('date', inplace=True)
    print("字段：", df.columns.tolist())

    plt.figure(figsize=(14, 6))
    plt.plot(df.index, df['main_net_inflow'], label='主力净流入', color='red')
    plt.plot(df.index, df['retail_net_inflow'], label='散户净流入', color='green')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8)
    plt.title('生益科技 主力与散户资金流向图')
    plt.xlabel('日期')
    plt.ylabel('资金净流入（元）')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("❌ 数据请求失败或无数据返回"