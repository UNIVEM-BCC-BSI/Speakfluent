#setup do jogo
largura = 1280
altura = 720
fps = 60
tilesize = 48

#Jogador
status = {'Vida': 3, 'Pontos': 0, 'Nivel': 2, 'Respawn': 0}

#objetivos
objetivos = ['Fale com os professores',
             'Fale com os professores',
             'Fale com os professores',
             'Saia da escola',
            ]

#UI
UI_fonte = 'graficos/fonte/upheavtt.ttf'
UI_fonte_tam = 30
UI_fonte_obj = 25
UI_fonte_inter = 30

#Cores gerais
COR_FUNDO_MENU = '#b5f7d5'
COR_FUNDO_GAMEOVER = '#8c0303'
UI_BG_COR = '#222222'
UI_BG_COR_PERG = 'white'
UI_BORDA_COR = '#111111'
COR_TEXTO = '#EEEEEE'
COR_PERG = '#000000'
UI_BORDA_ATIVA = 'lightblue'

#Perguntas

#Prof001
prof1 = 'graficos/profs/prof1.png'

perg_prof1 = [['The ___________ is where you can borrow books', 
               'Market',
               'Library',
               'Hospital',
               'Home',
               'Library'],                                        #Resposta

              ['I ________ watching ________ movies',
               'like / action',
               'enjoy / pasta',
               'cooking / computer',
               'must / use',
               'like / action'],                                  #Resposta

              ['Escolha as traduções de: Cadeira; Lápis; Escola; Amigos',
               'Block; Table; Pen; Colegues',
               'Chair; Eraser; Parents; college',
               'Chair; Pencil; School; Friends',
               'Block; Pencil; Friends; School',
               'Chair; Pencil; School; Friends']                  #Resposta
             ]

#Prof002
prof2 = 'graficos/profs/prof2.png'

perg_prof2 = [['Solve this: 16 x 17',
               'Two hundred seventy two',
               'One hundred and twelve',
               'Thirty thre',
               'Ninety seven',
               'Two hundred seventy two'],              #Resposta

              ['Solve this: (6 + 7) x 10',
               'Seventy six',
               'A hundred',
               'One hundred and Thirty',
               'Nine',
               'One hundred and Thirty'],               #Resposta

              ['Solve this: ((5 - 4) x (13 + 7)) / 5',
               'Sixty six',
               'Fifty',
               'Two',
               'Five',
               'Five']                                  #Resposta
             ]

#Prof003
prof3 = 'graficos/profs/prof3.png'


perg_prof3 = [['Where cells store their geneic info?',
               'RNA',
               'DNA',
               'Protein',
               'Lipid',
               'DNA'],                                 #Resposta

              ['Plants convert light in energy by doing:',
               'Cellular respiration',
               'Photosynthesis',
               'Fermentation',
               'Glycolysis',
               'Photosynthesis'],                      #Resposta

              ['Which of these are NOT found in living organisms',
               'Carbohydrates',
               'Lipids',
               'Nucleiic acids',
               'Minerals',
               'Minerals']                              #Resposta
             ]

#Correção prof
cor_prof = ['Congrats!!! Fale com o próximo professor ou tente de novo.',
            'Thats wrong :( Fale com o próximo professor ou tente de novo.',
            'Nós te ensinamos tudo o que tinhamos...']

#Biblioteca
perg_biblio = [['',
               '',
               '',
               '',
               '',
               '']]

#Correção biblioteca
cor_biblio = ['Não tenho mais nada para lhe ensinar']

#Fim
perg_fim = []