### 1. 임포트
import os
import sys
import urllib.request
import json
from pprint import pprint

### 2. 클라이언트 정보
# 바탕화면에 저장된 메모장에서 client id, pw 가져오기
# labels에 id, pw가 리스트 형태로 저장
file_path = 'papago_client.txt'
labels = open(file_path).read().splitlines()

## papago_client.txt 에서 라인으로 분별
client_id = labels[0]  # 개발자센터에서 발급받은 Client ID 값
client_secret = labels[1]  # 개발자센터에서 발급받은 Client Secret 값

### 3. 번역할 문장
file_path = 'nopebot_800min_edit.txt' # 번역할 문장
labels = open(file_path).read().splitlines() # 한줄한줄 나눔
line_len = len(labels)

print(line_len)

### 4. papago 작업
def ToEn(koText):
    encText = urllib.parse.quote(koText)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    transed = ''
    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        d = json.loads(result)
        transed = d['message']['result']['translatedText']

    else:
        transed = 'fail'
        print(transed)
        # print("Error Code:" + rescode)

    return transed

### 5. 테스트
test = ToEn('안녕하세요')
print(test)

### 6. papago 돌리기 -> 빈 문장이거나, 요청에 실패하면 write 하지 않음.
### => 혹시 몰라서 open 하고 n번 추가하고 close 시킴 (중간 과정까지라도 살려두려고)
now_line = 0  # 읽고 있는 문장 라인 번호 (전체 번호)
in_line = 0  # while in_line < n 번씩 끊어 읽을 때... (내부 끊어서 보는 번호)

while now_line < len(labels):  # 리스트 수 만큼 읽음
    in_line = 0  # 내부 라인 초기화
    # a => 더하는 모드 / w => 그냥 생편집
    f = open("ToEn_translated.txt", 'a')  # 열어주기~
    print("==================================================")
    while in_line < 5:
        if (len(labels) > now_line):  # 0-1. 파일 라인 내
            a = labels[now_line]  # now_line번째 줄 문장
            print(a)
            if (a != ""):  # 1-1. 공백이 아니면 번역한다
                en = ToEn(a)
                if (en == "fail"):  # 2-1. 실패면 저장 안한다.
                    print("fail")
                    print("in_line/now_line" + str(in_line) + "/" + str(now_line))
                else : # 2-2. papago 성공하면, 입력한다.
                    f.write(en + '\n')
        else:  # 1-2. 공백이면 공백 출력
            print("공백")

        print('line_num = ' + str(in_line))
        print('cycle = ' + str(now_line))

    else:  # 0-2. 파일 라인 도달
        print('추가 안함')

    # 계속 추가해주기
    in_line = in_line + 1
    now_line = now_line + 1
    # in_line < n 번 해줬으면, 닫아주기~
    f.close()

### 7. 파파고 API '유료' 버전 사용하면 활용할만 하다.
# 하... 200줄 정도 하면, 일일 API 요청 수 제한 걸리네요 ㅠㅠ
# 약 8000줄 정도니까... 40일 ㅋㅋㅋㅋㅋㅋ
# 한국어에서 다시 영어로 x2 ==> 헉! 최소 80일!