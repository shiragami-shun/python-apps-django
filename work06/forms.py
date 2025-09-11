from django import forms


class ReiwaForm(forms.Form):
    # 入力フィールドを定義
    year = forms.IntegerField(
        label="令和何年ですか？",
        min_value=1,  # 令和は1年以上
        widget=forms.NumberInput(attrs={"placeholder": "例: 5"})
    )


class BMIForm(forms.Form):
    weight = forms.FloatField(label="体重(kg)", min_value=0)
    height = forms.FloatField(label="身長(cm)", min_value=0)


class WarikanForm(forms.Form):
    total_amount = forms.FloatField(label="合計金額(円)", min_value=0)
    people = forms.IntegerField(label="人数", min_value=1)


class SavingsForm(forms.Form):
    monthly_amount = forms.FloatField(label="毎月の貯金額(円)", min_value=0)
    years = forms.IntegerField(label="貯金期間(年)", min_value=1)


class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="1つ目の数字")
    num2 = forms.FloatField(label="2つ目の数字")
    operation = forms.ChoiceField(
        label="演算",
        choices=[('+', '足し算'), ('-', '引き算'), ('*', '掛け算'), ('/', '割り算')]
    )