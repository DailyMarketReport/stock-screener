 #!/usr/bin/env python3
import sys
from src.screening.screener import check_my_investment_logic

# 純美股監控名單（已移除所有港股，你可以自行增減如 "TSLA", "AMD" 等）
TICKER_POOL = ["AAPL", "NVDA", "MSFT", "GOOG", "AMZN", "META", "NFLX"]

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行純美股投資 Logic 篩選與回測 ---")
    print("==========================================")
    
    triggered_count = 0
    for ticker in TICKER_POOL:
        print(f"正在分析並回測美股: {ticker} ...")
        res = check_my_investment_logic(ticker)
        if res:
            print(f"🔥 策略觸發：{res['Ticker']} ({res['Name']})")
            print(f"📈 5年歷史信號出現次數: {res['5Y_Signals']} 次")
            print(f"🎯 60日勝率 (>+10%): {res['60D_WinRate']}")
            print(f"💰 半凱利建議倉位: {res['Kelly_Position']}")
            print("------------------------------------------")
            triggered_count += 1
            
    print(f"--- 篩選結束，今日共有 {triggered_count} 隻美股觸發入場訊號 ---")

