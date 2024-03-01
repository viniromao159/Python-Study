class Triangulo:

    def __init__(self) -> None:
        self.__ladoA = float(input("Digite o valor do lado A: "))
        self.__ladoB = float(input("Digite o valor do lado B: "))
        self.__ladoC = float(input("Digite o valor do lado C: "))

    def calcularPerimetro (self):
        print("Calculando Perimetro...")
        return self.__ladoA + self.__ladoB + self.__ladoC

    def get_ladoMaior(self):
        if self.__ladoA > self.__ladoB and self.__ladoC:
            return f"Lado A é o maior: {self.__ladoA}"
        elif self.__ladoB > self.__ladoA and self.__ladoC:
            return f"Lado B é o maior: {self.__ladoB}"
        elif self.__ladoC > self.__ladoA and self.__ladoB:
            return f"Lado C é o maior: {self.__ladoC}"
        else:
            return f"Lados iguais -> {self.__ladoA} - {self.__ladoC} - {self.__ladoC}"
