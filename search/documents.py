from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from django_elasticsearch_dsl.fields import TextField,ObjectField,DateField

from .models import University


@registry.register_document
class UniversityDocument(Document):
    class Index:
        name = "university"
        settings={
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    class Django:
        model = University
        fields = [
            'id',
            'alpha_two_code',
            'country',
            'domain',
            'name',
            'web_page',
            'created_date',
        ]