# Dev. Lucas Fraga - 100 Days of Code: The Complete Python Pro Bootcamp - RachaConta 1.0
# PT-BR: Jogo de aventura ambientado em uma ilha do tesouro, onde os jogadores enfrentam diversos desafios e fazem escolhas ao longo do caminho para encontrar o tesouro escondido. Durante o desenvolvimento, foram aplicados os conhecimentos de uso de estruturas condicionais if, elif, e else.
# EN-US: An adventure game set on a treasure island, where players face various challenges and make choices along the way to find the hidden treasure. During development, knowledge of the use of conditional structures if, elif, and else was applied.

import time as t

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo (a) à Ilha do Tesouso!")
print("Sua missão é encontrar o grande tesouro do Pirata Harobed Sezenem.")

escolha01 = input('Você chegou em uma grande encruzilha e só pode escolher uma direção. Digite "esquerda" ou "direita\n').lower()
t.sleep(1)
if escolha01 == "esquerda":
    t.sleep(1)
    print("Excelente escolha!")
    t.sleep(1)
    escolha02 = input('Você chegou até um lago. Há uma ilha no meio do lago. Digite "esperar" para que um barco venha até você. Se desejar nadar, digite "nadar".\n').lower()
    if escolha02 == "esperar":
        t.sleep(1)
        print("Você foi sensato...")
        t.sleep(1)
        escolha03 = input('Você chegou à ilha ileso e longe dos perigos do lago. Na ilha há uma casa com três portas. Uma vermelha, uma amarela e outra azul. Qual cor você escolhe?\n').lower()
        if escolha03 == "vermelha":
            t.sleep(1)
            print("Talvez não tenha sido sua melhor opção...")
            t.sleep(1)
            print(r'''
                  (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                  ''')
            print("Hm, interessante... mas você encontrou o quarto do fogo! Você morre queimado, em chamas! Game over!")
        elif escolha03 == "azul":
            t.sleep(1)
            print("Que barulho é esse? Eu ouço grunidos ou serão rugidos?")
            t.sleep(1)
            print(r'''
                  (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"
                  ''')
            print("Não acredito, você encontrou o esconderijo das feras... elas estão famintas, você foi devorado!")
        elif escolha03 == "amarela":
            t.sleep(1)
            print("Meus olhos... quanto brilho! O que é aquilo? Não acredito!")
            t.sleep(1)
            print(r'''
                  _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
                  ''')
            print("Que sorte a sua! Você encontrou o grande tesouro! Você ganhou!")
        else:
            t.sleep(1)
            print("Bem, não entendi porque escolheu essa porta...")
            t.sleep(1)
            print("Você escolheu uma porta inexistente e perdeu! Game over!")
    else:
        t.sleep(1)
        print("Ela está atrás de você! Não importa o quão rápido você nade...")
        t.sleep(1)
        print(r'''    
                 |
                 |
                ,|.
               ,\|/.
             ,' .V. `.
            / .     . \.
           /_`       '_\.
          ,' .:     ;, `.
          |@)|  . .  |(@|
     ,-._ `._';  .  :`_,' _,-.
    '--  `-\ /,-===-.\ /-'  --`
   (----  _|  ||___||  |_  ----)
    `._,-'  \  `-.-'  /  `-._,'
             `-.___,-' 
              ''')
        print("Você foi devorado por uma grande truta furiosa! Game over!")
else: 
    print("Oh não! Você caiu em um buraco! Game over!")