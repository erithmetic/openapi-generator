# coding: utf-8

# flake8: noqa

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from petstore_api.api.another_fake_api import AnotherFakeApi
from petstore_api.api.default_api import DefaultApi
from petstore_api.api.fake_api import FakeApi
from petstore_api.api.fake_classname_tags_123_api import FakeClassnameTags123Api
from petstore_api.api.pet_api import PetApi
from petstore_api.api.store_api import StoreApi
from petstore_api.api.user_api import UserApi

# import ApiClient
from petstore_api.api_client import ApiClient
from petstore_api.configuration import Configuration
from petstore_api.exceptions import OpenApiException
from petstore_api.exceptions import ApiTypeError
from petstore_api.exceptions import ApiValueError
from petstore_api.exceptions import ApiKeyError
from petstore_api.exceptions import ApiAttributeError
from petstore_api.exceptions import ApiException
# import models into sdk package
from petstore_api.models.additional_properties_class import AdditionalPropertiesClass
from petstore_api.models.animal import Animal
from petstore_api.models.api_response import ApiResponse
from petstore_api.models.array_of_array_of_number_only import ArrayOfArrayOfNumberOnly
from petstore_api.models.array_of_number_only import ArrayOfNumberOnly
from petstore_api.models.array_test import ArrayTest
from petstore_api.models.capitalization import Capitalization
from petstore_api.models.cat import Cat
from petstore_api.models.cat_all_of import CatAllOf
from petstore_api.models.category import Category
from petstore_api.models.class_model import ClassModel
from petstore_api.models.client import Client
from petstore_api.models.dog import Dog
from petstore_api.models.dog_all_of import DogAllOf
from petstore_api.models.enum_arrays import EnumArrays
from petstore_api.models.enum_class import EnumClass
from petstore_api.models.enum_test import EnumTest
from petstore_api.models.file import File
from petstore_api.models.file_schema_test_class import FileSchemaTestClass
from petstore_api.models.foo import Foo
from petstore_api.models.format_test import FormatTest
from petstore_api.models.has_only_read_only import HasOnlyReadOnly
from petstore_api.models.health_check_result import HealthCheckResult
from petstore_api.models.inline_object import InlineObject
from petstore_api.models.inline_object1 import InlineObject1
from petstore_api.models.inline_object2 import InlineObject2
from petstore_api.models.inline_object3 import InlineObject3
from petstore_api.models.inline_object4 import InlineObject4
from petstore_api.models.inline_object5 import InlineObject5
from petstore_api.models.inline_response_default import InlineResponseDefault
from petstore_api.models.list import List
from petstore_api.models.map_test import MapTest
from petstore_api.models.mixed_properties_and_additional_properties_class import MixedPropertiesAndAdditionalPropertiesClass
from petstore_api.models.model200_response import Model200Response
from petstore_api.models.model_return import ModelReturn
from petstore_api.models.name import Name
from petstore_api.models.nullable_class import NullableClass
from petstore_api.models.number_only import NumberOnly
from petstore_api.models.order import Order
from petstore_api.models.outer_composite import OuterComposite
from petstore_api.models.outer_enum import OuterEnum
from petstore_api.models.outer_enum_default_value import OuterEnumDefaultValue
from petstore_api.models.outer_enum_integer import OuterEnumInteger
from petstore_api.models.outer_enum_integer_default_value import OuterEnumIntegerDefaultValue
from petstore_api.models.pet import Pet
from petstore_api.models.read_only_first import ReadOnlyFirst
from petstore_api.models.special_model_name import SpecialModelName
from petstore_api.models.tag import Tag
from petstore_api.models.user import User

