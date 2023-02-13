## 커스텀

1. requirements.txt의 regex 버전 제거

```
# regex==2017.4.5 # used by the bpe tokenizer
regex
```

2. requirements.txt에 googletrans 추가

```
googletrans==4.0.0-rc1
```

3. custom.py 추가 (한글 번역 기능)

- kor_to_eng()
- eng_to_kor()


## 테스트

- 입력

```bash
python gpt2_kor.py "베테랑 재즈피아니스트이자 '미국 최고의 음악 역사가'로 불리는 Ted Gioia는 재즈 스탠더드, 재즈의 역사, 재즈를 읽다 등 10권이 넘는 책을 썼으며, 스탠포드 재즈 연구 프로그램의 설립자 중 한명이기도 합니다."
```

- 출력

```
또한 Stanford Jazz Research Program의 이사회 회원이기도합니다.
```