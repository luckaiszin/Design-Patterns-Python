"""
Observer is a behavioral design pattern that allows objects to observe and respond to events happening in other objects.
(ex: um sistema de notificações)

O padrão Observer é utilizado quando você quer que um objeto (o sujeito) notifique automaticamente outros objetos (observadores) sobre mudanças em seu estado.
"""

from abc import ABC, abstractmethod

# Sujeito (Subject)
class WeatherStation:
    def __init__(self):
        self._observers = []  # Lista de observadores
        self._temperature = None

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def set_temperature(self, temp):
        self._temperature = temp
        self._notify_observers()

    def _notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)

# Observer (interface comum)
class Observer:
    """
    A interface Observer declara o método update, que é usado pelo sujeito para notificar os observadores.
    """

    @abstractmethod
    def update(self, temperature):
        pass

# Observadores concretos
class TemperatureDisplay(Observer):
    """
    O Display de temperatura implementa a interface Observer para exibir a temperatura atual.
    """

    def update(self, temperature):
        print(f"[Display] Temperatura atual: {temperature}°C")

class TemperatureLogger(Observer):
    """
    O Logger de temperatura implementa a interface Observer para registrar a temperatura em um arquivo.
    """

    def update(self, temperature):
        print(f"[Logger] Temperatura registrada: {temperature}°C")

# Uso
if __name__ == "__main__":
    station = WeatherStation()
    display = TemperatureDisplay()
    logger = TemperatureLogger()

    station.add_observer(display)
    station.add_observer(logger)

    station.set_temperature(25)
    station.set_temperature(30)
