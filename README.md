# Projecto para Unidade Curricular de Protecção de Dados

Este projeto tem como objectivo manipular, pseudonimizar, anonimizar e mascarar dados do famoso dataset do Titanic, utilizando Python e a biblioteca `pandas`.  
A estrutura do projecto inclui scripts para leitura e tratamento de colunas sensíveis.

---

## Dependências

• Antes de executar o projeto, é necessário instalar a biblioteca **pandas**: `pip install pandas`

• Também deve baixar o dataset original do Titanic no Kaggle: https://www.kaggle.com/code/chanchal24/titanic-dataset/input

• Além disso, o projecto utiliza as bibliotecas `secrets` e `hashlibs` para gerar identificadores e hashes seguros.

---

## Como Executar
1. Certifique-se de que os arquivos CSV estão dentro da pasta `data/`.
2. Execute o script principal: `python main.py`.
3. O script irá:

• Ler os datasets.

• Aplicar mascaramento nas colunas sensíveis.

• Gerar um dataset unificado pronto para generalização ou análise.

---

## Tecnologias Utilizadas
- `Python 3.13+`
- `pandas` para manipulação de dados
- `secrets` e `hashlib` para geração de identificadores seguros

---

## Resultados obtidos
- **`PassengerId`:** pseudonimizado com recurso a `hash`
- **`Name`:** encriptado com recurso a `hash` de comprimento longo
- **`Pclass`:** generalizado (*1*, *2*, *3* passam a ter códigos próprios)
- **`Sex`:** coluna removida
- **`Age`:** generalizada em categorias (*Adulto*/*Menor*)
- **`SibSp` + `Parch`:** juntos e generalizados em uma única coluna `NrFamiliares` (*Sem familiares*/*Pequena*/*Grande*)
- **`Ticket`:** mascarada
- **`Fare`:** generalizada em intervalos de $100
- **`Cabin`:** parcialmente mascaradas, ou denotados como `Desconhecido` em lugares sem valor
- **`Embarked`:** removidos

---

## Para melhor visualização
• Visite o directorio `notebooks/`

---

## Autores
• Francisco de Figueiredo Jr.

• Hamzah Braimo
