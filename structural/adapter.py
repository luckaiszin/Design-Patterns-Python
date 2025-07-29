"""
Adapter is a structural design pattern that allows objects with incompatible interfaces to collaborate.

O padrão Adapter é utilizado quando você quer que objetos com interfaces incompatíveis possam trabalhar juntos.

"""

class OldSystem:
    def request(self):
        return "Requisição no formato esperado."


class NewSystem:
    def specific_request(self):
        return "Requisição do novo sistema (formato incompatível)."

class Adapter:
    def __init__(self, new_system):
        self.new_system = new_system

    def request(self):
        # Adaptando a chamada
        return f"Adaptado: {self.new_system.specific_request()}"


old = OldSystem()
print(old.request())  # Saída normal

new = NewSystem()
adapted = Adapter(new)
print(adapted.request())  # Agora funciona com interface esperada
