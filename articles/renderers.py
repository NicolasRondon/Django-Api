from core.renderers import CodesuitJSONRenderer


class ArticleJSONRenderer(CodesuitJSONRenderer):
    object_label = 'article'
    pagination_object_label = 'articles'
    pagination_count_label = 'articlesCount'


class CommentJSONRenderer(CodesuitJSONRenderer):
    object_label = 'comment'
    pagination_object_label = 'comments'
    pagination_count_label = 'commentsCount'
