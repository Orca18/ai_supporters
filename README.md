# [ ai_supporters ]
=> GPT-2 개발 서포터
## clover
1. 노프 팀장님 스크립트 ( 음성 인식 → 텍스트 by. 클로버 )
## papago
2. 스피킹 스크립트 → 문장 자연스럽게 변환하는 용도

특징 : 스크립트.txt 파일을 줄(line)로 split 해서 번역함
- 한국어 ⇒ 영어
- 영어 ⇒ 한국어
## konltk
3. 불용어 제거 : 의미 없이, 불필요하게 반복되는거 제거 or 직접 제거

코드는 작성 했는데, 한국어는 역시 직접 지우는게 좋다.
## learning/generate
4. 학습 시키기

특징 : Sagemaker Studio Lab 기준 (최적 : batch 32, seq_len 128, epoch 4)
## generate
5. 문장 생성 테스트

특징 : 문장이 깔끔한거 쓰는게 좋다. (번역 작업 필요 없음)
## learning/chatbot
6. 챗봇 학습

송영숙님의 챗봇 데이터 : 
https://github.com/songys/Chatbot_data
## flask
7. 챗봇 테스트 & 서버

REST API 배포 ⇒ 문장 생성 & 챗봇
