from .models import TaskModel
from rest_framework import serializers

# class Taskserializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField()
#     desc = serializers.CharField()

# # class TaskSerializer(serializers.Serializer):
# #     id = serializers.IntegerField(read_only =True)
# #     title = serializers.CharField()
# #     desc = serializers.CharField()

#     def create(self,validated_data):
#         return TaskModel.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title',instance.title)
#         instance.desc = validated_data.get('desc',instance.desc)
#         instance.save()
#         return instance
    
from rest_framework import serializers
from .models import TaskModel

class Taskserializer(serializers.ModelSerializer):

    class Meta:
        model = TaskModel
        fields = '__all__'