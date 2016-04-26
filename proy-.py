# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 10:52:29 2016

@author: TOSHIBA
"""
## ¿Que estado, en promedio, necesita menos cotizaciones?
## ¿Cuántas cotizaciones, previo la compra, realizan los consumidores del estado de Florida?
## ¿En qué tiempo prudente se realizan las cotizaciones?
## ¿Del total de carros que porcentaje tiene menos de k años?
## ¿Que edad necesita menos cotizaciones para comprar un seguro?

import pandas as pd
import numpy as np 
import seaborn as sns

data = pd.read_csv('allstate.csv')
data.head()

## ¿Que estado, en promedio, necesita menos cotizaciones?
promedio = data.groupby("state")
promedio.shopping_pt.mean()
promedio.shopping_pt.mean().max()
#R// Florida  promedio de cotización 4.4384637820241419, es el que más cotizaciones tiene.

## ¿Cuántas cotizaciones, previo la compra, realizan los consumidores del estado de Florida?
filtro = data.state=='FL'
dat = data[filtro]

cotizacion = dat.groupby("shopping_pt")
cotizacion["shopping_pt"].sum()

## ¿En qué tiempo prudente se realizan las cotizaciones?
tiempo = data.groupby("time")
tiempo.shopping_pt.count().max()
