from os import system
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

doc = pd.read_csv('DatosEstadisticos.csv')

def Amenu():
    print("\t\t\t\t\t InfoCOVID")
    print()
    print("\t\t\tEl sistema que te brinda las ultimas estadisticas") 
    print("\t\t\t\tsobre el COVID-19 en Peru")
    print()
    print()
    print("\tA continuacion, escoga una opcion: ")
    print()
    print("\t1. Imprimir el DataFrame sobre los fallecidos por COVID-19 en Peru.") 
    print("\t2. Mostrar el numero de fallecidos segun su rango de edad")
    print("\t   (ninios, adolescentes, adultos y adultos mayores).")
    print("\t3. Mostrar el numero de fallecidos en cada departamento segun su sexo.") 
    print("\t4. Mostrar el porcentaje de fallecidos en cada departamento.") 
    print("\t5. Mostrar el porcentaje de los fallecidos que fueron hospitalizados en cada departamento.") 
    print("\t6. Mostrar el numero de hospitalizados que necesitaron ventilacion en cada departamento.") 
    print("\t7. Mostrar el numero de fallecidos segun cada criterio de fallecimiento") 
    print("\t   (clinico, nexo epidemiologico, SINADE, radiologico, virologico)") 
    print("\t   (investigacion Epidemiologica o serologico).")   
    print("\t8. Mostrar el porcentaje de fallecidos segun cada criterio de fallecimiento.")
    print("\t9. Mostrar el numero de fallecidos que estaban vacunados con x tipo") 
    print("\t   de vacuna segun su rango de edad.")  
    print("\t10. Mostrar el numero y sexo de fallecidos que fueron vacunados con 1 dosis de x tipo de vacuna") 
    print("\t11. Mostrar el numero y sexo de fallecidos que fueron vacunados con 2 dosis contra el")
    print("\t   COVID-19 en cada departamento.") 
    print("\t12. Salir")

departamentos = ['AMAZONAS', 'ANCASH', 'APURIMAC', 'AREQUIPA', 'AYACUCHO', 'CAJAMARCA', 'CALLAO', 'CUSCO',
                 'HUANCAVELICA', 'HUANUCO', 'ICA', 'JUNIN', 'LA LIBERTAD', 'LAMBAYEQUE',
                 'LIMA', 'LORETO', 'MADRE DE DIOS', 'MOQUEGUA', 'PASCO', 'PIURA','PUNO',
                 'SAN MARTIN', 'TACNA', 'TUMBES', 'UCAYALI']

def Afuncion1():
    print("\t\t\tDataFrame: Datos de fallecidos por COVID-19 en el Peru")
    print()
    print()
    print(doc)

def Afuncion2():
    Data = pd.DataFrame()
    print("NUMERO DE FALLECIDOS SEGUN SU RANGO DE EDAD")
    print()
    adultos_mayores = (doc['edad']>60)
    adultos = (doc["edad"] > 21) & (doc["edad"] <= 60)
    adol = (doc["edad"] > 13) & (doc["edad"] <= 21)
    ninos = (doc["edad"] > 0) & (doc["edad"] <= 13)
    Data["Adultos mayores"] = [sum(adultos_mayores)]
    Data["Adultos"] = [sum(adultos)]
    Data["Adolescentes"] = [sum(adol)]
    Data["Ninos"] = [sum(ninos)]
    print(Data)

def Afuncion3():
    print("NUMERO DE FALLECIDOS EN CADA DEPARTAMENTO SEGUN SU SEXO")
    print()
    DataM = []
    DataF = []
    num = len(departamentos)
    for i in range(num):
        DataM.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['sexo'] == 'M')]).count()))
    for i in range(num):
        DataF.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['sexo'] == 'F')]).count())) 
    dic ={'HOMBRES': DataM, 'MUJERES': DataF}
    print(pd.DataFrame(dic,index=[departamentos]))

def Afuncion4():
    print("PORCENTAJE DE FALLECIDOS EN CADA DEPARTAMENTO")
    print()
    Data = []
    num = len(departamentos)
    for i in range(num):
        Data.append((str(sum(doc['dpt_cdc']==departamentos[i])*100/10000))+"%")
    dic ={'PORCENTAJES': Data}
    print(pd.DataFrame(dic,index=[departamentos]))

def Afuncion5():
    print("PORCENTAJE DE FALLECIDOS QUE FUERON HOSPITALIZADOS EN CADA DEPARTAMENTO")
    print()
    Data = []
    num = len(departamentos)
    for i in range(num):
        Data.append((str(sum(doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_hospitalizado'] == 1)].count())*100/10000))+"%")
    dic ={'PORCENTAJES': Data}
    print(pd.DataFrame(dic,index=[departamentos]))

def Afuncion6():
    print("NUMERO DE HOSPITALIZADOS QUE NECESITARON VENTILACION EN CADA DEPARTAMENTO")
    print()
    Data = []
    num = len(departamentos)
    for i in range(num):
        Data.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['con_ventilacion'] == 1)]).count()))
    dic ={'Cantidad': Data}
    print(pd.DataFrame(dic,index=[departamentos]))

def Afuncion7():
    print("NUMERO DE FALLECIDOS SEGUN CADA CRITERIO DE FALLECIMIENTO")
    print()
    nombres = ['Criterio clinico','Criterio nexo epidemiologico','Criterio SINADEF','Criterio radiologico','Criterio virologico',
               'Criterio investigacion Epidemiologica','Criterio serologico']
    clinico = (doc['criterio_fallecido']=='Criterio clinico')
    epi = (doc['criterio_fallecido']=='Criterio nexo epidemiologico')
    sin = (doc['criterio_fallecido']=='Criterio SINADEF')
    rad = (doc['criterio_fallecido']=='Criterio radiologico')
    viro = (doc['criterio_fallecido']=='Criterio virologico')
    inv = (doc['criterio_fallecido']=='Criterio investigacion Epidemiologica')
    sero = (doc['criterio_fallecido']=='Criterio serologico')
    dic = {'CANTIDAD':[sum(clinico),sum(epi),sum(sin),sum(rad),sum(viro),sum(inv),sum(sero)]}
    print(pd.DataFrame(dic,index=[nombres]))
 
def Afuncion8():
    print("PORCENTAJE DE FALLECIDOS SEGUN CADA CRITERIO DE FALLECIMIENTO")
    print()
    Data = []
    nombres = ['Criterio clinico','Criterio nexo epidemiologico','Criterio SINADEF','Criterio radiologico','Criterio virologico',
               'Criterio investigacion Epidemiologica','Criterio serologico']
    clinico = (doc['criterio_fallecido']=='Criterio clinico')
    epi = (doc['criterio_fallecido']=='Criterio nexo epidemiologico')
    sin = (doc['criterio_fallecido']=='Criterio SINADEF')
    rad = (doc['criterio_fallecido']=='Criterio radiologico')
    viro = (doc['criterio_fallecido']=='Criterio virologico')
    inv = (doc['criterio_fallecido']=='Criterio investigacion Epidemiologica')
    sero = (doc['criterio_fallecido']=='Criterio serologico')
    Data.append(str(((sum(clinico)*100)/10000))+"%")
    Data.append(str(((sum(epi)*100)/10000))+"%")
    Data.append(str(((sum(sin)*100)/10000))+"%")
    Data.append(str(((sum(rad)*100)/10000))+"%")
    Data.append(str(((sum(viro)*100)/10000))+"%")
    Data.append(str(((sum(inv)*100)/10000))+"%")
    Data.append(str(((sum(sero)*100)/10000))+"%")
    dic = {'PORCENTAJE':Data}
    print(pd.DataFrame(dic,index=[nombres]))

def Afuncion9():
    print("NUMERO DE FALLECIDOS QUE ESTABAN VACUNADOS CON X TIPO DE VACUNA SEGUN SU RANGO DE EDAD")
    print()
    fab1_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 60)])
    fab1_adult1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 21) & (doc['edad'] <= 60)])
    fab1_adol1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 13) & (doc['edad'] <= 21)])
    fab1_n1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 0) & (doc['edad'] <= 13)])
    fab2_am1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 60)])
    fab2_adult1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 21) & (doc['edad'] <= 60)])
    fab2_adol1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 13) & (doc['edad'] <= 21)])
    fab2_n1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 0) & (doc['edad'] <= 13)])
    fab3_am1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 60)])
    fab3_adult1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 21) & (doc['edad'] <= 60)])
    fab3_adol1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 13) & (doc['edad'] <= 21)])
    fab3_n1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 0) & (doc['edad'] <= 13)])
    rango = ["Adultos Mayores","Adultos","Adolescentes","Ninos"]
    dic ={'PFIZER':[sum(fab1_am1.count()),sum(fab1_adult1.count()),sum(fab1_adol1.count()),sum(fab1_n1.count())],
          'SINOPHARM': [sum(fab2_am1.count()),sum(fab2_adult1.count()),sum(fab2_adol1.count()),sum(fab2_n1.count())],
          'ASTRAZENECA':[sum(fab3_am1.count()),sum(fab3_adult1.count()),sum(fab3_adol1.count()),sum(fab3_n1.count())]}
    print(pd.DataFrame(dic,index=[rango]))

def Afuncion10():
    print("NUMERO Y SEXO DE FALLECIDOS QUE FUERON VACUNADOS CON 1 DOSIS DE X TIPO DE VACUNA")
    print()
    nombre = ['PFIZER','SINOPHARM','ASTRAZENECA']
    fab1_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab1_am2 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab1_am3 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab2_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    fab2_am2 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    fab2_am3 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    M1 = sum(fab1_am1.count())
    M2 = sum(fab1_am2.count())
    M3 = sum(fab1_am3.count())
    F1 = sum(fab2_am1.count())
    F2 = sum(fab2_am2.count())
    F3 = sum(fab2_am3.count())
    dic = {'Hombres':[M1,M2,M3],'Mujeres':[F1,F2,F3]}
    print(pd.DataFrame(dic,index=[nombre]))

def Afuncion11():
    print("NUMERO Y SEXO DE FALLECIDOS QUE FUERON VACUNADOS CON 2 DOSIS EN CADA DEPARTAMENTO")
    print()
    Data = []
    Data1 = []
    num = len(departamentos)
    for i in range(num):
        Data.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_vacuna'] == 2) & (doc['sexo'] == 'M')]).count()))
    for i in range(num):
        Data1.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_vacuna'] == 2) & (doc['sexo'] == 'F')]).count()))
    dic ={'HOMBRES': Data, 
          'MUJERES': Data1}
    print(pd.DataFrame(dic,index=[departamentos]))


def funcion2():
    adultos_mayores = (doc['edad']>60)
    adultos = (doc["edad"] > 21) & (doc["edad"] <= 60)
    adol = (doc["edad"] > 13) & (doc["edad"] <= 21)
    ninos = (doc["edad"] > 0) & (doc["edad"] <= 13)

    rango = ['Adultos mayores', 'Adultos', 'Adolescentes', 'Ninos']
    muertes = [sum(adultos_mayores), sum(adultos), sum(adol), sum(ninos)]

    fig, ax = plt.subplots()
    ax.set_title('NUMERO DE FALLECIDOS SEGUN SU RANGO DE EDAD')
    ax.set_ylabel('Numero de muertes')
    ax.set_xlabel('Rango de edad')
    plt.bar(rango, muertes, color = ['#F2AAAE','#EEC151','#71C7E3','#AD5B8F'])
    plt.show()


def funcion3():
    DataM = []
    DataF = []
    num = len(departamentos)
    for i in range(num):
        DataM.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['sexo'] == 'M')]).count()))
    for i in range(num):
        DataF.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['sexo'] == 'F')]).count())) 
    x = np.arange(25) 
    longitud = np.arange(len(departamentos))
    width = 0.20
    fig, ax = plt.subplots()
    ax.set_title('NUMERO DE FALLECIDOS EN CADA DEPARTAMENTO SEGUN SU SEXO')
    ax.set_ylabel('Departamentos')
    ax.set_xlabel('Numero de muertes')
    plt.barh(longitud-0.1, DataM, width, color = ['#63B8B3']) 
    plt.barh(longitud+0.1, DataF, width,  color = ['#F9A2BF']) 
    plt.yticks(x, departamentos) 
    plt.legend(["Hombres","Mujeres"])
    plt.show()

def funcion4():
    Data = []
    num = len(departamentos)
    for i in range(num):
        Data.append(sum((doc['dpt_cdc']==departamentos[i])))
    fig, ax = plt.subplots()
    ax.set_title('PORCENTAJE DE FALLECIDOS EN CADA DEPARTAMENTO')
    colores = ['#F2AAAE','#D0AAD1', '#FFE7C1', '#D0E9E9', '#F4C09D','#97D8AE','#50bfc3',
                '#F1E1A6','#638A55','#9BBA74','#CDDB86', '#FCE7B2', '#E1B083', '#e74c3c',
                '#FC9F66','#FAC357','#FAE39C','#B8E0E3','#97C5D8','#84A9CD','#DCCBED',
                 'g', '#FCB7D0','#F07BBB', '#9979C1']
    plt.pie(Data, autopct="%1.2f %%", colors=colores)
    plt.legend(departamentos, bbox_to_anchor = (0.9,0.9))
    plt.show()

def funcion5():
    Data = []
    Data1 = []
    num = len(departamentos)
    for i in range(num):
        Data.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_hospitalizado'] == 1)]).count()))
    fig, ax = plt.subplots()
    colores = ['#F2AAAE','#D0AAD1', '#FFE7C1', '#D0E9E9', '#F4C09D','#97D8AE','#50bfc3',
               '#F1E1A6','#638A55','#9BBA74','#CDDB86', '#FCE7B2', '#E1B083', '#e74c3c',
               '#FC9F66','#FAC357','#FAE39C','#B8E0E3','#97C5D8','#84A9CD','#DCCBED',
                'g', '#FCB7D0','#F07BBB', '#9979C1']
    ax.pie(Data, autopct="%1.2f %%", colors = colores)
    ax.set_title('PORCENTAJE DE FALLECIDOS QUE FUERON HOSPITALIZADOS EN CADA DEPARTAMENTO')
    plt.legend(departamentos, bbox_to_anchor = (0.9,0.9))
    plt.show()

def funcion6():
    Data = []
    num = len(departamentos)
    for i in range(num):
        Data.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['con_ventilacion'] == 1)]).count()))
    fig, ax = plt.subplots()
    ax.set_title('NUMERO DE HOSPITALIZADOS QUE NECESITARON VENTILACION EN CADA DEPARTAMENTO')
    ax.set_ylabel('Departamentos')
    ax.set_xlabel('Numero de hospitalizados que necesitaron ventilacion')
    colores = ['#F2AAAE','#D0AAD1', '#FFE7C1', '#D0E9E9', '#F4C09D','#97D8AE','#50bfc3',
               '#F1E1A6','#638A55','#9BBA74','#CDDB86', '#FCE7B2', '#E1B083', '#e74c3c',
                '#FC9F66','#FAC357','#FAE39C','#B8E0E3','#97C5D8','#84A9CD','#DCCBED',
                'g', '#FCB7D0','#F07BBB', '#9979C1']
    plt.barh(departamentos,Data, color = colores)
    plt.show()

def funcion7():
    clinico = (doc['criterio_fallecido']=='Criterio clinico')
    epi = (doc['criterio_fallecido']=='Criterio nexo epidemiologico')
    sin = (doc['criterio_fallecido']=='Criterio SINADEF')
    rad = (doc['criterio_fallecido']=='Criterio radiologico')
    viro = (doc['criterio_fallecido']=='Criterio virologico')
    inv = (doc['criterio_fallecido']=='Criterio investigacion Epidemiologica')
    sero = (doc['criterio_fallecido']=='Criterio serologico')
    nombres = ['Clinico','Nexo epidemiologico','SINADEF','Radiologico','Virologico',
               'Inv. Epidemiologica','Serologico']
    muertes = [sum(clinico),sum(epi),sum(sin),sum(rad),sum(viro),sum(inv),sum(sero)]
    fig, ax = plt.subplots()
    ax.set_title('NUMERO DE FALLECIDOS SEGUN CADA CRITERIO DE FALLECIMIENTO')
    ax.set_ylabel('Criterios')
    ax.set_xlabel('Numero de muertes')
    colores = ['#B3DFEC', '#B9C0EA', '#E8A5CC', '#F282A7', '#F0725C', '#F6AC5A', '#9ADBC5']
    plt.barh(nombres,muertes, color = colores)
    plt.show()

def funcion8():
    Data = []
    clinico = (doc['criterio_fallecido']=='Criterio clinico')
    epi = (doc['criterio_fallecido']=='Criterio nexo epidemiologico')
    sin = (doc['criterio_fallecido']=='Criterio SINADEF')
    rad = (doc['criterio_fallecido']=='Criterio radiologico')
    viro = (doc['criterio_fallecido']=='Criterio virologico')
    inv = (doc['criterio_fallecido']=='Criterio investigacion Epidemiologica')
    sero = (doc['criterio_fallecido']=='Criterio serologico')
    nombres = ['Criterio clinico','Criterio nexo epidemiologico','Criterio SINADEF','Criterio radiologico','Criterio virologico',
               'Criterio investigacion Epidemiologica','Criterio serologico']
    Data.append(sum(clinico))
    Data.append(sum(epi))
    Data.append(sum(sin))
    Data.append(sum(rad))
    Data.append(sum(viro))
    Data.append(sum(inv))
    Data.append(sum(sero))
    fig, ax = plt.subplots()
    colores = ['#B3DFEC', '#B9C0EA', '#E8A5CC', '#F282A7', '#F0725C', '#F6AC5A', '#9ADBC5']
    ax.pie(Data, autopct="%2.2f %%", colors = colores)
    ax.set_title('PORCENTAJE DE FALLECIDOS SEGUN CADA CRITERIO DE FALLECIMIENTO')
    plt.legend(nombres, bbox_to_anchor = (0.9,0.9))
    plt.show()

def funcion9():
    fab1_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 60)]['fabricante_dosis1'])
    fab1_adult1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 21) & (doc['edad'] <= 60)]['fabricante_dosis1'])
    fab1_adol1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 13) & (doc['edad'] <= 21)]['fabricante_dosis1'])
    fab1_n1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['edad'] > 0) & (doc['edad'] <= 13)]['fabricante_dosis1'])
    fab2_am1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 60)]['fabricante_dosis1'])
    fab2_adult1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 21) & (doc['edad'] <= 60)]['fabricante_dosis1'])
    fab2_adol1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 13) & (doc['edad'] <= 21)]['fabricante_dosis1'])
    fab2_n1 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['edad'] > 0) & (doc['edad'] <= 13)]['fabricante_dosis1'])
    fab3_am1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 60)]['fabricante_dosis1'])
    fab3_adult1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 21) & (doc['edad'] <= 60)]['fabricante_dosis1'])
    fab3_adol1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 13) & (doc['edad'] <= 21)]['fabricante_dosis1'])
    fab3_n1 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['edad'] > 0) & (doc['edad'] <= 13)]['fabricante_dosis1'])
    rango = ["Adultos Mayores","Adultos","Adolescentes","Ninos"]
    x = np.arange(3) 
    nombres = ['PFIZER','SINOPHARM','ASTRAZENECA']
    ADM = [fab1_am1.count(),fab2_am1.count(),fab3_am1.count()]
    AD = [fab1_adult1.count(),fab2_adult1.count(),fab3_adult1.count()]
    Adol = [fab1_adol1.count(),fab2_adol1.count(),fab3_adol1.count()]
    Ninos = [fab1_n1.count(),fab2_n1.count(),fab3_n1.count()]
    longitud = np.arange(len(nombres))
    width = 0.20
    fig, ax = plt.subplots()
    ax.set_title('NUMERO DE FALLECIDOS QUE ESTABAN VACUNADOS CON X TIPO DE VACUNA SEGUN SU RANGO DE EDAD')
    ax.set_ylabel('Numero de muertes')
    ax.set_xlabel('Fabricante de la vacuna')
    plt.bar(longitud-0.2,ADM, width, color = ['#F2AAAE']) 
    plt.bar(longitud-0.1,AD, width, color = ['#EEC151']) 
    plt.bar(longitud+0.1,Adol, width, color = ['#71C7E3']) 
    plt.bar(longitud+0.2,Ninos, width, color = ['#AD5B8F']) 
    plt.xticks(x, nombres)
    plt.legend(["Adultos Mayores","Adultos","Adolescentes","Ninos"])
    plt.show()

def funcion10():
    fab1_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab1_am2 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab1_am3 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'M')])
    fab2_am1 = (doc[(doc['fabricante_dosis1'] == 'PFIZER') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    fab2_am2 = (doc[(doc['fabricante_dosis1'] == 'SINOPHARM') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    fab2_am3 = (doc[(doc['fabricante_dosis1'] == 'ASTRAZENECA') & (doc['flag_vacuna'] == 1) & (doc['sexo'] == 'F')])
    M1 = sum(fab1_am1.count())
    M2 = sum(fab1_am2.count())
    M3 = sum(fab1_am3.count())
    F1 = sum(fab2_am1.count())
    F2 = sum(fab2_am2.count())
    F3 = sum(fab2_am3.count())
    x = np.arange(3) 
    nombres = ['PFIZER', 'SINOPHARM', 'ASTRAZENECA']
    datosM = [M1,M2,M3]
    datosF = [F1,F2,F3]
    longitud = np.arange(len(nombres))
    width = 0.30
    fig, ax = plt.subplots()
    ax.set_title('NUMERO Y SEXO DE FALLECIDOS QUE FUERON VACUNADOS\n CON 1 DOSIS DE X TIPO DE VACUNA')
    ax.set_ylabel('Numero de muertes')
    ax.set_xlabel('Fabricante de la vacuna')
    plt.bar(longitud-0.1, datosM, width, color = ['#63B8B3']) 
    plt.bar(longitud+0.1, datosF, width,  color = ['#F9A2BF']) 
    plt.xticks(x, nombres) 
    plt.legend(["Hombres","Mujeres"])
    plt.show()

def funcion11():
    DataM = []
    DataF = []
    num = len(departamentos)
    for i in range(num):
        DataM.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_vacuna'] == 2) & (doc['sexo'] == 'M')]).count()))
    for i in range(num):
        DataF.append(sum((doc[(doc['dpt_cdc'] == departamentos[i]) & (doc['flag_vacuna'] == 2) & (doc['sexo'] == 'F')]).count()))
    x = np.arange(25) 
    longitud = np.arange(len(departamentos))
    width = 0.20
    fig, ax = plt.subplots()
    ax.set_title('NUMERO Y SEXO DE FALLECIDOS QUE FUERON VACUNADOS CON 2 DOSIS EN CADA DEPARTAMENTO')
    ax.set_ylabel('Departamentos')
    ax.set_xlabel('Numero de muertes')
    plt.barh(longitud-0.1, DataM, width, color = ['#63B8B3']) 
    plt.barh(longitud+0.1, DataF, width,   color = ['#F9A2BF']) 
    plt.yticks(x, departamentos) 
    plt.legend(["Hombres","Mujeres"])
    plt.show()



opcion = ' '
opcion_ = ' '
while True:
    system("cls")
    Amenu()
    print()
    opcion = input("Ingrese la opcion escogida: ")
    if opcion == '1':
        system("cls")
        Afuncion1()
        system("pause")

    if opcion == '2':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion2()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion2()
            system("pause")
        if opcion_=='3':
            system("cls")


    if opcion == '3':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion3()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion3()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '4':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion4()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion4()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '5':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion5()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion5()
            system("pause")
        if opcion_=='3':
            system("cls")


    if opcion == '6':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion6()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion6()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '7':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion7()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion7()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '8':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion8()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion8()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '9':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion9()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion9()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '10':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion10()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion10()
            system("pause")
        if opcion_=='3':
            system("cls")

    if opcion == '11':
        opcion_ = ''
        system("cls")
        while not(opcion_ == '1' or opcion_ == '2' or opcion_ == '3'):
                print("Elija una opcion: ")
                print("1. Tabla")
                print("2. Grafico")
                print("3. Regresar al menu principal")
                opcion_ = input("--> ")
                system("cls")
        if opcion_=='1':
            system("cls")
            Afuncion11()
            system("pause")
        if opcion_=='2':
            system("cls")
            funcion11()
            system("pause")
        if opcion_=='3':
            system("cls")
            
    if opcion == '12':
        break
