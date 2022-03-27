# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах


string = input()
cout = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
        else:
            a = string[i]
            print(cout, string[i])
            cout = 1
print(cout, string[i])


#другой вариант

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return ''

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding
def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    print(decode)
    return decode

encoded_val = rle_encode('AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE')
print(encoded_val)

rle_decode(encoded_val)
