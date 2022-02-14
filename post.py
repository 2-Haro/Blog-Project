class post:
  """
  게시물 클래스
  param id: 글 번호
  param title: 제목
  param content: 내용
  param view_count: 조회수
  """
  def __init__(self, id, title, content, view_count):
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count
  
  def mod_post(self, id, title, content, view_count): # 게시글 수정 메소드
    self.id = id
    self.title = title
    self.content = content
    self.view_count = view_count

  def add_view_count(self): # 조회수 증가 메소드
    self.view_count += 1

  def get_id(self): # id 속성 반환 메소드
    return self.id
  
  def get_title(self): # title 속성 반환 메소드
    return self.title

  def get_content(self): # content 속성 반환 메소드
    return self.content
  
  def get_view_count(self): # view_count 속성 반환 메소드
    return self.view_count

if __name__ == "__main__": # 테스트
  Post = post(1, "테스트", "테스트 1입니다", 0)
  # Post.mod_post(1, "테스트2", "테스트 2입니다", 0)
  # Post.add_view_count()
  print(f"{Post.get_id()} {Post.get_title()} {Post.get_content()} {Post.get_view_count()}")