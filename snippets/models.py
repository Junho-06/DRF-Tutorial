from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class Snippet(models.Model):

    # 작성 날짜 <자동으로 작성 시간이 저장됨>
    created = models.DateTimeField(auto_now_add=True)

    # 제목 <최대글자가 100자, 값이 빈 상태도 저장되는걸 허용, 기본값은 ''>
    title = models.CharField(max_length=100, blank=True, default='')

    # 내용 <최대 글자수가 없음>
    code = models.TextField()

    # <기본값이 False임>
    linenos = models.BooleanField(default=False)

    # 언어 <LANGUAGE_CHOICES 변수 값 들중에 선택함, 기본값이 pyhton, 최대 글자수 100자>
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)

    # 스타일 <STYLE_CHOICES 변수 값 들중에 선택함, 기본값은 friendly, 최대 글자수 100자>
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        # created를 기준으로 정렬함
        ordering = ['created']