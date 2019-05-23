import time, random

def main():
  end = 0
  first = 0
  max_prioridade = 0
  max_id = 20

  processos = list()
  processo_inicial = random.randint(1, 9)
  print("Processo "+ str(processo_inicial) +" detectou falha de coordenação")
  processos.append({'id': processo_inicial, 'prioridade': random.randint(1, 10) })

  for i in range(9):
    if(i >= processo_inicial):
      num_prio = random.randint(1, 10)
      processos.append({'id': i+1, 'prioridade': num_prio })
    else:
      num_prio = random.randint(1, 10)
      processos.append({'id': i, 'prioridade': num_prio })


  while end != 1:    
    for processo in processos:
      if(max_id == processo['id'] and max_prioridade == processo['prioridade']):
        print("Sou o processo "+str(processo['id'])+" e sou o novo coordenador")
        end = 1
        break       

      print("")
      print("-------------------------------------------")
      print("Maior Prioridade: "+str(max_prioridade)+" ")
      print("Maior id: "+str(max_id)+" ")
      print("-------------------------------------------")
      print("Sou o processo "+str(processo['id'])+" e minha prioridade é "+str(processo['prioridade'])+"")
      print("")

      if(first == 0):
        print("Iniciando eleição")
        max_prioridade = processo['prioridade']
        max_id = processo['id']

        first = 1
        print("Enviado para nó da direita")
        print("")
      else:
        if(max_prioridade >= processo['prioridade']):
          print("Minha prioridade é menor ou igual, passo adiante")
          print("")
        else:            
          max_prioridade = processo['prioridade']
          max_id = processo['id']
          print("Minha prioridade é maior, reenviando")
          print("")

      time.sleep(1)

if __name__ == '__main__':
    main()
