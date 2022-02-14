import os
import csv
from post import post

# data.csv 파일이 위치한 경로
file_path = "./data.csv"

# post 객체를 저장할 리스트
post_list = []

# data.csv 파일이 있을 때
if os.path.exists(file_path): # os.path 모듈 내의 exists 함수에 file_path를 인자로 넘겨줌 -> 경로에 파일이 있다면 True, 없다면 False 반환
  # 게시글 로딩
  print("게시글 로딩중...")
  file = open(file_path, "r", encoding="utf8")
  reader = csv.reader(file)
  for data in reader:
    Post = post(int(data[0]), data[1], data[2], int(data[3])) # data[0]: id, data[1]: title, data[2]: content, data[3]: view_count
    post_list.append(Post) # post 객체 2개(data.csv 파일의 첫번째 줄, 두번째 줄)를 post_list에 append
else: # 파일 생성
  file = open(file_path, "w", encoding="utf8", newline="")
  file.close()

# 게시글 쓰기
def write_post():
  print("\n- 게시글 쓰기 -")
  title = input("제목을 입력해 주세요: ")
  content = input("내용을 입력해 주세요: ")
  # 글 번호
  id = post_list[-1].get_id() + 1 # 리스트의 마지막 요소는 index -1로 접근할 수 있다
  Post = post(id, title, content, 0)
  post_list.append(Post)
  print("게시글이 등록되었습니다.")

# 게시글 목록
def list_post():
  print("\n- 게시글 목록 -")
  id_list = []
  for post in post_list:
    print("번호: ", post.get_id())
    print("제목: ", post.get_title())
    print("조회수: ", post.get_view_count())
    print("")
    id_list.append(post.get_id())

  while True:
    # 예외 처리
    try:
      id = int(input("* 글 번호를 선택해 주세요(메뉴로 돌아가려면 -1을 입력해 주세요.): "))
      if id in id_list:
        detail_post(id)
        break
      elif id == -1:
        break
      else:
        print("없는 글 번호입니다.")
    except ValueError:
      print("숫자를 입력해 주세요.")

# 게시글 상세
def detail_post(id):
  print("\n- 게시글 상세 -")
  for post in post_list:
    if post.get_id() == id:
      post.add_view_count() # post.py 파일의 add_view_count
      print("번호:", post.get_id())
      print("제목:", post.get_title())
      print("본문:", post.get_content())
      print("조회수:", post.get_view_count())
      target_post = post

  while True:
    print("* 수정: 1 삭제: 2 (메뉴로 돌아가려면 -1을 입력해 주세요.)")
    # 예외 처리
    try:
      choice = int(input())
      if choice == 1:
        update_post(target_post)
        break
      elif choice == 2:
        delete_post(target_post)
        break
      elif choice == -1:
        break
      else:
        print("잘못 입력했습니다.")
    except ValueError:
      print("숫자를 입력해 주세요.")

# 게시글 수정
def update_post(target_post):
  print("\n- 게시글 수정 -")
  title = input("제목을 입력해 주세요: ")
  content = input("본문을 입력해 주세요: ")
  target_post.mod_post(target_post.id, title, content, target_post.view_count) # post.py 파일의 mod_post
  print("게시글이 수정되었습니다.")

# 게시글 삭제
def delete_post(target_post):
  post_list.remove(target_post) # remove 메소드를 사용해서 삭제
  print("게시글이 삭제되었습니다.")

# 게시글 저장
def save():
  file = open(file_path, "w", encoding="utf8", newline="")
  writer = csv.writer(file)
  for post in post_list:
    row = [post.get_id(), post.get_title(), post.get_content(), post.get_view_count()] # csv 파일은 리스트 형태로 저장 가능
    writer.writerow(row)
  file.close()
  print("저장이 완료되었습니다.")
  print("프로그램 종료")

# 메뉴 출력
while True:
  print("\n- Haro's Blog -")
  print("- 메뉴를 선택해 주세요 -")
  print("1. 게시글 쓰기")
  print("2. 게시글 목록")
  print("3. 프로그램 종료")
  # 예외 처리
  try:
    choice = int(input())
  except ValueError: # 숫자를 입력하지 않았을 때 실행
    print("숫자를 입력해 주세요.")
  else: # 오류가 발생하지 않았을 때 실행
    if choice == 1:
      write_post()
    elif choice == 2:
      list_post()
    elif choice == 3:
      save()
      break
    else:
      print("1, 2, 3 중 하나를 입력해 주세요.")