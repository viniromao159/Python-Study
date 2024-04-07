from datetime import date

def voto(ano):
    idade = date.today().year - ano
    if idade < 16:
        return f"Com {idade} anos: VOTO NEGADO"
    elif idade < 18:
        return f"Com {idade} anos: VOTO OPCIONAL"
    elif idade < 65:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    else:
        return f"Com {idade} anos: VOTO OPCIONAL"

print(voto(1955))