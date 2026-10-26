#!/usr/bin/env python3
import sys
import pandas as pd
from src.screening.screener import check_my_investment_logic

def get_us_stock_pool():
    """
    自動獲取熱門美股池（透過開源的標普 500 成分股清單）
    """
    try:
        # 直接從維基百科自動爬取最新的 S&P 500 成分股代號（包含 500 隻最大的美股）
        url = "https://wikipedia.org"
        table = pd.read_html(url)
        df = table[0]
        tickers = df['Symbol'].tolist()
        # 修正部分代號格式（例如 BRK.B 改為 BRK-B）
        tickers = [t.replace('.', '-') for t in tickers]
        return tickers
    except Exception as e:
        print(f"自動抓取美股池失敗，使用預設科技股替代: {e}")
        return ["AAPL", "NVDA", "MSFT", "GOOG", "AMZN", "META", "NFLX", "TSLA", "AMD", "INTC"]

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行『全美股 S&P500』投資 Logic 篩選與回測 ---")
    print("==========================================")
    
    # 自動抓取 500 隻全美股核心資產
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
