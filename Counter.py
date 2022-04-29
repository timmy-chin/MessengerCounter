# print(word_list)

# with open('New_TextFile.txt', 'w') as f:
#     for word in word_list:
#         f.write(word)
def counter(person, text_file):
    person_list = []
    with open(text_file, 'r') as file:
        for word in file:
            word = word.replace('\n', '')
            if ':' in word or word[1:2].isdigit() or word == '' or word == 'Hello' or word == 'Facebook':
                continue
            else:
                person_list.append(word)

    person_num = 0
    timmy = 0
    count = 0
    for word in person_list:
        if word == person:
            person_num += 1
            count += 1

        if word == 'Timmy Chin':
            timmy += 1
            count += 1

    print(f'Total Messages Send by {person}: {person_num}')
    print(f'Total Messages Send by Timmy: {timmy}')
    print(f'Total Messages Send: {count}\n')

counter('Samanda Lai', 'SamandaChat.txt')
counter('Ashlyn Cheong Shi-Jin', 'AshlynChat.txt')
counter('Tze Tian', 'TzeTianChat.txt')
counter('George Singwen', 'GeorgeChat.txt')
counter('Ng Zhengyuan', 'ZhengYuanChat.txt')
counter('Wong Zheng Xian', 'WongChat.txt')

