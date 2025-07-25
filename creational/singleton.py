"""
Singleton is a design pattern that ensures a class has only one instance and provides a global point of access to it.
"""

### Problema:
# Logger, Imagine que você está desenvolvendo um sistema grande — por exemplo, um sistema bancário com múltiplos módulos: autenticação, transações, relatórios, etc.
# Cada parte do sistema precisa registrar mensagens em um arquivo de log para fins de auditoria e depuração. 
# Se cada módulo criasse sua própria instância da classe Logger, isso causaria problemas como:
# Concorrência na escrita do arquivo
# Duplicação de recursos
# Logs perdidos ou desorganizados

class Logger:

    _instance = None

    def __init__(self):
        self.some_attribute = None
        self.history = []

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


logger1 = Logger.instance()
logger2 = Logger.instance()

print(logger1 is logger2)

logger1.history.append("teste")
logger2.history.append("teste2")

print(logger2.history)
