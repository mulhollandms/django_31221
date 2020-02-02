from django.test import TestCase
from myapp.models import MyModel

# Create your tests here.
class TestMyApp(TestCase):
    fixtures = ['i_myapp']
    def test_mymodel(self):
        for mymodel_instance in MyModel.objects.all():
            self.assertEqual(type(mymodel_instance.metadata), dict)