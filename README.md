🎨 Padrões de Projeto em Python
Um repositório dedicado à implementação e ao estudo dos padrões de projeto clássicos (GoF - Gang of Four) utilizando a linguagem Python. O objetivo é fornecer exemplos claros, práticos e "pythônicos" de cada padrão.

📖 Sobre o Projeto
Este projeto nasceu da necessidade de ter um local centralizado com exemplos de fácil compreensão dos 23 padrões de projeto do livro "Design Patterns: Elements of Reusable Object-Oriented Software". Cada padrão é implementado em seu próprio arquivo, com comentários explicando a estrutura, os participantes e o problema que ele resolve.

Este repositório é ideal para:

Estudantes que estão aprendendo sobre arquitetura de software e padrões de projeto.

Desenvolvedores que desejam revisar um padrão específico antes de aplicá-lo.

Qualquer pessoa curiosa sobre como os padrões GoF se manifestam em Python.

🏛️ O que são Padrões de Projeto?
Em engenharia de software, um padrão de projeto (Design Pattern) é uma solução geral e reutilizável para um problema que ocorre com frequência dentro de um determinado contexto no projeto de software. Não se trata de um código finalizado que pode ser transformado diretamente em código, mas sim de uma descrição ou modelo de como resolver um problema que pode ser usado em muitas situações diferentes.

Os padrões são divididos em três categorias principais:

Criacionais: Padrões que abstraem o processo de instanciação de objetos.

Estruturais: Padrões que lidam com a composição de classes e objetos.

Comportamentais: Padrões que se concentram na comunicação e na atribuição de responsabilidades entre objetos.

📂 Padrões Implementados
Aqui está a lista dos 23 padrões de projeto GoF, separados por categoria.

🔷 Padrões Criacionais (Creational Patterns)
Padrões que fornecem mecanismos de criação de objetos, aumentando a flexibilidade e a reutilização do código existente.

Factory Method: Define uma interface para criar um objeto, mas deixa as subclasses decidirem qual classe instanciar.

Abstract Factory: Fornece uma interface para criar famílias de objetos relacionados ou dependentes sem especificar suas classes concretas.

Builder: Separa a construção de um objeto complexo de sua representação, permitindo que o mesmo processo de construção crie diferentes representações.

Singleton: Garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global a ela.

Prototype: Permite a criação de novos objetos através da cópia de uma instância existente.

🔶 Padrões Estruturais (Structural Patterns)
Padrões que explicam como montar objetos e classes em estruturas maiores, mantendo-as flexíveis e eficientes.

Adapter: Permite que interfaces incompatíveis trabalhem juntas.

Bridge: Desacopla uma abstração de sua implementação, para que as duas possam variar independentemente.

Composite: Compõe objetos em estruturas de árvore para representar hierarquias parte-todo.

Decorator: Adiciona novas funcionalidades a um objeto dinamicamente, envolvendo-o com um objeto "decorador".

Facade: Fornece uma interface simplificada para um sistema complexo de classes.

Flyweight: Minimiza o uso de memória ou custo computacional compartilhando o máximo possível com objetos similares.

Proxy: Fornece um substituto ou um espaço reservado para outro objeto para controlar o acesso a ele.

🔶 Padrões Comportamentais (Behavioral Patterns)
Padrões que se preocupam com algoritmos e a atribuição de responsabilidades entre os objetos.

Chain of Responsibility: Passa uma solicitação ao longo de uma cadeia de manipuladores.

Command: Encapsula uma solicitação como um objeto, permitindo parametrizar clientes com diferentes solicitações.

Iterator: Fornece uma maneira de acessar os elementos de um objeto agregado sequencialmente sem expor sua representação subjacente.

Mediator: Define um objeto que encapsula como um conjunto de objetos interage, promovendo o baixo acoplamento.

Memento: Captura e externaliza o estado interno de um objeto para que ele possa ser restaurado posteriormente.

Observer: Define uma dependência um-para-muitos entre objetos, de modo que, quando um objeto muda de estado, todos os seus dependentes são notificados.

State: Permite que um objeto altere seu comportamento quando seu estado interno muda.

Strategy: Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis.

Template Method: Define o esqueleto de um algoritmo em uma operação, adiando algumas etapas para as subclasses.

Visitor: Permite adicionar novas operações a uma estrutura de objetos sem modificar as classes dos elementos sobre os quais opera.

Interpreter: Dado uma linguagem, define uma representação para sua gramática junto com um interpretador que usa a representação para interpretar sentenças na linguagem.