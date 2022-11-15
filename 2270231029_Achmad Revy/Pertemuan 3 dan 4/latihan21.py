#Contoh penggunaan Nested Loop
#Catatan : Penggunaan modulo pada kondisional mengasumsikan nilai selain nol sebagai true (benar) dan nol sebagai false ( salah )

i = 2
while(i < 100):
    j = 2
    while(j <= (i/j)):
        if not(i%j): break
    j = j + 1
    if (j > i/j) : print(i, " is prime")
    i = i + 1
print("Good bye!")