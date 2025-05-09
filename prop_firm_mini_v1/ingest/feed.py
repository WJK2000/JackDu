
import pyupbit
def price(symbol):
    df = pyupbit.get_ohlcv(symbol, interval='minute15', count=1)
    return None if df is None else float(df['close'].iloc[-1])
