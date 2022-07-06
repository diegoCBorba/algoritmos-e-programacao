n_noticias = int(input())
count_v = 0
count_f = 0

for i in range(n_noticias):
    count_v = 0
    URL = str(input())
    s1 = str(input())
    s2 = str(input())
    s3 = str(input())
    s4 = str(input())

    if s1 == 'v':
        count_v += 1
    if s2 == 'v':
        count_v += 1
    if s3 == 'v':
        count_v += 1
    if s4 == 'v':
        count_v += 1

    if count_v == 0:
        print('{} - certamente falsa'.format(URL))
        count_f += 1
    elif count_v == 1:
        print('{} - provavelmente falsa'.format(URL))
        count_f += 1
    elif count_v == 2:
        print('{} - pode ser falsa'.format(URL))
    elif count_v == 3:
        print('{} - indeterminado'.format(URL))
    elif count_v == 4:
        print('{} - verdadeira'.format(URL))

percentual = (count_f/n_noticias)*100
print("percentual de notícias falsas {:.1f}".format(percentual))