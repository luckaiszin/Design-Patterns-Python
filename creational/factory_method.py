"""
Factory Method is a creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created.

Uma fábrica que decide qual "produto" criar.

"""

### Problema:
# Imagine que você está desenvolvendo um sistema para uma empresa de logística. A empresa 
# utiliza diferentes meios de transporte para entregar as mercadorias: caminhões e navios.

from abc import ABC, abstractmethod

# Interface do produto

class Transport(ABC):

    """
    A interface Transport declara a operação comum a todos os tipos de transporte.
    """

    @abstractmethod
    def deliver(self, id_package: str) -> str:
        pass

# Produtos Concretos
class Truck(Transport):

    """
    O Caminhão implementa a interface Transport para entregas terrestres.
    """

    def deliver(self, id_package: str) -> str:
        return f"Entregando pacote {id_package} por caminhão/via terrestre"
    
class Ship(Transport):

    """
    O Navio implementa a interface Transport para entregas marítimas.
    """

    def deliver(self, id_package: str) -> str:
        return f"Entregando pacote {id_package} por navio/via marítima"
    
class Airplane(Transport):

    """
    O Avião implementa a interface Transport para entregas aéreas.
    """

    def deliver(self, id_package: str) -> str:
        return f"Entregando pacote {id_package} por avião/via aérea"
    
# Creator class
# Ela declara o factory method que deve retornar um objeto de uma classe Transport.

class Logistic(ABC):

    """
    A classe Logistics declara o factory method que retorna um objeto da classe Transport.
    As subclasses de Logistics fornecerão a implementação deste método.
    """

    @abstractmethod
    def create_transport(self) -> Transport:
        """Este é o nosso Factory Method."""
        pass

    def plan_delivery(self, id_package: str) -> str:
        """
        O código principal da fábrica. Note que ele não depende das classes
        concretas de transporte. Ele funciona através da interface Transport.
        """
        transport = self.create_transport()
        result = transport.deliver(id_package)
        return result


# Fábricas concretas

class RoadLogistic(Logistic):

    """
    A fábrica de logística terrestre cria objetos do tipo Truck.
    """

    def create_transport(self) -> Transport:
        return Truck()
    

class SeaLogistic(Logistic):

    """
    A fábrica de logística marítima cria objetos do tipo Ship.
    """

    def create_transport(self) -> Transport:
        return Ship()

class FlyLogistic(Logistic):

    """
    A fábrica de logística aérea cria objetos do tipo Airplane.
    """

    def create_transport(self) -> Transport:
        return Airplane()

# Cliente

# O código cliente 
# decide qual tipo de logística é necessária e instancia a fábrica correspondente. 
# A partir daí, ele interage apenas com a interface da classe Logistics, sem nunca se acoplar diretamente às classes Truck ou Ship.

def client_code(logistics_factory: Logistic, package: str): ## o cliente não se preocupa com o tipo de transporte, apenas com a fábrica
    """
    O código cliente funciona com uma instância de uma subclasse concreta de
    Logistics, embora não saiba qual é. Ele age sobre a interface da fábrica.
    """
    print(f"Cliente: Não conheço a classe da fábrica, mas ela funciona.")
    delivery_result = logistics_factory.plan_delivery(package)
    print(f"Resultado: {delivery_result}\n")

if __name__ == "__main__":
    # A configuração da aplicação pode escolher a fábrica a ser usada.
    # Isso pode vir de um arquivo de configuração, da interface do usuário, etc.
    print("Iniciando a primeira entrega...")

    DELIVERY_TYPE = input("Escolha o tipo de entrega(terrestre, maritima, aerea): ") 

    if DELIVERY_TYPE == "terrestre":
        factory = RoadLogistic()
    elif DELIVERY_TYPE == "maritima":
        factory = SeaLogistic()
    elif DELIVERY_TYPE == "aerea":
        factory = FlyLogistic()
    else:
        raise ValueError("Tipo de logística desconhecido.")

    client_code(factory, "Caixa de Eletrônicos")

    # Trocando a fábrica facilmente
    print("Iniciando a segunda entrega...")
    client_code(RoadLogistic(), "Móveis para Escritório")


"""
RESUMO: o Cliente não se preocupa em instanciar o produto, apenas escolher o tipo de fábrica.
"""