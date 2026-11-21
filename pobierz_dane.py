import yfinance as yf
import pandas as pd

tickery = ["KO", "T", "MSFT", "PEP", "JNJ"]
wiersze = []


for ticker in tickery:
    spolka = yf.Ticker(ticker)
    dywidendy = spolka.dividends
    roczne = dywidendy.groupby(dywidendy.index.year).sum()
    for rok, kwota in roczne.items():
        if 2016 <= rok < 2026:
            wiersze.append({"ticker": ticker, "rok": rok, "dywidenda": round(kwota, 2)})

tabela = pd.DataFrame(wiersze)
print(tabela)
tabela.to_csv("dywidendy_roczne.csv", index=False)            
    