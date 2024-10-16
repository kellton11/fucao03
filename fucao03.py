# Crie duas funções:
# - calcular_area_base, que recebe o raio de um círculo e retorna sua área.

def calcular_area_base():
    r = float(input("digite o raio do círculo: "))
    f = r*r*3.14
    return f

area = calcular_area_base()
print(area)
# - calcular_volume_cilindro, que utiliza a função calcular_area_base para calcular o volume de um cilindro dado o raio e a altura.

def calcular_volume_cilindro():
    al = float(input("digite a altura do cilindro: "))
    volume = area*al
    return volume 

volume = calcular_volume_cilindro()
print(volume)
