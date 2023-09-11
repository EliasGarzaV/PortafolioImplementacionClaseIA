# Portafolio de Implementacion
Este es el repositorio de Implementación para la concentración en Inteligencia Artificial Avanzada de Elías Garza Valdés A01284041.
## Entregables
- [Entregable 1: 21/08/2023](Entregables/Entregable1.ipynb) - Este es el notebook en donde esta la implementación manual de una regresion multilinear correspondiente para la etapa 1.

- [Entregable 2: 31/08/2023](Entregables/Entregable2.ipynb) - Este es el notebook en donde esta la implementación con framework de algun modelo visto en clase.

- [Entregable 3: 05/09/2023](Entregables/Entregable3.ipynb) - Aqui viene el analisis sobre el desempeño de los modelos. 

- [Entregable Fianal: 11/09/2023](Entregables/EntregableFinal.ipynb) - Este es el resultado final con la concatenación de las entregas con todas las correcciones hechas. 

## Estructura del Repositorio 
```
📦PortafolioImplementacionClaseIA
 ┣ 📂Data
 ┃ ┣ 📜diabetes-dataset.csv
 ┃ ┗ 📜salary.csv
 ┣ 📂Entregables
 ┃ ┗ 📜Entregable1.ipynb
 ┣ 📂functions
 ┃ ┣ 📜evaluation.py
 ┃ ┗ 📜Multilinear_regression.py
 ┗ 📜README.md
```

## Sobre el problema y los datos

Tenemos un  problema de regresión con datos de profesores en una universidad con los cuales vamos a intentar predecir su salario. Tenemos un rango de variables como lo son su puesto actual, la materia que imparten, la cantidad de años desde que obtuvieron su doctorado, los años que llevan trabajando y su sexo. Asimismo, tambien tenemos la columna del salario de profesores para hacer la prueba. Este dataset lo pueden encontrar en [Datos_Salariales](Data/salary.csv).

## Modelado

En cuanto al modelo utilizado tenemos varias pruebas. Inicialmente haremos una regresión lineal tanto de la forma optima con mínimos cuadrados (el dataset no es muy grande asi que en este caso es la mejor opción ya que tenemos suficiente memoria para los cálculos) como a traves de un optimizador el cual intentará ir moviendo los valores de los coeficientes para llegar a un óptimo local.  

Posteriormente veremos que tal funciona otro modelo como arboles de regreción o xgboost. 

## Sobre los cambios y correcciones

Los siguientes son las correcciones que se le han aplicado a este documento a partir de la retroalimentación del profesor:

 - Añadir contexto sobre la base de datos y link en el `README.md` de este repositorio.
 - Añadir descripción del modelo utilizado en el `README:md`
 - El reporte ahora incluye la descripción de los datos asi como el nombre. 
 - Tenemos ahora el reporte generado de exploración de datos. 
 - Al inicio del reporte tenemos la explicación de que es un problema de regresión. 
 - Ahora se añade los resultados del conjunto de entrenamiento además del de pruebas.
 - El modelo ahora contiene pruebas ademas de las de entrenamiento (el testing al final)
 - Ahora se hace la comparación con residuales y la diferencia entre los resultados. 
 - Ahora se varian diversos hiperparámetros al momento de generar las pruebas. 


