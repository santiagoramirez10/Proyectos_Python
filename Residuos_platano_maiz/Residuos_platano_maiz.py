# -*- coding: utf-8 -*-
"""
@authores: 
Santiago Ramírez Pérez
John Camilo Sánchez Ortíz
David Alejandro Osorno D
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_platano="Platano.xlsx"
df_platano=pd.read_excel(file_platano)
file_maiz="Maiz.xlsx"
df_maiz=pd.read_excel(file_maiz)

header_platano=list(df_platano.head(0))
header_maiz=list(df_maiz.head(0))

Bajo_cauca=["CAUCASIA","CACERES","EL BAGRE","NECHI","TARAZA","ZARAGOZA"]
Magdalena_medio=["CARACOLI","MACEO","PUERTO BERRIO","PUERTO NARE","PUERTO TRIUNFO","YONDO"]
Nordeste=["AMALFI","ANORI","CISNEROS","REMEDIOS","SAN ROQUE","SANTO DOMINGO","SEGOVIA","VEGACHI","YALI","YOLOMBO"]
Norte=["ANGOSTURA","BELMIRA","BRICEÑO","CAMPAMENTO","CAROLINA DEL PRINCIPE","DON MATIAS","ENTRERRIOS","GOMEZ PLATA","GUADALUPE","ITUANGO","SAN ANDRES","SAN JOSE DE LA MONTAÑA","SAN PEDRO","SANTA ROSA DE OSOS","TOLEDO","VALDIVIA","YARUMAL"]
Occidente=["ABRIAQUI","ANZA","ARMENIA","BURITICA","CAICEDO","CAÑASGORDAS","DABEIBA","EBEJICO","FRONTINO","GIRALDO","HELICONIA","LIBORINA","OLAYA","PEQUE","SABANALARGA","SAN JERONIMO","SANTAFE DE ANTIOQUIA","SOPETRAN","URAMITA"]
Oriente=["ABEJORRAL","ALEJANDRIA","ARGELIA","CARMEN DE VIBORAL","COCORNA","CONCEPCION","EL PEÑOL","EL RETIRO","SANTUARIO","GRANADA","GUARNE","GUATAPE","LA CEJA","LA UNION","MARINILLA","NARIÑO","RIONEGRO","SAN CARLOS","SAN FRANCISCO","SAN LUIS","SAN RAFAEL","SAN VICENTE","SONSON"]
Suroeste=["AMAGA","ANDES","ANGELOPOLIS","BETANIA","BETULIA","CARAMANTA","CIUDAD BOLIVAR","CONCORDIA","FREDONIA","HISPANIA","JARDIN","JERICO","LA PINTADA","MONTEBELLO","PUEBLO RICO","SALGAR","SANTA BARBARA","TAMESIS","TARSO","TITIRIBI","URRAO","VALPARAISO","VENECIA"]
Uraba=["APARTADO","ARBOLETES","CAREPA","CHIGORODO","MURINDO","MUTATA","NECOCLI","SAN JUAN DE URABA","SAN PEDRO DE URABA","TURBO","VIGIA DEL FUERTE"]
Valle_aburra=["BARBOSA","BELLO","CALDAS","COPACABANA","ENVIGADO","GIRARDOTA","ITAGUI","LA ESTRELLA","MEDELLIN","SABANETA"]
Subregiones=[Bajo_cauca,Magdalena_medio,Nordeste,Norte,Occidente,Oriente,Suroeste,Uraba,Valle_aburra]
Subregiones_nombre=["BAJO CAUCA","MAGDALENA MEDIO","NORDESTE","NORTE","OCCIDENTE","ORIENTE","SUROESTE","URABA","VALLE DE ABURRA"]

platano_ant=df_platano[df_platano["DEPARTAMENTO"]=="ANTIOQUIA"]
maiz_ant=df_maiz[df_maiz["DEPARTAMENTO"]=="ANTIOQUIA"]

platano_ant=platano_ant.to_numpy()
maiz_ant=maiz_ant.to_numpy()
platano_ant=platano_ant.tolist()
maiz_ant=maiz_ant.tolist()

for i in range(len(platano_ant)):
    for j in range(len(Subregiones)):
        if platano_ant[i][3] in Subregiones[j]:
            platano_ant[i].append(Subregiones_nombre[j])
            break
for i in range(len(maiz_ant)):
    for j in range(len(Subregiones)):
        if maiz_ant[i][3] in Subregiones[j]:
            maiz_ant[i].append(Subregiones_nombre[j])
            break

FR_platano=5
YRS_platano=0.0661
PC_platano=0.0085

FR_maiz=0.9340
YRS_maiz=0.6417
PC_maiz=0.0144

for i in range(len(platano_ant)):
    platano_ant[i].append(platano_ant[i][12]*platano_ant[i][14]*FR_platano*YRS_platano*PC_platano)
for i in range(len(maiz_ant)):
    maiz_ant[i].append(maiz_ant[i][12]*maiz_ant[i][14]*FR_maiz*YRS_maiz*PC_maiz)


header_platano.append("SUBREGION")
header_maiz.append("SUBREGION")
header_platano.append("P.E.G. (TJ/Año)")
header_maiz.append("P.E.G. (TJ/Año)")
pd.DataFrame(platano_ant, columns=header_platano).to_excel(r"Platano_ant.xlsx",index=False)     
pd.DataFrame(maiz_ant, columns=header_maiz).to_excel(r"Maiz_ant.xlsx",index=False)