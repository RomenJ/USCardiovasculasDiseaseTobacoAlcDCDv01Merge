import pandas as pd
#fuente: https://nccd.cdc.gov/cdi/rdPage.aspx?rdReport=DPH_CDI.ExploreByTopic&islTopic=ART&islYear=9999&go=GO
try:
    df2=pd.read_csv('MortalityFromTotalCardiovascularDiseases.csv',  sep=';')
    df3=pd.read_csv('Tobacco1.csv', sep=';')
    df4=pd.read_csv('HeavyDrinking.csv', sep=';')

#    print(df2.info())
    print('+++++')
  #  print(df2.describe())


    #dfMergeado = dfMergeado[campos_deseados]

    #df3=df2[campos_deseados]
    print("Imprimir df2", df2)
    print("´´´........´´´´´´")
    print("Imprimir df3", df3)
    dfMergeado = df2.merge(df3, on='LocationDesc', how="outer", suffixes=('_mort', '_tabac'))
    campos_deseados = [
         'LocationDesc',
        'Question_mort',
        'Data_Value_mort',
        'Question_tabac',
        'Data_Value_tabac'
    ]
    dfMergeado = dfMergeado[campos_deseados]

    print(dfMergeado)
    dfMergeado2 = dfMergeado.merge(df4, on='LocationDesc', how="outer", suffixes=('_mortTab', '_alcho'))
    campos_deseados2 = [
    'LocationDesc',
    'Question_mort',
    'Data_Value_mort',
    'Question_tabac',
    'Data_Value_tabac',
    'Data_Value',
    'Question'
]
    dfMergeado2 = dfMergeado2[campos_deseados2]

    # Agregar la nueva columna Data_Value_Alcohol
    dfMergeado2['Data_Value_Alcohol'] = dfMergeado2['Data_Value']
    dfMergeado2['Question_Alcohol'] = dfMergeado2['Question']
    # Puedes eliminar la columna Data_Value_alcho si lo deseas
    dfMergeado2 = dfMergeado2.drop('Data_Value', axis=1)
    dfMergeado2 = dfMergeado2.drop('Question', axis=1)
    dfMergeado2.to_csv('nuevoDataFrameCombi4.csv', index=False)

    
    print('Se ha creado el archivo nuevoDataFrame.csv')


    """""

    
    df2=pd.read_csv('Tobacco1.csv')
    dfMergeado = df1.merge(df2, on='LocationDesc', how="outer")
    # Selecciona solo los campos deseados en el DataFrame resultante
    campos_deseados = [
    'LocationDesc',
    'Data_Value',
]


    dfMergeado = dfMergeado[campos_deseados]
    # Guarda el DataFrame en un archivo CSV
    dfMergeado.to_csv('PruebaaCorrAnalsisDrink.csv', index=False)
    print('Se ha creado el archivo PRUEBADFFabiLeadsRentas.csv')
"""""""""
except Exception as e:
    print(f"Error en tobacco: {e}")
