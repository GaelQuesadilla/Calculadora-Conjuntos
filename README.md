# Documentación del Generador de Conjuntos

Este programa permite generar conjuntos numéricos a partir de funciones matemáticas, listas predefinidas o combinaciones de ambas, con la posibilidad de trabajar en espacios unidimensionales (R¹) y bidimensionales (R²). A continuación, se explica su funcionamiento y las opciones disponibles.

---

## 1. Descripción General

El programa cuenta con dos secciones principales: **Conjunto A** y **Conjunto B**, cada una con su propio generador. Una vez generados, se pueden realizar operaciones de conjuntos tales como unión, diferencia, intersección, diferencia simétrica, disyuntiva y producto simétrico.

---

## 2. Parámetros del Generador

Cada generador tiene los siguientes parámetros configurables:

- **f(x):** Expresión que define la función a evaluar.

  - Puede ser una función matemática como `x`, `x**2`, `x**3`, etc.
  - Puede ser una lista de valores definida explícitamente: `[13,6,7,3]`.
  - Puede ser una función de dos variables para R² separada por coma: `x, x**2`.

- **x_0 (mínimo):** Valor entero inicial de la variable `x`.
- **x_f (máximo):** Valor entero final de la variable `x`.
- **p (paso):** Incremento entero para cada valor de `x`.

---

## 3. Reglas de Generación

### 3.1. Funciones de una variable (R¹)

Si introduces una función como `x`, `x**2` o similar:

- Se generará un conjunto evaluando la función para cada valor de `x` desde `x_0` hasta `x_f`, avanzando de acuerdo con `p`.
- Ejemplo:
  - **Entrada:**
    ```
    f(x) = x**2
    x_0 = 0
    x_f = 5
    p = 1
    ```
  - **Salida:** `{0, 1, 4, 9, 16, 25}`

### 3.2. Listas explícitas

Si introduces una lista como `f(x) = [13,6,7,3]`, el programa generará el conjunto **ignorando los valores de `x_0`, `x_f` y `p`**, utilizando directamente los valores de la lista.

### 3.3. Funciones de dos variables (R²)

Para generar puntos en el plano (pares ordenados), se pueden ingresar dos funciones separadas por coma. Por ejemplo:

- **Entrada:**

```
f(x) = x, x**2
x_0 = -2
x_f = 2
p = 1
```

- **Salida:** `{(-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4)}`

---

## 4. Operaciones de Conjuntos

Una vez generados los conjuntos A y B, se pueden aplicar las siguientes operaciones:

- **Unión (A ∪ B):** Combina todos los elementos de ambos conjuntos sin duplicados.
- **Diferencia (A − B):** Devuelve los elementos que están en A pero no en B.
- **Intersección (A ∩ B):** Devuelve los elementos que están en ambos conjuntos.
- **Diferencia simétrica:** Elementos que están en A o B pero no en ambos.
- **Disyuntiva:** Combinación lógica basada en las diferencias (depende de la implementación lógica definida en el programa).
- **Producto simétrico:** Calcula el producto cartesiano con condiciones especiales según la configuración.

---

## 5. Notas Importantes

- Todos los valores de `x_0`, `x_f` y `p` **deben ser enteros**.
- Si se usa una lista explícita, los valores de rango y paso serán ignorados.
- Las funciones deben ser expresadas en sintaxis de Python (`x**2` para potencias, no `x^2`).
- Para R², asegúrate de separar las dos funciones con una coma.

---

## 6. Ejemplos de Uso

1. **Generar números naturales:**

```
f(x) = x
x_0 = 1
x_f = 5
p = 1
```

**Resultado:** `{1, 2, 3, 4, 5}`

2. **Generar cuadrados perfectos:**

```
f(x) = x**2
x_0 = 0
x_f = 4
p = 1
```

**Resultado:** `{0, 1, 4, 9, 16}`

3. **Usar una lista personalizada:**

**Resultado:** `{0, 1, 4, 9, 16}`

3. **Usar una lista personalizada:**

f(x) = [10, 20, 30]

**Resultado:** `{10, 20, 30}`

4. **Generar puntos de una parábola en R²:**

```
f(x) = x, x**2
x_0 = -3
x_f = 3
p = 1
```

**Resultado:** `{(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)}`

---

## 7. Posibles Errores y Recomendaciones

- **Error de sintaxis:** Verifica que la función esté escrita correctamente (`x**2` en lugar de `x^2`).
- **Rangos vacíos:** Si `x_0 > x_f` y `p` es positivo, no se generará ningún valor.
- **Paso cero:** No se permite `p = 0`, ya que causaría un bucle infinito.

---

## 8. Conclusión

Este programa es una herramienta flexible para la generación y manipulación de conjuntos numéricos y puntos en el plano. Permite crear datos a partir de funciones, listas o combinaciones de ambas, y aplicar operaciones de conjuntos de forma sencilla e intuitiva.
