f = open('dict.txt')
f1 = open('keywords.txt')


def get_dict_from_file(file):
    return dict((line.strip().split(' ')[0], line.strip().split(' ')[1]) for line in file)

numbers = get_dict_from_file(f)
keywords = get_dict_from_file(f1)
print("Welcome to the program! Please, write your number up to 1 billion")
words = input()
tmp = 0
if type(words) == int:
    while True:
        tmp = words % 10
        print(tmp)
words = words.lower().strip()
eachword = words.split()
sum = 0
result = 0
for x in eachword:
    sum += float(numbers.get(x, 0))
    if x in keywords:
        sum -= float(numbers[x])
        result += sum * float(numbers[x])
        sum = 0.
result += sum
print(result)
f.close()
f1.close()
