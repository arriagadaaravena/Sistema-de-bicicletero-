# 🚲 Sistema de Bicicletero

Programa en Python que calcula el valor final del arriendo mensual de un bicicletero y de un candado, aplicando descuentos según la cantidad de días de uso y si la persona es estudiante.

## 🧩 Situación inicial

Un bicicletero universitario ofrece arriendo mensual de espacio para bicicletas y candados de seguridad, con descuentos diferenciados según el tipo de usuario (estudiante o no) y la cantidad de días de uso durante el mes, para incentivar el uso frecuente y beneficiar a la comunidad estudiantil.

## 🚀 Funcionalidades implementadas

- **Ingreso validado de datos**: solicita los días de uso y si la persona es estudiante (`S`/`N`), validando que los días sean mayores a 0 y que la respuesta sea una opción válida antes de calcular.
- **Descuento del bicicletero por tramos**: aplica distintos porcentajes de descuento combinando dos factores — días de uso (10-19 días, 20 o más días) y si la persona es estudiante o no.
- **Descuento del candado**: los estudiantes obtienen un descuento base adicional, más un descuento extra si usaron el bicicletero 15 días o más.
- **Resumen final**: muestra el valor final a pagar por el bicicletero y por el candado, ya con los descuentos aplicados.

## 🛠️ Tecnologías utilizadas

- Python 3

## 📂 Estructura del proyecto

Sistema-de-bicicletero/
└── bicicletero.py # Lógica completa: validación, cálculo de descuentos y resumen

## ▶️ Cómo ejecutarlo

1. Clona este repositorio o descarga el archivo.
2. Ejecuta el script:
```bash
   python bicicletero.py
```
3. Ingresa la cantidad de días que usaste el bicicletero y si eres estudiante (`S` o `N`).
4. Revisa el resumen con el valor final del bicicletero y del candado.

## 🧠 Decisiones de diseño

- **Validación combinada con `and`**: se exige que los días sean mayores a 0 **y** que la respuesta de estudiante sea una opción válida (`s` o `n`) antes de continuar, evitando que datos parcialmente incorrectos generen cálculos sin sentido.
- **Constantes en mayúsculas (`BICICLETERO_MENSUAL`, `CANDADO`)**: los valores base de arriendo se definieron como constantes para separarlos claramente de los datos ingresados por el usuario.
- **Descuentos combinados por tramos**: el descuento del bicicletero depende de dos variables a la vez (días de uso y tipo de persona), por lo que se estructuró con condicionales anidados para cubrir todas las combinaciones posibles sin duplicar lógica innecesaria.
- **Descuento adicional del candado por días de uso**: se separó el descuento base por ser estudiante del descuento extra por uso prolongado (15+ días), para que cada beneficio se pueda ajustar de forma independiente en el futuro.

## 👤 Autora

Abigail Betsabé Arriagada Aravena — Proyecto realizado durante la formación en Python de la asignatura Fundamentos de la programación (Duoc UC).