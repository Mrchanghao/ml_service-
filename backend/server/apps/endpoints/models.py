from django.db import models


# Create your models here.

class Endpoint(models.Model):
    """
    the endpoint object 은 ml api의 엔드포인트를 나타낸다
    속성
    name
    owner
    created_at: the date when endpoint was created
    """
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    '''
    ml 알고리즘 객체를 나타냄
    속성
    name
    description:  알고리즘이 어떻게 작동하는지에 대한 짧은 설명
    code
    version
    owner
    created_At
    parent_endpoint
    '''

    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=50000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
    상태 변화를 나타낸다
    속성
    status: etc --> testing, staging, production, ab_testing
    active: 현재 운영되는지 true or false
    created_by: creator 의 이름
    created_at
    parent_mlalgorithm: 참조하는 mlalgorithm
    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)


class MLRequest(models.Model):
    '''
    ml 알고리즘에 모든 요청에 대해 정보를 지킨다.
    속성
    input_data: input data to ml algorithm in json format
    full_response : response of the algorithm
    feedback: response에 대한 피드백
    created_at : date when req
    parent_mlalgorithm: 계산하기 위해 참조한 알고리즘
    '''
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)
