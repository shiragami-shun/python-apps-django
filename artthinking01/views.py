from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from googletrans import Translator
from .models import Book
from .forms import BookForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Post
from django.db import connections


def home(request):
    return render(request, "artthinking01/home.html")


def book_list(request):
    books = Book.objects.using('artthinking01').all()  # ← データベースを指定
    return render(request, "artthinking01/book_list.html", {"books": books})


def translate(request):
    return render(request, "artthinking01/translate.html")


def ranking(request):
    # お気に入り数が多い順に並べる
    books = Book.objects.using('artthinking01').all().order_by('-favorites')
    
    return render(request, "artthinking01/ranking.html", {"books": books})


def timeline(request):
    """artthinking01 データベースの Post テーブルから投稿を取得して表示"""

    posts = []  # 投稿データを入れるリスト

    try:
        # ここで artthinking01 データベースに接続
        with connections['artthinking01'].cursor() as cursor:
            cursor.execute("""
                SELECT id, name, title, content, date
                FROM artthinking01_post
                ORDER BY date DESC;
            """)
            rows = cursor.fetchall()  # 全行を取得

            # rows を辞書形式に変換して扱いやすくする
            for row in rows:
                posts.append({
                    'id': row[0],
                    'name': row[1],
                    'title': row[2],
                    'content': row[3],
                    'date': row[4],
                })

    except Exception as e:
        print("❌ 投稿データ取得エラー:", e)

    # 投稿データをテンプレートに渡す
    return render(request, 'artthinking01/timeline.html', {'posts': posts})


def favorites(request):
    """お気に入りに登録された本を表示"""
    try:
        favorites = Book.objects.using(
            'artthinking01'
            ).filter(favorites__gt=0).order_by('-favorites')
    except Exception as e:
        print("❌ お気に入り取得エラー:", e)
        favorites = []

    return render(
        request, 'artthinking01/favorites.html', {'favorites': favorites}
        )


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
        name = request.POST.get('name')
        title = request.POST.get('title')
        content = request.POST.get('content')

        if name and title and content:
            # artthinking01 データベースに保存
            Post.objects.using('artthinking01').create(
                name=name,
                title=title,
                content=content
            )
            return redirect('add_timeline')

    # 投稿一覧を artthinking01 から取得
    posts = Post.objects.using('artthinking01').all().order_by('-date')
    return render(request, 'artthinking01/add_timeline.html', {'posts': posts})


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            # 通常 save() は default DB に保存されるので
            # .save(using='artthinking01') と指定する
            book.save(using='artthinking01')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'artthinking01/add_book.html', {'form': form})


def delete_book(request, pk):
    book = Book.objects.using('artthinking01').get(pk=pk)
    book.delete(using='artthinking01')
    return redirect('book_list')


def edit_book(request, pk):
    book = get_object_or_404(Book.objects.using('artthinking01'), pk=pk)
    if request.method == "POST":
        form = BookForm(
            request.POST, request.FILES, instance=book
            )  # request.FILESを追加
        if form.is_valid():
            book_instance = form.save(commit=False)
            book_instance.save(using='artthinking01')
            return redirect('book_list')  # 保存後に本一覧へ
    else:
        form = BookForm(instance=book)
    return render(
        request,
        'artthinking01/edit_book.html',
        {'form': form, 'book': book}
    )


def favorite_book(request, pk):
    """本をお気に入りに追加"""
    try:
        book = Book.objects.using('artthinking01').get(pk=pk)
        book.favorites = (book.favorites or 0) + 1
        book.save(using='artthinking01')
    except Book.DoesNotExist:
        pass  # 本が存在しない場合は無視
    return redirect('book_list')
