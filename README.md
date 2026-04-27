# SME0610 - ProgMat

## Sumário
1. [Guia para PySCIPOpt](#guia-para-pyscipopt)  
2. [Como Instalar](#como-instalar)  
3. [Conceitos Básicos (Modelagem)](#conceitos-básicos-modelagem)  
4. [Trabalhando com Variáveis](#trabalhando-com-variáveis)  
5. [Restrições e Função Objetiva](#restrições-e-função-objetiva)  

---

## Guia para PySCIPOpt

### Breve descrição
A biblioteca **PySCIPOpt** permite modelar problemas de Programação Linear (LP), Programação Linear Inteira Mista (MIP) e Programação Não Linear Inteira Mista (MINLP).  

Para a solução, a interface utiliza o solver **SCIP (Solving Constraint Integer Programs)**, que é um dos solvers não comerciais mais rápidos para problemas de otimização mista.

### Objetivo do repositório
Este repositório serve como um tutorial para PySCIPOpt. O conteúdo inclui uma introdução básica (objeto Model, informações de solução e configuração de parâmetros), além de variáveis e constantes no SCIP.

---

## Como instalar
Para utilizar este repositório, instale a biblioteca Python com o comando:

```bash
pip install pyscipopt
```

> **Nota:**  
> Para evitar conflitos de versão e permissões, recomenda-se o uso de um ambiente virtual Python.

---

## Conceitos Básicos (Modelagem)

### Objeto `Model`
O objeto `Model` é o centro do fluxo de trabalho. Para utilizá-lo:

```python
from pyscipopt import Model

model = Model()
```

### Método essencial
Para otimizar o modelo:

```python
model.optimize()
```

### Fluxo de trabalho
O processo segue os seguintes passos:

1. Criação do modelo: instanciação do objeto `Model`;  
2. Adição de variáveis;  
3. Adição de restrições;  
4. Definição da função objetivo;  
5. Otimização do modelo.  

---

## Trabalhando com Variáveis

### Adicionar variáveis

```python
x = model.addVar(vtype='C', lb=0, ub=None, name='x')
```

### Atributos

- `name`: nome da variável  
- `vtype`: tipo da variável  

| Tipo               | Abreviação | Descrição                                   |
|--------------------|------------|---------------------------------------------|
| Contínua           | C          | Variável contínua                           |
| Inteira            | I          | Apenas valores inteiros                     |
| Binária            | B          | Restrita a 0 ou 1                           |
| Inteira implícita  | M          | Contínua, mas pode ser inferida como inteira |

- `lb`: limite inferior (lower bound)  
- `ub`: limite superior (upper bound)  

### Recuperar valores

Após a otimização:

```python
model.getVal(x)
```

Retorna um `float` e só deve ser chamado após `model.optimize()`.

---

## Restrições e Função Objetiva

### Restrições

```python
cons_1 = model.addCons(x + y <= 5, name='cons_1')
```

Operadores disponíveis:
- `==` (igualdade)  
- `<=` (menor ou igual)  
- `>=` (maior ou igual)  

### Função Objetiva

```python
model.setObjective(2 * x + y, sense="minimize")
```

Parâmetros:
- expressão da função objetivo  
- `sense`: `"minimize"` ou `"maximize"`  

---

> **Sugestões:**  
> Caso queira contribuir com melhorias, fique à vontade para entrar em contato.