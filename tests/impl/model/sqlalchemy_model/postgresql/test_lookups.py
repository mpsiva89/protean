import pytest

# Standard Library Imports
from datetime import datetime

# Protean
from protean.core.aggregate import BaseAggregate
from protean.core.field.basic import List, String
from protean.impl.repository.sqlalchemy_repo import Any, In


class GenericPostgres(BaseAggregate):
    ids = List()
    role = String()


@pytest.mark.postgresql
class TestLookups:
    def test_any_lookup(self, test_domain):
        model_cls = test_domain.get_model(GenericPostgres)

        identifier = "foobar"
        lookup = Any("ids", identifier, model_cls)
        expr = lookup.as_expression()

        assert str(expr.compile()) == ":param_1 = ANY (public.any_user.ids)"
        assert expr.compile().params == {"param_1": "foobar"}

    def test_in_lookup(self, test_domain):
        model_cls = test_domain.get_model(GenericPostgres)

        target_roles = ["foo", "bar", "baz"]
        lookup = In("role", target_roles, model_cls)
        expr = lookup.as_expression()

        assert (
            str(expr.compile()) == "public.any_user.role IN (:role_1, :role_2, :role_3)"
        )
        assert expr.compile().params == {
            "role_1": "foo",
            "role_2": "bar",
            "role_3": "baz",
        }

    def test__lookup(self, test_domain):
        model_cls = test_domain.get_model(GenericPostgres)

        target_roles = ["foo", "bar", "baz"]
        lookup = In("role", target_roles, model_cls)
        expr = lookup.as_expression()

        assert (
            str(expr.compile()) == "public.any_user.role IN (:role_1, :role_2, :role_3)"
        )
        assert expr.compile().params == {
            "role_1": "foo",
            "role_2": "bar",
            "role_3": "baz",
        }
