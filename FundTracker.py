import os
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from statsmodels.tsa.holtwinters import ExponentialSmoothing

refresh_token = os.environ.get("10JQKA_REFRESH_TOKEN", "")
fund_code = '512480.SH'
start_date = (datetime.today() - timedelta(days=365 * 1)).strftime('%Y-%m-%d')
end_date = datetime.today().strftime('%Y-%m-%d')


def get_access_token(refresh_token):
    url = 'https://ft.10jqka.com.cn/api/v1/get_access_token'
    headers = {
        'Content-Type': 'application/json',
        'refresh_token': refresh_token
    }
    response = requests.post(url=url, headers=headers)
    return json.loads(response.content)['data']['access_token']


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


def forecast_valuation(df, periods=180):
    model = ExponentialSmoothing(df['finalValuation'], trend='add', seasonal='add', seasonal_periods=20)
    fit = model.fit()
    forecast_index = pd.date_range(start=df.index[-1] + timedelta(days=1), periods=periods, freq='D')
    forecast = fit.forecast(periods)
    forecast = pd.Series(forecast, index=forecast_index)
    return forecast


def main():
    access_token = get_access_token(refresh_token)
    df = get_fund_valuation(access_token, fund_code, start_date, end_date)

    print("历史估值样本（头部）:")
    print(df.head())

    forecast = forecast_valuation(df)

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
