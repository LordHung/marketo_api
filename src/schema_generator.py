from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework import exceptions
from rest_framework.permissions import AllowAny
from rest_framework.renderers import CoreJSONRenderer
from rest_framework.response import Response
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView
from rest_framework_swagger import renderers


class MarketoSchemaGenerator(SchemaGenerator):
    def get_filter_fields(self, path, method, view):
        if not getattr(view, 'filter_backends', None):
            return []

        fields = []
        for filter_backend in view.filter_backends:
            fields += filter_backend().get_schema_fields(view)

        ret = []
        for field in fields:
            if method == 'GET':
                if field.location == 'query' and field.schema != 'DELETE':
                    ret.append(field)
            elif method == 'POST':
                if field.location != 'query' and field.schema != 'PUT':
                    ret.append(field)
            elif method == 'PUT':
                if field.location != 'query':
                    ret.append(field)
            elif method == 'DELETE':
                if field.schema == 'DELETE':
                    ret.append(field)
        return ret


def get_swagger_view(title=None, url=None, patterns=None, urlconf=None):
    """
    Returns schema view which renders Swagger/OpenAPI.
    """
    class SwaggerSchemaView(APIView):
        _ignore_model_permissions = True
        exclude_from_schema = True
        permission_classes = [AllowAny]
        # permission_required = None
        renderer_classes = [
            CoreJSONRenderer,
            renderers.OpenAPIRenderer,
            renderers.SwaggerUIRenderer
        ]

        def get(self, request):
            generator = MarketoSchemaGenerator(
                title=title,
                url=url,
                patterns=patterns,
                urlconf=urlconf
            )
            schema = generator.get_schema(request=request)

            if not schema:
                raise exceptions.ValidationError(
                    'The schema generator did not return a schema Document'
                )

            return Response(schema)

    return SwaggerSchemaView.as_view()
