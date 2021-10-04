tekst = str(input("Witaj, podaj tekst do rozszyfrowania:  ").lower())

print(tekst.replace("@", "a").replace('8', 'b').replace('(', 'c').replace('*', 'd').replace('0', 'e').replace('&', 'f')
.replace('_', 'g').replace('-', 'h').replace('1', 'i').replace('6', "j").replace('!', 'k').replace('#', 'l')
.replace('=', 'w').replace('9', 'n').replace(')', 'o').replace('3', "p").replace('^', 'q').replace('%', "r")
.replace('$', 's').replace('4', 't').replace('>', 'u').replace('/', "x").replace('7', 'y').replace('2', 'z').replace('`', 'v'))
