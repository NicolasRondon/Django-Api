from core.renderers import CodesuitJSONRenderer


class ProfileJSONRenderer(CodesuitJSONRenderer):
    object_label = 'profile'
    pagination_object_label = 'profiles'
    pagination_count_label = 'profilesCount'