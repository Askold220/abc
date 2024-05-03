
from django.shortcuts import render
from .forms import MessageForm

def message_form(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            return render(request, 'message_sent.html')
    else:
        form = MessageForm()
    return render(request, 'message_form.html', {'form': form})
