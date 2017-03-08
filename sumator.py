a = [int(i) for i in list(reversed(input("Pierwsza liczba binarna:")))]
b = [int(i) for i in list(reversed(input("Druga liczba binarna:")))]
wynik = [int(i) for i in list('0000')]
bp = [int(i) for i in list('00000')]
for i in range(len(a)):
    if a[i] == 0 and b[i] == 0 and bp[i] == 0:
        wynik[i] = 0
    if a[i] ^ b[i] == 1 and bp[i] == 0:
        wynik[i] = 1
    if a[i] == 1 and b[i] == 1 and bp[i] == 0:
        wynik[i] = 0
        bp[i+1] = 1
    if a[i] == 0 and b[i] == 0 and bp[i] == 1:
        wynik[i] = 1
    if a[i] ^ b[i] == 1 and bp[i] == 1:
        wynik[i] = 0
        bp[i+1] = 1
    if a[i] == 1 and b[i] == 1 and bp[i] == 1:
        wynik[i] = 1
        bp[i+1] = 1
if bp[4] == 1:
    wynik = wynik + [1]
print(''.join(str(i) for i in list(reversed(wynik))))

