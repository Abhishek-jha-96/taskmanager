from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from Manager.models import Tasks
from Manager.serializer import TaskSerializer, UserSerializer
from Manager.views import TaskDetail
from rest_framework.authtoken.models import Token

class TaskDetailTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token, _ = Token.objects.get_or_create(user=self.user)
        self.task = Tasks.objects.create(title='Test Task', description='Task description', owner=self.user)
        self.view = TaskDetail.as_view()

    def test_task_detail_authenticated(self):
        # Serialize the expected data
        expected_data = TaskSerializer(self.task).data

        request = self.factory.get(f'/manage/Tasks/')
        force_authenticate(request, user=self.user, token=self.token.key)
        response = self.view(request, pk=self.task.pk)

        # Deserialize the response data for comparison
        actual_data = TaskSerializer(response.data).data

        self.assertEqual(response.status_code, 200 if request.user == self.user else 403)
        self.assertEqual(actual_data, expected_data)

    def test_task_detail_unauthenticated(self):
        request = self.factory.get(f'/manage/Tasks/')
        response = self.view(request, pk=self.task.pk)
        self.assertEqual(response.status_code, 401)  # Expecting Unauthorized
