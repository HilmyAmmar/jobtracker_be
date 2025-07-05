from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer

# Create your views here.
class JobView(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        jobs_serializer = JobSerializer(jobs, many=True)
        return Response(jobs_serializer.data)
    
    def get_id(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job_serializer = JobSerializer(job)
            return Response(job_serializer.data)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        
    def post(self, request):
        job_serializer = JobSerializer(data=request.data)
        if job_serializer.is_valid():
            job_serializer.save()
            return Response(job_serializer.data, status=201)
        return Response(job_serializer.errors, status=400)
    
    def put(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job_serializer = JobSerializer(job, data=request.data, partial=True)
            if job_serializer.is_valid():
                job_serializer.save()
                return Response(job_serializer.data)
            return Response(job_serializer.errors, status=400)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
        
    def patch(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job_serializer = JobSerializer(job, data=request.data, partial=True)
            if job_serializer.is_valid():
                job_serializer.save()
                return Response(job_serializer.data)
            return Response(job_serializer.errors, status=400)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)

        
    def delete(self, request, job_id):
        try:
            job = Job.objects.get(id=job_id)
            job.delete()
            return Response({"message": "Job deleted successfully"}, status=204)
        except Job.DoesNotExist:
            return Response({"error": "Job not found"}, status=404)
            

        