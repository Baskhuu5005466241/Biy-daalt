############################################
# 1  Давхрын хэд дэх хаалга
# davhar=5
# haalga=4 
# toot=10

# i = (toot - 1) // haalga + 1
# c = (toot - 1) % haalga + 1
# print(i, c)
############################################
# 2 Орц, давхар, хаалга
# davhar=5
# orts=3
# haalga=4
# toot=32

# toot-=1

# a= toot // (davhar * haalga)+1
# i=toot % (davhar * haalga) 

# d= i// haalga+1
# c= i % haalga+1
# print( a, d, c)
############################################
# 3  Нийлбэр 1
# def number(n):
#     return (n * (n + 1)) // 2

# n = int(input("natural too oruulna uu: "))

# result = number(n)
# print("хүртэлх натурал тоонуудын нийлбэр", n, "бол", result)



############################################
# 4  Нийлбэр 2
# def number(n):
#     return (n * (n + 1) * (2 * n + 1)) // 6

# n = int(input("Дурын тоо оруулна уу: "))
# result = number(n)
# print(n,"Хүртэлх тооны квадратуудын нийлбэр нь", result)


# 5  Нийлбэр 3
# def first(n):
#     hariu = (n + 1) // 2
#     number = hariu * (2 * 1 + (hariu - 1) * 2) // 2
    
#     return number

# n = int(input("Сондгой тоо оруулна уу: "))

# if n % 2 == 1:
#     result = first(n)
#     print(f" hurtleh sondgoi toonii {n} bol {result}")
# else:
#     print("Сондгой тоо оруулна уу!")


# 6  Ахмад орны цифр
# def test(n):
#     n_str = str(n)
#     return int(n_str[0])
# n = int(input("Duriin too oruulna uu: "))

# result = test(n)
# print(result)

############################################
# 6
# def first(n):
#     hariu = (n + 1) // 2
#     number = hariu * (2 * 1 + (hariu - 1) * 2) // 2
    
#     return number

# n = int(input("Сондгой тоо оруулна уу: "))

# if n % 2 == 1:
#     result = first(n)
#     print(f" hurtleh sondgoi toonii niilber bol {result}")
# else:
#     print("Сондгой тоо оруулна уу!")

# def test(n):
#     n_str = str(n)
#     return int(n_str[0])

# n = int(input("Duriin too oruulna uu: "))

# result = test(n)
# print(result)

# 7  Цифрүүдийн нийлбэр
# def first(number):
#     hariu = 0
#     while number > 0:
#         test = number % 10
#         hariu += test
#         number //= 10
#     return hariu

# number = int(input("Enter a number: "))
# result = first(number)
# print(result)

# 8 Тэгш цифрүүдийн нийлбэр
# def test(number):
#     total = 0
#     while number > 0:
#         too = number % 10
#         if too % 2 == 0:
#             total += too
#         number //= 10
#     return total

# number = int(input("Enter a number: "))

# result = test(number)
# print(result)

#9 Сондгой цифрүүдийн тоо
# number = input("Toonuud oruulna uu: ")


# odd_count = 0


# for digit in number:
    
#     digit_int = int(digit)
    
    
#     if digit_int % 2 != 0:
#         odd_count += 1


# print("Сондгой тоо:", odd_count," байна")


#10 Цифрийн давталт


# numbers = input("Бүхэл тоо болон хэдэн ширхэгийг нь олох гэж буй тоогоо оруул: ").split()
# number = numbers[0]
# digit_to_find = numbers[1]


# digit_count = 0


# for digit in number:
#     if digit == digit_to_find:
#         digit_count += 1


# print("Таны тоо болох:", digit_to_find, "нь", number, "дотор", digit_count, "ширхэг байна.")


#11 Тоон дахь их цифр

# numbers = input("Тоо оруулна уу: ").split()

# ih_too = -1
# for i in numbers:
#     i_int = int(i)

#     for too in str(i_int):
#         too_int = int(too)
        
        
#         if too_int > ih_too:
#             ih_too = too_int


# print("Их тоо:", ih_too)

# numbers = input("Тоо оруулна уу: ").split()
# numbers = [int(num) for num in numbers]  

# largest_digit = max(int(digit) for num in numbers for digit in str(num))

# print("Их тоо:", largest_digit)

#12 Тоон дахь бага цифр

# too= input("Тоонууд оруулна уу: ").split()

# too= [int(num) for num in too]

# baga_too = min(too)


# print("Бага тоо:", baga_too)


#13 Тоон дахь их цифр

# too= input("Тоонууд оруулна уу: ").split()

# too= [int(num) for num in too]

# ih_too = max(too)


# print("Их тоо:", ih_too)

###############################################################
#14 Тонгорогсон тоо


# numbers = input("Enter a list of integers separated by spaces: ").split()


# numbers = [int(num) for num in numbers]


# numbers.sort(reverse=True)


# rounded_numbers = [str(round(num)) for num in numbers]
# print("Rounded numbers:", " ".join(rounded_numbers))

# numbers = input("Тоонууд оруулна уу: ").split()
# numbers = [int(num) for num in numbers]

# print("Non-rounded numbers (reversed order):")
# for num in reversed(numbers):
#     print(num, end=" ")

# numbers = input("Enter a list of integers separated by spaces: ").split()
# numbers = [int(num) for num in numbers]

# for num in reversed(numbers):
    

###############################################
# 14. Тонгорогсон тоо

a = 1234
b = 0
while a > 0:
    b = b * 10 + a % 10
    a = a // 10

print(b)

def reverse_number(a):
    b = 0
    while a > 0:
        b = b * 10 + a % 10
        a = a // 10
    return b


a = int(input("Enter a number: "))


b = reverse_number(a)

print("Reversed number:", b)





############################
#15. Палиндром эсэх
# def palindrome(input_string):
#     input_string = input_string.replace(" ", "").lower()
    
#     # Compare the string with its reverse
#     return input_string == input_string[::-1]

# # Get input from the user
# user_input = input("Enter a string: ")

# if palindrome(user_input):
#     print("Палиндром")
# else:
#     print("Палиндром биш")


################################
#16. Хоёрын зэрэгт
##########ЧАДСАНГҮЙ
# n = int(input())
# d = 1

# i = 2

# while i <= n:
#     d = i
#     i *= 2

#     if d == n:
#         print("YES")
#     else:
#         print("NO")

# n = int(input())

# if n > 0 and (n or (n - 1)) == 0:
#     print("YES")
# else:
#     print("NO")


# n = 1
# d = 1
# i = 2

# while i <= n:
#     if d == n and n % 2 == 0:
#         print("YES")
        
#     else:
#         print("NO")
#     i = i * 2



############################
#17. Гурвын зэрэгтэд хураа

        
# n = int(input('Enter a number:'))

# while n % 3 == 0:
#     n = n / 3



# print(n)

#####################################
#18. Тооны факториал

# n = int(input('too oruulna uu'))
# a = 1
# found = True

# for i in range(1, n + 1):
#     a *= i
#     if a == n:
#         found = True
#         print(i)
#         break
#     else:
#         found = False

# if not found:
#     print("No")

#####################################
#19. ХИЕХ

# a = 9  
# b = 15  
# n = 1  

# for i in range(2, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         n = i
# print(n)

#####################################
#20. ХБЕХ
# a = 9
# b = 15
# n = 1

# for i in range(max(a, b), a * b + 1):
#     if i % a == 0 and i % b == 0:
#         n = i
#         break

# print(n)



####################################
#21. Бутархайг хураа

# a, b = map(int, input().split())
# i=0
# c=0
# d=0
# e=0

# for i in range(1, min(a, b) + 1):
#     if a % i == 0 and b % i == 0:
#         c = i

# e = a // c
# d = b // c
    
# print(f"{e}/{d}")
    
#####################################
#22. Цифр давталт
# a = 4

# for i in range(a):
#     print(a)

# a = 4

# for i in range(a):
#     print(a, end=' ')


#####################################
#23. Цифр хүртэлх

# a = 4

# for i in range(a):
#     print(i, end=' ')


#####################################
#24. Есөөс цифр хүртэл
# a = 5

# for i in range(9, a - 1, -1):
#     print(i, end=' ')



#####################################
#25. Давхар давталт 0

# n = int(input("Too oruul: "))  
# for i in range(n):
#     for j in range(1, n + 1):
#         print(j, end='')
#     print()


#####################################
#26. Давхар давталт 1

# n = 5

# for i in range(n):
#     for j in range(n, 0, -1):
#         print(j, end='')
#     print()



#####################################
#27. Давхар давталт 2

# n = 5

# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

####################################
#28. Давхар давталт 3

# n = 5

# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()

####################################
#29. Давхар давталт 4

# n = 5 

# for i in range(1, n + 1):
#     for j in range(n, n - i, -1):
#         print(j, end=' ')
#     print()


####################################
#30. Давхар давталт 5

# n = 5  

# for i in range(n, 0, -1):
#     for j in range(n, n - i, -1):
#         print(j, end=' ')
#     print()



####################################
#31. Шагай

# a=4
# b=(a+1)*(a+2)*(a+3)/6

# print(b)


####################################
#32. Гурвалжны хэлбэр

# a, b, c = 5, 3, 4 

# a2 = a * a
# b2 = b * b
# c2 = c * c

# if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
#     print('right')
# elif a2 + b2 < c2 or a2 + c2 < b2 or b2 + c2 < a2:
#     print('obtuse')
# else:
#     print('acute')


####################################
#33. Гурван тооны ХБЕХ

# a, b, c = map(int, input("Тоо оруулна уу: ").split())

# if a > b and a > c:
#     d = a
# elif b > a and b > c:
#     d = b
# else:
#     d = c

# while True:
#     if d % a == 0 and d % b == 0 and d % c == 0:
#         print(d)
#         break
#     d += 1


####################################
#34. Цөөн квадрат

# n, m = map(int, input('too oruulna uu').split())

# while n > 0:
#     if n < m:
#         n, m = m, n
#     print(m, n // m)
#     n = n % m


####################################
#35. Залгаад квадрат зэрэг

# a = int(input())
# n = 0
# d = 1
# c = a
# k = 2

# while c != 0:
#     c = c // 10
#     n = n + 1

# for i in range(1, n + 1):
#     d = d * 10

# a = a + d
# a = (a * 10) + 1
# a = a * a

# print(a)
####
# a = int(input('too oruulna uu'))
# s = 1
# b = a

# while a > 0:
#     a = a // 10
#     s = s * 10

# b = (b + s) * 10 + 1
# b = b * b

# print(b)
################################
#36. Гипотенуз

# import math

# m, n = map(float, input('too oruulna uu').split())
# b = math.sqrt(m**2 + n**2)

# print(b)


################################
#37. Гурвалжны талбай

# import math

# a, b, c = map(float, input('too oruulna uu').split())
# p = (a + b + c) / 2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))

# print(f"{s:.2f}")


#################################
#38. Дугуйн талбай

# import math

# p = float(input('too oruulna uu'))
# r = p / (2 * 3.141592)
# s = r**2 * 3.141592

# print(s)


#################################
#39. Хоёр цэгийн хоорондох зай

# import math

# a, b = map(float, input('too oruulna uu').split())
# c, d, e, f = map(float, input().split())
# g, h, i, j, k, l = map(float, input().split())

# m = abs(b - a)
# n = math.sqrt((e - c)**2 + (f - d)**2)
# o = math.sqrt((g - j)**2 + (h - k)**2 + (i - l)**2)

# print(m,n,o)


#################################
#40. 2 тооны дундаж

# import math
# a, b = map(float, input('too oruulna uu').split())
# average = (a + b) / 2
# square_root = math.sqrt(a * b)
# print(average,square_root)


#################################
#41. Нийлбэр 4

# n = int(input('too oruulna uu'))

# sum_of_n = (n + 1) * n // 2

# ans = sum_of_n ** 2

# print(ans)


#################################
#42. Тойргийн талбай, урт

# import math

# r = float(input('too oruulna uu'))

# ans = 2 * math.pi * r
# sum_area = math.pi * r**2

# print(f"{sum_area:.1f} {ans:.1f}")


##################################
#43. Массив нийлбэр

# a = int(input())
# c = 0
# b = []

# while a != 0:
#     b.append(int(input()))
#     c = c + b[-1]
#     a = a - 1

# print('Hariu bol:'+str(c))



################################
#44. Массив тэгээс их нийлбэр

# n = int(input())
# too = []

# for i in range(n):
#     too.append(int(input()))

# niilber = 0

# for i in range(n):
#     if too[i] > 0:
#         niilber += too[i]

# print(niilber)



################################
#45. Муугийн тоо

# n = int(input())
# numbers = []

# for i in range(n):
#     numbers.append(int(input()))

# niilber = 0

# for i in range(n):
#     if numbers[i] < 60:
#         niilber += 1

# print('Муу дүнтэй сурагч '+str(niilber)+ ' байна.')



################################
#46. Сондгой нь их үү

# t=0
# s=0
# n = int(input())
# list = []

# for i in range(n):
#     list.append(int(input()))
#     if list[i] % 2 == 0:
#         t += list[i]
#     else:
#         s += list[i]

# if t < s:
#     print("YES")
# else:
#     print("NO")



################################
#47. Массивын их

# a = int(input())
# c = 0
# e = 0
# b = input().split()
# c = int(b[0])

# for x in range(a):
#     d = int(b[x])
#     if c < d:
#         c = d

# print('Hamgiin ih too '+str(c))


################################
#48. Массивын бага

# n = int(input())
# a = [int(x) for x in input().split()]

# c = a[0]

# for i in range(n):
#     c = min(c, a[i])

# print('Hamgiin baga too '+str(c))


################################
#49. Массивт өгөгдсөн тоо хэд

# n = int(input())
# a = [int(x) for x in input().split()]
# k = int(input())

# s = 0

# for i in range(n):
#     if a[i] == k:
#         s += 1

# print(f"{k} {s}")



#################################
#50. Массивын их нь хэд дэх

# n = int(input('too oruul'))
# a = [int(x) for x in input().split()]
# b = 0
# s = 0
# d = -132423

# for i in range(1, n + 1):
#     if a[i] > d:
#         d = a[i]

# for i in range(n, 0, -1):
#     if a[i] == d:
#         s = i

# print(f"{d} {s}")


##################################
#51. Массивын их хэд

# n = int(input())
# k = int(input())
# huudas = 0
# duusah = [0]

# for i in range(1, n + 1):
#     s, f = map(int, input().split())
#     duusah.append(f)

# for i in range(1, n + 1):
#     if k <= duusah[i]:
#         huudas = i
#         break

# if huudas == 1:
#     print(n)
# else:
#     if huudas > 1:
#         print(n - (huudas - 1))



##################################Third Page
#52. Массивт байгаа эсэх

# n = int(input('too oruul'))
# a = [0] + list(map(int, input('too oruul').split()))
# p = 0
# b = int(input('too oruul'))

# for i in range(1, n + 1):
#     if a[i] == b:
#         print("YES")
#         break
#     p += 1

# if p == n:
#     print("NO")



##################################
#53. Факториалын хүрд

# n = int(input('too oruul '))
# s = 1

# for j in range(1, n + 1):
#     s *= j
#     print(str(j) + '!' + ' ' + str(s))



##################################
#54. Үржвэр нийлбэр 1

# n = int(input('too oruul '))
# a = 0

# for i in range(1, n + 1):
#     a = a + (i + 1) * i

# print(a)


##################################
#55. Үржвэр нийлбэр 2

# n = int(input('too oruul '))
# b = 0

# for i in range(1, n + 1):
#     b = b + i * (n - i + 1)

# print(b)


###################################
#56. Үржвэр нийлбэр 3

# n = int(input('too oruul '))
# s = 0

# for i in range(1, n, 2):
#     s = s + i * (i + 1)

# print(s)
##2

# n = int(input('too oruul '))
# b = 0

# for i in range(1, n, 2):
#     if n % 2 == 0:
#         b = b + i * (i + 1)

# print(b)



####################################
#57. Үржвэр нийлбэр 4

# n = int(input('too oruul '))
# s = 0

# for i in range(1, n + 1):
#     s += i * (i + 1) * (i + 2)

# print(s)





####################################
#58. Давхар факториал

# n = int(input('too oruul '))
# s = 1
# b = 1

# for i in range(1, n + 1):
#     if i % 2 == 0:
#         s *= i
#     else:
#         b *= i

# if n % 2 == 0:
#     print(s)
# else:
#     print(b)




####################################
#59. Зэрэгтүүдийн нийлбэр

# a, n = map(int, input().split())
# i, s = 1, 1

# while n != 0:
#     i *= a
#     s += i
#     n -= 1

# print(s)



####################################
#59. Факториалуудын нийлбэр

# a = int(input('too oruul '))
# p = 0
# s = 1

# for i in range(1, a + 1):
#     s = s * i
#     p = p + s

# print(str(p))




####################################
#60. Синус нийлбэр 1

# import math

# x, n = map(float, input('too oruul ').split())
# c = 1
# s = 0

# for i in range(1, int(n) + 1):
#     c *= x
#     s += math.sin(c)

# print(f"{s:.3f}")




####################################
#61. Синус нийлбэр 2

# import math

# x, n = map(float, input(' too oruul ').split())
# c = 1
# s = 0

# for i in range(1, int(n) + 1):
#     c *= math.sin(x)
#     s += c

# print(f"{s:.3f}")





##################################
#62. Синус нийлбэр 3

# import math

# x, n = map(float, input('too oruul ').split())
# d = math.sin(x)
# s = 0

# for i in range(1, int(n) + 1):
#     s += d
#     d = math.sin(d)

# print(f"{s:.3f}")


##################################
#63. Синус косинус

# import math

# def sum(n):
#     Sinsum = 0
#     Cossum = 0
#     for i in range(1, n + 1):
#         Sinsum += math.sin(i)
#         Cossum += math.cos(i)
#     return Sinsum, Cossum

# def main():
#     n = int(input('too oruul '))
#     urj = 1
#     for i in range(1, n + 1):
#         SinSum, CosSum = sum(i)
#         urj *= CosSum / SinSum

#     print(f"{urj:.3f}")

# if __name__ == "__main__":
#     main()




##################################
#64. Косинус

# import math

# n = int(input('too oruul '))
# d = 0
# d = math.cos(n)

# for i in range(n, 1, -1):
#     d = math.cos((i - 1) + d)

# print(f"{d:.3f}")




##################################
#65. Квадратын урвуу үржвэр

# import math

# a = float(input('too oruul '))
# b = 1
# d = 1

# while b <= a:
#     c = 1 + (1 / math.pow(b, 2))
#     d = d * c
#     b = b + 1

# print(f"{d:.3f}")




##################################
#66. Квадрат язгуур доорх 2

# import math

# a = float(input('too oruul '))
# b = 0

# for i in range(1, int(a) + 1):
#     b = math.sqrt(b + 2)

# print(f"{b:.9f}")




##################################
#67. Арифметик дундаж

# n = int(input('too oruul '))
# a = [float(input()) for _ in range(n)]

# s = sum(a)
# p = s / n

# print('hariu:'+f"{p:.2f}")




##################################
#68. Хүүн довтолгоо

# n = int(input('too oruul'))
# a = [0] * 89
# a[1] = 1
# a[2] = 2

# for i in range(3, n + 1):
#     a[i] = a[i - 1] + a[i - 2]

# print(a[n])




##################################
#69. Супер жаал саад тойрон

# n, s = map(int, input().split())
# a = [int(x) for x in input().split()]

# marshrut = [0] * 101
# for k in a:
#     marshrut[k] = -1

# marshrut[0] = 1
# if marshrut[1] != -1:
#     marshrut[1] = 1
# else:
#     marshrut[1] = 0

# if marshrut[2] != -1:
#     marshrut[2] = marshrut[1] + marshrut[0]
# else:
#     marshrut[2] = 0

# for i in range(3, n + 1):
#     if marshrut[i] != -1:
#         marshrut[i] = marshrut[i - 1] + marshrut[i - 2] + marshrut[i - 3]
#     else:
#         marshrut[i] = 0

# print(marshrut[n])



##################################
#70. Хүү гишгүүрт мөнгө төлбөл

# max = 40

# n = int(input())
# cost = [0] + list(map(int, input().split()))
# gishguur = [-1] * (max + 1)

# def f(i):
#     if i == 1:
#         return cost[1]

#     if gishguur[i] != -1:
#         return gishguur[i]

#     gishguur[i] = min(f(i - 1) + cost[i], f(i - 2) + cost[i])
#     return gishguur[i]

# result = f(n)
# print(result)




##################################
#71. Бага төлөх гишгүүрүүд

# n = int(input())  # Number of elements
# b = [0] + list(map(int, input().split()))  # List of elements, adding a dummy element at index 0

# a = [0] * (n + 1)
# c = [0] * (n + 1)
# d = [0] * (n + 1)

# a[1] = b[1]
# a[2] = b[2]
# c[1] = 0
# c[2] = 0

# for i in range(3, n + 1):
#     if a[i - 1] < a[i - 2]:
#         a[i] = a[i - 1] + b[i]
#         c[i] = i - 1
#     else:
#         a[i] = a[i - 2] + b[i]
#         c[i] = i - 2

# print(a[n])

# j = 0
# while n != 0:
#     j += 1
#     d[j] = n
#     n = c[n]

# for i in range(j, 0, -1):
#     print(d[i], end=" ")





##################################
#72. Фибоначчийн n дахь гишүүн


# f = True
# num = 0

# while f:
#     num = int(input("A="))
#     if 1 <= num <= 45:
#         f = False
#     else:
#         print("1 <= n <= 45!")

# arr = [1] * 100000
# a, b, c = 0, num - 1, num - 2

# for i in range(num):
#     arr[i] = 1

# a = arr[b] + arr[c]
# print(a)



##################################
#73. Фибаноччийн гишүүний цифр

# a = int(input('too oruul '))
# b = [0] * 101
# b[0] = 1
# b[1] = 1

# for i in range(2, a + 1):
#     b[i] = (b[i - 2] + b[i - 1]) % 10

# print(b[a])



##################################
#74. Энгийн дараалал

# a = int(input('too oruul '))
# b = [0] * (a + 1)
# b[0] = 1
# b[1] = 1

# i = 1
# while i <= a // 2:
#     b[i * 2] = b[i] + b[i - 1]
#     b[i * 2 + 1] = b[i] - b[i - 1]
#     i += 1

# print(b[a])


##################################
#75. Зальжин дараалал

# a = int(input('too oruul '))
# n = [0] * 10000
# n[0] = 1
# n[1] = 1
# n[2] = 2
# b = 2

# while b <= a:
#     n[2 * b] = n[b] + 1
#     n[2 * b - 1] = n[2 * b] + n[b - 1]
#     b += 1

# print(n[a])



##################################
#76. Супер жаал

# n = int(input('too oruul '))

# if n == 1:
#     result = 1
# elif n == 2:
#     result = 2
# elif n == 3:
#     result = 4
# else:
#     a, b, c = 1, 2, 4
#     for i in range(4, n + 1):
#         a, b, c = b, c, a + b + c
#     result = c

# print(result)




##################################
#77. Хүү саадыг тойрон

# n, k = map(int, input('too oruul ').split())
# huu = [0] * 100
# huu[0] = 1

# if k != 1:
#     huu[1] = 1

# i = 2
# while i <= n:
#     if i != k:
#         if i - 1 != k:
#             huu[i] += huu[i - 1]
#         if i - 2 != k:
#             huu[i] += huu[i - 2]
#     i += 1

# print(huu[n])



##################################
#78. Оронгийн тоо

# n = input('toonuud zaigui oruulna uu')
# a = len(n)
# print(a)


##################################
#79. Илэрхийлэл 1
# a = int(input('too oruul '))
# k = 0
# l = 1
# i = 1

# while i <= a:
#     j = 1
#     while j <= 2 * i:
#         l = l * j
#         j += 1
#     k = k + l
#     l = 1
#     i += 1

# print(k)




##################################
#80. Жижгээс томд

# s = input('Жижиг үсэг оруул ')
# print(chr(ord(s) - 32))


##################################
#81. Дараагийн тэмдэгт

# a = input('тэмдэгт оруул: ')
# k = chr(ord(a) + 1)
# print(a + k)


##################################
#81. Тоонд харгалзах тэмдэгт

# n = int(input('too oruul '))
# print(chr(n))


##################################
#82. Тэмдэгтэд харгалзах код

# a = input('Үсэг оруул ')
# if a==a:
#     print(ord(a))



##################################
#83. Том үсэгт шилжүүл

# a, b, c = input('3 ширхэг тэмдэг оруул ').split()
# a, b, c = a.upper(), b.upper(), c.upper()
# print(a, b, c)



##################################
#84. Тоо сэргээх

# a = 0
# str = input('12r3 gej bichne uu:')
# for i in str:
#     if i.isdigit():
#         a = a * 10 + int(i)

# result = a * a
# print(result)


##################################
#85. Шоо
# n = int(input('шоо:'))
# a = (n + 1) * (n + 2) * (n + 3) * (n + 4) * (n + 5) // 120
# print(a)


##################################
#86. Тооны цифрээс үүсэх их тоо

# n = 1928374
# a = [0] * 10000
# i = 1

# while n > 0:
#     w = n % 10
#     a[i] = w
#     n = n // 10
#     i += 1

# for q in range(1, i):
#     for j in range(q + 1, i):
#         if a[q] < a[j]:
#             t = a[q]
#             a[q] = a[j]
#             a[j] = t

# for p in range(1, i):
#     print(a[p], end="")


##################################
#87. Тооноос бага тоо

# n = 34032
# a = [0] * 10
# while n > 0:
#     a[n % 10] += 1
#     n //= 10

# l = 1
# while a[l] == 0:
#     l += 1

# output = str(l)
# a[l] -= 1

# for i in range(10):
#     for j in range(a[i]):
#         output += str(i)

# print(output)


##################################
#88. ЭЕШ





##################################
#89. Давталт
# n = int(input('toonuud zaigui oruul:'))
# n1 = 0
# n2 = 0
# n3 = 0
# i = 0
# a = [0] * 100

# while n != n3:
#     l = 0
#     n1 = 0
#     n2 = 0
#     n3 = n

#     l = 0
#     num = n
#     while num > 0:
#         a[l] = num % 10
#         num //= 10
#         l += 1

#     for j in range(l):
#         for k in range(j, l):
#             if a[j] < a[k]:
#                 a[j], a[k] = a[k], a[j]

#     for j in range(l):
#         n1 = n1 * 10 + a[j]
#         n2 = n2 * 10 + a[l - j - 1]

#     n = n1 - n2
#     i += 1

# print(i)




##################################
#90. Дараалал

# n, m, k = map(int, input('3 utga zaigaar tusgaarlan oruul:').split())
# a = []

# for i in range(n, m + 1):
#     for o in str(i):
#         a.append(int(o))

# a.sort(reverse=True)
# result = a[k - 1] if k <= len(a) else -1

# print(result)


##################################
#91. Өр авлага

# n, m = map(int, input().split())

# a = []
# for i in range(m):
#     og, av, orr = map(int, input().split())
#     a.append({'og': og, 'av': av, 'orr': orr})

# s = 0

# for i in range(m):
#     for j in range(m):
#         if a[i]['og'] == a[j]['av'] and a[j]['orr'] > 0:
#             if a[i]['orr'] == a[j]['orr']:
#                 a[j]['av'] = a[i]['av']
#                 a[i]['orr'] = 0
#                 break
#             elif a[i]['orr'] < a[j]['orr']:
#                 a[i]['og'] = a[j]['og']
#                 a[j]['orr'] -= a[i]['orr']
#                 j = -1
#             else:
#                 a[j]['av'] = a[i]['av']
#                 a[i]['orr'] = a[i]['orr']

# for i in range(m):
#     s += a[i]['orr']
# print('hariu bol:', s)



##################################
#92. Хөгжилтэй цохилт

# n = int(input('input oruul:'))
# m = {}
# for i in range(4):
#     s = input('input oruul:')
#     for j in range(4):
#         if s[j] == '.':
#             continue
#         else:
#             if s[j] in m:
#                 m[s[j]] += 1
#                 if m[s[j]] > n * 2:
#                     print("NO")
#                     exit(0)
#             else:
#                 m[s[j]] = 1

# print("YES")


##################################
#93. К үет массив
# t, shalgah = map(int, input().split())
# davharsh = shalgah
# beta = [0] * 10
# a = 0
# b = 0

# input = list(map(int, input().split()))
# for i in range(1, t + 1):
#     beta[i] = input[i - 1]

# for i in range(1, shalgah + 1):
#     a = a * 10 + beta[i]

# davtalt = t // shalgah - 1
# n = 0

# for i in range(1, t + 1):
#     n = n * 10 + beta[i]
#     if i % shalgah == 0:
#         if n == a:
#             b += 1
#         n = 0

# if b == 1:
#     orchlolt = t // shalgah
#     print(orchlolt)
# else:
#     orchlolt = t // shalgah - b
#     print(orchlolt)


##################################
#94. Урвуулах тоглоом

# n = int(input())
# arr = list(map(int, input().split()))

# result = 0
# val = 0
# temp = 0
# k = 0

# for i in range(n):
#     if arr[i] == 0:
#         temp += 1
#         if val < temp:
#             val = temp
#             k = i
#     else:
#         temp = 0

# j = k - val + 1

# for i in range(j, k + 1):
#     arr[i] = 1

# temp = 0

# for i in range(n):
#     if arr[i] == 1:
#         temp += 1
#         if result < temp:
#             result = temp
#     else:
#         temp = 0

# print(result)



##################################
#94. Луунууд
# s, n = map(int, input().split())
# luu = []

# for i in range(n):
#     a, b = map(int, input().split())
#     luu.append((a, b))

# luu.sort()

# for i in range(n):
#     if s > luu[i][0]:
#         s += luu[i][1]
#     else:
#         print("NO")
#         break
# else:
#     print("YES")



##################################
#95. Боломжит замууд


##################################
#95. Шинэ жилийн тээвэр
# def main():
#     n, o = map(int, input().split())
#     n = n - 1
#     k = [0] * 100
#     k[0] = 1

#     for a in range(1, n + 1):
#         k[a] = int(input())

#     b = 0
#     for a in range(n + 1):
#         e = k[a] + b
#         b = b + 1

#         if e == o:
#             print("YES")
#             return 0
#         else:
#             e = 0

#     print("NO")
#     return 0

# if __name__ == "__main__":
#     main()



##################################
#96. Бүжгийн хос

# def main():
#     n = int(input())
#     k = [0] * 100
#     u = [0] * 100
#     y = [0] * 100
#     m = 0
#     b = 0

#     i = 1
#     k_values = list(map(int, input().split()))
#     while i <= n:
#         k[i] = k_values[i - 1]
#         i += 1

#     j = 1
#     while j <= n:
#         i = 1
#         while i <= n:
#             if k[i] > m:
#                 m = k[i]
#             i += 1

#         u[j] = m

#         i = 1
#         while i <= n:
#             if k[i] == m:
#                 k[i] = 0
#                 break
#             i += 1

#         m = 0
#         j += 1

#     n = int(input())
    
#     i = 1
#     k_values = list(map(int, input().split()))
#     while i <= n:
#         k[i] = k_values[i - 1]
#         i += 1

#     j = 1
#     while j <= n:
#         i = 1
#         while i <= n:
#             if k[i] > m:
#                 m = k[i]
#             i += 1

#         y[j] = m

#         i = 1
#         while i <= n:
#             if k[i] == m:
#                 k[i] = 0
#                 break
#             i += 1

#         m = 0
#         j += 1

#     j = 1
#     while j <= n:
#         i = 1
#         while i <= n:
#             if u[j] == y[i] or u[j] - 1 == y[i] or u[j] + 1 == y[i]:
#                 u[j] = 0
#                 y[i] = 0
#                 b += 1
#                 break
#             i += 1
#         j += 1

#     if b > 0:
#         b -= 1

#     print(b)


# main()
