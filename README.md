# ring-election-simulation
Algoritmo que simula o funcionamento da eleição em anel em python

# Eleição em anel
Quando um processo identificar a ausência de um líder (falha), ele inicia o processo de eleição primeiramente marcando-se como participante e em seguida enviando uma mensagem de eleição contendo seu identificador para seu vizinho no anel.

Ao receber uma mensagem de eleição, um processo deve comparar o identificador contido na mensagem com o seu próprio. Se o identificador recebido for maior, o processo deve passar adiante a mensagem para seu vizinho. Se por outro lado, o identificador contido na mensagem for menor que o identificador do processo em questão e o mesmo ainda não for um participante, então este deverá substituir o conteúdo da mensagem pelo seu próprio identificador antes de enviá-la para seu
vizinho.

# Funcionamento
