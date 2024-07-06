from requests import request


def calculadora():

    num1 = float(input("Ingrese el primer n�mero: "))
    num2 = float(input("Ingrese el segundo n�mero: "))
    print("Seleccione la operaci�n:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicaci�n")
    print("4. Divisi�n")
    operacion = input("Ingrese el n�mero de la operaci�n (1/2/3/4): ")
    if operacion == '1':
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    elif operacion == '2':
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    elif operacion == '3':
        resultado = num1 * num2
        print(f"El resultado de la multiplicaci�n es: {resultado}")
    elif operacion == '4':
        if num2 != 0:
            resultado = num1 / num2
            print(f"El resultado de la divisi�n es: {resultado}")  
    else:
        print("Operaci�n no v�lida")




using (request)
def obtener_genero(nombre):
  
    url = f"https://api.agify.io/?name={nombre}"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if 'age' in datos:
            return datos['age']
        else:
            return "No se pudo determinar el g�nero."
    else:
        return "Error al realizar la solicitud."

def main():
    nombre = input("Ingrese un nombre: ")
    genero = obtener_genero(nombre)
    print(f"El g�nero del nombre {nombre} es: {genero}")
    calculadora()

