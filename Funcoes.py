#Esta função foi criada para gerar senhas para os pacientes por ordem de chegada
def gerarSenha(tipo, consultorio, contadorcomumDermatologia, contadorcomumEndocrinologia, contadorcomumOrtopedia, contadorpreferencialDermatologia, contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):
  
    if(tipo=="C" or tipo=="c"):
        if(consultorio=="d" or consultorio=="D"):
            if(contadorcomumDermatologia<10):
                senha="cd00"+str(contadorcomumDermatologia)
                
            elif(contadorcomumDermatologia>=10 and contadorcomumDermatologia<100):
                senha="cd0"+str(contadorcomumDermatologia)
                
            elif(contadorcomumDermatologia>=100):
                senha="cd"+str(contadorcomumDermatologia)
                
        elif(consultorio=="E" or consultorio=="e"):
            if(contadorcomumEndocrinologia<10):
                senha="ce00"+str(contadorcomumEndocrinologia)
                
            elif(contadorcomumEndocrinologia>=10 and contadorcomumEndocrinologia<100):
                senha="ce0"+str(contadorcomumEndocrinologia)
               
            elif(contadorcomumEndocrinologia>=100):
                senha="ce"+str(contadorcomumEndocrinologia)
                
        elif(consultorio=="O" or consultorio=="o"):
            if(contadorcomumOrtopedia<10):
                senha="co00"+str(contadorcomumOrtopedia)
                
            elif(contadorcomumOrtopedia>=10 and contadorcomumOrtopedia<100):
                senha="co0"+str(contadorcomumOrtopedia)
                
            elif(contadorcomumOrtopedia>=100):
                senha="co"+str(contadorcomumOrtopedia)
               
    else:
        if(consultorio=="d" or consultorio=="D"):
            if(contadorpreferencialDermatologia<10):
                senha="pd00"+str(contadorpreferencialDermatologia)
               
            elif(contadorpreferencialDermatologia>=10 and contadorpreferencialDermatologia<100):
                senha="pd0"+str(contadorpreferencialDermatologia)
                
            elif(contadorpreferencialDermatologia>=100):
                senha="pd"+str(contadorpreferencialDermatologia)
                
        elif(consultorio=="E" or consultorio=="e"):
            if(contadorpreferencialEndocrinologia<10):
                senha="pe00"+str(contadorpreferencialEndocrinologia)
                
            elif(contadorpreferencialEndocrinologia>=10 and contadorpreferencialEndocrinologia<100):
                senha="pe0"+str(contadorpreferencialEndocrinologia)
                
            elif(contadorpreferencialEndocrinologia>=100):
                senha="pe"+str(contadorpreferencialEndocrinologia)
                
        elif(consultorio=="O" or consultorio=="o"):
            if(contadorpreferencialOrtopedia<10):
                senha="po00"+str(contadorpreferencialOrtopedia)
                
            elif(contadorpreferencialOrtopedia>=10 and contadorpreferencialOrtopedia<100):
                senha="po0"+str(contadorpreferencialOrtopedia)

            elif(contadorpreferencialOrtopedia>=100):
                senha="po"+str(contadorpreferencialOrtopedia)
               
    return senha

#Esta função serve para verificar se um valor digitado é composto apenas por numeros
def VerificarInt(valor):
    if(valor.isdigit()):
        return True
    else:
      return False

#Esta função serve para validar a hora, visto que tem que ser um valor inteiro e estar no intervalo de 0 a 24
def ValidarHora(boolhora, hora):
    boolh=False
    while True:
        while(boolhora):
            hora=int(hora)
            if(hora<=0 or hora>24):
                hora=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter. OBS.: 0<=hora<=24\n")
                boolhora=VerificarInt(hora)
            else:
                boolh=True
                break
        if(boolh):
            break
        while not boolhora:
            hora=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter\n")
            boolhora=VerificarInt(hora)
    return hora

#Esta função serve para validar o minuto da hora, visto que tem que ser um valor inteiro e estar no intervalo de 0 a 60
def ValidarMinuto(boolminuto, minuto):
    boolm=False
    while True:
        while(boolminuto):
            minuto=int(minuto)
            if(minuto<0 or minuto>60):
                minuto=input("Minuto inserido inválido para inserir o minuto você deve digitar o minuto ex: são 12:40,\n"
                       "então você deve digitar 40 e apertar enter. OBS.: 0<=minuto<=60\n")
                boolminuto=VerificarInt(minuto)
            else:
                boolm=True
                break
        if(boolm):
            break
        while(not boolminuto):
            minuto=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter\n")
            boolminuto=VerificarInt(minuto)
    return minuto

#Esta função serve para validar a opção de entrada do menu, visto que tem que ser um valor inteiro e estar no intervalo de 1 a 9
def ValidarOpcao(boolOpcao, opcao):
    boolo=False
    while True:
        while(boolOpcao):
            opcao=int(opcao)
            if(opcao<0 and opcao>9):
                MENU()
                opcao=input("Digite uma opção válida\n")
                boolOpcao=VerificarInt(opcao)
            else:
                boolo=True
                break
        if(boolo):
            break
        while(not boolOpcao):
            MENU()
            opcao=input("Opção invalida, por favor escolha uma opção válida")
            boolOpcao=VerificarInt(opcao)
    return opcao

#Esta função serve para imprimir o menu
def MENU():

    print("##########################################################")
    print("#                         MENU                           #")
    print("##########################################################")
    print("#  [1] - Emitir nova senha                               #")
    print("#  [2] - Chamar paciente para atendimento                #")
    print("#  [3] - Pular paciente                                  #")
    print("#  [4] - Encerrar uma consulta realizada                 #")
    print("#  [5] - Exibir fila de espera                           #")
    print("#  [6] - Exibir pacientes atendidos no dia               #")
    print("#  [7] - Exibir tempo médio de espera dos pacientes      #")
    print("#  [8] - Exibir tempo médio de atendimento dos pacientes #")
    print("#  [9] - Encerrar programa                               #")
    print("##########################################################")

def EmitirSenha(contadorcomumDermatologia, contadorcomumEndocrinologia, contadorcomumOrtopedia, contadorpreferencialDermatologia, contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):

    #pacienteComum=[]
    #pacientePrioritario=[]
    tipo=input("Digite 'C' para paciente comum e 'P' para preferencial\n")
    while(tipo!="c" and tipo!="C" and tipo!="p" and tipo!="P"):
        tipo=input("Tipo inválido, digite 'C' para paciente comum e 'P' para preferencial\n")
    nome=input("Digite seu nome\n")
    print("Para inserir o horário você deve primeiro digitar a hora ex: são 12:40, então você deve digitar 12 e apertar enter\n"
          "Depois você digita os minutos ex: são 12:40, então você deve digitar 40 e apertar enter")
    hora=input("Digite a hora\n")
    boolhora=VerificarInt(hora)
    hora=ValidarHora(boolhora, hora)
    minuto=input("Digite o minuto\n")
    boolminuto=VerificarInt(minuto)
    minuto=ValidarMinuto(boolminuto, minuto)
    consultorio=input("Digite o consultório de atendimento do paciente:\n"
                     "D - Dermatologia\n"
                     "E - Endocrinologia\n"
                     "O - Ortopedia\n")
    while(consultorio!="D" and consultorio!="d" and consultorio!="E" and consultorio!="e"
          and consultorio!="O" and consultorio!="o"):
     consultorio=input("Consultório digitado inválido, digite o consultório de atendimento do paciente:\n"
                     "D - Dermatologia\n"
                     "E - Endocrinologia\n"
                     "O - Ortopedia\n")
    senha=gerarSenha(tipo, consultorio, contadorcomumDermatologia, contadorcomumEndocrinologia, contadorcomumOrtopedia, contadorpreferencialDermatologia, contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia)
    return [tipo, nome, hora, minuto, consultorio, senha]



def ChamarPacienteParaAtendimento():
    print('Esta função serve para chamar pacientes para serem atendidos');

def PularPaciente():
    print("Esta função serve para chamar pacientes")

def EncerrarConsulta():
    print("Esta função serve para encerrar uma consulta")

def ExibirFilaDeEspera():
    print("Esta função serve para exibir as filas de espera do ambulatorio")

def ExibirPacientesAtendidosNoDia():
    print("Esta função serve para exibir pacientes atendidos no dia ")

def ExibirTempoMedioDeEsperaDosPacientes():
    print("Esta funçõ serve para exibir o tempo medio de espera dos pacientes")
def ExibirTempoMedioDeAtendimentoDosPacientes():
    print("Esta função serve para exibir tempo médio de atendimento dos pacientes")
