#!/usr/bin/env python3
import sys
import pandas as pd
from src.screening.screener import check_my_investment_logic

def get_us_stock_pool():
    """
    從 GitHub 穩定的靜態開源資源獲取 S&P 500 成分股名單，100% 防 403 封鎖
    """
    try:
        # 使用開源社區長期維護的靜態 S&P 500 CSV 數據
        url = "https://githubusercontent.com"
        df = pd.read_csv(url)
        tickers = df['Symbol'].tolist()
        # 轉換部分特殊標的符號（如 BF.B 改為 BF-B）
        tickers = [t.replace('.', '-') for t in tickers]
        return tickers
    except Exception as e:
        print(f"靜態加載美股池失敗，使用預設核心美股替代: {e}")
        return ["AAPL", "NVDA", "MSFT", "GOOG", "AMZN", "META", "NFLX", "TSLA", "AMD", "QCOM", "AVGO", "COST"]

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行『全美股 S%P500 穩定版』投資 Logic 篩選 ---")
    print("==========================================")
    
    # 穩定獲取 500 隻全美股核心資產
    TICKER_POOL = get_us_stock_pool()
    print(f"成功加載美股掃描池，共計 {len(TICKER_POOL)} 隻股票。")
    
    triggered_count = 0
    for ticker in TICKER_POOL:
        res = check_my_investment_logic(ticker)
        if res:
            print(f"🔥 策略觸發：{res['Ticker']} ({res['Name']})")
            print(f"📈 5年歷史信號出現次數: {res['5Y_Signals']} 次")
            print(f"🎯 60日勝率 (>+10%): {res['60D_WinRate']}")
            print(f"💰 半凱利建議倉位: {res['Kelly_Position']}")
            print("------------------------------------------")
            triggered_count += 1
            
    print(f"--- 篩選結束，今日共有 {triggered_count} 隻美股觸發入場訊號 ---")

