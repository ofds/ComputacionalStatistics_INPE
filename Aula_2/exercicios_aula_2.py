# -*- coding: utf-8 -*-
"""Exercicios Aula 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GV5kuJZ3j9GdilexhYldERf1k8YRIACp
"""

print(f"Estatistica Computacional - CAP")
print(f"Otto Ferreira dos Santos")
print(f"Aula 2")

print(f"Exercicio 1: Numeros Aleatórios")
import random

print(f"Gere alguns numeros aleatórios\n")
print(f"Gerando 5 sementes aleatórias entre 0 e 999999:")
seeds = list()
for i in range(5):
  seeds.append(random.randint(0,999999))
print(f"As 5 sementes geradas são: {seeds}")

print(f"Gerando uma sequência de 10000 numeros aleatórios para cada semente.")
print(f"Para o histograma utilizaremos a biblioteca Seaborn e Numpy")
import seaborn as sns
import numpy as np

i=0
print(f"\nUtilizando a semente {seeds[i]}")
random.seed(seeds[i])
sequence = list()
for n in range(10000):
  sequence.append(random.randint(0,10000))
  #print(sequence[n])
sns.set_style('darkgrid')
numpyArray = np.array(sequence)
sns.histplot(numpyArray, stat='count',discrete=True)
i+=1

print(f"\nUtilizando a semente {seeds[i]}")
random.seed(seeds[i])
sequence = list()
for n in range(10000):
  sequence.append(random.randint(0,10000))
  #print(sequence[n])
sns.set_style('darkgrid')
numpyArray = np.array(sequence)
sns.histplot(numpyArray, stat='count',discrete=True)
i+=1

print(f"\nUtilizando a semente {seeds[i]}")
random.seed(seeds[i])
sequence = list()
for n in range(10000):
  sequence.append(random.randint(0,10000))
  #print(sequence[n])
sns.set_style('darkgrid')
numpyArray = np.array(sequence)
sns.histplot(numpyArray, stat='count',discrete=True)
i+=1

print(f"\nUtilizando a semente {seeds[i]}")
random.seed(seeds[i])
sequence = list()
for n in range(10000):
  sequence.append(random.randint(0,10000))
  #print(sequence[n])
sns.set_style('darkgrid')
numpyArray = np.array(sequence)
sns.histplot(numpyArray, stat='count',discrete=True)
i+=1

print(f"\nUtilizando a semente {seeds[i]}")
random.seed(seeds[i])
sequence = list()
for n in range(10000):
  sequence.append(random.randint(0,10000))
  #print(sequence[n])
sns.set_style('darkgrid')
numpyArray = np.array(sequence)
sns.histplot(numpyArray, stat='count',discrete=True)
i+=1

######################################################################################################################################################################################################
######################################################################################################################################################################################################
##############################################################               PARTE 2              ####################################################################################################
######################################################################################################################################################################################################
######################################################################################################################################################################################################

print(f"Estatística Descritiva")
print("Utilizaremos as bibliotecas Numpy e SciPy para as ajudar nas nossas contas")
print("Calcule o minimo, o maximo, a média, a moda, a mediana, o range, a soma, a varianca e o desvio padrao para a sequência")
from scipy import stats

print("Utilizando o seed de 1")
print("Gerando uma sequência de 5 valores")
sequence = list()
random.seed(1)
for i in range(5):
  sequence.append(random.randint(0,100))
print(f"Sequência gerada: {sequence}")
numpyArray = np.array(sequence)
print(f"O minimo valor é {np.min(numpyArray)}.\nO maximo é {np.max(sequence)}.\nA media é {np.average(sequence)}")
print(f"A moda é {np.max(stats.mode(numpyArray)[0])}.\nA mediana é {(np.median(numpyArray)):.0f}\nO range é {np.max(sequence)-np.min(sequence)}")
print(f"A soma é {np.sum(numpyArray):.0f}.\nA variancia é {np.var(sequence):.2f} \nO desvio padrão é {np.std(sequence):.2f}")

print("Utilizando o seed de 1")
print("Gerando uma sequência de 100 valores na faixa de [0-999]")
sequence = list()
random.seed(1)
for i in range(100):
  sequence.append(random.randint(0,100))
print(f"Sequência gerada: {sequence}")
numpyArray = np.array(sequence)
print(f"O minimo é {np.min(numpyArray)}\nO maximo é {np.max(sequence)}\nA media é {np.average(sequence)}")
print(f"A moda é {np.max(stats.mode(numpyArray)[0])} com {np.max(stats.mode(numpyArray)[1])} ocorrências\nA mediana é {(np.median(numpyArray)):.0f}\nO range é {np.max(sequence)-np.min(sequence)}")
print(f"A soma é {np.sum(numpyArray):.0f}\nA variancia é {np.var(sequence):.2f} \nO desvio padrão é {np.std(sequence):.2f}")
sns.set_style('darkgrid')
sns.histplot(numpyArray, stat='count')

print("O numpy possui uma maneira facil de calcular os percentiles, usando a funcao percentile")
print("Calcularemos os 11 percentiles: de 0% até 100%, usando um passo de 10%")
for n in range(0,110,10):
  print(f"O percentile {n}% é {np.percentile(numpyArray, n):.0f}")

print("Podemos calculcar a média de duas maneiras, somando todos os valores e dividindo a soma pela quantidade de valores")
print("Ou podemos pegar os valores, multiplica-los por um peso, nesse caso o inverso da quantidade, e fazer a soma desses valores, com isso teremos uma soma ponderada.")
print("Faremos a soma ponderada utilizando a sequencia gerada de 100 numeros")
sum = 0
for n in sequence:
  sum += n/len(sequence)
print(f"A soma ponderada teve um resultado de {sum}")

print("Visualization, plot the generated sequence as a time series, bar graph, pie graph, box-plot")
print(sequence)
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,15)

sequenceDataFrame = pd.DataFrame(sequence, columns=["Valor"]) 
sequenceDataFrame.plot(xlabel='tempo (s)', ylabel="Valor",kind='line', title='Time Series')
plt.show()

sequenceDataFrame.plot(xlabel='tempo (s)', ylabel="Valor",kind='bar', title='Vertical Bar Graph')
plt.show()

sequenceDataFrame.plot(xlabel='tempo (s)', ylabel="Valor",kind='barh', title='Horizontal Bar Graph')
plt.show()

plt.rcParams["figure.figsize"] = (20,20)
count = sequenceDataFrame.groupby('Valor').size()
countDataFrame = pd.DataFrame(count)
print(countDataFrame.transpose())
countDataFrame.plot.pie(subplots=True, legend=None, title='Pie Plot')

data = list()
sequence.sort()
for i in range(4):
  data.append(sequence[(i*25):((i+1)*25)])

sortedDataFrame = pd.DataFrame(data)
print(sortedDataFrame)
sortedDataFrame.transpose().plot.box(title='Box plot')
plt.show()

print("Média Móvel - Como calcular a média movel?")
print("Escolha um intervalo, no nosso caso terá 7 valores, percorra os dados fazendo a média com 7 valores, se possivel.")
print("Usaremos a mesma sequencia aleatoria gerada para os exercicios anteriores")
sequence = list()
random.seed(1)
janela = 7
for i in range(100):
  sequence.append(random.randint(0,100))

dia = 1
mediaMovel = list()
while(dia<=len(sequence)):
  inicio = (dia-janela) if (dia-janela)>=0 else 0 # faz com que nao ultrapassamos os limites da lista
  fim = dia
  valores = sequence[inicio:dia]
  #print(valores)
  mediaMovel.append(np.average(valores))
  #print(f"A média movel entre os dias {inicio} e {fim} foi de {mediaMovel[len(mediaMovel)-1]}")
  dia +=1
print("O grafico da média movel é o seguinte:")
plt.rcParams["figure.figsize"] = (15,15)
mediaMovelDataFrame = pd.DataFrame(mediaMovel, columns=["Média"]) 
mediaMovelDataFrame.plot(xlabel='tempo (d)', ylabel="Média",kind='line', title='Time Series')
plt.show()

print("Calculo de Pi com numeros aletórios")
print("Vi um tempo atrás um video que falava sobre o metodo Monte carlo de testes que usava exatamente esse exemplo, tentarei reproduzi-lo por memoria")
print("Tem a seguinte logica: gerarei uma serie pares de numeros aleatórios entre -1 e 1, se esse ponto estiver dentro de um circulo situado na origem com raio 1, direi que ele caiu dentro do circulo e guardarei a quantida de pontos que cairam no circulos")
print("Guardarei tambem a quantidade total de numeros gerados")
print("Como a area do circulo é (pi* r * r) e a area de um quadrado é (2r)*(2r) podemos calculcar pi usando a proporção entre pontos dentro do circulo e o total de pontos, que deve se aproximar de pi/4 ao aumentarmos os numeros de pontos gerados")

import random 
import math
quantidadeCirculo = 0
gerados = 0
limites = [10,100,1000,10000,100000,1000000,99999999]
for r in limites:
  for i in range(r):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (math.sqrt(x*x + y*y)) <=1:
      quantidadeCirculo += 1
    gerados+=1
  print(f"{r} Pontos. Pi calculado foi {(quantidadeCirculo/gerados)*4}")