"""Module to setup Factories and other required artifacts for tests"""
import os

import pytest

os.environ['PROTEAN_CONFIG'] = 'tests.support.sample_config'


@pytest.fixture(autouse=True)
def run_around_tests():
    """Initialize DogModel with Dict Repo"""
    from protean.core.repository import repo_factory
    from tests.support.dog import (DogModel, RelatedDogModel, DogRelatedByEmailModel,
                                   HasOneDog1Model, HasOneDog2Model, HasOneDog3Model)
    from tests.support.human import (HumanModel, HasOneHuman1Model,
                                     HasOneHuman2Model, HasOneHuman3Model)

    repo_factory.register(DogModel)
    repo_factory.register(RelatedDogModel)
    repo_factory.register(DogRelatedByEmailModel)
    repo_factory.register(HasOneDog1Model)
    repo_factory.register(HasOneDog2Model)
    repo_factory.register(HasOneDog3Model)
    repo_factory.register(HumanModel)
    repo_factory.register(HasOneHuman1Model)
    repo_factory.register(HasOneHuman2Model)
    repo_factory.register(HasOneHuman3Model)

    # A test function will be run at this point
    yield

    repo_factory.Dog.delete_all()
    repo_factory.RelatedDog.delete_all()
    repo_factory.DogRelatedByEmail.delete_all()
    repo_factory.HasOneDog1.delete_all()
    repo_factory.HasOneDog2.delete_all()
    repo_factory.HasOneDog3.delete_all()
    repo_factory.Human.delete_all()
    repo_factory.HasOneHuman1.delete_all()
    repo_factory.HasOneHuman2.delete_all()
    repo_factory.HasOneHuman3.delete_all()
