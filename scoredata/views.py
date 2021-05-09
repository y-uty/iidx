from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Scoresp, CsvUpload
from .forms import CsvUploadForm, VersionChoice
from .functions import GetVersionNo

def score_entry(request):
    if request.method=='POST':
        form = CsvUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            score_entry_exec()
            return redirect('score_entry')
    else:
        form = CsvUploadForm()
    return render(request, 'scoredata/score_entry.html', {'form':form})

def score_view(request):
    uploaded_all = CsvUpload.objects.all()

    if request.method=='POST':
        ver_no_choosed = request.POST['ver_list'] # formから送信された値を受け取る
        score_all = Scoresp.objects.filter(ver_no=ver_no_choosed) # 受け取った値を条件に再検索
        ver_choice = VersionChoice() # リストを初期化するけど、選んだ値が選択された状態にできる？
        return render(request, 'scoredata/score_view.html', {'score_all':score_all,'uploaded_all':uploaded_all,'ver_choice':ver_choice})
    else:
        ver_choice = VersionChoice()

    score_all = Scoresp.objects.all()
    
    return render(request, 'scoredata/score_view.html', {'score_all':score_all,'uploaded_all':uploaded_all,'ver_choice':ver_choice})

def score_entry_exec():
    import pandas as pd
    import os

    # アップロードしたCSVの最新版を取り込む
    uploaded_newest = list(CsvUpload.objects.order_by('-created_date').values_list('uploaded').first())
    in_score = pd.read_csv('media/' + uploaded_newest[0], encoding='utf-8')

    # A/H譜面からレベル12のみを抽出してまとめる
    score_spa = in_score[in_score['ANOTHER 難易度']==12][['タイトル','ジャンル','アーティスト','バージョン','ANOTHER 難易度','ANOTHER スコア','ANOTHER PGreat','ANOTHER Great','ANOTHER ミスカウント','ANOTHER クリアタイプ','ANOTHER DJ LEVEL']]
    score_sph = in_score[in_score['HYPER 難易度']==12][['タイトル','ジャンル','アーティスト','バージョン','HYPER 難易度','HYPER スコア','HYPER PGreat','HYPER Great','HYPER ミスカウント','HYPER クリアタイプ','HYPER DJ LEVEL']]
    score_spa['譜面'] = 'ANOTHER'
    score_sph['譜面'] = 'HYPER'
    score_spa.columns=['タイトル','ジャンル','アーティスト','バージョン','難易度','スコア','PGreat','Great','ミスカウント','クリアタイプ','DJ LEVEL','譜面']
    score_sph.columns=['タイトル','ジャンル','アーティスト','バージョン','難易度','スコア','PGreat','Great','ミスカウント','クリアタイプ','DJ LEVEL','譜面']
    score_sp = pd.concat([score_spa, score_sph], axis=0)
    score_sp.reset_index(drop=True, inplace=True)

    # 今作未プレイの「---」はそのまま登録できないので置換
    score_sp['ミスカウント'] = score_sp['ミスカウント'].replace('---', 999)
    score_sp['DJ LEVEL'] = score_sp['DJ LEVEL'].replace('---', '')

    # データの洗替登録
    Scoresp.objects.all().delete()
    for i in range(len(score_sp)):
        Scoresp.objects.create(
            title = score_sp['タイトル'][i],
            genre = score_sp['ジャンル'][i],
            artist = score_sp['アーティスト'][i],
            ver_name = score_sp['バージョン'][i],
            ver_no = GetVersionNo(score_sp['バージョン'][i]),
            difficulty = score_sp['譜面'][i],
            level = score_sp['難易度'][i],
            score = score_sp['スコア'][i],
            pgreat = score_sp['PGreat'][i],
            great = score_sp['Great'][i],
            misscount = score_sp['ミスカウント'][i],
            cleartype = score_sp['クリアタイプ'][i],
            djlevel = score_sp['DJ LEVEL'][i]
        )
        count_ins = i
