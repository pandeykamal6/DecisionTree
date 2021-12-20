from flask import Flask,render_template,request
import pickle
application=Flask(__name__)
@application.route('/')
def homepage():
    return render_template('index.html')
@application.route('/submit',methods=['POST'])
def result():
    pas_class=request.form['cls']
    pas_age=request.form['age']
    fare=request.form['fare']
    family_size=request.form['fsize']
    children=request.form['cld']
    female=request.form['fml']
    male=request.form['ml']
    dt_model=pickle.load(open('Titanic_dt.pickle','rb'))
    result=dt_model.predict([[pas_class,pas_age,fare,family_size,children,female,male]])
    if result==1:
        return 'Chances of Survival of Passenger is High'
    else:
        return 'Chances of Survival of Passenger is Low'
if __name__=='__main__':
    application.run(debug=True)




