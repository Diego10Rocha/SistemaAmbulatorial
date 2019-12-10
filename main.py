from Funcoes import *;
opcao=0
contadorcomum=1
contadorpreferencial=1
listaPacienteComum=[]
listaPacientePrioritario=[]
while(opcao!=9):
    MENU()
    opcao=input("Escolha uma opção\n")
    boolOpcao=VerificarInt(opcao)
    opcao=ValidarOpcao(boolOpcao, opcao)
    if(opcao==1):
        pacientes=(EmitirSenha(contadorcomum, contadorpreferencial))
        if(pacientes[0]=="c" or pacientes[0]=="C"):
            listaPacienteComum.append(pacientes)
            contadorcomum+=1
        elif(pacientes[0]=="p" or pacientes[0]=="P"):
            listaPacientePrioritario.append(pacientes)
            contadorpreferencial+=1
        print(listaPacienteComum)
    elif(opcao==2):
        ChamarPacienteParaAtendimento()
    elif(opcao==3):
        PularPaciente()
    elif(opcao==4):
        EncerrarConsulta()
    elif(opcao==5):
        ExibirFilaDeEspera()
    elif(opcao==6):
        ExibirPacientesAtendidosNoDia()
    elif(opcao==7):
        ExibirTempoMedioDeEsperaDosPacientes()
    elif(opcao==8):
        ExibirTempoMedioDeAtendimentoDosPacientes()
