import random

ali_nome = input('Qual o nome do seu personagem? ')
ali_vida = int(input('\nQuantos pontos de vida têm seu personagem? O limite é 100. '))
while ali_vida >= 101:
	ali_vida = int(input('\nVocê tem vida demais! O valor máximo é 100. Por favor, selecione outro valor: '))

ali_forca = int(input('\nQual a força do seu personagem? Selecione um número de 1 a 10: '))
while ali_forca > 10:
	ali_forca = int(input('\nVocê é muito forte! Por favor, selecione um valor entre 1 e 10: '))

ali_defesa = int(input('\nQual é a sua defesa? Selecione um número de 1 a 10: '))
while ali_defesa > 10:
	ali_defesa = int(input('\nDefesa impenetrável! Por favor, selecione um valor entre 1 e 10: '))


#Valores Inimigo
ini_vida = random.randint(1, 100)
ini_forca = random.randint(1, 10)
ini_defesa = random.randint(1, 10)



def ali_atacando(ini_defesa):
    global ini_vida
    dano_ali = max(0, ali_forca * 2 - ini_defesa)
    ini_vida -= dano_ali
    return dano_ali

def ini_atacando(ali_defesa):
    global ali_vida
    dano_ini = max(0, ini_forca * 2 - ali_defesa)
    ali_vida -= dano_ini
    return dano_ini
    
def ini_defen():
    global ali_atacando

#começo dos turnos
round = 0


#começo da rodada
while ini_vida > 0 and ali_vida > 0:
    print(f'\nRodada {round+1}')
    ali_acao = int(input('\nO que você vai fazer?\n1- Atacar | 2- Defender\n'))

#ação inimiga
    ini_acao = random.randint(1, 2)
    if ini_acao == 1:
        ini_atacando(ali_defesa)
    else:
        ini_defen()
    

#printar ação inimiga
    if ini_acao == 1:
      print('\nO inimigo atacou!')
    else:
      print('\nO inimigo se defende.')

    round +=1
    
#ação aliada
    if ali_acao == 1 and ini_acao == 1:
        dano_ali = ali_atacando(ini_defesa)
        dano_ini = ini_atacando(ali_defesa)
        print(f'\nAmbos se atacam! Você causou {dano_ali} de dano e perdeu {dano_ini} pontos de vida devido ao ataque inimigo.')
    elif ali_acao == 1 and ini_acao == 2:
        dano_ali = ali_atacando(ini_defesa)
        print('\nSeu ataque bate na defesa inimiga.')
        if (ali_forca * 2) > (ini_defesa):
            print(f'Felizmente, você causou {dano_ali} de dano.')
    elif ali_acao == 2 and ini_acao == 1:
        dano_ini = ini_atacando(ali_defesa)
        print('\nVocê prepara sua defesa.')
        if (ini_forca * 2) > (ali_defesa):
            print(f'Ele é forte! Você sofreu {dano_ini} de dano.')
    elif ali_acao == 2 and ini_acao == 2:
        print('\nAmbos erguem seus escudos... meio constrangedor...')
    else:
        print('Ação Inválida!')

print(
f'\n--- FIM DA RODADA ---'
f'\nVida de {ali_nome}: {ali_vida}'
f'\nVida do Inimigo: {ini_vida}'
)

if ini_vida > 0 and ali_vida > 0:
        input('\nAperte ENTER para continuar...')

if ali_vida <= 0:
    print(f'\n{ali_nome} foi derrotado!')
elif ini_vida <= 0:
    print('\nO inimigo foi derrotado!')