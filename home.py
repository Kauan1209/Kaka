import sys
import os
import time
#ESCOLHER O QUE QUER ABRIR

print('Meunu de Estudo Enem.     by: Kauan')

menu = input('''
Qual menu você gostaria de acessar:

1 = Matemática
2 = Biologia
3 = Química
4 = Física
5 = Historía
6 = Geografia
7 = Filosofia
8 = Sociologia
9 = Português
''')

if menu == '1':
    
    acessar = input('''
    Acessar:
    1 = Matematica basica
    2 = Estatistica
    3 = Analise combinatoria
    4 = Probabilidade
    5 = Geometria
    6 = Trigonometria
    7 = PA E PG
    8 = Função
    9 = Equação
    10 = Matemática Financeira



     ''')

    time.sleep(1)

    print('='*50)
    print('Processando...')
    print('='*50)

    time.sleep(1)

     #Abrir aplicativo ou programa a partir da palavra.

            
    if acessar == '1':
        print(os.startfile('file:///C:/Users/kkaua/Downloads/cronogramaRENATOPALMEIRA.pdf'))
        print(os.startfile('https://www.youtube.com/watch?v=ddZHkCUcYRM&ab_channel=UmbertoMannarino')) #Matematica basica
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Matematica Basica.docx'))

    elif acessar == '2':   
        print(os.startfile('https://www.youtube.com/watch?v=CG_AGULJJz8')) #Estatistca
        print(os.startfile('https://www.youtube.com/watch?v=tuzbYoeum7E'))
        print(os.startfile('https://www.coladaweb.com/matematica/estatistica'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Estatistica.docx'))

    elif acessar == '3':
        print(os.startfile('https://www.youtube.com/watch?v=6V3tvH6gw0Y')) #Analise Combinatoria
        print(os.startfile('https://www.youtube.com/watch?v=8RScR7dKsgQ'))
        print(os.startfile('https://brasilescola.uol.com.br/matematica/analise-combinatoria.htm')) 
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Analise Combinatoria.docx'))

    elif acessar == '4':
        print(os.startfile('https://www.youtube.com/watch?v=blEUTcx16N8')) # Probabilidade
        print(os.startfile('https://www.youtube.com/watch?v=8g571hUvgeo'))
        print(os.startfile('https://www.todamateria.com.br/probabilidade/'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Probabilidade.docx'))

    elif acessar == '5':
        print(os.startfile('https://www.youtube.com/watch?v=JRsDEkW_6O0'))
        print(os.startfile('https://geekiegames.geekie.com.br/blog/geometria-enem-resumo/'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Geometria.docx'))   

    elif acessar == '6':
        print(os.startfile('https://www.youtube.com/watch?v=7rVOU1fQnVE')) # Trigonometria
        print(os.startfile('https://www.youtube.com/watch?v=4sTUs4ll3dI'))
        print(os.startfile('https://www.todamateria.com.br/trigonometria/'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Trigonometria.docx'))

    elif acessar == '7':
        print(os.startfile('https://www.youtube.com/watch?v=dCZdpm9AO9c')) #PA E PG 
        print(os.startfile('https://mundoeducacao.uol.com.br/matematica/progressao.htm'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo PA e PG.docx')) 

    elif acessar == '8':
        print(os.startfile('https://www.youtube.com/watch?v=4UhpJjFJ0N0')) # Funçoes
        print(os.startfile('https://brasilescola.uol.com.br/matematica/funcoes.htm'))
        print(os.startfile('https://www.youtube.com/watch?v=hgKTmAO-k7E'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Funçoes.docx'))

    elif acessar == '9':
        print(os.startfile('https://www.youtube.com/watch?v=UAXyCXpyDTM')) # Equação
        print(os.startfile('https://brasilescola.uol.com.br/o-que-e/matematica/o-que-e-equacao.htm#:~:text=Equa%C3%A7%C3%A3o%20%C3%A9%20uma%20express%C3%A3o%20alg%C3%A9brica,n%C3%BAmeros%20por%20meio%20de%20equa%C3%A7%C3%B5es.'))                   
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Equação.docx'))

    elif acessar == '10':
        print(os.startfile(('https://www.youtube.com/watch?v=6xaj2E__p2c'))) # Matematica financeira
        print(os.startfile('https://www.youtube.com/watch?v=vxKV2UZkKm8'))
        print(os.startfile('https://www.todamateria.com.br/matematica-financeira-conceitos-formulas/#:~:text=A%20matem%C3%A1tica%20financeira%20%C3%A9%20a,conhecer%20suas%20aplica%C3%A7%C3%B5es%20%C3%A9%20fundamental.'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Resumo Matematica Financeira.docx'))

    else:
            exit()            

if menu == '2':

    acessar = input('''
    Acessar:
    1 = Ecologia
    2 = Origem e Evolução
    3 = Bioquímica
    4 = Citologia
    5 = Ácidos Nucleos
    6 = Metabolismo Energético
    7 = Génetica
    8 = Taxonomia
    9 = Fisiologia
    10 = Zoologia
    ''')
    
    
    time.sleep(1)

    print('='*50)
    print('Processando...')
    print('='*50)

    time.sleep(1)
    
    
    
    if acessar == '1':
        print(os.startfile('https://www.youtube.com/watch?v=5vX_ZSKpHjw'))
        print(os.startfile('https://querobolsa.com.br/enem/biologia/ecologia'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Ecologia.docx'))

    elif acessar == '2':
        print(os.startfile('https://www.youtube.com/watch?v=4WO-A_GaA1o'))
        print(os.startfile('https://www.youtube.com/watch?v=xIqT3gDLGxE'))
        print(os.startfile('https://www.youtube.com/watch?v=piRSx5SvYv8'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjk8P7-2ZHuAhXhD7kGHV1SAqkQFjAAegQIBhAC&url=https%3A%2F%2Fquerobolsa.com.br%2Fenem%2Fbiologia%2Forigem-da-vida&usg=AOvVaw2z7CbkWiZZS02kkclaQrIk'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwi-tJmO2pHuAhUCE7kGHc3mDOYQFjAAegQIBhAC&url=https%3A%2F%2Fquerobolsa.com.br%2Fenem%2Fbiologia%2Fevolucao&usg=AOvVaw2lAWl95DmnsbOmJVyAvn0C'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Origem e Evolução.docx'))
    
    elif acessar == '3':
        print(os.startfile('https://www.youtube.com/watch?v=xStiJXvGYEM&list=PLXXIkklJqmKlb1KTGx8mpBQN3we6K7tkb'))
        print(os.startfile('https://brasilescola.uol.com.br/biologia/bioquimica.htm'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Bioquimica.docx'))

    elif acessar == '4':
        print(os.startfile('https://www.youtube.com/watch?v=c8fXVU8J_3M'))
        print(os.startfile('https://www.youtube.com/watch?v=rjH2xzCwNx0'))
        print(os.startfile('https://www.youtube.com/watch?v=6JTxkhEzbz4'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjihJqe4JHuAhWyEbkGHVBHAdYQFjAHegQIEBAC&url=https%3A%2F%2Fwww.todamateria.com.br%2Fcitologia%2F%23%3A~%3Atext%3DA%2520Citologia%2520ou%2520Biologia%2520Celular%2Cdo%2520microsc%25C3%25B3pio%2520s%25C3%25A3o%2520fatos%2520relacionados.&usg=AOvVaw2SmgL02iqulTeqd662iiJx'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Citologia.docx'))
    
    elif acessar == '5':
        print(os.startfile('https://www.youtube.com/watch?v=Z4CIF570jFo'))
        print(os.startfile('https://www.youtube.com/watch?v=LFqaBPFXAh0'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiUi8TH4JHuAhXFHbkGHWU0BUEQFjAHegQILxAC&url=https%3A%2F%2Fbrasilescola.uol.com.br%2Fbiologia%2Facidos-nucleicos.htm%23%3A~%3Atext%3DOs%2520%25C3%25A1cidos%2520nucleicos%2520podem%2520ser%2Co%2520%25C3%25A1cido%2520ribonucleico%2520(RNA).&usg=AOvVaw2fNMDIwtoG1mBXWgPgD97l'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Acidos Nucleos.docx'))
    
    elif acessar == '6':
        print(os.startfile('https://www.youtube.com/watch?v=QwYZNRiTk4s'))
        print(os.startfile('https://www.youtube.com/watch?v=fB643XtE5TQ'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjx-5jh4JHuAhXKH7kGHcCUCW0QFjAFegQICxAC&url=https%3A%2F%2Fwww.todamateria.com.br%2Fmetabolismo-energetico%2F%23%3A~%3Atext%3DO%2520metabolismo%2520energ%25C3%25A9tico%2520%25C3%25A9%2520o%2CS%25C3%25A3o%2520rea%25C3%25A7%25C3%25B5es%2520de%2520s%25C3%25ADntese.&usg=AOvVaw0LQnVj3wn5e5sbv8i1eh4k'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Mentabolismo Energetico.docx'))

    elif acessar == '7':
        print(os.startfile('https://www.youtube.com/watch?v=Mf47u0uIsjg'))
        print(os.startfile('https://www.youtube.com/watch?v=-Vv3USW7iRU'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiRvf7r4JHuAhXfHrkGHQEbAJ8QFjACegQIExAC&url=https%3A%2F%2Fwww.todamateria.com.br%2Fintroducao-a-genetica%2F%23%3A~%3Atext%3DEle%2520representa%2520a%2520constitui%25C3%25A7%25C3%25A3o%2520gen%25C3%25A9tica%2Cmais%2520sobre%2520Fen%25C3%25B3tipo%2520e%2520Gen%25C3%25B3tipo.&usg=AOvVaw2BxTfhRTrFanOZJXm3y1WA'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Genetica.docx'))

    elif acessar == '8':
        print(os.startfile('https://www.youtube.com/watch?v=gcrn43B5HK8'))
        print(os.startfile('https://www.youtube.com/watch?v=eCEOc7J_nqU'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiNheyP4ZHuAhVdJrkGHfLaCgcQFjAKegQIARAC&url=https%3A%2F%2Fwww.biologianet.com%2Fbiodiversidade%2Fclassificacao-biologica-taxonomia.htm&usg=AOvVaw3X2XwuMBueHewHSXz92zBU'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Taxonomia.docx'))

    elif acessar == '9':
        print(os.startfile('https://www.youtube.com/watch?v=1E8EOECv4mY'))
        print(os.startfile('https://www.youtube.com/watch?v=6aEbi_MZnfM'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjYpcuq4ZHuAhVzHrkGHStRCWMQFjAQegQIBRAC&url=https%3A%2F%2Fbrasilescola.uol.com.br%2Fbiologia%2Ffisiologia.htm&usg=AOvVaw1tBD9zlqQ6VZFBcY7uLVPh'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Fisiologia.docx'))

    elif acessar == '10':
        print(os.startfile('https://www.youtube.com/watch?v=Ei5PWJrX9To'))
        print(os.startfile('https://www.youtube.com/watch?v=wX2T2CaVmaA&list=PLj4yVuRqCKGEqZKk3heq70oIw9eWUnLrg'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiMsNrM4ZHuAhU8HrkGHUQXDbQQFjABegQIDRAC&url=https%3A%2F%2Fwww.infoescola.com%2Fbiologia%2Fzoologia%2F%23%3A~%3Atext%3DZoologia%2520%25C3%25A9%2520a%2520ci%25C3%25AAncia%2520que%2520estuda%2520a%2520vida%2520animal.&usg=AOvVaw3UTYLcX0TRxBcsqhAWbuk3'))
        print(os.startfile(r'C:\Users\kkaua\Documents\Resumos ENEM 2021\Biologia\Resumo Zoologia.docx'))


    else:
        exit()
            
if menu == '3':
    
    acessar = input('''
    
    Acessar:
    
    1 = Estudo da Materia
    2 = Estrutura Atômica
    3 = Função Inorgânica
    4 = Termoquimica
    5 = Equlíbrio Química
    6 = Quiímica Orgânica
    7 = Reações Orgânica
    8 = Isomeria
    9 = Química Ambiental
    10 = Estequiometria
    
    ''')

    if acessar == '1'
        print(os.startfile('https://www.youtube.com/watch?v=jS6yUf0bSKg&list=PLLRm2uQu-csvkfjK1O_xPKtSsc0hqjTg5'))
        print(os.startfile('https://www.youtube.com/watch?v=isPzCiQ0WEs'))
        print(os.startfile('https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwiRzN_E15TuAhUBGbkGHVwZBXAQFjAEegQIEBAC&url=https%3A%2F%2Fmundoeducacao.uol.com.br%2Fquimica%2Fintroducao-quimica.htm%23%3A~%3Atext%3DMat%25C3%25A9ria%252C%2520no%2520estudo%2520de%2520Qu%25C3%25ADmica%2Cportanto%252C%2520tem%2520volume%2520e%2520massa.&usg=AOvVaw0YP2oRP8KXV1EEVx4DsWJB'))
        print(os.startfile(''))

    elif acessar == '2'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
    
    elif acessar == '3'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '4'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '5'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '6'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '7'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '8'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
    
    elif acessar == '9'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    elif acessar == '10'
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))
        print(os.startfile(''))

    else:
        exit()

else:
    exit()
