from jobserver.api.models import Job
from jobserver.api.models import JobOutput
from jobserver.api.models import Workspace
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class JobOutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = JobOutput
        fields = ["name", "location", "privacy_level"]


class WorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="workspaces-detail")

    class Meta:
        model = Workspace
        fields = ["id", "url", "name", "repo", "branch", "db", "owner", "created_at"]
        read_only_fields = ["created_at"]


class JobSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="jobs-detail")
    outputs = JobOutputSerializer(many=True, required=False)
    workspace = WorkspaceSerializer(read_only=True)
    workspace_id = serializers.PrimaryKeyRelatedField(
        queryset=Workspace.objects.all(), source="workspace"
    )

    class Meta:
        model = Job
        fields = [
            "url",
            "backend",
            "started",
            "operation",
            "status_code",
            "status_message",
            "outputs",
            "workspace",
            "workspace_id",
            "created_at",
            "started_at",
            "completed_at",
            "callback_url",
        ]
        read_only_fields = ["created_at", "started_at", "completed_at"]

    def create(self, validated_data):
        outputs_data = validated_data.pop("outputs", [])
        job = Job.objects.create(**validated_data)
        for output_data in outputs_data:
            JobOutput.objects.create(job=job, **output_data)
        return job

    def update(self, instance, validated_data):
        outputs_data = validated_data.pop("outputs", [])
        if validated_data.get("workspace", None):
            raise ValidationError("You cannot change a job's workspace")
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if instance.outputs.count() and outputs_data:
            raise ValidationError("You can only set outputs for a job once")
        for output_data in outputs_data:
            instance.outputs.create(**output_data)
        instance.save()
        return instance


class JobWithInlineWorkspaceSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="jobs-detail")
    outputs = JobOutputSerializer(many=True, required=False)
    workspace = WorkspaceSerializer()

    class Meta:
        model = Job
        fields = [
            "url",
            "backend",
            "db",
            "started",
            "operation",
            "status_code",
            "status_message",
            "outputs",
            "workspace",
            "created_at",
            "started_at",
            "completed_at",
            "callback_url",
        ]
        read_only_fields = fields
