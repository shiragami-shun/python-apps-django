from django.shortcuts import render, get_object_or_404, redirect
from .models import Memo
from .forms import MemoForm


def memo_list(request):
    """メモ一覧を表示"""
    memos = Memo.objects.all().order_by('-created_at')
    return render(request, 'work08/memo_list.html', {'memos': memos})


def memo_create(request):
    """新しいメモを作成"""
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'work08/memo_edit.html', {'form': form})


def memo_edit(request, pk):
    """既存のメモを編集"""
    memo = get_object_or_404(Memo, pk=pk)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'work08/memo_edit.html', {'form': form})
