questions = [
    {
        "question": "조별 과제에서 당신의 역할은?",
        "choice1": "자료조사 및 정리",
        "choice2": "정리된 자료로 PPT 만들기 (발표 빼고)",
    },
    {
        "question": "이 중에서 운명적인 이끌림이 느껴지는 것은? 없다면 눈을 감고 찍어보세요!",
        "choice1": "흑백으로 이루어진 데이터베이스에서 원하는 정보만 쏙 뽑아내서 정리하기",
        "choice2": "컬러풀한 화면을 보며 사용자가 보기 좋고 편리하게 정보 배치하기",
    },
    {
        "question": "밴드에 들어가기로 했어요. (실력은 동일하다고 했을 때)",
        "choice1": "보컬 할래.",
        "choice2": "베이스기타 할래.",
    },
    {
        "question": "아이언맨 수트과 자비스 중 하나를 만들 수 있다면?",
        "choice1": "자비스",
        "choice2": "아이언맨 수트",
    }
]

cnt=0
for i in range(0,4):
  for key, value in questions[i].items():
    print(key,": ", value)
  a = int(input("해당되는것에 번호를 입력해주세요(1 or 2) : "))
  if(a==1):
    cnt += 1

if(cnt>=3):
  print("백엔드 개발자")
elif(cnt==2):
  print("풀스택 개발자")
else:
  print("프론트엔드 개발자")