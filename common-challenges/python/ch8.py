def birthdayCakeCandles(candles):
    
    tallest = max(candles)
    n_tallest = 0

    for candle in candles:
        if candle == tallest:
            n_tallest += 1

    return n_tallest
