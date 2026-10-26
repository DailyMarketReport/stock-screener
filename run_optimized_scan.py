#!/usr/bin/env python3
import sys
from src.screening.screener import check_my_investment_logic

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行『全美股 480+ 隻擴大池 + RSI 45放寬版』篩選 ---")
    print("==========================================")
    
    # 方案 A 核心：擴展至去重後 480+ 隻核心美國股票池
    TICKER_POOL = [
        "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "GOOG", "META", "BRK-B", "UNH", "JNJ",
        "XOM", "JPM", "TSLA", "V", "PG", "MA", "AVGO", "HD", "CVX", "MRK", "ABBV", "COST",
        "PEP", "ADBE", "KO", "WMT", "MCD", "CSCO", "TMO", "CRM", "BAC", "ACN", "CMCSA",
        "LIN", "NFLX", "AMD", "ORCL", "ABT", "TXN", "PM", "UPS", "NEE", "AMGN", "HON",
        "COP", "RTX", "LOW", "SPGI", "IBM", "AXP", "INTC", "CAT", "LMT", "MS", "DE",
        "GS", "GE", "BKNG", "NKE", "SBUX", "PLD", "MDLZ", "BLK", "AMT", "ISRG", "TJX",
        "CB", "MMC", "ADI", "NOW", "CVS", "GILD", "T", "LRCX", "MO", "SYK", "ZTS",
        "CI", "DHR", "ELV", "VRTX", "SLB", "BDX", "REGN", "BMY", "BSX", "ADP", "EOG",
        "PGR", "HCA", "ITW", "WM", "FCX", "HUM", "NOC", "MCO", "ETN", "PH", "ECL",
        "AON", "EMR", "MAR", "MPC", "ORLY", "CSX", "MCK", "ROP", "NSC", "GD", "MDT",
        "AIG", "D", "KMB", "SRE", "SO", "DUK", "PFE", "WFC", "USB", "SCHW", "AMAT",
        "MU", "INTU", "SNPS", "CDNS", "PANW", "KLAC", "EQIX", "DLR", "CARR", "TT",
        "IR", "VMC", "MLM", "JCI", "NUE", "STLD", "RS", "FDX", "UNP", "ODFL", "EXPD",
        "CHRW", "JBHT", "LUV", "DAL", "UAL", "AAL", "F", "GM", "BBY", "TSCO", "AZO",
        "GME", "HAS", "MAT", "TGT", "KSS", "JWN", "M", "HLT", "WYNN", "LVS", "RCL",
        "CCL", "NCLH", "DRI", "YUM", "CMG", "DPZ", "WEN", "QSR", "EL", "CL", "CHD",
        "CLX", "ADM", "BG", "TSN", "HRL", "CPB", "K", "GIS", "POST", "MKC", "SJM",
        "TAP", "BUD", "SAM", "STZ", "BF-B", "BTI", "UVV", "EW", "ZBH", "ALGN", "DXCM",
        "PODD", "TFX", "THC", "UHS", "WBA", "CNC", "COF", "DFS", "SOFI", "STT", "NTRS",
        "AMP", "BEN", "IVZ", "TROW", "RJF", "LPLA", "TRV", "ALL", "MET", "PRU", "LNC",
        "VOYA", "AFL", "CBOE", "CME", "ICE", "NDAQ", "MKTX", "MSCI", "FACT", "PSA",
        "EXR", "CUBE", "IRM", "NXPI", "MCHP", "ON", "SWKS", "QRVO", "MPWR", "TER",
        "ASML", "AFT", "AIZ", "ALLE", "ANSS", "AOS", "APA", "APTV", "ARE", "ATO",
        "AWK", "BKR", "BXP", "CAG", "CDW", "CE", "CF", "CNP", "COO", "CPT", "CTRA",
        "CTSH", "CTVA", "DAY", "DD", "FANG", "FAST", "FE", "FFIV", "FITB", "FMC",
        "FOXA", "FOX", "FRT", "FTNT", "FTV", "GEN", "GNRC", "HASI", "HBAN", "HES",
        "HPE", "HPQ", "HST", "HZNP", "IDXX", "IEX", "INCY", "INVH", "IP", "IPG",
        "JKHY", "JNPR", "KEY", "KEYS", "KIM", "LDOS", "LECO", "LKQ", "LNT", "LUM",
        "LYB", "MTB", "MTD", "NI", "NORD", "NRG", "NTAP", "NWL", "NWSA", "NWS",
        "O", "OKE", "OMC", "OTIS", "PARA", "PAYX", "PAYC", "PBI", "PEAK", "KDP",
        "PNW", "POOL", "PNR", "PPG", "PRGO", "PTC", "PWR", "RL", "RMD", "ROL",
        "RHI", "SBAC", "SEDG", "SEE", "SHW", "STX", "STE", "STT", "SWK", "SWKS",
        "TECH", "TEL", "TER", "TFX", "TPR", "TRMB", "TROW", "TYL", "VRSN", "VRSK",
        "VFC", "VTRS", "VTI", "WAB", "WAT", "WEC", "WELL", "WST", "WRK", "WXY",
        "WY", "WYN", "XEL", "XRAY", "XYL", "ZBRA", "ZION"
    ]
    
    # 自動去重與排序
    TICKER_POOL = sorted(list(set(TICKER_POOL)))
    print(f"成功加載大型美股池，共計 {len(TICKER_POOL)} 隻核心股票。")
    
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

