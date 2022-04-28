# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as grafico
#import variaveis1 as variaveis

dados = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/precoVoo/Clean_Dataset.csv")
#print(dados.describe())

# a) Does price vary with Airlines?
precoLinhaAerea = dados.iloc[:,[1,11]]
# print(precoLinhaAerea["airline"].value_counts())

vistara = precoLinhaAerea[precoLinhaAerea["airline"] == "Vistara"]
air_india = precoLinhaAerea[precoLinhaAerea["airline"] == "Air_India"]
indigo = precoLinhaAerea[precoLinhaAerea["airline"] == "Indigo"]
go_first = precoLinhaAerea[precoLinhaAerea["airline"] == "GO_FIRST"]
airasia = precoLinhaAerea[precoLinhaAerea["airline"] == "AirAsia"]
spicejet = precoLinhaAerea[precoLinhaAerea["airline"] == "SpiceJet"]

vistara = vistara.sample(5000)
air_india = air_india.sample(5000)
indigo = indigo.sample(5000)
go_first = go_first.sample(5000)
airasia = airasia.sample(5000)
spicejet = spicejet.sample(5000)

vistaraMed = np.mean(vistara["price"])
vistaraVar = np.var(vistara["price"])

airindiaMed = np.mean(air_india["price"])
airindiaVar = np.var(air_india["price"])

indigoMed = np.mean(indigo["price"])
indigoVar = np.var(indigo["price"])

go_firstMed = np.mean(go_first["price"])
go_firstVar = np.var(go_first["price"])

airasiaMed = np.mean(airasia["price"])
airasiaVar = np.var(airasia["price"])

spicejetMed = np.mean(spicejet["price"])
spicejetVar = np.var(spicejet["price"])

#============ESTIMATIVA=DENTRO=(DENOMINADOR)=========================
mediaDasVariancias_a = np.mean([vistaraVar,airindiaVar,indigoVar,go_firstVar,airasiaVar,spicejetVar])

#============ESTIMATIVA=ENTRE=(NUMERADOR)=========================
varianciaDasMedias_a = np.var([vistaraMed,airindiaMed,indigoMed,go_firstMed,airasiaMed,spicejetMed])

varianciaEntreMedias_a = (varianciaDasMedias_a*5000)/mediaDasVariancias_a

valorF_a = varianciaEntreMedias_a/mediaDasVariancias_a
#print(valorF_a)
""" 
graus de liberdade 5 e 30 (5 e 29994) = 2,53
não é significativo para 5% de intervalo de confiança pois valorF < 2,53 para uma amostra de 5000 
""" 

# b) How is the price affected when tickets are bought in just 1 or 2 days before departure?

doisOuUm = dados[dados["days_left"] <= 2]
doisOuUm = doisOuUm.iloc[:,[10,11]]
doisOuUm = doisOuUm.sample(5000)

maisQueDois = dados[dados["days_left"] > 2]
maisQueDois = maisQueDois.iloc[:,[10,11]]
maisQueDois = maisQueDois.sample(5000)

#print(doisOuUm["price"].describe())
#print(maisQueDois["price"].describe())

doisOuUmMedia = np.mean(doisOuUm["price"])
doisOuUmVar = np.var(doisOuUm["price"])
maisQueDoisMedia = np.mean(maisQueDois["price"])
maisQueDoisVar = np.var(maisQueDois["price"])

mediaDasVariancias_b = np.mean([doisOuUmVar,maisQueDoisVar])
varianciaDasMedias_b = np.var([doisOuUmMedia,maisQueDoisMedia])
varianciaEntreMedias_b = (varianciaDasMedias_b*5000)/mediaDasVariancias_b
valorF_b = varianciaEntreMedias_b/mediaDasVariancias_b

#print(valorF_b)
#grafico.boxplot([doisOuUm["price"],maisQueDois["price"]])
#grafico.grid()
#grafico.show()
""" 
Graus de liberdade 1 e 10 (1 e 4999) = 4,96 não é significativo para 5% de intervalo de confiança pois valorF < 4,96 para uma amostra de 5000. A análise revelou que o preço médio das passagens compradas em 1 ou 2 dias antes da partida é sempre maior que comprada com mais de 2 dias de partida. 
"""

# c) Does ticket price change based on the departure time and arrival time?
""" 
Os preços das passagems apresentam diferenças significativas. Ex: mais de 75% das passagens de "partir tarde da noite para chegar cedo" são mais baratas que mais de 75% das passagens "partir de noite para chegar depois do entardecer (Evening)". Ou seja, sais mais barato partir tarde da noite para chegar cedo do que partir de noite para chegar depois do entardecer.
"""
tempoDepArr = dados.iloc[:,[4,6,11]]
#print(tempoDepArr["departure_time"].value_counts())
#print(variaveis1.varianciaEntreMedias/variaveis1.mediaDasVariancias)

# d) How the price changes with change in Source and Destination?
"""  
A hipótese nula é rejeitada pois razãoF é sempre maior que o valor tabelado(1,524). Isso significa que existem diferenças significativas. A rota Delhi-Hyderabad apresenta as passagens mais baratas sendo 75% dos preços abaixo de 26388. Enquanto que o trajeto Chennai-Bangalore apresenta a média de preço mais alta custando 25081.85
"""
fonteDestinoArr = dados.iloc[:,[3,7,11]]
cidadeFonteDestino = ["Delhi","Mumbai","Bangalore","Kolkata","Hyderabad","Chennai"]

possibilidades = []
paraGraficoCaixa = []
for i in range(0,len(cidadeFonteDestino),1):
    for j in range(0,len(cidadeFonteDestino),1):
        if cidadeFonteDestino[i] == cidadeFonteDestino[j]: continue
        teste = fonteDestinoArr[fonteDestinoArr["source_city"] == cidadeFonteDestino[i]]
        teste = teste[teste["destination_city"] == cidadeFonteDestino[j]]
        #teste = teste.sample(3000)
        paraGraficoCaixa.append(teste["price"])
        possibilidades.append({
            "fonte":cidadeFonteDestino[i],
            "destino":cidadeFonteDestino[j],
            "resumo":teste.describe()
        })

mediaDasVariancias_d = []
varianciaDasMedias_d = []
for i in possibilidades:
    variancia = (i["resumo"].loc["std"])*(i["resumo"].loc["std"])
    media = i["resumo"].loc["mean"]
    mediaDasVariancias_d.append(variancia)
    varianciaDasMedias_d.append(media)

mediaDasVariancias_d = np.mean(mediaDasVariancias_d)
varianciaDasMedias_d = np.var(varianciaDasMedias_d)
varianciaEntreMedias_d = ((varianciaDasMedias_d*3000)/mediaDasVariancias_d)
razaoF_d = varianciaEntreMedias_d/mediaDasVariancias_d
#print(razaoF_d)
""" grafico.boxplot(paraGraficoCaixa)
grafico.grid()
grafico.show() """

# e) How does the ticket price vary between Economy and Business class ?
"""
Existem diferenças significativas. A classe influencia nos preços da passagem. 75% dos preços da classe business (> 45185) são mais caros que todos os preços da classe economy(max = 42349).
"""
economiaBusiness = dados.iloc[:,[8,11]]
classeEconomia = economiaBusiness[economiaBusiness["class"] == "Economy"]
classeBusiness = economiaBusiness[economiaBusiness["class"] == "Business"]

classeEconomia = classeEconomia.sample(10000)
classeBusiness = classeBusiness.sample(10000)

print(classeEconomia["price"].describe())
print(classeBusiness["price"].describe())

ecoVariancia = np.var(classeEconomia["price"])
busVariancia = np.var(classeBusiness["price"])
ecoMedia = np.mean(classeEconomia["price"])
busMedia = np.mean(classeBusiness["price"])

mediaDasVariancias_e = np.mean([ecoVariancia,busVariancia])
varianciaDasMedias_e = np.var([ecoMedia,busMedia])
varianciaEntreMedias_e = ((varianciaDasMedias_e*10000)/mediaDasVariancias_e)
razaoF_e = varianciaEntreMedias_e/mediaDasVariancias_e
#print(razaoF_e)

""" grafico.boxplot([classeEconomia["price"],classeBusiness["price"]])
grafico.grid()
grafico.show() """

"""
The various features of the cleaned dataset are explained below:
1) Airline: The name of the airline company is stored in the airline column. It is a categorical feature having 6 different airlines.
2) Flight: Flight stores information regarding the plane's flight code. It is a categorical feature.
3) Source City: City from which the flight takes off. It is a categorical feature having 6 unique cities.
4) Departure Time: This is a derived categorical feature obtained created by grouping time periods into bins. It stores information about the departure time and have 6 unique time labels.
5) Stops: A categorical feature with 3 distinct values that stores the number of stops between the source and destination cities.
6) Arrival Time: This is a derived categorical feature created by grouping time intervals into bins. It has six distinct time labels and keeps information about the arrival time.
7) Destination City: City where the flight will land. It is a categorical feature having 6 unique cities.
8) Class: A categorical feature that contains information on seat class; it has two distinct values: Business and Economy.
9) Duration: A continuous feature that displays the overall amount of time it takes to travel between cities in hours.
10)Days Left: This is a derived characteristic that is calculated by subtracting the trip date by the booking date.
11) Price: Target variable stores information of the ticket price. """