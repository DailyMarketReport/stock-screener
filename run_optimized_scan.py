#!/usr/bin/env python3
import sys
from src.screening.screener import check_my_investment_logic

if __name__ == "__main__":
    print("==========================================")
    print("--- 開始執行『1000 隻美股特大池 + GitHub App 推送』篩選 ---")
    print("==========================================")
    
    # 內嵌 1000 隻核心美國股票池（免聯網，100% 成功）
    TICKER_POOL = [
        # --- 標普前 100 與超級科技巨頭 ---
        "AAPL", "MSFT", "AMZN", "NVDA", "GOOGL", "GOOG", "META", "BRK-B", "UNH", "JNJ",
        "XOM", "JPM", "TSLA", "V", "PG", "MA", "AVGO", "HD", "CVX", "MRK", "ABBV", "COST",
        "PEP", "ADBE", "KO", "WMT", "MCD", "CSCO", "TMO", "CRM", "BAC", "ACN", "CMCSA",
        "LIN", "NFLX", "AMD", "ORCL", "ABT", "TXN", "PM", "UPS", "NEE", "AMGN", "HON",
        "COP", "RTX", "LOW", "SPGI", "IBM", "AXP", "INTC", "CAT", "LMT", "MS", "DE",
        "GS", "GE", "BKNG", "NKE", "SBUX", "PLD", "MDLZ", "BLK", "AMT", "ISRG", "TJX",
        "CB", "MMC", "ADI", "NOW", "CVS", "GILD", "T", "LRCX", "MO", "SYK", "ZTS",
        "CI", "DHR", "ELV", "VRTX", "SLB", "BDX", "REGN", "BMY", "BSX", "ADP", "EOG",
        "PGR", "HCA", "ITW", "WM", "FCX", "HUM", "NOC", "MCO", "ETN", "PH", "ECL",
        # --- 精選大型與中型市值成長股 ---
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
        "RHI", "SBAC", "SEDG", "SEE", "SHW", "STX", "STE", "SWK", "TECH", "TEL",
        "TPR", "TRMB", "TYL", "VRSN", "VRSK", "VFC", "VTRS", "VTI", "WAB", "WAT",
        "WEC", "WELL", "WST", "WRK", "WXY", "WY", "WYN", "XEL", "XRAY", "XYL",
        "ZBRA", "ZION", "PLTR", "SQ", "DKNG", "HOOD", "UBER", "LYFT", "SNOW", "NET",
        "CRWD", "DDOG", "ZS", "OKTA", "MDB", "TEAM", "WDAY", "SPLK", "FSLR", "ENPH",
        # --- 新增 600 隻核心美股（擴大網羅面） ---
        "AA", "AAL", "AAON", "AAP", "AAWW", "ABG", "ABM", "ABMD", "ABTX", "ACA",
        "CHTR", "CPRT", "KHC", "WBA", "BILI", "PDD", "LI", "NIO", "XPEV", "FUTU",
        "TME", "JD", "NTES", "TAL", "EDU", "ZTO", "KE", "BZ", "IQ", "VNET",
        "ACM", "ACGL", "ACHC", "ACI", "ACIW", "AEIS", "AER", "AFG", "AGCO", "AGIO",
        "AGNC", "AGR", "AHL", "AHT", "AI", "AIN", "AIT", "AIZ", "AJG", "AKAM",
        "AL", "ALB", "ALEE", "ALEX", "ALG", "ALGM", "ALGT", "ALK", "ALKS", "ALLY",
        "ALNY", "ALR", "ALRM", "ALSN", "ALT", "ALTA", "ALTR", "AM", "AMBA", "AMBC",
        "AMC", "AMCR", "AME", "AMED", "AMG", "AMH", "AMKR", "AMN", "AMPH", "AMSF",
        "AMWD", "AN", "ANAB", "ANAT", "ANDE", "ANE", "ANET", "ANF", "ANGI", "ANIK",
        "ANIP", "ANNX", "ANSS", "ANTM", "AOUT", "APAM", "APD", "APG", "APH", "APLE",
        "APLS", "APOG", "APP", "APPN", "APPS", "APRE", "APT", "APTM", "APTV", "APYX",
        "AQN", "AQUA", "AR", "ARAV", "ARCB", "ARCH", "ARCM", "ARDX", "ARE", "ARES",
        "ARGO", "ARGX", "ARHS", "ARI", "ARKO", "ARKR", "ARLO", "ARMK", "ARNA", "ARNC",
        "AROW", "ARPA", "ARVN", "ARW", "ARWR", "ASA", "ASAN", "ASB", "ASGN", "ASH",
        "ASIX", "ASLE", "ASLN", "ASMB", "ASND", "ASO", "ASPN", "ASR", "ASRT", "ASYS",
        "ATAX", "ATC", "ATCO", "ATEA", "ATER", "ATEX", "ATGE", "ATH", "ATHA", "ATHM",
        "ATI", "ATKR", "ATLC", "ATLO", "ATNI", "ATNX", "ATOM", "ATOS", "ATR", "ATRA",
        "ATRC", "ATRI", "ATRO", "ATSG", "ATTO", "ATUS", "ATVI", "AU", "AUDC", "AUPH",
        "AUTL", "AUTO", "AVA", "AVNS", "AVNT", "AVNW", "AVO", "AVRO", "AVT", "AVXL",
        "AVY", "AWI", "AWK", "AWR", "AX", "AXDX", "AXGN", "AXL", "AXON", "AXP",
        "AXSM", "AXTA", "AY", "AYI", "AYLA", "AYRO", "AYTU", "AZN", "AZO", "AZPN",
        "AZRE", "AZYO", "AZZ", "BA", "BABY", "BANC", "BAND", "BANF", "BANR", "BASE",
        "BATRA", "BATT", "BAX", "BB", "BBAR", "BBBY", "BBCP", "BBD", "BBDC", "BBGI",
        "BBIO", "BBLN", "BBQ", "BBSI", "BBU", "BBY", "BC", "BCBP", "BCEI", "BCLI",
        "BCML", "BCO", "BCOM", "BCOR", "BCOV", "BCPC", "BCRX", "BCSF", "BCTF", "BCYC",
        "BDC", "BDMD", "BDN", "BDR", "BDSI", "BDTX", "BE", "BEAM", "BEAT", "BECN",
        "BEDU", "BELFA", "BELFB", "BEN", "BEPC", "BERY", "BEST", "BFAM", "BFC", "BFIN",
        "BFS", "BFST", "BG", "BGCP", "BHE", "BHF", "BHLB", "BHR", "BHVN", "BIG",
        "BIGC", "BIIB", "BILI", "BILL", "BIMI", "BIO", "BIOC", "BIOL", "BIOS", "BIP",
        "BISC", "BITF", "BIVI", "BJ", "BJRI", "BK", "BKD", "BKE", "BKH", "BKI",
        "BKKT", "BKR", "BKSC", "BKYI", "BL", "BLBD", "BLCM", "BLD", "BLDR", "BLFS",
        "BLFY", "BLI", "BLIN", "BLK", "BLKB", "BLMN", "BLND", "BLNG", "BLNK", "BLPH",
        "BLRX", "BLU", "BLUE", "BLX", "BMA", "BMCH", "BMEA", "BMI", "BMRC", "BMRN",
        "BMTC", "BMTX", "BNED", "BNFT", "BNGO", "BNL", "BNR", "BNSO", "BNTX", "BOOT",
        "BORR", "BOSC", "BOTJ", "BOX", "BOXL", "BP", "BPTH", "BPY", "BPYPM", "BR",
        "BRBR", "BRBS", "BRC", "BRDG", "BREW", "BRFS", "BRG", "BRID", "BRKL", "BRKR",
        "BRLI", "BRLT", "BRMK", "BRN", "BRO", "FSLY", "PINS", "SNAP", "TWLO", "DOCU",
        "RNG", "BAND", "VNOM", "FANG", "PXD", "APA", "MRO", "DVN", "HAL", "BKR",
        "SLB", "FTI", "NOV", "HP", "NBR", "PTEN", "BOOM", "OII", "MRC", "DNOW",
        "CLF", "X", "STLD", "NUE", "CMC", "RS", "ATI", "HMY", "AU", "KGC",
        "IAG", "NGD", "SAND", "OR", "WPM", "FNV", "RGLD", "AA", "CENX", "KALU",
        "CF", "MOS", "SMG", "AVNT", "HUN", "OLN", "WLK", "NEU", "KWR", "IOSP",
        "GPRE", "ALB", "SQM", "LIVN", "LTHM", "MP", "UCTT", "LRCX", "AMAT", "ASML",
        "TOELY", "OTIS", "CARR", "FI", "PAYX", "FAST", "EXPD", "JBHT", "ODFL", "KNX",
        "CHRW", "ATSG", "XPO", "RXO", "GXO", "ARCB", "SAIA", "YRCW", "HUBG", "MATX",
        "ALGT", "SKYW", "HA", "JBLU", "SAVE", "ALK", "LUV", "DAL", "UAL", "AAL",
        "HTZ", "CAR", "EXPR", "GCO", "URBN", "ANF", "AEO", "PLCE", "GES", "TLYS",
        "BOOT", "LE", "FL", "FINV", "LX", "QFIN", "JFU", "AMTD", "HKD", "TOP",
        "HUDI", "WNW", "EDTK", "METX", "COE", "JCOM", "ZENV", "TUYA", "YSG", "LOOK"
    ]
    
    # 自動去重與排序
    TICKER_POOL = sorted(list(set(TICKER_POOL)))
    print(f"成功加載特大美股池，共計 {len(TICKER_POOL)} 隻核心股票。")
    
    triggered_count = 0
    for ticker in TICKER_POOL:
        res = check_my_investment_logic(ticker)
        if res:
            # 只要有觸發，就在日誌頂端打印出火爆警告
            print(f"🔥 【ALERT】策略觸發：{res['Ticker']} ({res['Name']}) | 5年歷史信號: {res['5Y_Signals']} 次 | 勝率: {res['60D_WinRate']} | 建議倉位: {res['Kelly_Position']}")
            triggered_count += 1
            
    print(f"--- 篩選結束，今日共有 {triggered_count} 隻美股觸發入場訊號 ---")
    
    # 核心 GitHub App 推送控制邏輯
    if triggered_count > 0:
        print(f"\n📢 發現符合條件的股票！故意觸發中斷以向 GitHub Mobile App 發送強制推送通知。")
        sys.exit(1) # 讓 Actions 變紅叉，進而觸發手機 App 的即時彈窗通知
    else:
        print("\n😴 今日沒有股票觸發，保持綠燈完成，手機不打擾。")


