
class Node:     #Criação da classe do Nó
  def __init__(self,data) -> None:                                                  # none indica pra não esperar retorno do classe
    self.data = data    #recebe o valor do data
    self.next = None    #Indica que o proximo valor sempre será nulo
