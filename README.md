# SME0610-ProgMat


## Sumário
1. [Guia para pyscipopt](#guia-para-pyscipopt)
2. [Como Instalar](#como-instalar)
3. [Conceitos básicos (Modelagem)](#conceitos-básicos-modelagem)
4. [Trabalhando com variáveis](#trabalhando-com-variáveis)
5. [Restrições e Funções Objetivas](restrições-e-funções-objetivas)


## Guia para pyscipopt
### Breve descrição
Esta biblioteca PySCIPOpt permite modelar problemas de programação linear (LP), programação linear inteira mista (MIP) e programação não-linear inteira mista (MINLP). Para a solução, a interface utiliza o solver SCIP (Solving Constraint Integer Programs) com suas principais funcionalidades para solução dos problemas mistos, visto que é um dos solvers não-comerciais mais rápidos do mercado para otimização mista.

### Objetivo do repositório
Esta seção serve como tutorial para PySCIPOpt. O conteúdo presente envolve uma introdução básica (model object, solution information, parameter settings), variáveis em SCIP e constantes em SCIP.


## Como instalar
Para utilização deste repositório, você deve instalar a biblioteca Python em seu sistema. No terminal, rode o comando:
'''Bash
pip install pyscipopt
'''
> [!Note]
> Para evitar conflitos de versionamento e permissão com o sistema, é recomendado utilizar um ambiente virtual em Python.


## Conceitos Básicos (Modelagem)
### Objeto 'Model'
O 'Model' object é o centro do fluxo de trabalho do programa para interação. Para uso, deve-se importar diretamente da biblioteca.
'''
from pyscipot import Model
scip = Model()
'''

### Métodos Essenciais
Para otimizar o problema objetivo, deve-se realizar tal função:
'''Python
model.optmize()
'''

### Fluxo de Trabalho
Define-se por:
1. Criação do modelo: é a instanciação do objeto 'Model' para otimização de um problema;
2. Adicionar variáveis: são as variáveis presentes no problema.
3. Adicionar restrições: formas de limitação do espaço amostral da otimização;
4. Definir objetivo: é a função a ser maximizada/minimizada diante das variáveis e restrições presentes;
5. Otimização: momento em que o solver atua para otimizar a programação e retornar os resultados.


## Trabalhando com Variáveis
### Adicionar Variáveis
A partir da instanciação do 'Model' object, as variáveis são definidas seguindo:

'''Python
x = model.addVar(vtype='C', lb=0, ub=None, name='x')
'''

Como exemplo da inicialização de uma variável.

### Atributos
* 'name': nome da variável;
* 'vtype': tipos de variáveis
| Tipo | Abreviação | Descrição |
| :--- | :--- | :---: |
| Contínua | C | Variável contínua |
| Inteira | I | Variável inteira, inviável de ter frações |
| Binária | B | Variável binária restrita a 0 e 1 |
| Inteira Implícita | M | Variável contínua, porém pode ser inferida como inteira em qualquer solução válida |
* 'lb': Lower bound, isto é, limite inferior;
* 'up': Upper bound, isto é, limite superior.

### Recuperar valores
Após otimização, encontra-se soluções viáveis para o problema, para isso serve a funcionalidade 'model.getVal(x)'.
Retorna um 'float' e deve ser chamada, somente, após a função de otimização 'model.optimize()' ter sido concluida.


## Restrições e Funções Objetivas
### Restrições
Uso do 'model.addCons()' serve para adicionar uma restrição ao problema.

'''Python
cons_1 = model.addCons(x + y <= 5, name='cons_1')
'''

Os operadores utilizados são: == (igualdade), <= (menor ou igual), >= (maior ou igual).

### Função Objetiva
Uso do 'model.setObjective()' para definir a expressão linear a ser otimizada junto ao direcionamento da mesma.

'''Python
model.setObjective(2 * x + y, sense="minimize")
'''

Desta forma, os atributos são: função objetiva e direcionamento ("minimize" e/ou "maximize").

> [!SUGESTÕES]
> Caso queira sugerir algo, entre em contato.