# ring-election-simulation
Algoritmo que simula o funcionamento da eleição em anel em python.
> [Demonstração de funcionamento](https://repl.it/@sant0will/ring-election)

# Eleição em anel
Quando um processo identificar a ausência de um líder (falha), ele inicia o processo de eleição primeiramente marcando-se como participante e em seguida enviando uma mensagem de eleição contendo seu identificador para seu vizinho no anel.

Ao receber uma mensagem de eleição, um processo deve comparar o identificador contido na mensagem com o seu próprio. Se o identificador recebido for maior, o processo deve passar adiante a mensagem para seu vizinho. Se por outro lado, o identificador contido na mensagem for menor que o identificador do processo em questão e o mesmo ainda não for um participante, então este deverá substituir o conteúdo da mensagem pelo seu próprio identificador antes de enviá-la para seu
vizinho.

# Funcionamento
Na construção do código foram utilizadas listas, variáveis de controle e laços de repetição.
> Variáveis
```
  end = 0 # Controla o fim do loop geral
  first = 0 # Controla a entrada apenas do primeiro item a uma condição
  max_prioridade = 0 # Controla o valor da maior prioridade entre os processos
  max_id = 20 # Controla qual processo tem a maior prioridade  
```

> Processos
```
  # Todos os processos possuem prioridade randômica
  processos = list() # Criação da lista de processos
  
  # Simulação de falha de coordenação em um processo randômico
  processo_inicial = random.randint(1, 9)
  print("Processo "+ str(processo_inicial) +" detectou falha de coordenação")
  
  #Adição do primeiro processo a lista de processos
  processos.append({'id': processo_inicial, 'prioridade': random.randint(1, 10) })

  #Adição do restante dos processos
  for i in range(9):
    if(i >= processo_inicial):
      num_prio = random.randint(1, 10)
      processos.append({'id': i+1, 'prioridade': num_prio })
    else:
      num_prio = random.randint(1, 10)
      processos.append({'id': i, 'prioridade': num_prio })  
```
> Eleição
```
while end != 1:    
    for processo in processos:
      # Se o processo atual tem maior prioridade depois de passar por todos os nós finaliza a execução
      if(max_id == processo['id'] and max_prioridade == processo['prioridade']):
        print("Sou o processo "+str(processo['id'])+" e sou o novo coordenador")
        end = 1
        break       

      # Mostrando prioridades e processo atual
      print("")
      print("-------------------------------------------")
      print("Maior Prioridade: "+str(max_prioridade)+" ")
      print("Maior id: "+str(max_id)+" ")
      print("-------------------------------------------")
      print("Sou o processo "+str(processo['id'])+" e minha prioridade é "+str(processo['prioridade'])+"")
      print("")

      # Se for a primeira execução ...
      if(first == 0):
        print("Iniciando eleição")3
        # Prioridade e id setados por ser a primeira execução
        max_prioridade = processo['prioridade']
        max_id = processo['id']

        first = 1
        print("Enviado para nó da direita")
        print("")
      else:
        # Se a prioridade do processo atual for menor que a variável de controle  ...
        if(max_prioridade >= processo['prioridade']):
          print("Minha prioridade é menor ou igual, passo adiante")
          print("")
        else:            
          max_prioridade = processo['prioridade']
          max_id = processo['id']
          print("Minha prioridade é maior, reenviando")
          print("")
      # Intervalo de 1s para melhorar visualização
      time.sleep(1)
```



