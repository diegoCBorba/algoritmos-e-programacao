primos = 0
total_cinema = 0
total_boliche = 0

while primos < 7:
    filme = str(input().upper())
    primos += 1

    if filme == "CINEMA":
        total_cinema += 1

    if filme == "BOLICHE":
        total_boliche += 1

if total_cinema > total_boliche:
    print("CINEMA")

elif total_boliche > total_cinema:
    print("BOLICHE")
