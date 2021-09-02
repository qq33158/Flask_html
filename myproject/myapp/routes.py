# HOME page route
# Use render_template() function # 處理template的function
from flask import render_template
from flask import flash,redirect,jsonify
from flask_sqlalchemy import SQLAlchemy
from myapp import app
from myapp.forms import UseModelForm1, UseModelForm2, UseModelForm3
from myapp.models import MLTrain
import json
from myapp.model import model

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='無殼蝸牛')

@app.route('/usemodel', methods=['GET','POST'])
def usemodel():
    form = UseModelForm2()
    if form.validate_on_submit():
        res1 = model.add({form.model.data},{form.model1.data},{form.model2.data},{form.param.data}) # 連model
        return render_template('use_model.html', title='Predict', results = [1],results2=res1[0],results3=res1[1], form=form)
   
    return render_template('use_model.html', title='Predict', form=form)

@app.route('/usemodel_pro', methods=['GET','POST'])
def usemodel_pro():
    form = UseModelForm3()
    if form.validate_on_submit():
        flash(f'Use Model requested for model: {form.model.data}')
        sql_cmd = f"""SELECT * FROM predict_pro WHERE zipcode='{form.model.data}';"""
        db = SQLAlchemy()
        query_data = db.engine.execute(sql_cmd)
        list1 = []
        for row in query_data:
            json_data = {'zipcode':0,'address':0,'lat':0,'lng':0,\
                         'bedroom':0,'bathroom':0,'sqft':0,'Predict_price_sqft':0,'Actual_price_sqft':0}
            json_data['zipcode'] = row[0]
            json_data['address'] = row[1]
            json_data['lat'] = row[2]
            json_data['lng'] = row[3]
            json_data['bedroom'] = row[4]
            json_data['bathroom'] = row[5]
            json_data['sqft'] = row[6]
            json_data['Predict_price_sqft'] = row[7]
            json_data['Actual_price_sqft'] = row[8]
            list1 += [json_data]
        with open('myapp/static/file3.json', 'w+', encoding='utf8') as f:
            json.dump(list1, f,ensure_ascii=False)
        return render_template('use_model_pro.html', title='Predict', results=query_data, form=form)
    return render_template('use_model_pro.html', title='Predict_Pro', form=form)

@app.route('/information', methods=['GET','POST'])
def information():
    form = UseModelForm1()
    if form.validate_on_submit():
        if form.model.data == form.model1.data:
            if form.model2.data == 'school':
                sql_cmd1 = f"""SELECT zipcode, grade1_5 , grade6_8 , grade9_12 FROM inf_list WHERE zipcode='{form.model.data}';"""
                db = SQLAlchemy()
                query_data = db.engine.execute(sql_cmd1)
                list1 = []
                list2 = ['zipcode','grade1_5' , 'grade6_8' , ' grade9_12']
                i=0
                for row in query_data:
                    for row1 in row:
                            json_data = {'country':0,'population':0}
                            json_data['country'] = list2[i]
                            json_data['population'] = row1
                            list1 += [json_data]
                            i+=1
                    with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
                    with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
            elif form.model2.data == 'walk_transit':
                sql_cmd1 = f"""SELECT zipcode, walkscore , transitscore FROM inf_list WHERE zipcode='{form.model.data}';"""
                db = SQLAlchemy()
                query_data = db.engine.execute(sql_cmd1)
                list1 = []
                list2 = ['zipcode','walkscore','transitscore']
                i=0
                for row in query_data:
                    for row1 in row:
                            json_data = {'country':0,'population':0}
                            json_data['country'] = list2[i]
                            json_data['population'] = row1
                            list1 += [json_data]
                            i+=1
                    with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
                    with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
            elif form.model2.data == 'year_price':
                sql_cmd1 = f"""SELECT zipcode, before2018, 2019y, 2020y, 2021y FROM inf_list WHERE zipcode='{form.model.data}';"""
                db = SQLAlchemy()
                query_data = db.engine.execute(sql_cmd1)
                list1 = []
                list2 = ['zipcode','before2018','2019','2020','2021']
                i=0
                for row in query_data:
                    for row1 in row:
                            json_data = {'country':0,'population':0}
                            json_data['country'] = list2[i]
                            json_data['population'] = row1
                            list1 += [json_data]
                            i+=1
                    with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
                    with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
            else:
                sql_cmd1 = f"""SELECT zipcode, AfricanRatio, LatinoRatio, AsianRatio, IndianRatio, OthersRatio FROM inf_list WHERE zipcode='{form.model.data}';"""
                db = SQLAlchemy()
                query_data = db.engine.execute(sql_cmd1)
                list1 = []
                list2 = ['zipcode','AfricanRatio','LatinoRatio','AsianRatio','IndianRatio','OthersRatio']
                i=0
                for row in query_data:
                    for row1 in row:
                            json_data = {'country':0,'population':0}
                            json_data['country'] = list2[i]
                            json_data['population'] = row1
                            list1 += [json_data]
                            i+=1
                    with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)
                    with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                        json.dump(list1, f,ensure_ascii=False)          
        else:
            if form.model2.data == 'school':
                sql_cmd1 = f"""SELECT zipcode, grade1_5 , grade6_8 , grade9_12 FROM inf_list WHERE zipcode='{form.model.data}';"""
                sql_cmd2 = f"""SELECT zipcode, grade1_5 , grade6_8 , grade9_12 FROM inf_list WHERE zipcode='{form.model1.data}';"""
                db = SQLAlchemy()
                query_data1 = db.engine.execute(sql_cmd1)
                query_data2 = db.engine.execute(sql_cmd2)
                list1 = []
                list2 = []
                list3 = ['zipcode','grade1_5' , 'grade6_8' , ' grade9_12']
                i=0
                for row in query_data1:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[i]
                        json_data['population'] = row1
                        list1 += [json_data]
                        i+=1
                with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                    json.dump(list1, f,ensure_ascii=False)
                j=0
                for row in query_data2:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[j]
                        json_data['population'] = row1
                        list2 += [json_data]
                        j+=1
                with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                    json.dump(list2, f,ensure_ascii=False)
            elif form.model2.data == 'walk_transit':
                sql_cmd1 = f"""SELECT zipcode, walkscore , transitscore FROM inf_list WHERE zipcode='{form.model.data}';"""
                sql_cmd2 = f"""SELECT zipcode, walkscore , transitscore FROM inf_list WHERE zipcode='{form.model1.data}';"""
                db = SQLAlchemy()
                query_data1 = db.engine.execute(sql_cmd1)
                query_data2 = db.engine.execute(sql_cmd2)
                list1 = []
                list2 = []
                list3 = ['zipcode','walkscore','transitscore']
                i=0
                for row in query_data1:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[i]
                        json_data['population'] = row1
                        list1 += [json_data]
                        i+=1
                with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                    json.dump(list1, f,ensure_ascii=False)
                j=0
                for row in query_data2:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[j]
                        json_data['population'] = row1
                        list2 += [json_data]
                        j+=1
                with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                    json.dump(list2, f,ensure_ascii=False)
            elif form.model2.data == 'year_price':
                sql_cmd1 = f"""SELECT zipcode, before2018, 2019y, 2020y, 2021y FROM inf_list WHERE zipcode='{form.model.data}';"""
                sql_cmd2 = f"""SELECT zipcode, before2018, 2019y, 2020y, 2021y FROM inf_list WHERE zipcode='{form.model1.data}';"""
                db = SQLAlchemy()
                query_data1 = db.engine.execute(sql_cmd1)
                query_data2 = db.engine.execute(sql_cmd2)
                list1 = []
                list2 = []
                list3 = ['zipcode','before2018','2019','2020','2021']
                i=0
                for row in query_data1:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[i]
                        json_data['population'] = row1
                        list1 += [json_data]
                        i+=1
                with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                    json.dump(list1, f,ensure_ascii=False)
                j=0
                for row in query_data2:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[j]
                        json_data['population'] = row1
                        list2 += [json_data]
                        j+=1
                with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                    json.dump(list2, f,ensure_ascii=False)
            else:
                sql_cmd1 = f"""SELECT zipcode, AfricanRatio, LatinoRatio, AsianRatio, IndianRatio, OthersRatio FROM inf_list WHERE zipcode='{form.model.data}';"""
                sql_cmd2 = f"""SELECT zipcode, AfricanRatio, LatinoRatio, AsianRatio, IndianRatio, OthersRatio FROM inf_list WHERE zipcode='{form.model1.data}';"""
                db = SQLAlchemy()
                query_data1 = db.engine.execute(sql_cmd1)
                query_data2 = db.engine.execute(sql_cmd2)
                list1 = []
                list2 = []
                list3 = ['zipcode','AfricanRatio','LatinoRatio','AsianRatio','IndianRatio','OthersRatio']
                i=0
                for row in query_data1:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[i]
                        json_data['population'] = row1
                        list1 += [json_data]
                        i+=1
                with open('myapp/static/file1.json', 'w+', encoding='utf8') as f:
                    json.dump(list1, f,ensure_ascii=False)
                j=0
                for row in query_data2:
                    for row1 in row:
                        json_data = {'country':0,'population':0}
                        json_data['country'] = list3[j]
                        json_data['population'] = row1
                        list2 += [json_data]
                        j+=1
                with open('myapp/static/file2.json', 'w+', encoding='utf8') as f:
                    json.dump(list2, f,ensure_ascii=False)
    
    sql_cmd = """
    SELECT * FROM hotprice ORDER BY Actual_price_sqft DESC LIMIT 10;
    """
    db = SQLAlchemy()
    query_data = db.engine.execute(sql_cmd)
    list1 = []
    for row in query_data:
        json_data = {'country':0,'population':0}
        json_data['country'] = row[0]
        json_data['population'] = row[1]
        list1 += [json_data]
    with open('myapp/static/file.json', 'w+', encoding='utf8') as f:
        json.dump(list1, f,ensure_ascii=False)
    return render_template('information.html' ,title='Information' , results=query_data, form=form) 

@app.route('/aboutus')
def aboutus():
    members = {'id': 'BDSE19_3'}
    project = [
        {
        'code': '組長 秦忻榆',
        'name': 'Hadoop系統架構建置 網路爬蟲 資料蒐集'
        },
        {
        'code': '組員 林循恩',
        'name': 'Hadoop系統架構建置 網路爬蟲 資料探索性分析 機器學習建模 '
        },
        {
        'code': '組員 徐佳芸',
        'name': 'Hadoop系統架構建置 網路爬蟲  資料探索性分析 網頁建置'
        },
        {
        'code': '組員 游敏卉',
        'name': 'Hadoop系統架構建置 網路爬蟲 回歸建模  '
        },
        {
        'code': '組員 魏辰儒',
        'name': 'Hadoop系統架構建置 網路爬蟲 資料整合分析 機器學習建模'
        },
    ]
    return render_template('aboutus.html', title='Aboutus', members=members, project=project)