from django.test import TestCase
from snippets.models import Snippet

from snippets.serializers import SnippetSerializer, SnippetModelSerializer
from rest_framework.renderers import JSONRenderer

from django.utils.six import BytesIO
from rest_framework.parsers import JSONParser


# Create your tests here.
class SnippetSerializerTastCase(TestCase):
    def setUp(self):
        self.snippet_1 = Snippet.objects.create(code='foo = "bar"\n')
        self.snippet_2 = Snippet.objects.create(code='print "hello, world"\n')

    def test_base(self):
        serializer = SnippetSerializer(self.snippet_2)
        print "\n", serializer.data, "\n"

        content = JSONRenderer().render(serializer.data)
        print "\n", content, "\n"
        self.assertEqual(type(content), str)

        stream = BytesIO(content)
        data = JSONParser().parse(stream)

        serializer = SnippetSerializer(data=data)
        print serializer.is_valid()

        print serializer.validated_data

        serializer.save()

    def test_querysets(self):
        serializer = SnippetSerializer(Snippet.objects.all(), many=True)
        print serializer.data
        print type(serializer.data)

        content = JSONRenderer().render(serializer.data)
        print content


class SnippetModelSerializerTestCase(TestCase):
    def setUp(self):
        self.snippet_1 = Snippet.objects.create(code='foo = "bar"\n')
        self.snippet_2 = Snippet.objects.create(code='print "hello, world"\n')

    def test_base(self):
        serializer = SnippetModelSerializer()
        print repr(serializer)


class CommonTestCase(TestCase):
    def test_common(self):
        a = 5
        l = (1, 2, 3)
        if l.__contains__(a):
            print a
