tipo_cha = int(input())
resposta_part = input().split()
resposta_part_int = []
count = 0

for i in resposta_part:
    resposta_part_int.append(int(i))

for x in resposta_part_int:
    if x == tipo_cha:
        count += 1

print(count)
