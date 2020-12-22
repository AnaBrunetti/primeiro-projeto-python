import os
import json
os.system('cls')


#função para calcular a media do aluno.
def media (nota1, nota2):
    return ((nota1 + nota2)/2)

#função para calcular se o aluno foi aprovado ou reprovado.
def resultado (media, media_min):
    if media(nota1, nota2) >= media_min:
         resultado = "Aprovado"
    else:
        resultado = "Reprovado"
    return resultado

#inicialização de dicionários e listas.

lista_nome_import = []
lista_export = []
lista_nome = []
dic_cadastro = {}
lista_nome2 = []

#informações pedidas no cadastro, dentro de uma lista.
cadastro=["NOME COMPLETO", "DATA DE NASCIMENTO", "NOME DO PAI", "NOME DA MÃE", "SEXO" , "ESTADO RESIDENTE", "CIDADE RESIDENTE", "TELEFONE", "NOTA 1", "NOTA 2", "MEDIA", "RESULTADO"]

#iniciador da condição.
opção = "S"
#condição.
while (opção.upper() == "S"):
    #menu.
    print("Bem Vindo !!\n Menu: \n 1- Novo Cadastro\n 2- Exclussão de Cadastro\n 3- Visualização de alunos em ordem alfabetica. \n 4- Exportação. \n 5- Visualização de cadastros exportados")
    escolha=int(input(""))

    #condição das escolhas.
    while (escolha != 1) and (escolha != 2) and (escolha != 3) and (escolha != 4) and (escolha != 5):
        print("Opção inválida. Digite novamente.")
        escolha=int(input(""))

    else:
        os.system('cls')

        #condições e comandos da escolha 1.
        if escolha == 1:
            acesso="negado"
            while acesso == "negado":
                senha=(input("Digite a senha: "))
                
                if senha == "1234":
                    acesso = "permitido"
                    os.system('cls')
                    print("ACESSO PERMITIDO.")
                    nome=(input("Insira o nome completo: "))
                    lista_nome2.append(nome.upper())
                    data_nasc=(input("Informe a data de nascimento (ex: 20/3/1999): "))
                    nome_do_pai=(input("Insira o nome do pai. Caso não possuir, digite <não possui>. : "))
                    nome_da_mae=(input("Insira o nome da mãe. Caso não possuir, digite <não possui>. : "))
                    
                    sexo=(input("Informe o sexo, <F> para feminino, <M> para masculino ou <O> para outro. : "))
                    while (sexo.upper() != "F") and (sexo.upper() != "M") and (sexo.upper() != "O"):
                        print("Sexo inválido. Por favor, informe novamente.")
                        sexo=(input("Informe o sexo: ")) 
                    
                    estado_res=(input("Insira a UF residente: "))
                    cidade_res=(input("Insira a cidade residente: "))
                    telefone=int(input("Insira o telefone: "))
                    nota1=float(input("Informe o valor da nota 1: "))
                    nota2=float(input("Informe o valor da nota 2: "))
                    media_min=float(input("Informe a média mínima para ser aprovado: "))

                    dic_cadastro[nome.upper()] = {cadastro[0]  : nome.upper()}, {cadastro[1]  : data_nasc.upper()}, {cadastro[2]  : nome_do_pai.upper()}, {cadastro[3]  : nome_da_mae.upper()}, {cadastro[4]  : sexo.upper()} , {cadastro[5]  : estado_res.upper()}, {cadastro[6]  : cidade_res.upper()}, {cadastro[7]  : telefone}, {cadastro[8]  : nota1}, {cadastro[9]  : nota2}, {cadastro[10]  : media(nota1, nota2)}, {cadastro[11]  : resultado(media, media_min)}
                    
                
                else:
                    print("ACESSO NEGADO.")

        #condições e comandos da escolha 2.
        elif escolha == 2:
            acesso="negado"
            while acesso == "negado":
                senha=(input("Digite a senha: "))
                
                if senha == "1234":
                    os.system('cls')
                    acesso = "permitido"
                    print("ACESSO PERMITIDO. \n 2-Exclussão de Cadastro. \n Lembre-se, caso já exportado, não poderá ser excluído.\n Por favor, digite o Nome do aluno: \n")
                    nome = input("")
                    try:
                        if dic_cadastro[nome.upper()] != "":
                            del dic_cadastro[nome.upper()]
                            lista_nome2.remove(nome.upper())
                            


                        print("Removido com sucesso.")
                    except KeyError:
                        print("Cadastro não encontrado.")
                
                else:
                    print("ACESSO NEGADO.")


        #condições e comandos da escolha 3.
        elif escolha == 3:
            acesso="negado"
            while acesso == "negado":
                senha=(input("Digite a senha: "))
                if senha == "1234":
                    os.system('cls')
                    acesso = "permitido"
                    print("ACESSO PERMITIDO. \n 3- Visualização de alunos em ordem alfabetica.\n")
                    
                    try:
                            op2 = open("lista_nome.json", "r", encoding= "utf-8")
                            ln = json.load(op2)
                            ln.sort()
                            str(ln).replace('[]', "")
                            op2.close()
                            lista_nome_import.clear()
                            for item in ln:
                                lista_nome_import.append(item)
                            
                            lista_nome_import.sort()


                            print("Esses são todos os alunos cadastrados:")
                            cont = 1
                            for item in lista_nome_import:
                                print(f"{cont} - {item}")
                                cont = cont + 1
                            
                            
                    
                    except ValueError:
                        print("Não existem alunos cadastrados. \n")
                                  
                else:
                    print("ACESSO NEGADO.")      

        #condições e comandos da escolha 4.
        elif escolha == 4:
            acesso="negado"
            while acesso == "negado":
                senha=(input("Digite a senha: "))
                if senha == "1234":
                    os.system('cls')
                    acesso = "permitido"
                    print("ACESSO PERMITIDO. \n 4- Exportação de Cadastro.")

                    print("Deseja exportar os cadastro inseridos ? <s>im ou <n>ão")
                    escolha2 = (input(""))
                    if (escolha2.upper() == "S"):
                        
                        ##condições e comandos de exportação e importação.
                        if dic_cadastro != "":
                            
                            
                            lista_export.clear()
                            lista_export.append(str(dic_cadastro))
                            str(lista_export).strip('[]')

                            

                            try:
                                op = open ("cadastro.json", "r", encoding="utf-8")
                                le = json.load(op)
                                op.close()
                                lista_export.append(le)
                                str(lista_export).strip('[]')
                            
                            except ValueError:
                                f = open ("cadastro.json", "w")
                                json.dump(lista_export,f, indent= 4)   
                            
                                f.close()

                            f = open ("cadastro.json", "w")
                            json.dump(lista_export,f, indent= 4)   
                            
                            f.close()
                            lista_nome.clear()
                            
                            for item in lista_nome2:
                                lista_nome.append(item)
                            
                            try:
                                op2 = open("lista_nome.json", "r", encoding= "utf-8")
                                ln = json.load(op2)
                                op2.close()
                                for item in ln:
                                    for item2 in lista_nome2:
                                        if item != item2:
                                            lista_nome.append(item)


                            except ValueError:

                                h = open ("lista_nome.json", "w")
                                json.dump(lista_nome,h, indent= 4)   
                            
                                h.close()

                            
                            h = open ("lista_nome.json", "w")
                            json.dump(lista_nome,h, indent= 4)   
                            
                            h.close()

                            dic_cadastro.clear()
                            lista_export.clear()
                            lista_nome.clear()
                            lista_nome2.clear()

                            

                        print("Cadastros Exportados com sucesso")

                    elif (escolha2.upper() != "N") and (escolha2.upper() != "S"):
                        print("Escolha inválida.")


                else:
                    print("ACESSO NEGADO.")                                    

        #condições e comandos da escolha 5.
        elif escolha == 5:
            acesso="negado"
            while acesso == "negado":
                senha=(input("Digite a senha: "))
                if senha == "1234":
                    os.system('cls')
                    acesso = "permitido"
                    print("ACESSO PERMITIDO. \n 5- Visualização de cadastros exportado.")

                    print("Esses são todos os cadastros exportados via JSON :")
                    op = open ("cadastro.json", "r", encoding= "utf-8")
                    str(op).strip('[]')
                    li = json.load(op)
                    str(li).strip('[]')
                    op.close()
                    print(str(li).replace("{","\n").replace("}", "\n").replace("," , "").replace("]" , "").replace("[", "").replace("'", "").replace("(", "").replace(")", ""))
                    
               
                else:
                    print("ACESSO NEGADO.")

    #condições e comandos para o usuário decidir se continua ou não a inserção de informações.
    print("Deseja realizar outra operação ? <S> para sim ou <N> para não.")
    opção=(input(""))
    os.system('cls')
    cont = 0


else: 
    if (opção.upper() == "N"):
        print("Programa Finalizado.")

    else:
        print("Opção inválida. Por favor reinicie o programa.")
        print("Programa Finalizado.")
