word_list = ['world','apple','grape','local','level','sushi','adieu','audio','scale','osake','stare','porno','truck']

import random

a = random.choice(word_list)
print('메스가키식 wordle: 5자리의 단어를 5번 내에 맞추면 되는 허-접 오니짱에게 안성맞춤인 게임')
print('오..오니짱 5글자야... 절대로 오니짱을 걱정해서 이러는건 아니니깐..응...')
user_input = str(input())
def lenth(user_input):
     if len(user_input) == 5:
        print('흐-응? 오니짱치고 제법인걸? 시작할게')
        return
     else:
        print('허-접 오니짱에겐 5글자라는 규칙조차 어려운걸까?\n 한번더 5글자가 아닌 글자를 입력하면 게임 종료니깐 조심하라고 허-접 오니짱')
        user_input = str(input())
        if len(user_input) != 5:
            print('도태한남새끼')
            exit()
        else: 
            return
         
lenth(user_input)

list(user_input)
list(a)
for i in range(6):
    for n in range (0,5):
        if a in user_input:
            print('흐-응? 오니짱치고 제법인걸? 정답이야')
            exit()
        user_input[n]
        a[n]
        if user_input[n] == a[n]:
            print(f'베...베츠니 오니짱이 못할거라고 생각한건 아니니깐.. {n+1}번 스펠링이 위치와 철자모두 같아') 

        elif user_input[n] in a:
            print(f'흐-응? 오니짱 치곤 제법인걸..?{n+1}번 스펠링이 위치는 틀리지만 단어 안에 있어')

        else:
            print(f'허-접 좆-밥 오니짱~~ {n+1}번 스펠링은 포함되어 있지 않다고?')
        n = n + 1
        if n == 5:
            n = n - 4
            print('베...베츠니 오니짱이 좋아서 기회주는건 아니니깐... 한번 더 해봐')
            print('오..오니짱 5글자야... 절대로 오니짱을 걱정해서 이러는건 아니니깐..응...')
            user_input = str(input())
            lenth(user_input)
    if i == 5:
        print('허-접, 좆-밥, 영어도 못하는 병ㅡ신')
        break