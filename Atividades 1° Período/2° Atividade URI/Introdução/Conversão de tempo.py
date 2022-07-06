entrada = int(input())

if entrada >= 3600:
    horasH = entrada//3600
    horasM = (entrada % 3600)//60
    horasS = ((entrada % 3600) % 60)
    print("{}:{}:{}".format(horasH, horasM, horasS))

elif 60 <= entrada < 3600:
    horasM = entrada // 60
    horasS = entrada % 60
    print("0:{}:{}".format(horasM, horasS))

else:
    print("0:0:{}".format(entrada))
