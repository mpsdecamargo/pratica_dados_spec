# PARTE 03 – Matemática e Lógica

## Lógica

### Exercício 1

#### Questão

O quilo da maçã num mercado em Taubaté é 20% mais barato que o quilo da
maçã em São José dos Campos; o quilo da maçã em São Paulo é 20% mais caro que em São José dos Campos. Comprei maçã em Taubaté por R$6,00 o quilo. Quanto custa o quilo da maçã em São Paulo?

#### Resposta

Definindo as variáveis:
1kg_Taubaté = 0.8 \* 1kg_SJC
1kg_SP = 1.2 \* 1kg_SJC
1kg_Taubaté = R$6,00

Pergunta: 1kg_SP = ?

Resolução:
1kg_SJC = 1kg_Taubaté / 0.8
1kg_SP = 1.2 \* 6 / 0.8 = 9

#### Resposta Final = 1 quilo da maçã em São Paulo é R$9,00

### Exercício 2

#### Questão

O campeonato brasileiro de futebol (série A) é disputado por 20 times em um sistema de pontos corridos, da seguinte forma:
    i. Cada time joga com cada um dos adversários duas vezes (uma vez em casa, e outra na casa do adversário)
    ii. Em cada jogo, cada time faz um certo número de gols. Quem fizer mais gols vence a partida, e caso o número de gols dos dois times seja igual ocorre empate.
    iii. Um time ganha 3 pontos para cada vitória, 1 ponto para cada empate, e nenhum ponto por uma derrota.
    iv. No final do torneio, os times são classificados pelo número de pontos em ordem decrescente (o primeiro lugar sendo o time que fez mais pontos), e caso dois ou mais times tenham o mesmo número de pontos, são classificados de acordo com os seguintes critérios, nessa ordem:
        1. Número de vitórias;
        2. Saldo de gols: a diferença entre o número de gols que o time fez e o número de gols que o time sofreu no campeonato inteiro;
        3. Gols pró: o número de gols que o time fez no campeonato inteiro
        4. Se o empate persistir, sorteio.
    v. O primeiro lugar após a classificação dos times é o campeão do torneio.
    vi. Além disso, os quatro últimos (ou seja, os que ocuparem as posições de 17 a 20) são rebaixados para a divisão inferior.

Responda as perguntas abaixo:
    a) Quantas partidas são jogadas por um time no campeonato inteiro?
    b) Considerando todos os times e o campeonato inteiro, quantas partidas ocorrem no total?
    c) Considerando as regras (inclusive critérios de desempate) descritos acima, e considerando todos os possíveis resultados que podem ocorrer nas partidas, qual é a menor pontuação possível com que um time pode ser campeão?
    d) Qual é a maior pontuação possível com a qual um time ainda pode ser rebaixado?

#### Resposta

Resolução:
a)
    1 time tem 19 adversários
    Cada time joga 38 jogos (2 \* 19)
b)
    Como a ordem não importa, é um problema de combinação de 20 times em jogos entre 2 times
    C20,2 = 20!/(2!)\*(20-2)! = (20 \* 19 \* 18!)/2 \* 18! = 20 \* 19 / 2 = 190
    Como são 2 jogos de cada combinação, o número de jogos no campeonato é 380.
c)
    Quando um time perde ganha 0 pontos, mas o outro ganha 3, o que aumenta a pontuação necessária para um vencedor do campeonato.
    Nesse caso, um campeonato onde todos os jogos fossem empates, todos os times teriam de concorrer ao sorteio, pois cada um teria 38 pontos.
d)
    Seguindo o mesmo raciocínio de c, a maior pontuação seria quando todos os times ganham 3 pontos na mesma quantidade.
    Se existem 20 times, o número de jogos no campeonato é 380 e a pontuação de cada é igual, a resposta seria 380 vitórias, que dariam 3 pontos por vitória ao time vencedor, divididos pelo número de times, ou seja, a média.
    Resposta = 380 \* 3 / 20 = 57.

#### Resposta Final = a) 38 jogos por time | b) 380 jogos no campeonato | c) menor pontuação para vencer seria 38 pontos | d) maior pontuação para ser rebaixado é 57 pontos

## Probabilidade

### Exercício 3

#### Questão
Jogamos dois dados idênticos, não-viesados e independentes sobre uma mesa (de forma aleatória).
    1. Qual a probabilidade de a soma dos números na face de cima nos dois dados ser ímpar?
    2. Qual a probabilidade de o produto dos números na face de cima dos dois dados ser ímpar?
    3. Qual a probabilidade da soma dos números dos dois dados ser menor ou igual a 5?

#### Resposta

Resolução
1\. P(Face1 + Face 2 = ímpar)
Faces = 1,2,3,4,5,6
ímpares são somas entre pares e ímpares
Caso 1: Face 1 -> 1,3,5 + Face 2 -> 2,4,6
Caso 2: Face 1 -> 2,4,6 + Face 2 -> 1,5,6
P(caso 1) = 3/6 \* 3/6 = 9/36
P(caso 2) = 3/6 \* 3/6 = 9/36
P(Total) = P(caso 1) Ou P(caso 2) = P(caso 1) + P(caso 2) = 9/36 + 9/36 =  18/36 = 50%

2\.P(Face1 \* Face 2 = ímpar)
ímpares são produtos entre ímpares e ímpares
P(Total) = P(Face 1 = ímpar) \* P(Face 2 = ímpar) = 3/6 \* 3/6 = 9/36 = 25%

3\. P(Face1 + Face2 <=5)
Caso 1: P(Face 1 ou Face 2 = 4) e outra face = 1
Caso 2: P(Face 1 ou Face 2 = 3) e outra face <3
Caso 3: P(Face 1 ou Face 2 < 3)
P(Total) = P(Caso 1) + P(Caso 2) + P(Caso 3) = (2\*(1/6\*1/6))+(2\*(1/6\*2/6))+(2/6\*2/6) = (2/36) + (4/36) + (4/36) = 10/36 = 27,78%

#### Resposta Final = 1\. 50% | 2\. 25% | 3\. 27,78%

### Exercício 4

#### Questão

Em uma urna, há 54 bolas vermelhas e 18 bolas azuis.

Inicialmente, tiramos uma bola ao acaso da urna, olhamos a sua cor, e deixamos
fora. Depois, continuamos tirando bolas ao acaso da urna até obter a
primeira bola com cor diferente da primeira - quando isso ocorrer, devolvemos
essa última bola (a primeira com cor diferente) a urna e recomeçamos o
processo.

Para exemplificar, suponha que a primeira bola que retiramos seja vermelha -
removemos a bola vermelha, de forma que temos 53 vermelhas e 18 azuis na
urna. A segunda também é vermelha, logo retiramos e temos 52 vermelhas
e 18 azuis. A terceira é azul, logo devolvemos essa bola a urna e o número
de bolas não se altera, e o jogo "zera", recomeçando, mas agora com 52 bolas
vermelhas e 18 azuis.

Qual a probabilidade de a última bola retirada ser azul?

#### Resposta

Definição:
Início: 54 V (vermelhas) e 18 A (azuis) = 72 bolas no total (T)
Retirada = R
Número de retiradas = R(num)
Após Retirada Inicial (R1):
SE R1 = V:
P(V2) = (54 -1) / (72 - R)
Se R1 = A
P(A2) = (18 - 1) / (72 - R)
MAS: se cor R1 = cor R2, devolve-se R2 e novo_T = 72 - R

Pergunta:
P(R72 = A) = ?

Resolução:
Se R1 = V, todas as bolas azuis serão retornadas, então teria-se que esgotar todas as bolas vermelhas
Se R1 = A, todas as bolas vermelhas serão retornadas, então teria-se que esgotar todas as bolas azuis. Nesse caso, não será possível ter a última bola retirada como azul

P(R72 = A) = P(R1 = V) = 54/72 = 75%

#### Resposta Final = 75%
