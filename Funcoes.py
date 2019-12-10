def gerarSenha(tipo, consultorio, contadorcomum, contadorpreferencial):
    #pacienteComum=[]
    #pacientePrioritario=[]

    if(tipo=="C" or tipo=="c"):
        if(consultorio=="d" or consultorio=="D"):
            if(contadorcomum<10):
                senha="cd00"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=10 and contadorcomum<100):
                senha="cd0"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=100):
                senha="cd"+str(contadorcomum)
                #pacienteComum.append()
        elif(consultorio=="E" or consultorio=="e"):
            if(contadorcomum<10):
                senha="ce00"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=10 and contadorcomum<100):
                senha="ce0"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=100):
                senha="ce"+str(contadorcomum)
                #pacienteComum.append()
        elif(consultorio=="O" or consultorio=="o"):
            if(contadorcomum<10):
                senha="ce00"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=10 and contadorcomum<100):
                senha="ce0"+str(contadorcomum)
                #pacienteComum.append()
            elif(contadorcomum>=100):
                senha="ce"+str(contadorcomum)
                #pacienteComum.append()
        contadorcomum+=1
    else:
        if(consultorio=="d" or consultorio=="D"):
            if(contadorpreferencial<10):
                senha="pd00"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=10 and contadorpreferencial<100):
                senha="pd0"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=100):
                senha="pd"+str(contadorpreferencial)
                #pacientePrioritario.append()
        elif(consultorio=="E" or consultorio=="e"):
            if(contadorpreferencial<10):
                senha="pe00"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=10 and contadorpreferencial<100):
                senha="pe0"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=100):
                senha="pe"+str(contadorpreferencial)
                #pacientePrioritario.append()
        elif(consultorio=="O" or consultorio=="o"):
            if(contadorpreferencial<10):
                senha="pe00"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=10 and contadorpreferencial<100):
                senha="pe0"+str(contadorpreferencial)
                #pacientePrioritario.append()
            elif(contadorpreferencial>=100):
                senha="pe"+str(contadorpreferencial)
                #pacientePrioritario.append()
        contadorpreferencial+=1
    return senha

def VerificarInt(valor):
    if(valor.isdigit()):
        return True
    else:
      return False

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

def ValidarOpcao(boolOpcao, opcao):
    boolo=False
    while True:
        opcao=int(opcao)
        while(boolOpcao):
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

def EmitirSenha(contadorComum, contadorPreferencial):

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
    senha=gerarSenha(tipo, consultorio, contadorComum, contadorPreferencial)
    return (tipo, nome, hora, minuto, consultorio, senha)



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
