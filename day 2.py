#####15.01.2021

#s1 = "I have a pen, "
#s2 = "I have an apple.... "
#s3 = "MMMM...APPLEPEN"

#print(s1 + s2 + s3)


#####
    # s = 'spam'
    # s[1] = 'b'

#s = 'spam'
#s = s[0] + 'b' + s[2:]

#print(s)


#####
#len("appleeeeeeeeeee")


#####

#string = input("Введите какое-нибудь число: ")
#if string.isnumeric():
#   number = int(string)
#   print(number)


##### Работа со строками
# Следующий пример позволяет удалять пробелы в конце и начале строки:
    
string = "   привет мир!  "
string = string.strip()
print(string)


# Так можно дополнить строку пробелами и выполнить выравнивание:

print("iPhone 7:", "52000".rjust(10))
print("Huawei P10:", "36000".rjust(10))

##### Поиск подстроки в строке
# find(str): поиск подстроки str производится с начала строки и до её конца;

welcome = "Hello world! Goodbye world!"
index = welcome.find("wor")
print(index)       # 6


# "find(str, start)" с помощью параметра start задаётся начальный индекс, и именно с него и выполняется поиск;

index = welcome.find("wor",10)
print(index)       # 21


# "find(str, start, end)" посредством параметра end задаётся конечный индекс, поиск выполняется до него. 

index = welcome.find("wor",10,15)
print(index)       # -1


##### Замена в строке
phone = "+1-234-567-89-10"

# Чтобы в Python заменить в строке одну подстроку на другую, применяют метод "replace()"

edited_phone = phone.replace("-", " ")
print(edited_phone)     # +1 234 567 89 10

#//dited_phone = phone.replace("-", "")
#//print(edited_phone)     # +12345678910

#//edited_phone = phone.replace("-", "", 1)
#//print(edited_phone)     # +1234-567-89-10

### "replace(old, new)" подстрока old заменяется на new
### "replace(old, new, num)" параметр num показывает, сколько вхождений подстроки old требуется заменить на new.


#/////////////////////////////////
words = ["Let", "me", "speak", "from", "my", "heart", "in", "English"]

# символ разделителя - пробел

sentence = " ".join(words)
print(sentence)  # Let me speak from my heart in English


# символ разделителя - вертикальная черта

sentence = " | ".join(words)
print(sentence)  # Let | me | speak | from | my | heart | in | English


# а если вместо списка в метод join передать простую строку, разделитель будет вставляться уже между символами:

word = "hello"
joined_word = "|".join(word)
print(joined_word)      # h|e|l|l|o