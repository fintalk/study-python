# P138 の条件式に論理演算子を使った例，を写経し実行して下さい
# pass 

# 以下のディクショナリは，名前とテスト結果の辞書です．各要素に対して，以下の処理を行って下さい.(ヒント：P123のキーを使ったループを使いましょう)

testscore = {
    'Curtice': 54,  'Aurie': 98,  'Nikolia': 34,  
    'Konstanze': 1,  'Thorvald': 98,  'Allyson': 89,  
    'Paquito': 26,  'Mathilde': 26,  'Sampson': 100,  'Edvard': 84}

for name in testscore:
    if testscore[name] < 60:
        print(name, "不合格！")
    elif 75 > testscore[name] >= 60:
        print(name, "合格です")
    else:
        print(name, "素晴らしい！合格です")

# 以下のディクショナリは，名前とテスト結果の辞書です．各要素に対して，以下の処理を行って下さい.（ヒント：P122のキーの存在確認を使ってみましょう）

testscore2 = {
    'Zonda': {'score': 69, 'subject': '算数'},
    'Randi': {'score': 55, 'subject': '理科'},
    'Valentina': {'score': 53, 'subject': '算数'},
    'Miof mela': {'score': 89, 'subject': '社会'},
    'Kort': {'score': 98, 'subject': '算数'},
    'Odelia': {'score': 28, 'subject': '理科'},
    'Charissa': {'score': 37, 'subject': '社会'},
    'Francklin': {'score': 18, 'subject': '国語'},
    'Pat': {'score': 95, 'subject': '社会'},
    'Dori': {'score': 95, 'subject': '算数'}
    }

for name in testscore2:
    score_dict = testscore2[name]
    if score_dict['subject']=='算数':
        if score_dict['score'] < 60:
            print(name, "不合格！")
        elif 60 <= score_dict['score'] < 75:
            print(name, "合格です")
        else:
            print(name, "素晴らしい！合格です")
    else:
        print(name, "テストを受けて下さい")
        



        
    
