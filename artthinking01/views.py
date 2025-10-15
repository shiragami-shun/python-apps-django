from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from googletrans import Translator
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import TimelinePost
from .forms import TimelinePostForm


def home(request):
    return render(request, "artthinking01/home.html")


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, "artthinking01/add_book.html", {"form": form})


def book_list(request):
    books = Book.objects.using('artthinking01').all()  # ← データベースを指定
    return render(request, "artthinking01/book_list.html", {"books": books})


def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(
        request, "artthinking01/edit_book.html", {"form": form, "book": book}
        )


def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')
    return render(request, "artthinking01/delete_book.html", {"book": book})


def translate(request):
    return render(request, "artthinking01/translate.html")


def ranking(request):
    return render(request, "artthinking01/ranking.html")


def timeline(request):
    return render(request, "artthinking01/timeline.html")


def favorites(request):
    return render(request, "artthinking01/favorites.html")


@csrf_exempt
def translate_api(request):
    if request.method != "POST":
        return JsonResponse({"error": "POSTのみ対応"}, status=405)

    try:
        data = json.loads(request.body.decode("utf-8"))
        text = data.get("text", "").strip()
        target = data.get("target_lang", "").strip()

        if not text:
            return JsonResponse({"error": "翻訳テキストがありません"}, status=400)
        if not target:
            return JsonResponse({"error": "ターゲット言語がありません"}, status=400)

        # googletrans が扱う言語コードと入力コードのマッピング
        # (zh-Hans/zh-Hant -> zh-cn/zh-tw 等の変換は内部で調整)
        mapper = {
            "zh-Hans": "zh-cn",
            "zh-Hant": "zh-tw",
            # 必要なら他のマッピングを追加
        }
        dest = mapper.get(target, target)

        translator = Translator()
        translated = translator.translate(text, dest=dest)

        return JsonResponse({"translated_text": translated.text})
    except Exception as e:
        # エラー情報は開発中のみ詳細出力して良い（本番では控えめに）
        return JsonResponse({"error": f"翻訳エラー: {str(e)}"}, status=500)


def add_timeline(request):
    if request.method == 'POST':
        form = TimelinePostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timeline')  # 投稿後に自分のページへリダイレクト
    else:
        form = TimelinePostForm()
    posts = TimelinePost.objects.order_by('-created_at')  # 新しい順
    return render(
        request, 'artthinking01/add_timeline.html',
        {'form': form, 'posts': posts}
        )
