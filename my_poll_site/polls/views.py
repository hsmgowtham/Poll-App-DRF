from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import F

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from general_utils.utils import get_formatted_response

from .models import Choice, Question
from .serializers import QuestionSerializer


class DashboardAPIView(viewsets.ViewSet):
    """
    API Endpoint that allows users to view list of recently published top 5 questions
    """
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        queryset = Question.objects.order_by("-pub_date")[:5]
        serializer = self.serializer_class(queryset, many=True)

        formatted_response = get_formatted_response(
            status=status.HTTP_200_OK,
            data=serializer.data,
            message="",
            total_count=queryset.count(),
        )
        return Response(formatted_response)
    
    def retrieve(self, request, pk=None, *args, **kwargs):
        question = Question.objects.filter(id=pk)
        instance = question.first()

        if not instance:
            formatted_response = get_formatted_response(
                status=status.HTTP_404_NOT_FOUND,
                message="Question not found.",
            )
        else:
            serializer = self.serializer_class(instance)

            formatted_response = get_formatted_response(
                status=status.HTTP_200_OK,
                message="",
                data=serializer.data,
            )

        return Response(formatted_response)
    
    def update(self, pk=None, *args, **kwargs):
        question = Question.objects.filter(id=pk)
        instance = question.first()
        if not instance:
            formatted_response = get_formatted_response(
                status=status.HTTP_404_NOT_FOUND,
                message="Question not found.",
            )
        else:
            serializer = self.serializer_class(instance)

            formatted_response = get_formatted_response(
                status=status.HTTP_200_OK,
                message="",
                data=serializer.data,
            )

        return Response(formatted_response)

    # permission_classes = [permissions.IsAuthenticated]


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
