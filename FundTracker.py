import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# === 设置 ===
refresh_token = "eyJzaWduX3RpbWUiOiIyMDI1LTA3LTIxIDExOjMzOjQyIn0=.eyJ1aWQiOiIxMTQwODMyNjEiLCJ1c2VyIjp7ImFjY291bnQiOiJ6cXNiMDYwIiwiYXV0aFVzZXJJbmZvIjp7IkVleGNlbFBheWVycyI6IjE3MzU5NTUyMzgwMDAifSwiY29kZUNTSSI6W10sImNvZGVaekF1dGgiOltdLCJoYXNBSVByZWRpY3QiOmZhbHNlLCJoYXNBSVRhbGsiOmZhbHNlLCJoYXNDSUNDIjpmYWxzZSwiaGFzQ1NJIjpmYWxzZSwiaGFzRXZlbnREcml2ZSI6ZmFsc2UsImhhc0ZUU0UiOmZhbHNlLCJoYXNGYXN0IjpmYWxzZSwiaGFzRnVuZFZhbHVhdGlvbiI6ZmFsc2UsImhhc0hLIjp0cnVlLCJoYXNMTUUiOmZhbHNlLCJoYXNMZXZlbDIiOmZhbHNlLCJoYXNSZWFsQ01FIjpmYWxzZSwiaGFzVHJhbnNmZXIiOmZhbHNlLCJoYXNVUyI6ZmFsc2UsImhhc1VTQUluZGV4IjpmYWxzZSwiaGFzVVNERUJUIjpmYWxzZSwibWFya2V0QXV0aCI6eyJEQ0UiOmZhbHNlfSwibWF4T25MaW5lIjoxLCJub0Rpc2siOmZhbHNlLCJwcm9kdWN0VHlwZSI6IlNVUEVSQ09NTUFORFBST0RVQ1QiLCJyZWZyZXNoVG9rZW5FeHBpcmVkVGltZSI6IjIwMjYtMDEtMDQgMDk6NDc6MTgiLCJzZXNzc2lvbiI6IjNmMGRjNDFlYmIwNTQ5MDczOWMxMDFhMzRjMmU1OTJmIiwic2lkSW5mbyI6ezY0OiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDE6IjEwMSIsMjoiMSIsNjc6IjEwMTExMTExMTExMTExMTExMTExMTExMSIsMzoiMSIsNjk6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDU6IjEiLDY6IjEiLDcxOiIxMTExMTExMTExMTExMTExMTExMTExMDAiLDc6IjExMTExMTExMTExIiw4OiIwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSIsMTM4OiIxMTExMTExMTExMTExMTExMTExMTExMTExIiwxMzk6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDE0MDoiMTExMTExMTExMTExMTExMTExMTExMTExMSIsMTQxOiIxMTExMTExMTExMTExMTExMTExMTExMTExIiwxNDI6IjExMTExMTExMTExMTExMTExMTExMTExMTEiLDE0MzoiMTEiLDgwOiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDgxOiIxMTExMTExMTExMTExMTExMTExMTExMTEiLDgyOiIxMTExMTExMTExMTExMTExMTExMTAxMTAiLDgzOiIxMTExMTExMTExMTExMTExMTEwMDAwMDAiLDg1OiIwMTExMTExMTExMTExMTExMTExMTExMTEiLDg3OiIxMTExMTExMTAwMTExMTEwMTExMTExMTEiLDg5OiIxMTExMTExMTAxMTAxMDAwMDAwMDExMTEiLDkwOiIxMTExMTAxMTExMTExMTExMTAwMDExMTExMCIsOTM6IjExMTExMTExMTExMTExMTExMDAwMDExMTEiLDk0OiIxMTExMTExMTExMTExMTExMTExMTExMTExIiw5NjoiMTExMTExMTExMTExMTExMTExMTExMTExMSIsOTk6IjEwMCIsMTAwOiIxMTExMDExMTExMTExMTExMTEwIiwxMDI6IjEiLDQ0OiIxMSIsMTA5OiIxIiw1MzoiMTExMTExMTExMTExMTExMTExMTExMTExIiw1NDoiMTEwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLDU3OiIwMDAwMDAwMDAwMDAwMDAwMDAwMDEwMDAwMDAwMCIsNjI6IjExMTExMTExMTExMTExMTExMTExMTExMSIsNjM6IjExMTExMTExMTExMTExMTExMTExMTExMSJ9LCJ0cmFuc0F1dGgiOmZhbHNlLCJ1aWQiOiIxMTQwODMyNjEiLCJ1c2VyVHlwZSI6IkZSRUVJQUwiLCJ3aWZpbmRMaW1pdE1hcCI6e319fQ==.8DAA52AF252B8FE7ABBA8E5E8FE0B998AF38582C32D169AFA3C6F5DE6C3817A9"
  # 替换为你的 refresh_token
fund_code = '512480.SH'  # ETF 代码，注意 SH 表示上交所
start_date = (datetime.today() - timedelta(days=365 * 1)).strftime('%Y-%m-%d')  # 获取近一年数据
end_date = datetime.today().strftime('%Y-%m-%d')

# === Step 1: 获取 access_token ===
def get_access_token(refresh_token):
    url = 'https://ft.10jqka.com.cn/api/v1/get_access_token'
    headers = {
        'Content-Type': 'application/json',
        'refresh_token': refresh_token
    }
    response = requests.post(url=url, headers=headers)
    return json.loads(response.content)['data']['access_token']

# === Step 2: 获取基金估值数据（日频）===
def get_fund_valuation(access_token, code, start_date, end_date):
    url = 'https://ft.10jqka.com.cn/api/v1/final_fund_valuation'
    headers = {'Content-Type': 'application/json', 'access_token': access_token}
    payload = {
        "codes": code,
        "functionpara": {
            "beginDate": start_date,
            "endDate": end_date
        },
        "outputpara": "date:Y,finalValuation:Y,netAssetValue:Y,deviation:Y"
    }
    res = requests.post(url, headers=headers, json=payload)
    raw = json.loads(res.content)
    print("API原始返回：", json.dumps(raw, indent=2, ensure_ascii=False))

    records = raw['tables'][0]['table']['records']
    df = pd.DataFrame(records)
    df['date'] = pd.to_datetime(df['date'])
    df.set_index('date', inplace=True)
    df = df.sort_index()
    return df

# === Step 3: 使用 Holt-Winters 模型进行估值预测 ===
def forecast_valuation(df, periods=180):
    model = ExponentialSmoothing(df['finalValuation'], trend='add', seasonal='add', seasonal_periods=20)
    fit = model.fit()
    forecast_index = pd.date_range(start=df.index[-1] + timedelta(days=1), periods=periods, freq='D')
    forecast = fit.forecast(periods)
    forecast = pd.Series(forecast, index=forecast_index)
    return forecast

# === Step 4: 主程序逻辑 ===
def main():
    access_token = get_access_token(refresh_token)
    df = get_fund_valuation(access_token, fund_code, start_date, end_date)

    print("历史估值样本（头部）:")
    print(df.head())

    forecast = forecast_valuation(df)

    # 可视化
    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df['finalValuation'], label='历史估值')
    plt.plot(forecast.index, forecast, label='未来半年估值预测', linestyle='--')
    plt.title(f"{fund_code} 估值预测（未来半年）")
    plt.xlabel("日期")
    plt.ylabel("估值")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
