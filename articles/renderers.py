from core.renderers import CodesuitJSONRenderer


class ArticleJSONRenderer(CodesuitJSONRenderer):
    object_label = 'article'
    object_label_plural = 'articles'


class CommentJSONRenderer(CodesuitJSONRenderer):
    object_label = 'comment'
    object_label_plural = 'comments'
