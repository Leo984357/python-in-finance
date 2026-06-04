import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

access_token = os.environ.get("10JQKA_ACCESS_TOKEN", "")

url = "https://ft.10jqka.com.cn/api/v1/capital_flow"
headers = {
    "Content-Type": "application/json",
    "access_token": access_token
}
payload = {
    "codes": "600183.SH",
    "startdate": "2024-01-01",
    "enddate": "2025-07-21",
    "frequency": "D"
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
    print("❌ 数据请求失败或无数据返回")
