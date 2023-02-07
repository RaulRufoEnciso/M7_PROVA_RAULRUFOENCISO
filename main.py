import matplotlib.pyplot as plt
import mitjanaAlumnes as ma

print(ma.mitjanaalumnes())

def creagrafica():
    mitAl = ma.mitjanaalumnes()

    x = list(mitAl.iloc[:, 0])
    y = list(mitAl.iloc[:, 1])

    plt.bar(x, y, color="red")
    plt.title("RAUL RUFO ENCISO")
    plt.xlabel("ALUMNAT")
    plt.ylabel("NOTAS")
    plt.show()


creagrafica()

