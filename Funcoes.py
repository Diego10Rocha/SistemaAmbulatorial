#Esta função foi criada para gerar senhas para os pacientes por ordem de chegada
def gerarSenha(tipo, consultorio, contadorcomumDermatologia, contadorcomumEndocrinologia,
               contadorcomumOrtopedia, contadorpreferencialDermatologia,
               contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):

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
def SolicitarHora():
    print("Para inserir o horário você deve primeiro digitar a hora ex: são 12:40, então você deve digitar 12 e apertar enter\n"
                        "Depois você digita os minutos ex: são 12:40, então você deve digitar 40 e apertar enter")
    hora=input("Digite a hora\n")
    boolhora=VerificarInt(hora)
    boolh=False
    while True:
        while(boolhora):
            hora=int(hora)
            if(hora<0 or hora>=24):
                hora=input("Hora inserida inválida para inserir o horário você deve primeiro digitar a hora ex: são 12:40,\n"
                       "então você deve digitar 12 e apertar enter. OBS.: 0<=hora<24\n")
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
def SolicitarMinuto():
    minuto=input("Digite o minuto\n")
    boolminuto=VerificarInt(minuto)
    boolm=False
    while True:
        while(boolminuto):
            minuto=int(minuto)
            if(minuto<0 or minuto>=60):
                minuto=input("Minuto inserido inválido para inserir o minuto você deve digitar o minuto ex: são 12:40,\n"
                       "então você deve digitar 40 e apertar enter. OBS.: 0<=minuto<60\n")
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

def VariacaoDeTempo(hora_inicio, minuto_inicio, hora_final, minuto_final):
    minuto_inicio=minuto_inicio+(hora_inicio*60)
    minuto_final=minuto_final+(hora_final*60)
    variacao=0
    if(minuto_final>=minuto_inicio):
        variacao=minuto_final-minuto_inicio
    else:
        variacao=(24*60-minuto_inicio)+minuto_final
    hora_total=variacao//60
    minuto_total=(variacao%60)
    return hora_total, minuto_total

def Gerar_Tabela_Pacientes_Em_Espera(tabela, lista_Pacientes_Espera, hora, minuto):
    for i in range(len(lista_Pacientes_Espera)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Espera[i][2], lista_Pacientes_Espera[i][3],
                                                   hora, minuto)
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        if(lista_Pacientes_Espera[i][4]=="d" or lista_Pacientes_Espera[i][4]=="D"):
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Dermatologia", "Em espera", tempo_espera_na_fila])
        elif(lista_Pacientes_Espera[i][4]=="e" or lista_Pacientes_Espera[i][4]=="E"):
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Endocrinologia", "Em espera", tempo_espera_na_fila])
        else:
            tabela.add_row([lista_Pacientes_Espera[i][5], lista_Pacientes_Espera[i][1], "Ortopedia", "Em espera", tempo_espera_na_fila])

    return tabela

def Gerar_Tabela_Pacientes_Atendidos(tabela, lista_Pacientes_Atendidos):
    for i in range(len(lista_Pacientes_Atendidos)):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Atendidos[i][2], lista_Pacientes_Atendidos[i][3],
                                             lista_Pacientes_Atendidos[i][6], lista_Pacientes_Atendidos[i][7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"
        hora_atendimento, minuto_atendimento=VariacaoDeTempo(lista_Pacientes_Atendidos[i][6], lista_Pacientes_Atendidos[i][7],
                                          lista_Pacientes_Atendidos[i][8], lista_Pacientes_Atendidos[i][9])
        tempo_atendimento=str(hora_atendimento)+" h : "+str(minuto_atendimento)+" min"
        if(lista_Pacientes_Atendidos[i][4]=="d" or lista_Pacientes_Atendidos[i][4]=="D"):
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Dermatologia", "Dra. Silvia Melo"])
        elif(lista_Pacientes_Atendidos[i][4]=="e" or lista_Pacientes_Atendidos[i][4]=="E"):
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Endocrinologia", "Dr. Fernando Santos"])
        else:
            tabela.add_row([lista_Pacientes_Atendidos[i][1], tempo_espera_na_fila, tempo_atendimento, "Ortopedia", "Dra. Maria do Carmo Silva"])

    return tabela

def Gerar_Tabela_Pacientes_Em_Atendimento(tabela, lista_Pacientes_Atendimento):
    if(lista_Pacientes_Atendimento):
        hora_espera_na_fila, minuto_espera_na_fila=VariacaoDeTempo(lista_Pacientes_Atendimento[2], lista_Pacientes_Atendimento[3],
                                                   lista_Pacientes_Atendimento[6], lista_Pacientes_Atendimento[7])
        tempo_espera_na_fila=str(hora_espera_na_fila)+" h : "+str(minuto_espera_na_fila)+" min"

        if(lista_Pacientes_Atendimento[4]=="d" or lista_Pacientes_Atendimento[4]=="D"):
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Dermatologia", "Em atendimento", tempo_espera_na_fila])
        elif(lista_Pacientes_Atendimento[4]=="e" or lista_Pacientes_Atendimento[4]=="E"):
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Endocrinologia", "Em atendimento", tempo_espera_na_fila])
        else:
            tabela.add_row([lista_Pacientes_Atendimento[5], lista_Pacientes_Atendimento[1], "Ortopedia", "Em atendimento", tempo_espera_na_fila])

    return tabela

def CalculaTempoTotalDeEspera(hora_total, minuto_total, listaAtendidos):
    hora_inicial = 0
    minuto_inicial = 0
    hora_final = 0
    minuto_final = 0
    for i in range(len(listaAtendidos)):
        hora_inicial+=listaAtendidos[i][2]
        minuto_inicial+=listaAtendidos[i][3]
        hora_final+=listaAtendidos[i][6]
        minuto_final+=listaAtendidos[i][7]

    variacao_hora_total, variacao_minuto_total = VariacaoDeTempo(hora_inicial, minuto_inicial, hora_final, minuto_final)
    hora_total+=variacao_hora_total
    minuto_total+=variacao_minuto_total
    return hora_total, minuto_total


def CalculaTempoTotalDeAtendimento(hora_total, minuto_total, listaAtendidos):
    hora_inicial = 0
    minuto_inicial = 0
    hora_final = 0
    minuto_final = 0
    for i in range(len(listaAtendidos)):
        hora_inicial+=listaAtendidos[i][6]
        minuto_inicial+=listaAtendidos[i][7]
        hora_final+=listaAtendidos[i][8]
        minuto_final+=listaAtendidos[i][9]

    variacao_hora_total, variacao_minuto_total = VariacaoDeTempo(hora_inicial, minuto_inicial, hora_final, minuto_final)
    hora_total+=variacao_hora_total
    minuto_total+=variacao_minuto_total
    return hora_total, minuto_total

def CalculaMedia(tempo, quantidade):
    if(quantidade):
        media=tempo/quantidade
        return media
    else:
        return 0
def Formatarhora(tempoEmMinutos):
    if((tempoEmMinutos//60 == 0) and ((tempoEmMinutos%60)//1 == 0) and (((tempoEmMinutos%60)%1)*60 == 0)):
        hora_formatada = "--------------"
    elif(tempoEmMinutos//60==0):
        hora_formatada = \
            str((tempoEmMinutos%60)//1)+" min : "+str(((tempoEmMinutos%60)%1)*60)+" s"
    else:
        hora_formatada = \
            str(tempoEmMinutos//60)+" h : "+str((tempoEmMinutos%60)//1)+" min : "+str(((tempoEmMinutos%60)%1)*60)+" s"
    return hora_formatada

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

def EmitirSenha(contadorcomumDermatologia, contadorcomumEndocrinologia,
                contadorcomumOrtopedia, contadorpreferencialDermatologia,
                contadorpreferencialEndocrinologia, contadorpreferencialOrtopedia):

    #pacienteComum=[]
    #pacientePrioritario=[]
    tipo=input("Digite 'C' para paciente comum e 'P' para preferencial\n")
    while(tipo!="c" and tipo!="C" and tipo!="p" and tipo!="P"):
        tipo=input("Tipo inválido, digite 'C' para paciente comum e 'P' para preferencial\n")
    nome=input("Digite seu nome\n")
    while(nome==""):
        nome=input("Valor inválido. Digite seu nome\n")

    hora=SolicitarHora()
    minuto=SolicitarMinuto()
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



def ChamarPacienteParaAtendimento(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                                  paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                                  listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                                  listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                                  listaEsperaPacientePrioritarioOrtopedia, tamComumDermatologiaAtendido,
                                  tamComumEndocrinologiaAtendido, tamComumOrtopediaAtendido,
                                  tamPrioritarioDermatologiaAtendido, tamPrioritarioEndocrinologiaAtendido,
                                  tamPrioritarioOrtopediaAtendido, ultimo_paciente_chamado_dermatologia,
                                  ultimo_paciente_chamado_endocrinologia, ultimo_paciente_chamado_ortopedia,
                                  ordem_chegada_dermatologia, ordem_chegada_endocrinologia,
                                  ordem_chegada_ortopedia, dados_Pacientes):

    opcao=0
    hora_atendimento_Dermatologia = 0
    minuto_atendimento_Dermatologia = 0
    hora_atendimento_Endocrinologia = 0
    minuto_atendimento_Endocrinologia = 0
    hora_atendimento_Ortopedia = 0
    minuto_atendimento_Ortopedia = 0
    chama_comum = False
    chama_preferencial = False
    MSG="O paciente não compareceu, selecione a opção 3 para pular o paciente"
    comparecimento="n"
    while(opcao!="4"):
        print("##########################################################")
        print("#                         MENU                           #")
        print("##########################################################")
        print("#  [1] - Chamar para consultório de Dermatologia         #")
        print("#  [2] - Chamar para consultório de Endocrinologia       #")
        print("#  [3] - Chamar para consultório de Ortopedia            #")
        print("#  [4] - SAIR                                            #")
        print("##########################################################")
        opcao=input("Escolha uma opção: \n")

        if(opcao=="1"):
            while(comparecimento=="n" or comparecimento=="N"):
                comparecimento=" "
                if(not paciente_em_antendimento_Dermatologia and
                        (listaEsperaPacientePrioritarioDermatologia or listaEsperaPacienteComumDermatologia)):
                    if(not ultimo_paciente_chamado_dermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(not ultimo_paciente_chamado_dermatologia and not listaEsperaPacientePrioritarioDermatologia
                         and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacientePrioritarioDermatologia and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacienteComumDermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(ultimo_paciente_chamado_dermatologia):
                        if(ultimo_paciente_chamado_dermatologia[0]=="c" or ultimo_paciente_chamado_dermatologia[0]=="C"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                chama_preferencial = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True
                        elif(ultimo_paciente_chamado_dermatologia[0]=="p" or ultimo_paciente_chamado_dermatologia[0]=="P"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                if(ordem_chegada_dermatologia[0][0]=="p" or ordem_chegada_dermatologia[0][0]=="P"):
                                    chama_preferencial = True
                                elif(listaEsperaPacienteComumDermatologia):
                                    chama_comum = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True

                    if(chama_preferencial):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacientePrioritarioDermatologia[0][5], "-", listaEsperaPacientePrioritarioDermatologia[0][1],
                              "- Consultório de Dermatologia")

                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o proximo. "
                                        "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento=="S" or comparecimento=="s"):
                                paciente_em_antendimento_Dermatologia = listaEsperaPacientePrioritarioDermatologia[0]
                                ultimo_paciente_chamado_dermatologia = paciente_em_antendimento_Dermatologia
                                hora_atendimento_Dermatologia=SolicitarHora()
                                minuto_atendimento_Dermatologia=SolicitarMinuto()
                                paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                                paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                                for i in range(len(ordem_chegada_dermatologia)):
                                    if(ordem_chegada_dermatologia[i][5] == paciente_em_antendimento_Dermatologia[5]):
                                        ordem_chegada_dermatologia.pop(i)
                                        break
                                listaEsperaPacientePrioritarioDermatologia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                chama_preferencial = False
                                dados_Pacientes, listaEsperaPacientePrioritarioDermatologia=\
                                    PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioDermatologia[0][5],
                                                  listaEsperaPacientePrioritarioDermatologia)
                    elif(chama_comum):
                        print("Próxima senha do consultório de DERMATOLOGIA:")
                        print(listaEsperaPacienteComumDermatologia[0][5], "-", listaEsperaPacienteComumDermatologia[0][1],
                              "- Consultório de Dermatologia")
                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                        "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento=="S" or comparecimento=="s"):
                                paciente_em_antendimento_Dermatologia=listaEsperaPacienteComumDermatologia[0]
                                ultimo_paciente_chamado_dermatologia = paciente_em_antendimento_Dermatologia
                                hora_atendimento_Dermatologia=SolicitarHora()
                                minuto_atendimento_Dermatologia=SolicitarMinuto()
                                paciente_em_antendimento_Dermatologia.append(hora_atendimento_Dermatologia)
                                paciente_em_antendimento_Dermatologia.append(minuto_atendimento_Dermatologia)
                                for i in range(len(ordem_chegada_dermatologia)):
                                    if(ordem_chegada_dermatologia[i][5] == paciente_em_antendimento_Dermatologia[5]):
                                        ordem_chegada_dermatologia.pop(i)
                                        break
                                listaEsperaPacienteComumDermatologia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                chama_comum = True
                                dados_Pacientes, listaEsperaPacienteComumDermatologia=\
                                    PularPaciente(dados_Pacientes,listaEsperaPacienteComumDermatologia[0][5],
                                                  listaEsperaPacienteComumDermatologia)

                else:
                    print("Não há pacientes na lista de espera de dermatologia, ou já possui um paciente sendo atendido")
                    break
            break
        elif(opcao=="2"):
            while(comparecimento == "n" or comparecimento == "N"):
                comparecimento=""
                chama_comum = False
                chama_preferencial = False
                if(not paciente_em_antendimento_Endocrinologia and (listaEsperaPacienteComumEndocrinologia
                                                                    or listaEsperaPacientePrioritarioEndocrinologia)):
                    if(not ultimo_paciente_chamado_dermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(not ultimo_paciente_chamado_dermatologia and not listaEsperaPacientePrioritarioDermatologia
                         and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacientePrioritarioDermatologia and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacienteComumDermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(ultimo_paciente_chamado_dermatologia):
                        if(ultimo_paciente_chamado_dermatologia[0]=="c" or ultimo_paciente_chamado_dermatologia[0]=="C"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                chama_preferencial = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True
                        elif(ultimo_paciente_chamado_dermatologia[0]=="p" or ultimo_paciente_chamado_dermatologia[0]=="P"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                if(ordem_chegada_dermatologia[0][0]=="p" or ordem_chegada_dermatologia[0][0]=="P"):
                                    chama_preferencial = True
                                elif(listaEsperaPacienteComumDermatologia):
                                    chama_comum = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True

                    if(chama_preferencial):
                        print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                        print(listaEsperaPacientePrioritarioEndocrinologia[0][5], "-" , listaEsperaPacientePrioritarioEndocrinologia[0][1],
                              "- Consultório de Endocrinologia")
                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                        "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento=="S" or comparecimento=="s"):
                                paciente_em_antendimento_Endocrinologia = listaEsperaPacientePrioritarioEndocrinologia[0]
                                hora_atendimento_Endocrinologia = SolicitarHora()
                                minuto_atendimento_Endocrinologia = SolicitarMinuto()
                                paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                                paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                                listaEsperaPacientePrioritarioEndocrinologia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                dados_Pacientes, listaEsperaPacientePrioritarioEndocrinologia =\
                                    PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioEndocrinologia[0][5],
                                                  listaEsperaPacientePrioritarioEndocrinologia)
                    elif(chama_comum):
                        print("Próxima senha do consultório de ENDOCRINOLOGIA:")
                        print(listaEsperaPacienteComumEndocrinologia[0][5], "-", listaEsperaPacienteComumEndocrinologia[0][1],
                              "- Consultório de Endocrinologia")
                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para pular o paciente e chamar o próximo. "
                                        "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento=="S" or comparecimento=="s"):
                                paciente_em_antendimento_Endocrinologia=listaEsperaPacienteComumEndocrinologia[0]
                                hora_atendimento_Endocrinologia=SolicitarHora()
                                minuto_atendimento_Endocrinologia=SolicitarMinuto()
                                paciente_em_antendimento_Endocrinologia.append(hora_atendimento_Endocrinologia)
                                paciente_em_antendimento_Endocrinologia.append(minuto_atendimento_Endocrinologia)
                                listaEsperaPacienteComumEndocrinologia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                dados_Pacientes, listaEsperaPacienteComumEndocrinologia=\
                                    PularPaciente(dados_Pacientes, listaEsperaPacienteComumEndocrinologia[0][5],
                                                  listaEsperaPacienteComumEndocrinologia)
                else:
                    print("Não há pacientes na lista de espera de endocrinologia, ou já possui um paciente sendo atendido")
                    break
            break
        elif(opcao=="3"):
            while(comparecimento=="n" or comparecimento=="N"):
                comparecimento=""
                chama_comum = False
                chama_preferencial = False
                if(not paciente_em_antendimento_Ortopedia and (listaEsperaPacienteComumOrtopedia
                        or listaEsperaPacientePrioritarioOrtopedia)):
                    if(not ultimo_paciente_chamado_dermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(not ultimo_paciente_chamado_dermatologia and not listaEsperaPacientePrioritarioDermatologia
                         and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacientePrioritarioDermatologia and listaEsperaPacienteComumDermatologia):
                        chama_comum = True
                    elif(not listaEsperaPacienteComumDermatologia and listaEsperaPacientePrioritarioDermatologia):
                        chama_preferencial = True
                    elif(ultimo_paciente_chamado_dermatologia):
                        if(ultimo_paciente_chamado_dermatologia[0]=="c" or ultimo_paciente_chamado_dermatologia[0]=="C"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                chama_preferencial = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True
                        elif(ultimo_paciente_chamado_dermatologia[0]=="p" or ultimo_paciente_chamado_dermatologia[0]=="P"):
                            if(listaEsperaPacientePrioritarioDermatologia):
                                if(ordem_chegada_dermatologia[0][0]=="p" or ordem_chegada_dermatologia[0][0]=="P"):
                                    chama_preferencial = True
                                elif(listaEsperaPacienteComumDermatologia):
                                    chama_comum = True
                            elif(listaEsperaPacienteComumDermatologia):
                                chama_comum = True

                    if(chama_preferencial):
                        print("Próxima senha do consultório de ORTOPEDIA:")
                        print(listaEsperaPacientePrioritarioOrtopedia[0][5], "-", listaEsperaPacientePrioritarioOrtopedia[0][1],
                              "- Consultório de Ortopedia")
                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                                 "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento == "S" or comparecimento == "s"):
                                paciente_em_antendimento_Ortopedia = listaEsperaPacientePrioritarioOrtopedia[0]
                                hora_atendimento_Ortopedia = SolicitarHora()
                                minuto_atendimento_Ortopedia = SolicitarMinuto()
                                paciente_em_antendimento_Ortopedia.append(hora_atendimento_Ortopedia)
                                paciente_em_antendimento_Ortopedia.append(minuto_atendimento_Ortopedia)
                                listaEsperaPacientePrioritarioOrtopedia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                dados_Pacientes, listaEsperaPacientePrioritarioOrtopedia =\
                                    PularPaciente(dados_Pacientes, listaEsperaPacientePrioritarioOrtopedia[0][5],
                                                  listaEsperaPacientePrioritarioOrtopedia)
                    elif(chama_comum):
                        print("Próxima senha do consultório de ORTOPEDIA:")
                        print(listaEsperaPacienteComumOrtopedia[0][5], "-", listaEsperaPacienteComumOrtopedia[0][1],
                              "- Consultório de Ortopedia")
                        while(comparecimento!="n" and comparecimento!="N" and comparecimento!="s" and comparecimento!="S"):
                            comparecimento=input("O paciente compareceu? Digite 'N' para voltar ao menu e pular paciente. "
                                        "Digite 'S' para continuar com o atendimento\n")
                            if(comparecimento == "S" or comparecimento == "s"):
                                paciente_em_antendimento_Ortopedia = listaEsperaPacienteComumOrtopedia[0]
                                hora_atendimento_Ortopedia = SolicitarHora()
                                minuto_atendimento_Ortopedia = SolicitarMinuto()
                                paciente_em_antendimento_Ortopedia.append(hora_atendimento_Ortopedia)
                                paciente_em_antendimento_Ortopedia.append(minuto_atendimento_Ortopedia)
                                listaEsperaPacienteComumOrtopedia.pop(0)
                            elif(comparecimento=="n" or comparecimento=="N"):
                                dados_Pacientes, listaEsperaPacienteComumOrtopedia =\
                                    PularPaciente(dados_Pacientes, listaEsperaPacienteComumOrtopedia[0][5],
                                                  listaEsperaPacienteComumOrtopedia)
                else:
                    print("Não há pacientes na lista de espera de ortopedia, ou já possui um paciente sendo atendido")
                    break
            break
    return paciente_em_antendimento_Ortopedia, paciente_em_antendimento_Endocrinologia, \
           paciente_em_antendimento_Dermatologia, hora_atendimento_Dermatologia, \
           minuto_atendimento_Dermatologia, hora_atendimento_Endocrinologia, \
           minuto_atendimento_Endocrinologia, hora_atendimento_Ortopedia, \
           minuto_atendimento_Ortopedia, listaEsperaPacienteComumDermatologia, \
           listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia, \
           listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia, \
           listaEsperaPacientePrioritarioOrtopedia, dados_Pacientes, ultimo_paciente_chamado_dermatologia, \
           ultimo_paciente_chamado_endocrinologia, ultimo_paciente_chamado_ortopedia, ordem_chegada_dermatologia, \
           ordem_chegada_endocrinologia, ordem_chegada_ortopedia


def PularPaciente(dados_Pacientes, excluir_Paciente, listaEspera):

    del dados_Pacientes[excluir_Paciente]
    for i in range(len(listaEspera)):
        if(listaEspera[i][5] == excluir_Paciente):
            listaEspera.pop(i)
            break
    print("Paciente excluido do banco de dados")
    return dados_Pacientes, listaEspera
def EncerrarConsulta(paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                    paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,
                    listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,
                    listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,
                    listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes):
    opcao="0"
    while(opcao!="4"):
        print("################################################################")
        print("#                           MENU                               #")
        print("################################################################")
        print("#  [1] - Encerrar consulta do consultório de Dermatologia      #")
        print("#  [2] - Encerrar consulta do consultório de Endocrinologia    #")
        print("#  [3] - Encerrar consulta do consultório de Ortopedia         #")
        print("#  [4] - SAIR                                                  #")
        print("################################################################")
        opcao=input("Escolha uma opção: \n")

        if(opcao=="1"):
            if(paciente_em_antendimento_Dermatologia):
                if(paciente_em_antendimento_Dermatologia[0]=="c" or paciente_em_antendimento_Dermatologia[0]=="C"):
                    listaPacienteComumAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                    paciente_em_antendimento_Dermatologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoDermatologia)
                    listaPacienteComumAtendidoDermatologia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoDermatologia[tamLista-1].append(minuto)
                else:
                    listaPacientePrioritarioAtendidoDermatologia.append(paciente_em_antendimento_Dermatologia)
                    paciente_em_antendimento_Dermatologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoDermatologia)
                    listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoDermatologia[tamLista-1].append(minuto)
            break
        elif(opcao=="2"):
            if(paciente_em_antendimento_Endocrinologia):
                if(paciente_em_antendimento_Endocrinologia[5]=="c" or paciente_em_antendimento_Endocrinologia[5]=="C"):
                    Paciente_Encerrar=paciente_em_antendimento_Endocrinologia
                    listaPacienteComumAtendidoEndocrinologia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Endocrinologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoEndocrinologia)
                    listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoEndocrinologia[tamLista-1].append(minuto)
                else:
                    Paciente_Encerrar=paciente_em_antendimento_Endocrinologia
                    listaPacientePrioritarioAtendidoEndocrinologia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Endocrinologia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacientePrioritarioAtendidoEndocrinologia)
                    listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoEndocrinologia[tamLista-1].append(minuto)
            break
        elif(opcao=="3"):
            if(paciente_em_antendimento_Ortopedia):
                if(paciente_em_antendimento_Ortopedia[5]=="c" or paciente_em_antendimento_Ortopedia[5]=="C"):
                    Paciente_Encerrar=paciente_em_antendimento_Ortopedia
                    listaPacienteComumAtendidoOrtopedia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Ortopedia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacienteComumAtendidoOrtopedia)
                    listaPacienteComumAtendidoOrtopedia[tamLista-1].append(hora)
                    listaPacienteComumAtendidoOrtopedia[tamLista-1].append(minuto)
                else:
                    Paciente_Encerrar=paciente_em_antendimento_Ortopedia
                    listaPacientePrioritarioAtendidoOrtopedia.append(Paciente_Encerrar)
                    paciente_em_antendimento_Ortopedia=[]
                    hora=SolicitarHora()
                    minuto=SolicitarMinuto()
                    tamLista=len(listaPacientePrioritarioAtendidoOrtopedia)
                    listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(hora)
                    listaPacientePrioritarioAtendidoOrtopedia[tamLista-1].append(minuto)
            break

    return paciente_em_antendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,\
           paciente_em_antendimento_Ortopedia, listaPacienteComumAtendidoDermatologia,\
           listaPacienteComumAtendidoEndocrinologia, listaPacienteComumAtendidoOrtopedia,\
           listaPacientePrioritarioAtendidoDermatologia, listaPacientePrioritarioAtendidoEndocrinologia,\
           listaPacientePrioritarioAtendidoOrtopedia, dados_Pacientes

def ExibirFilaDeEspera(paciente_em_atendimento_Dermatologia, paciente_em_antendimento_Endocrinologia,
                        paciente_em_antendimento_Ortopedia, listaEsperaPacienteComumDermatologia,
                        listaEsperaPacientePrioritarioDermatologia, listaEsperaPacienteComumEndocrinologia,
                        listaEsperaPacientePrioritarioEndocrinologia, listaEsperaPacienteComumOrtopedia,
                        listaEsperaPacientePrioritarioOrtopedia):
    hora=SolicitarHora()
    minuto=SolicitarMinuto()
    from prettytable import PrettyTable
    tabela = PrettyTable(["Senha", "Nome do paciente", "Consultório", "Situação", "Tempo de espera"])

    # Alinha as colunas
    tabela.align["Senha"] = "l"
    tabela.align["Nome do paciente"] = "l"
    tabela.align["Consultório"]="l"
    tabela.align["Situação"] = "l"
    tabela.align["Tempo de espera"] = "l"

    # Deixa um espaço entre a borda das colunas e o conteúdo (default)
    tabela.padding_width = 1

    tabela=Gerar_Tabela_Pacientes_Em_Atendimento(tabela, paciente_em_atendimento_Dermatologia)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacienteComumDermatologia, hora, minuto)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacientePrioritarioDermatologia, hora, minuto)
    tabela=Gerar_Tabela_Pacientes_Em_Atendimento(tabela, paciente_em_antendimento_Endocrinologia)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacienteComumEndocrinologia, hora, minuto)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacientePrioritarioEndocrinologia, hora, minuto)
    tabela=Gerar_Tabela_Pacientes_Em_Atendimento(tabela, paciente_em_antendimento_Ortopedia)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacienteComumOrtopedia, hora, minuto)
    tabela=Gerar_Tabela_Pacientes_Em_Espera(tabela, listaEsperaPacientePrioritarioOrtopedia, hora, minuto)
    print(tabela)
def ExibirPacientesAtendidosNoDia(listaPacienteComumAtendidoDermatologia, listaPacienteComumAtendidoEndocrinologia,
                                  listaPacienteComumAtendidoOrtopedia, listaPacientePrioritarioAtendidoDermatologia,
                                  listaPacientePrioritarioAtendidoEndocrinologia, listaPacientePrioritarioAtendidoOrtopedia):
    from prettytable import PrettyTable
    tabela = PrettyTable(["Nome do paciente", "Tempo de espera na fila", "Tempo de Atendimento", "Consultório", "Médico do Consultório"])

    # Alinha as colunas
    tabela.align["Nome do paciente"] = "l"
    tabela.align["Tempo de espera na fila"] = "l"
    tabela.align["Tempo de Atendimento"]="l"
    tabela.align["Consultório"] = "l"
    tabela.align["Médico do Consultório"] = "l"

    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacienteComumAtendidoDermatologia)
    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacientePrioritarioAtendidoDermatologia)
    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacienteComumAtendidoEndocrinologia)
    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacientePrioritarioAtendidoEndocrinologia)
    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacienteComumAtendidoOrtopedia)
    tabela=Gerar_Tabela_Pacientes_Atendidos(tabela, listaPacientePrioritarioAtendidoOrtopedia)

    print(tabela)
def ExibirTempoMedioDeEsperaDosPacientes(listaPacienteComumAtendidoDermatologia, listaPacienteComumAtendidoEndocrinologia,
                                         listaPacienteComumAtendidoOrtopedia, listaPacientePrioritarioAtendidoDermatologia,
                                         listaPacientePrioritarioAtendidoEndocrinologia, listaPacientePrioritarioAtendidoOrtopedia,
                                         paciente_em_atendimento_Dermatologia, paciente_em_atendimento_Endocrinologia,
                                         paciente_em_atendimento_Ortopedia):
    from prettytable import PrettyTable
    tabela=PrettyTable()
    dados=["Tempo de espera médio de todos os pacientes do Ambulatório",
           "Tempo de espera médio dos pacientes comuns no Ambulatório",
           "Tempo de espera médio dos pacientes preferenciais no Ambulatório",
           "Tempo de espera médio dos pacientes comuns no consultório de dermatologia",
           "Tempo de espera médio dos pacientes preferenciais no consultório de dermatologia",
           "Tempo de espera médio dos pacientes comuns no consultório de endocrinologia",
           "Tempo de espera médio dos pacientes preferenciais no consultório de endocrinologia",
           "Tempo de espera médio dos pacientes comuns no consultório de ortopedia",
           "Tempo de espera médio dos pacientes preferenciais no consultório de ortopedia"]


    #Criação previas de variaveis que serão utilizadas para fazer os calculos
    hora_total_ambulatorio = 0
    minuto_total_ambulatorio = 0
    hora_paciente_comum_ambulatorio = 0
    minuto_paciente_comum_ambulatorio = 0
    hora_paciente_preferencial_ambulatorio = 0
    minuto_paciente_preferencial_ambulatorio = 0
    hora_paciente_preferencial_dermatologia = 0
    minuto_paciente_preferencial_dermatologia = 0
    hora_paciente_preferencial_endocrinologia = 0
    minuto_paciente_preferencial_endocrinologia = 0
    hora_paciente_preferencial_ortopedia = 0
    minuto_paciente_preferencial_ortopedia = 0
    hora_paciente_comum_dermatologia = 0
    minuto_paciente_comum_dermatologia = 0
    hora_paciente_comum_endocrinologia = 0
    minuto_paciente_comum_endocrinologia = 0
    hora_paciente_comum_ortopedia = 0
    minuto_paciente_comum_ortopedia = 0

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes no ambulatorio
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoDermatologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoDermatologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoEndocrinologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoEndocrinologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoOrtopedia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoOrtopedia)
    if(paciente_em_atendimento_Dermatologia):
        hora_total_ambulatorio, minuto_total_ambulatorio = \
            CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, [paciente_em_atendimento_Dermatologia])
    if(paciente_em_atendimento_Endocrinologia):
        hora_total_ambulatorio, minuto_total_ambulatorio = \
            CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, [paciente_em_atendimento_Endocrinologia])
    if(paciente_em_atendimento_Ortopedia):
        hora_total_ambulatorio, minuto_total_ambulatorio = \
            CalculaTempoTotalDeEspera(hora_total_ambulatorio, minuto_total_ambulatorio, [paciente_em_atendimento_Ortopedia])

    tempo_em_minutos_total=minuto_total_ambulatorio+(hora_total_ambulatorio*60)

    quantidade_total = len(listaPacientePrioritarioAtendidoDermatologia)+len(listaPacienteComumAtendidoDermatologia) \
                       + len(listaPacientePrioritarioAtendidoEndocrinologia)+len(listaPacienteComumAtendidoEndocrinologia)\
                       + len(listaPacientePrioritarioAtendidoOrtopedia)+len(listaPacienteComumAtendidoOrtopedia)
    if(paciente_em_atendimento_Dermatologia):
        quantidade_total+=1
    if(paciente_em_atendimento_Endocrinologia):
        quantidade_total+=1
    if(paciente_em_atendimento_Ortopedia):
        quantidade_total+=1

    media_total_ambulatorio = CalculaMedia(tempo_em_minutos_total, quantidade_total)
    media_total_ambulatorio_formatada = Formatarhora(media_total_ambulatorio)

    #Bloco de codigo para calcular a media de tempo de espera dos pacientes comuns no ambulatorio
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoDermatologia)
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoEndocrinologia)
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoOrtopedia)

    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="c" or paciente_em_atendimento_Dermatologia[5][0]=="C"):
            hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, [paciente_em_atendimento_Dermatologia])
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="c" or paciente_em_atendimento_Endocrinologia[5][0]=="C"):
            hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, [paciente_em_atendimento_Endocrinologia])
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="c" or paciente_em_atendimento_Ortopedia[5][0]=="C"):
            hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, [paciente_em_atendimento_Ortopedia])
    tempo_em_minutos_comum_ambulatorio = minuto_paciente_comum_ambulatorio+(hora_paciente_comum_ambulatorio*60)
    quantidade_comum_ambulatorio = len(listaPacienteComumAtendidoDermatologia)+len(listaPacienteComumAtendidoEndocrinologia)\
                                   +len(listaPacienteComumAtendidoOrtopedia)

    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="c" or paciente_em_atendimento_Dermatologia[5][0]=="C"):
            quantidade_comum_ambulatorio+=1
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="c" or paciente_em_atendimento_Endocrinologia[5][0]=="C"):
            quantidade_comum_ambulatorio+=1
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="c" or paciente_em_atendimento_Ortopedia[5][0]=="C"):
            quantidade_comum_ambulatorio+=1

    media_paciente_comum_ambulatorio = CalculaMedia(tempo_em_minutos_comum_ambulatorio, quantidade_comum_ambulatorio)
    media_paciente_comum_ambulatorio_formatada = Formatarhora(media_paciente_comum_ambulatorio)

    #Bloco de codigo para calcular a media de tempo de espera dos pacientes preferenciais no ambulatorio
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoDermatologia)
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = CalculaTempoTotalDeEspera\
        (hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoEndocrinologia)
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeEspera(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoOrtopedia)

    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="p" or paciente_em_atendimento_Dermatologia[5][0]=="P"):
            hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, [paciente_em_atendimento_Dermatologia])
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="p" or paciente_em_atendimento_Endocrinologia[5][0]=="P"):
            hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, [paciente_em_atendimento_Endocrinologia])
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="p" or paciente_em_atendimento_Ortopedia[5][0]=="P"):
            hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, [paciente_em_atendimento_Ortopedia])

    tempo_em_minutos_preferencial_ambulatorio = minuto_paciente_preferencial_ambulatorio+(hora_paciente_preferencial_ambulatorio*60)
    quantidade_preferencial_ambulatório = len(listaPacientePrioritarioAtendidoDermatologia)+len(listaPacientePrioritarioAtendidoEndocrinologia)\
                                          + len(listaPacientePrioritarioAtendidoOrtopedia)

    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="p" or paciente_em_atendimento_Dermatologia[5][0]=="P"):
            quantidade_preferencial_ambulatório+=1
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="p" or paciente_em_atendimento_Endocrinologia[5][0]=="P"):
            quantidade_preferencial_ambulatório+=1
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="p" or paciente_em_atendimento_Ortopedia[5][0]=="P"):
            quantidade_preferencial_ambulatório+=1

    media_paciente_preferencial_ambulatorio = CalculaMedia(tempo_em_minutos_preferencial_ambulatorio, quantidade_preferencial_ambulatório)
    media_paciente_preferencial_ambulatorio_formatada = Formatarhora(media_paciente_preferencial_ambulatorio)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes comuns do consultorio de dermatologia
    hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia, listaPacienteComumAtendidoDermatologia)
    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="c" or paciente_em_atendimento_Dermatologia[5][0]=="C"):
            hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia, [paciente_em_atendimento_Dermatologia])
    tempo_em_minutos_comum_dermatologia = minuto_paciente_comum_dermatologia+(hora_paciente_comum_dermatologia*60)
    quantidade_comum_dermatologia = len(listaPacienteComumAtendidoDermatologia)
    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="c" or paciente_em_atendimento_Dermatologia[5][0]=="C"):
            quantidade_comum_dermatologia+=1
    media_paciente_comum_dermatologia = CalculaMedia(tempo_em_minutos_comum_dermatologia, quantidade_comum_dermatologia)
    media_paciente_comum_dermatologia_formatada = Formatarhora(media_paciente_comum_dermatologia)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes preferenciais do consultorio de dermatologia
    hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia = CalculaTempoTotalDeEspera\
        (hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia, listaPacientePrioritarioAtendidoDermatologia)
    if(paciente_em_atendimento_Dermatologia):
        if(paciente_em_atendimento_Dermatologia[5][0]=="p" or paciente_em_atendimento_Dermatologia[5][0]=="P"):
            hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia, [paciente_em_atendimento_Dermatologia])

    tempo_em_minutos_preferencial_dermatologia =  minuto_paciente_preferencial_dermatologia + (hora_paciente_preferencial_dermatologia*60)
    quantidade_preferencial_dermatologia = len(listaPacientePrioritarioAtendidoDermatologia)
    media_paciente_preferencial_dermatologia = CalculaMedia( tempo_em_minutos_preferencial_dermatologia, quantidade_preferencial_dermatologia)
    media_paciente_preferencial_dermatologia_formatada = Formatarhora(media_paciente_preferencial_dermatologia)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes comuns do consultorio de endocrinologia
    hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia, listaPacienteComumAtendidoEndocrinologia)
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="c" or paciente_em_atendimento_Endocrinologia[5][0]=="C"):
            hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia, [paciente_em_atendimento_Endocrinologia])
    tempo_em_minutos_comum_endocrinologia = minuto_paciente_comum_endocrinologia+(hora_paciente_comum_endocrinologia*60)
    quantidade_comum_endocrinologia = len(listaPacienteComumAtendidoEndocrinologia)
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="c" or paciente_em_atendimento_Endocrinologia[5][0]=="C"):
            quantidade_comum_endocrinologia+=1
    media_paciente_comum_endocrinologia = CalculaMedia(tempo_em_minutos_comum_endocrinologia, quantidade_comum_endocrinologia)
    media_paciente_comum_endocrinologia_formatada = Formatarhora(media_paciente_comum_endocrinologia)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes preferenciais do consultorio de endocrinologia
    hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia = CalculaTempoTotalDeEspera\
        (hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia, listaPacientePrioritarioAtendidoEndocrinologia)
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="p" or paciente_em_atendimento_Endocrinologia[5][0]=="P"):
            hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia, [paciente_em_atendimento_Endocrinologia])

    tempo_em_minutos_preferencial_endocrinologia =  minuto_paciente_preferencial_endocrinologia + (hora_paciente_preferencial_endocrinologia*60)
    quantidade_preferencial_endocrinologia = len(listaPacientePrioritarioAtendidoEndocrinologia)
    if(paciente_em_atendimento_Endocrinologia):
        if(paciente_em_atendimento_Endocrinologia[5][0]=="p" or paciente_em_atendimento_Endocrinologia[5][0]=="P"):
            quantidade_preferencial_endocrinologia+=1
    media_paciente_preferencial_endocrinologia = CalculaMedia( tempo_em_minutos_preferencial_endocrinologia, quantidade_preferencial_endocrinologia)
    media_paciente_preferencial_endocrinologia_formatada = Formatarhora(media_paciente_preferencial_endocrinologia)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes comuns do consultorio de ortopedia
    hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia = \
        CalculaTempoTotalDeEspera(hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia, listaPacienteComumAtendidoOrtopedia)
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="c" or paciente_em_atendimento_Ortopedia[5][0]=="C"):
            hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia = \
                CalculaTempoTotalDeEspera(hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia, [paciente_em_atendimento_Ortopedia])
    quantidade_comum_ortopedia = len(listaPacienteComumAtendidoOrtopedia)
    tempo_em_minutos_comum_ortopedia = minuto_paciente_comum_ortopedia+(hora_paciente_comum_ortopedia*60)
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="c" or paciente_em_atendimento_Ortopedia[5][0]=="C"):
            quantidade_comum_ambulatorio+=1
    media_paciente_comum_ortopedia = CalculaMedia(tempo_em_minutos_comum_ortopedia, quantidade_comum_ortopedia)
    media_paciente_comum_ortopedia_formatada = Formatarhora(media_paciente_comum_ortopedia)

    #Bloco de codigo para calcular a media do tempo de espera dos pacientes preferenciais do consultorio de ortopedia
    hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia = CalculaTempoTotalDeEspera\
        (hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia, listaPacientePrioritarioAtendidoOrtopedia)
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="p" or paciente_em_atendimento_Ortopedia[5][0]=="P"):
            hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia = \
                CalculaTempoTotalDeEspera(hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia, [paciente_em_atendimento_Ortopedia])

    tempo_em_minutos_preferencial_ortopedia =  minuto_paciente_preferencial_ortopedia + (hora_paciente_preferencial_ortopedia*60)
    quantidade_preferencial_ortopedia = len(listaPacientePrioritarioAtendidoOrtopedia)
    if(paciente_em_atendimento_Ortopedia):
        if(paciente_em_atendimento_Ortopedia[5][0]=="p" or paciente_em_atendimento_Ortopedia[5][0]=="P"):
            quantidade_preferencial_ortopedia+=1
    media_paciente_preferencial_ortopedia = CalculaMedia( tempo_em_minutos_preferencial_ortopedia, quantidade_preferencial_ortopedia)
    media_paciente_preferencial_ortopedia_formatada = Formatarhora(media_paciente_preferencial_ortopedia)

    valores=[media_total_ambulatorio_formatada, media_paciente_comum_ambulatorio_formatada, media_paciente_preferencial_ambulatorio_formatada,
             media_paciente_comum_dermatologia_formatada, media_paciente_preferencial_dermatologia_formatada, media_paciente_comum_endocrinologia_formatada,
             media_paciente_preferencial_endocrinologia_formatada, media_paciente_comum_ortopedia_formatada, media_paciente_preferencial_ortopedia_formatada]

    tabela.add_column("Dados", dados)
    tabela.add_column("Valores", valores)

    # Controla o alinhamento horizontal
    tabela.align["Dados"] = "l"
    tabela.align["Valores"] = "l"

    print(tabela)

def ExibirTempoMedioDeAtendimentoDosPacientes(listaPacienteComumAtendidoDermatologia, listaPacienteComumAtendidoEndocrinologia,
                                              listaPacienteComumAtendidoOrtopedia, listaPacientePrioritarioAtendidoDermatologia,
                                              listaPacientePrioritarioAtendidoEndocrinologia, listaPacientePrioritarioAtendidoOrtopedia):
    from prettytable import PrettyTable
    tabela=PrettyTable()
    dados=["Tempo de atendimento médio de todos os pacientes do Ambulatório",
           "Tempo de atendimento médio dos pacientes comuns no Ambulatório",
           "Tempo de atendimento médio dos pacientes preferenciais no Ambulatório",
           "Tempo de atendimento médio dos pacientes comuns no consultório de dermatologia",
           "Tempo de atendimento médio dos pacientes preferenciais no consultório de dermatologia",
           "Tempo de atendimento médio dos pacientes comuns no consultório de endocrinologia",
           "Tempo de atendimento médio dos pacientes preferenciais no consultório de endocrinologia",
           "Tempo de atendimento médio dos pacientes comuns no consultório de ortopedia",
           "Tempo de atendimento médio dos pacientes preferenciais no consultório de ortopedia"]

    #Criação previas de variaveis que serão utilizadas para fazer os calculos
    hora_total_ambulatorio = 0
    minuto_total_ambulatorio = 0
    hora_paciente_comum_ambulatorio = 0
    minuto_paciente_comum_ambulatorio = 0
    hora_paciente_preferencial_ambulatorio = 0
    minuto_paciente_preferencial_ambulatorio = 0
    hora_paciente_preferencial_dermatologia = 0
    minuto_paciente_preferencial_dermatologia = 0
    hora_paciente_preferencial_endocrinologia = 0
    minuto_paciente_preferencial_endocrinologia = 0
    hora_paciente_preferencial_ortopedia = 0
    minuto_paciente_preferencial_ortopedia = 0
    hora_paciente_comum_dermatologia = 0
    minuto_paciente_comum_dermatologia = 0
    hora_paciente_comum_endocrinologia = 0
    minuto_paciente_comum_endocrinologia = 0
    hora_paciente_comum_ortopedia = 0
    minuto_paciente_comum_ortopedia = 0

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes no ambulatorio
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoDermatologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoDermatologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoEndocrinologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoEndocrinologia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacienteComumAtendidoOrtopedia)
    hora_total_ambulatorio, minuto_total_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_total_ambulatorio, minuto_total_ambulatorio, listaPacientePrioritarioAtendidoOrtopedia)

    tempo_em_minutos_total=minuto_total_ambulatorio+(hora_total_ambulatorio*60)

    quantidade_total = len(listaPacientePrioritarioAtendidoDermatologia)+len(listaPacienteComumAtendidoDermatologia) \
                       + len(listaPacientePrioritarioAtendidoEndocrinologia)+len(listaPacienteComumAtendidoEndocrinologia)\
                       + len(listaPacientePrioritarioAtendidoOrtopedia)+len(listaPacienteComumAtendidoOrtopedia)

    media_total_ambulatorio = CalculaMedia(tempo_em_minutos_total, quantidade_total)
    media_total_ambulatorio_formatada = Formatarhora(media_total_ambulatorio)

    #Bloco de codigo para calcular a media de tempo de atendimento dos pacientes comuns no ambulatorio
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoDermatologia)
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoEndocrinologia)
    hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_ambulatorio, minuto_paciente_comum_ambulatorio, listaPacienteComumAtendidoOrtopedia)

    tempo_em_minutos_comum_ambulatorio = minuto_paciente_comum_ambulatorio+(hora_paciente_comum_ambulatorio*60)
    quantidade_comum_ambulatorio = len(listaPacienteComumAtendidoDermatologia)+len(listaPacienteComumAtendidoEndocrinologia)\
                                   +len(listaPacienteComumAtendidoOrtopedia)

    media_paciente_comum_ambulatorio = CalculaMedia(tempo_em_minutos_comum_ambulatorio, quantidade_comum_ambulatorio)
    media_paciente_comum_ambulatorio_formatada = Formatarhora(media_paciente_comum_ambulatorio)

    #Bloco de codigo para calcular a media de tempo de atendimento dos pacientes preferenciais no ambulatorio
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoDermatologia)
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = CalculaTempoTotalDeAtendimento\
        (hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoEndocrinologia)
    hora_paciente_preferencial_ambulatorio, minuto_paciente_comum_ambulatorio = \
        CalculaTempoTotalDeAtendimento(hora_paciente_preferencial_ambulatorio, minuto_paciente_preferencial_ambulatorio, listaPacientePrioritarioAtendidoOrtopedia)

    tempo_em_minutos_preferencial_ambulatorio = minuto_paciente_preferencial_ambulatorio+(hora_paciente_preferencial_ambulatorio*60)
    quantidade_preferencial_ambulatório = len(listaPacientePrioritarioAtendidoDermatologia)+len(listaPacientePrioritarioAtendidoEndocrinologia)\
                                          + len(listaPacientePrioritarioAtendidoOrtopedia)

    media_paciente_preferencial_ambulatorio = CalculaMedia(tempo_em_minutos_preferencial_ambulatorio, quantidade_preferencial_ambulatório)
    media_paciente_preferencial_ambulatorio_formatada = Formatarhora(media_paciente_preferencial_ambulatorio)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes comuns do consultorio de dermatologia
    hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_dermatologia, minuto_paciente_comum_dermatologia, listaPacienteComumAtendidoDermatologia)

    tempo_em_minutos_comum_dermatologia = minuto_paciente_comum_dermatologia+(hora_paciente_comum_dermatologia*60)
    quantidade_comum_dermatologia = len(listaPacienteComumAtendidoDermatologia)

    media_paciente_comum_dermatologia = CalculaMedia(tempo_em_minutos_comum_dermatologia, quantidade_comum_dermatologia)
    media_paciente_comum_dermatologia_formatada = Formatarhora(media_paciente_comum_dermatologia)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes preferenciais do consultorio de dermatologia
    hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia = CalculaTempoTotalDeAtendimento\
        (hora_paciente_preferencial_dermatologia, minuto_paciente_preferencial_dermatologia, listaPacientePrioritarioAtendidoDermatologia)

    tempo_em_minutos_preferencial_dermatologia =  minuto_paciente_preferencial_dermatologia + (hora_paciente_preferencial_dermatologia*60)
    quantidade_preferencial_dermatologia = len(listaPacientePrioritarioAtendidoDermatologia)
    media_paciente_preferencial_dermatologia = CalculaMedia( tempo_em_minutos_preferencial_dermatologia, quantidade_preferencial_dermatologia)
    media_paciente_preferencial_dermatologia_formatada = Formatarhora(media_paciente_preferencial_dermatologia)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes comuns do consultorio de endocrinologia
    hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_endocrinologia, minuto_paciente_comum_endocrinologia, listaPacienteComumAtendidoEndocrinologia)

    tempo_em_minutos_comum_endocrinologia = minuto_paciente_comum_endocrinologia+(hora_paciente_comum_endocrinologia*60)
    quantidade_comum_endocrinologia = len(listaPacienteComumAtendidoEndocrinologia)

    media_paciente_comum_endocrinologia = CalculaMedia(tempo_em_minutos_comum_endocrinologia, quantidade_comum_endocrinologia)
    media_paciente_comum_endocrinologia_formatada = Formatarhora(media_paciente_comum_endocrinologia)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes preferenciais do consultorio de endocrinologia
    hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia = CalculaTempoTotalDeAtendimento\
        (hora_paciente_preferencial_endocrinologia, minuto_paciente_preferencial_endocrinologia, listaPacientePrioritarioAtendidoEndocrinologia)

    tempo_em_minutos_preferencial_endocrinologia =  minuto_paciente_preferencial_endocrinologia + (hora_paciente_preferencial_endocrinologia*60)
    quantidade_preferencial_endocrinologia = len(listaPacientePrioritarioAtendidoEndocrinologia)

    media_paciente_preferencial_endocrinologia = CalculaMedia( tempo_em_minutos_preferencial_endocrinologia, quantidade_preferencial_endocrinologia)
    media_paciente_preferencial_endocrinologia_formatada = Formatarhora(media_paciente_preferencial_endocrinologia)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes comuns do consultorio de ortopedia
    hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia = \
        CalculaTempoTotalDeAtendimento(hora_paciente_comum_ortopedia, minuto_paciente_comum_ortopedia, listaPacienteComumAtendidoOrtopedia)

    quantidade_comum_ortopedia = len(listaPacienteComumAtendidoOrtopedia)
    tempo_em_minutos_comum_ortopedia = minuto_paciente_comum_ortopedia+(hora_paciente_comum_ortopedia*60)

    media_paciente_comum_ortopedia = CalculaMedia(tempo_em_minutos_comum_ortopedia, quantidade_comum_ortopedia)
    media_paciente_comum_ortopedia_formatada = Formatarhora(media_paciente_comum_ortopedia)

    #Bloco de codigo para calcular a media do tempo de atendimento dos pacientes preferenciais do consultorio de ortopedia
    hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia = CalculaTempoTotalDeAtendimento\
        (hora_paciente_preferencial_ortopedia, minuto_paciente_preferencial_ortopedia, listaPacientePrioritarioAtendidoOrtopedia)

    tempo_em_minutos_preferencial_ortopedia =  minuto_paciente_preferencial_ortopedia + (hora_paciente_preferencial_ortopedia*60)
    quantidade_preferencial_ortopedia = len(listaPacientePrioritarioAtendidoOrtopedia)
    media_paciente_preferencial_ortopedia = CalculaMedia( tempo_em_minutos_preferencial_ortopedia, quantidade_preferencial_ortopedia)
    media_paciente_preferencial_ortopedia_formatada = Formatarhora(media_paciente_preferencial_ortopedia)

    valores=[media_total_ambulatorio_formatada, media_paciente_comum_ambulatorio_formatada, media_paciente_preferencial_ambulatorio_formatada,
             media_paciente_comum_dermatologia_formatada, media_paciente_preferencial_dermatologia_formatada, media_paciente_comum_endocrinologia_formatada,
             media_paciente_preferencial_endocrinologia_formatada, media_paciente_comum_ortopedia_formatada, media_paciente_preferencial_ortopedia_formatada]

    tabela.add_column("Dados", dados)
    tabela.add_column("Valores", valores)

    # Controla o alinhamento horizontal do texto contido na tabela
    tabela.align["Dados"] = "l"
    tabela.align["Valores"] = "l"

    print(tabela)
