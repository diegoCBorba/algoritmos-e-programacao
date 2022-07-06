def vogais():

  vogais = ['a','e','i','o','u']

  entrada = input().lower()

  if len (entrada) != 1:
    print ('1 caractere, por favor!')

  else:
    if entrada [0] in vogais:
      print ('Eh vogal')
    else:
      print ('Nao eh vogal')

vogais()