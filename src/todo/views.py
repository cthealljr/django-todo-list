from collections.abc import Sequence
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
)

from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from django.urls import reverse

from .models import TodoItem

# Create your views here.

class ListTodoItems(ListView):
    """ Class-based view to list all Todo items. """
    template_name = "todo/list_todos.html"
    model = TodoItem

    def get_ordering(self) -> Sequence[str]:
        # Only supports order by a single column, for now.
        return [self.request.GET.get("sort_by", "name")]


class CreateTodoItem(CreateView):
    """ Class-based view to create a new Todo item. """
    template_name = "todo/create_todo.html"
    model = TodoItem
    fields = [
        "name",
        "description",
        "due_date",
    ]

    def get_success_url(self) -> str:
        return reverse("todo-list")


class DeleteTodoItem(DeleteView):
    """ Class-based view to delete a Todo item. """
    template_name = "todo/todo_confirm_delete.html"
    model = TodoItem

    def get_success_url(self) -> str:
        return reverse("todo-list")


@require_POST
def handle_mark_todo_done(request, todo_id):
    """ Function-based view to mark a Todo item as done. """
    # Lookup Todo item by the given id
    item = TodoItem.objects.get(id=todo_id)

    # Check if item is already marked as done
    if not item.done:
        item.done = True
        item.save()

    # Redirect back to the todo list
    return redirect(reverse("todo-list"))

