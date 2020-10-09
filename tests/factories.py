import factory

from jobserver.models import Job, JobOutput, JobRequest, User, Workspace


class JobFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Job

    job_request = factory.SubFactory("tests.factories.JobRequestFactory")


class JobOutputFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobOutput

    location = factory.Sequence(lambda n: f"location {n}")


class JobRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = JobRequest

    created_by = factory.SubFactory("tests.factories.UserFactory")
    workspace = factory.SubFactory("tests.factories.WorkspaceFactory")

    requested_actions = []


class WorkspaceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Workspace

    repo = factory.Sequence(lambda n: "http://example.com/org-{n}/repo-{n}")


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user-{n}")
    email = factory.Sequence(lambda n: f"user-{n}@example.com")
