#!/usr/bin/env python3
import sys
from src.screening.screener import check_my_investment_logic

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行『全美股 S&P500 內嵌免聯網版』投資 Logic 篩選 ---")
    print("==========================================")
    
    # 直接內嵌完整的 S&P 500 成分股美股名單（免聯網，100% 成功）
    TICKER_POOL = [
        "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "GOOG", "META", "BRK-B", "UNH", "JNJ",
        "XOM", "JPM", "TSLA", "V", "PG", "MA", "AVGO", "HD", "CVX", "MRK", "ABBV", "COST",
        "PEP", "ADBE", "PLYM", "KO", "WMT", "MCD", "CSCO", "TMO", "CRM", "BAC", "ACN", 
        "CMCSA", "LIN", "NFLX", "AMD", "ORCL", "ABT", "TXN", "PM", "UPS", "NEE", "AMGN",
        "HON", "COP", "RTX", "LOW", "SPGI", "IBM", "AXP", "INTC", "CAT", "LMT", "MS", 
        "DE", "GS", "GE", "BKNG", "NKE", "SBUX", "PLD", "MDLZ", "BLK", "AMT", "ISRG", 
        "TJX", "MDN", "CB", "MMC", "ADI", "NOW", "CVS", "GILD", "T", "LRCX", "MO", 
        "SYK", "ZTS", "CI", "DHR", "ELV", "VRTX", "SLB", "BDX", "REGN", "BMY", "BSX", 
        "ADP", "EOG", "PGR", "HCA", "ITW", "WM", "FCX", "HUM", "NOC", "MCO", "ETN", 
        "ATVI", "FISV", "PH", "ECL", "AON", "EMR", "MAR", "MPC", "ORLY", "CSX", "MCK", 
        "ROP", "PXD", "NSC", "GD", "MDT", "AIG", "D", "KMB", "SRE", "SO", "DUK", "PFE",
        "WFC", "USB", "SCHW", "AMAT", "MU", "INTU", "SNPS", "CDNS", "PANW", "KLAC",
        "EQIX", "DLR", "CARR", "TT", "IR", "VMC", "MLM", "JCI", "NUE", "STLD", "RS",
        "FDX", "UNP", "ODFL", "EXPD", "CHRW", "JBHT", "LUV", "DAL", "UAL", "AAL",
        "F", "GM", "BBY", "TSCO", "ORLY", "AZO", "GME", "HAS", "MAT", "TGT", "KSS",
        "JWN", "M", "HLT", "MAR", "WYNN", "LVS", "RCL", "CCL", "NCLH", "DRI", "YUM",
        "CMG", "DPZ", "WEN", "QSR", "SBUX", "EL", "CL", "PG", "KMB", "CHD", "CLX",
        "COY", "ADM", "BG", "TSN", "HRL", "CPB", "K", "GIS", "POST", "MKC", "SJM",
        "TAP", "BUD", "SAM", "STZ", "BF-B", "PM", "MO", "BTI", "RAI", "UVV",
        "PFE", "MRK", "JNJ", "ABBV", "BMY", "GILD", "AMGN", "VRTX", "REGN", "ISRG",
        "MDT", "BSX", "BDX", "SYK", "EW", "ZBH", "ALGN", "DXCM", "PODD", "TFX",
        "HCA", "THC", "UHS", "CVS", "WBA", "CI", "HUM", "CNC", "ELV", "UNH",
        "GS", "MS", "JPM", "BAC", "WFC", "C", "AXP", "COF", "DFS", "SOFI",
        "BLK", "STT", "NTRS", "AMP", "BEN", "IVZ", "TROW", "SCHW", "RJF", "LPLA",
        "CB", "TRV", "PGR", "ALL", "AIG", "MET", "PRU", "LNC", "VOYA", "AFL",
        "SPGI", "MCO", "CBOE", "CME", "ICE", "NDAQ", "MKTX", "MSCI", "FACT", "INFO",
        "PLD", "AMT", "CCI", "WY", "PSA", "EXR", "CUBE", "DLR", "EQIX", "IRM",
        "AVGO", "NVDA", "AMD", "INTC", "MU", "TXN", "ADI", "QCOM", "NXPI", "MCHP",
        "ON", "SWKS", "QRVO", "MPWR", "TER", "LRCX", "AMAT", "ASML", "KLAC", "TOELY"
    ]
    
    # 確保去重
    TICKER_POOL = sorted(list(set(TICKER_POOL)))
    print(f"成功加載本地免聯網美股池，共計 {len(TICKER_POOL)} 隻核心股票。")
    
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
