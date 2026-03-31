# Laboratório 6 – Tokenização com BPE e WordPiece

Este repositório contém a implementação do Laboratório 6 da disciplina Tópicos em Inteligência Artificial.

O objetivo deste laboratório foi compreender como modelos de linguagem tratam o texto através de técnicas de sub-palavras, implementando o algoritmo BPE (Byte Pair Encoding) do zero e explorando o funcionamento do WordPiece na prática.

---

## Objetivo

Demonstrar como um vocabulário pode ser construído a partir de pares de caracteres frequentes e como isso permite representar palavras de forma eficiente, mesmo quando elas não aparecem diretamente no vocabulário.

---

## O que foi implementado

### 1. Contagem de pares (get_stats)

Foi implementada uma função responsável por percorrer o vocabulário inicial e contar a frequência de todos os pares adjacentes de símbolos.

Essa etapa é a base do algoritmo BPE.

---

### 2. Fusão de pares (merge_vocab)

Foi criada uma função que recebe o par mais frequente e realiza a fusão no vocabulário, substituindo ocorrências como:

```
e s → es
```

Essa etapa permite a criação progressiva de novos tokens.

---

### 3. Loop de treinamento do BPE

Foi implementado um laço de repetição com 5 iterações, onde a cada passo:

- o par mais frequente é identificado
- o merge é realizado
- o vocabulário é atualizado e exibido

Ao final das iterações, é possível observar a formação de tokens morfológicos, como:

```
est</w>
```

---

### 4. WordPiece (Hugging Face)

Foi utilizado o tokenizer:

```
bert-base-multilingual-cased
```

para analisar a segmentação de palavras em sub-palavras.

Foi testada a frase:

```
Os hiper-parâmetros do transformer são inconstitucionalmente difíceis de ajustar.
```

---

## WordPiece e sub-palavras

Os tokens que começam com "##" representam a continuação de uma palavra.

Por exemplo, a palavra "inconstitucionalmente" pode ser dividida em partes menores como:

```
in, ##cons, ##tit, ##ucional, ##mente
```

O prefixo "##" indica que aquele token não inicia uma nova palavra, mas continua a anterior.

Essa abordagem permite que o modelo consiga lidar com palavras desconhecidas, pois ele pode quebrá-las em partes menores já existentes no vocabulário, evitando falhas no processamento.

---

## Estrutura do projeto

```
lab-tokenizadorBPE
│
├── main.py
└── README.md
```

---

## Como executar

Execute o código com:

```
python main.py
```

O programa irá exibir:

- as frequências dos pares
- as fusões realizadas em cada iteração
- o vocabulário atualizado
- a tokenização com WordPiece

---

## Observação sobre uso de IA

Ferramentas de inteligência artificial foram utilizadas apenas nas partes permitidas do laboratório, como auxílio na manipulação de strings e construção das funções de substituição.

Nas demais etapas, como implementação do algoritmo BPE, lógica de fusão e interpretação dos resultados, a IA foi utilizada apenas para esclarecimento de dúvidas pontuais, sendo a implementação realizada de forma própria.

---

## Autor

Guilherme Ruben