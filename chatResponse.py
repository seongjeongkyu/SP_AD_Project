def chatRecognizing(word):
    if word in mydic.keys():
        message = mydic[word]
    else:
        message = '뭐라는거야;; 대답을 알려줘야 하지'
    return message


mydic = {
    '뽕순아 안녕' : '안녕! ㅎㅎ',
    '뽕순아 사랑해' : '내가 더♥',
}