from django.core.exceptions import PermissionDenied
from django.urls import reverse
class SitePermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # サーバー起動時
    def __call__(self, request):
        # リクエスト前処理
        response = self.get_response(request)
        # レスポンス後処理
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        has_site_permisson = False
        if request.user.is_superuser or request.user.is_staff:
            has_site_permisson = True
        admin_index = reverse('admin:index')
        print(admin_index)
        # 権限を持っていないユーザーが/admin/配下にきたらエラー
        if request.path.startswith(admin_index):
            if not has_site_permisson:
                raise PermissionDenied
        print(has_site_permisson)
        request.user.has_site_permission = has_site_permisson

