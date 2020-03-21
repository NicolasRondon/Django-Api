import json
from core.renderers import CodesuitJSONRenderer


class UserJSONRenderer(CodesuitJSONRenderer):
    object_label = 'user'

    def render(self, data, media_type=None, renderer_context=None):
        token = data.get('token', None)

        if token is not None and isinstance(token, bytes):
            data['token'] = token.decode('utf-8')

        return super(UserJSONRenderer, self).render(data)
