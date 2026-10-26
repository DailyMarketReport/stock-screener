def check_my_investment_logic(ticker_symbol):
    """
    純美股投資Logic：市值>50億美元、成交>1000萬美元、ROE>15%、3年盈利增長>10% + 5年勝率回測
    """
    try:
        import yfinance as yf
        import pandas_ta as ta
        stock = yf.Ticker(ticker_symbol)
        info = stock.info
        
        # 1. 基本面：市值與ROE過濾（單位均為美元）
        market_cap = info.get("marketCap", 0)
        roe = info.get("returnOnEquity", 0)
        if market_cap < 5_000_000_000 or roe < 0.15:
            return None
            
        # 2. 基本面：近3年盈利增長 > 10%
        financials = stock.financials
        if "Net Income" not in financials.index or financials.shape[1] < 4:
            return None
        net_inc = financials.loc["Net Income"].dropna()
        if net_inc.iloc[0] <= 0 or (net_inc.iloc[0] - net_inc.iloc[3]) / net_inc.iloc[3] < 0.10:
            return None

        # 3. 5年歷史數據回測技術面 (回踩50日線 + RSI<40) 與成交額
        df = stock.history(period="5y")
        if len(df) < 250: return None
        
        # 檢查近期日成交額是否 > 1000萬美元
        recent_turnover = df['Close'].iloc[-1] * df['Volume'].iloc[-1]
        if recent_turnover < 10_000_000:
            return None
            
        df['MA50'] = ta.sma(df['Close'], length=50)
        df['RSI'] = ta.rsi(df['Close'], length=14)
        df.dropna(inplace=True)
        
        # 訊號條件：現價在MA50的1.02倍內且RSI<40
        df['Signal'] = (df['Close'] >= df['MA50']) & (df['Close'] <= df['MA50'] * 1.02) & (df['RSI'] < 40)
        
        signal_indices = df[df['Signal']].index
        total_signals = len(signal_indices)
        if total_signals == 0: return None
            
        wins = 0
        for idx in signal_indices:
            loc = df.index.get_loc(idx)
            future_df = df.iloc[loc+1 : loc+61]
            if len(future_df) < 10: continue
            if (future_df['High'].max() - df.loc[idx, 'Close']) / df.loc[idx, 'Close'] >= 0.10:
                wins += 1
                
        win_rate = wins / total_signals
        
        # 4. 凱利公式建議倉位 (盈虧比 b = 2)
        b = 2.0
        kelly_f = max(0, (b * win_rate - (1.0 - win_rate)) / b) * 0.5
        
        if df['Signal'].iloc[-1]: # 今天剛好觸發
            return {
                "Ticker": ticker_symbol,
                "Name": info.get("shortName", "N/A"),
                "5Y_Signals": total_signals,
                "60D_WinRate": f"{win_rate*100:.1f}%",
                "Kelly_Position": f"{kelly_f*100:.1f}%"
            }
    except:
        return None
    return None

