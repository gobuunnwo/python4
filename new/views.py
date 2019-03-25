from django.shortcuts import render,redirect
from .models import Todo

from django.views.decorators.http import require_POST
from .forms import TodoForm

def home(request):
    # modelsのTodoクラスのobjectsを取得
    todo_list=Todo.objects.order_by('id')
    #forms.pyのTodoクラスから作ったformオブジェクトの作成（TodoFormクラスの中に入る）
    form=TodoForm()
    context={
        'todo_list':todo_list, 
        'form':form
    }
    return render(request, 'todo/home.html',context)


@require_POST
def addTodo(request):
    form=TodoForm(request.POST)

    if form.is_valid():
        new_todo=Todo(text=request.POST['text'])
        new_todo.save()
    # print(request.POST['text'])
    # new/urlsの'home'に飛ぶ
    return redirect('home')