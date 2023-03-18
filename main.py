message=input("Введите сообщение:")
lenght = len(message)
print("Количество символов:",lenght)
print("Второй символ:",message[1])
print("Последний символ:",message[-1])
print("Первые три символа:",message[:3])
print("Последние три символа:",message[3:])
print(f"\033[34\033[43m{message}\033[0m")
cipher_one=message
message_one=message.replace("т", "с")
message_one=message_one.replace("и", "о")
print("Шифр 1:",cipher_one)
cipher_two=message[::-1]
print("Шифр 2:",cipher_two)
cipher_three=message[::2]+message[1::2]
print("Шифр 3:",cipher_three)
first_letter=message[0]
last_letter=message[-1]
number_of_characters=len(message)
cipher_four=last_letter+message[1:number_of_characters-1]+first_letter
print("Шифр 4:",cipher_four)
half_lenght = len(message)//2
cipher_five = message[half_lenght:] + message[:half_lenght]
print("Шифр 5",cipher_five)
message_one_decoding=cipher_one
message_one_decoding=message_one_decoding.replace("с","т")
message_one_decoding=message_one_decoding.replace("о","и")
print("Расшифровка 1:",message_one_decoding)
message_two_decoding=cipher_two[::-1]
print("Расшифровка 2:",message_two_decoding)
message_three_decoding=""
one_line=message[::2]
two_line=message[1::2]
for symbol in range(len(one_line)):
    message_three_decoding+=one_line[symbol]
    if symbol<len(two_line):
        message_three_decoding+=two_line[symbol]
print("Расшифровка 3:",message_three_decoding)
message_four_decoding=f"\033[34\033[43m\033[0m{message}"
print("Расшифровка 4:",message_four_decoding)
first_letter=cipher_four[0]
last_letter=cipher_four[-1]
number_of_characters=len(cipher_four)
message_five_decoding=last_letter+cipher_four[1:number_of_characters-1]+first_letter
print("Расшифровка 5:",message_five_decoding)