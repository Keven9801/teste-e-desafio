def verificar_tweet(texto):
  if len(texto) <= 140:
    return "tweet"
  else:
    return "mute"
    
#entrada 

texto = input()

resultado = verificar_tweet(texto)

print(resultado)




#IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
#- "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
# casos, é necessário converter/tratar os dados de entrada; 
#"print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
#mpressão dos dados de saída. 

#T = input()    
#   TODO Ler a variável de entrada e verificar se ela possui mais ou menos que 140 caracteres.
 #  Se for maior imprima "MUTE" e se for igual ou menor imprima "TWEET".
    