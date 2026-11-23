# Pobiera roczne dywidendy i ceny spółek z Yahoo Finance i zapisuje do CSV

import yfinance as yf
import pandas as pd

tickery = ["KO", "T", "MSFT", "PEP", "JNJ"]
wiersze = []
wiersze_ceny = []


for ticker in tickery:
    spolka = yf.Ticker(ticker)
    dywidendy = spolka.dividends
    roczne = dywidendy.groupby(dywidendy.index.year).sum()
    for rok, kwota in roczne.items():
        if 2016 <= rok < 2026:
            wiersze.append({"ticker": ticker, "rok": rok, "dywidenda": round(kwota, 2)})

    historia = spolka.history(start="2016-01-01", end="2026-01-01", auto_adjust=False)
    ceny = historia["Close"]
    ceny_roczne = ceny.groupby(ceny.index.year).last()
    for rok, cena in ceny_roczne.items():
        wiersze_ceny.append({"ticker": ticker, "rok": rok, "cena": round(cena, 2)})


tabela_ceny = pd.DataFrame(wiersze_ceny)
print(tabela_ceny)
tabela_ceny.to_csv("ceny_roczne.csv", index=False)

    
tabela = pd.DataFrame(wiersze)
print(tabela)
tabela.to_csv("dywidendy_roczne.csv", index=False)            


