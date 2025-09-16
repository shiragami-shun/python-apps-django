from django.shortcuts import render

# Create your views here.

import random


def omikuji(request):
    omikuji_result = None

    # ボタンが押されたらランダムでおみくじを選ぶ
    if request.method == "POST":
        omikuji_list = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
        omikuji_result = random.choice(omikuji_list)

    return render(
        request,
        "work07/omikuji.html",
        {"omikuji_result": omikuji_result}
    )


def janken(request):
    result = None
    choices = ["グー", "チョキ", "パー"]
    computer_choice = None
    user_choice = None

    # ボタンが押されたときだけ処理
    if request.method == "POST":
        # どのボタンが押されたか
        user_choice = request.POST.get("choice")
        computer_choice = random.choice(choices)

        # 勝敗判定
        if user_choice == computer_choice:
            result = "あいこ"
        elif (user_choice == "グー" and computer_choice == "チョキ") or \
             (user_choice == "チョキ" and computer_choice == "パー") or \
             (user_choice == "パー" and computer_choice == "グー"):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け…"

    return render(request, "work07/janken.html", {
        "result": result,
        "user_choice": user_choice,
        "computer_choice": computer_choice,
    })


def hi_low(request):
    message = None
    new_number = None
    last_number = None

    # セッションで前回の数字を保存
    if "last_number" not in request.session:
        request.session["last_number"] = random.randint(1, 13)

    last_number = request.session["last_number"]

    if request.method == "POST":
        guess = request.POST.get("guess")  # "Hi" か "Low"
        new_number = random.randint(1, 13)
        request.session["last_number"] = new_number  # 次回用に保存

        if guess == "Hi":
            if new_number > last_number:
                message = f"正解！前回: {last_number}, 今回: {new_number}"
            elif new_number == last_number:
                message = f"同じ数字でした！前回: {last_number}, 今回: {new_number}"
            else:
                message = f"ハズレ…前回: {last_number}, 今回: {new_number}"
        elif guess == "Low":
            if new_number < last_number:
                message = f"正解！前回: {last_number}, 今回: {new_number}"
            elif new_number == last_number:
                message = f"同じ数字でした！前回: {last_number}, 今回: {new_number}"
            else:
                message = f"ハズレ…前回: {last_number}, 今回: {new_number}"

    return render(request, "work07/hi_low.html", {
        "last_number": last_number,
        "message": message
    })
