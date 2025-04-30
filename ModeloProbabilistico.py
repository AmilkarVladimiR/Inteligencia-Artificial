import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns
import matplotlib.pyplot as plt

# Paso 1: Ingreso de datos
datos = []
print("Ingreso de datos para entrenamiento")
print("Ingresa los datos de consumo de gasolina en base al peso, potencia y tamaño de rueda.")
print("Ejemplo: 1200,100,15,6.5 (peso(kg), potencia(hp), rueda(pulgadas), consumo(L/km))")
print("Escribe 'fin' para terminar el ingreso.\n")

while True:
    entrada = input("Ingresa peso, potencia, rueda, consumo separados por coma: ")
    if entrada.lower() == 'fin':
        break
    try:
        peso, potencia, rueda, consumo = map(float, entrada.split(","))
        datos.append([peso, potencia, rueda, consumo])
    except:
        print("Error: Asegúrate de ingresar 4 valores numéricos separados por coma.")

# Validación mínima
if len(datos) < 5:
    print("\n Se necesitan al menos 5 ejemplos para un modelo más preciso.")
    exit()

# Paso 2: Crear DataFrame
df = pd.DataFrame(datos, columns=["peso", "potencia", "rueda", "consumo"])

# Paso 3: Visualización de correlaciones
print("\n Matriz de correlación entre variables:")
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title("Matriz de correlación")
plt.show()

# Separar variables y etiquetas
X = df[["peso", "potencia", "rueda"]]
y = df["consumo"]

# Paso 4: Escalado de datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Paso 5: División entrenamiento/prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Paso 6: Entrenamiento
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Paso 7: Evaluación del modelo
y_train_pred = modelo.predict(X_train)
y_test_pred = modelo.predict(X_test)

print("\n Evaluación del modelo:")
print(f"🔹 R² Score (Entrenamiento): {r2_score(y_train, y_train_pred):.2f}")
print(f"🔹 R² Score (Prueba): {r2_score(y_test, y_test_pred):.2f}")
print(f"🔹 Error cuadrático medio (Prueba): {mean_squared_error(y_test, y_test_pred):.2f}")

# Paso 8: Mostrar coeficientes
print("\n Modelo entrenado correctamente.")
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")

# Paso 9: Guardar el modelo entrenado y el escalador
joblib.dump(modelo, "modelo_consumo.pkl")
joblib.dump(scaler, "escalador.pkl")
print(" Modelo y escalador guardados como 'modelo_consumo.pkl' y 'escalador.pkl'")

# Paso 10: Predicción nueva
print("\n Ahora puedes predecir el consumo de un nuevo coche.")
peso = float(input("Peso del coche (kg): "))
potencia = float(input("Potencia del coche (hp): "))
rueda = float(input("Tamaño de la rueda (pulgadas): "))

entrada_nueva = [[peso, potencia, rueda]]
entrada_nueva_scaled = scaler.transform(entrada_nueva)
prediccion = modelo.predict(entrada_nueva_scaled)

print(f"\n Predicción: El consumo estimado es de {prediccion[0]:.2f} L/km")
