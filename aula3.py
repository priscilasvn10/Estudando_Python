a = int(input('Primeiro bimestre: '))
if a > 10 :
    a= int(input('Você difitou errado Primeiro bimestre: '))

b = int(input('Segundo bimestre: '))
if b > 10 :
    b= int(input('Você difitou errado Segundo bimestre: '))

c = int(input('Terceiro bimestre: '))
if c > 10 :
    c= int(input('Você difitou errado Terceiro bimestre: '))

d = int(input('Quarto bimestre: '))
if d > 10 :
    d= int(input('Você difitou errado Quarto bimestre: '))
    

media = (a+b+c+d)/4
print ('Média: {}'.format(media))
# if a <= 10 and b <= 10 and c <= 10 and d <= 10
#     print ('Média: {}'.format(media))
# else:
#     print('Foi informado alguma nota errada!')

# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# mod_a = a % 2
# mod_b = b % 2
# if mod_a == 0 or not  mod_b > 0:
#     print('Foi digitado um número é PAR!')
# else:
#     print('Nenhum número é PAR foi digitado!')


# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c= int(input('Terceiro valor: '))
#
# if a>b and a>c:
#     print('O maior número é {}'.format(a))
# elif b>a and b>c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é {}'.format(c))