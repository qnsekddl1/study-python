# 상속 예제
# 게시글 - 댓글(상속 관계)
# 게시글: 게시글 번호, 작성자, 제목, 내용
class Post:
    # 정적변수의 선언
    post_number = 0
    # 게시글 중 post_writer, post_title, post_content의 내용을 전달 받는다
    def __init__(self, post_writer, post_title, post_content):

        # 게시글 번호 자동 증가
        Post.post_number += 1
        # 게시글의 번호
        self.post_number = Post.post_number
        # 게시글의 작성자
        self.post_writer = post_writer
        # 게시글의 제목
        self.post_title = post_title
        # 게시글의 내용
        self.post_content = post_content

    # 게시글 class에 게시글 정보 출력 메소드를 만들고
    def post_info(self):
        # 게시글 번호, 게시글 작성자, 게시글 제목, 게시글 내용을 출력하는 메소드
        print(f'{self.post_number}, {self.post_writer}, {self.post_title}, {self.post_content}')

# 댓글: 댓글 번호, 게시글 번호, 작성자, 댓글 내용

# 부모 생성자: Post, 자식 생성자: Comment
class Comment(Post):
    # 정적 변수 선언
    comment_number = 0
    # 부모 생성자의 
    def __init__(self, post_writer, post_title, post_content, comment_content):
        super().__init__(post_writer, post_title, post_content)
        # 댓글 번호 자동 증가
        Comment.comment_number =+ 1
        # 부모 생성자의 post.number를 받아온다
        self.post_number = Post.post_number
        # 부모 생성자의 post.writer를 받아온다
        self.post_writer = post_writer
        # comment_number가 1씩 증가 한다
        self.comment_number = Comment.comment_number
        # 댓글의 내용
        self.comment_content = comment_content

    # 댓글 class에서 정보 출력 메소드를 상속받고
# 댓글 class에 게시글 정보 출력 메소드를 만들고
    def comment_info(self):
        # 부모 생성자에서의 게시글 정보를 가져와서
        super().post_info()
        # 댓글 정글 정보에 추가 해서 출력 하는 메소드
        print(f'{self.post_number}, {self.comment_number}, {self.post_writer}, {self.comment_content}')


# lee = Post('이기영', '안녕하세요', '반갑습니다')
# kwon = Post('권가은','안녕하세요', '잘부탁드리겠습니다')

kim = Comment('김아무개','반갑습니다','잘부탁드립니다', '어쩌라고')


# lee.post_info()
# kwon.post_info()
kim.comment_info()
