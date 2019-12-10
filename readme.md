# Generador de sesiones
Este programa genera las sesiones que se dictarán en una asignatura en un rango de tiempo.

Por ejemplo, si la asignatura programación se dicta desde el 1 de agosto de 2020, termina el 30 de noviembre de 2020 y se dicta los días lunes, miercoles y viernes, el programa se ejecutará:
```
python programa.py -a programacion.csv -fi 2020-08-01 -ff 2020-11-30 -d LU MI VI
```

Este comando generará el archivo `programacion.csv` con las sesiones a dictar.
Si alguna fecha es festivo, se marcará en el archivo generado.
