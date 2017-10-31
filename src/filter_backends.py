import coreapi
from rest_framework.filters import BaseFilterBackend


class StoreFilterBackend(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='icon',
            location='form',
            required=True,
            type='file',
            description='image file',
        ),
            coreapi.Field(
            name='title',
            location='form',
            required=True,
            type='string',
            description='title',
        )
        ]
