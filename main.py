print('_'*65)
print('                 TESTE SINTOMAS DA DENGUE'           )
print('_'*65)
print(' ')
print('Olá! Te faremos algumas perguntas relacionadas à Dengue\ne por meio delas te passar algumas orientações.')
print("_"*65)

p_doenca = int(input('Possui alguma doença, como Diabetes ou Hipertensão?\nCaso sim digite 1, caso não 0\n'))
print(' ')

sint1 = int(input('Está com febre ou dor de cabeça na região dos olhos?\nCaso sim digite 1, caso não 0\n'))
print(' ')

sint2 = int(input('Sente dor muscular, cansaço ou náuseas?\nCaso sim digite 1, caso não 0\n'))
print(' ')

sint3 = int(input('Tem dor abdominal, diarréia ou vermelhidão pelo corpo?\nCaso sim digite 1, caso não 0\n'))
print(' ')

result = p_doenca + sint1 + sint2 + sint3
if (result == 4):
    print('Atenção! Você apresenta todos sintomas da Dengue, recomendamos que vá ao médico mais próximo\ne receba o tratamento o quanto antes!')
elif (result == 3):
        print('Você apresenta a maioria dos sintomas, recomendamos que vá ao médico para que\nreceba o diagnóstico completo e faça o tratamento.')
elif (result <= 2 and result >= 1):
            print('Você apresenta alguns sintomas, recomendamos que fique de repouso e se mantenha hidratado.\nObserve se há alguma piora no seu caso, se sim, não hesite em ir ao hospital.')
elif (result == 0):
                print('Você não apresenta nenhum sintoma, mas observe os seus familiares e vizinhos se há casos pela região\nlembre-se de tomar todas as providências para colaborar com o combate a Dengue.')
print('-'*130)
print('E lembre-se! A prevenção da dengue pode ser feita com práticas simples que evitam principalmente a reprodução do mosquito\ntransmissor através da eliminação de objetos que acumulem água parada como pneus, garrafas e plantas.')
print('-'*130)