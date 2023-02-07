import pandas as pd

def mitjanaalumnes():
    mitalum = pd.read_csv("Raúl Rufo Enciso_Llistat.csv", usecols=["NAME", "NOTES"])
    return mitalum.dropna().groupby(by='NAME').mean()
