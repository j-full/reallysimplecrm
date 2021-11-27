from django.contrib.auth.mixins import UserPassesTestMixin

class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.created_by