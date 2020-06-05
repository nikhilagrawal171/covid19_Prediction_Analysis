from flask import Flask,render_template,request
import pandas as pd

app = Flask(__name__)
import pickle

file=open('model.pkl','rb')
lr=pickle.load(file)
file.close()

#file1=open('modelActive','rb')
#m=pickle.load(file1)
#file1.close()
@app.route('/',methods=["GET","POST"])
def hello_world():
	#if request.method=="POST":
		#print(request.form)
		##myDict=request.form
		#fever=int(myDict['fever'])
		#age=int(myDict['age'])
		#pain=int(myDict['pain'])
		#runnynose=int(myDict['runnynose'])
		#diffbreath=int(myDict['diffbreath'])
		#inputFeatures=[fever,pain,age,runnynose,diffbreath]
		#infProb=lr.predict_proba([inputFeatures])[0][1]
		#print(infProb)
		#return render_template('result.html',inf=round(infProb*100))
	return render_template('index.html')   

@app.route('/outbreak',methods=["GET","POST"])
def outbreak():
	if request.method=="POST":
                #print(request.form)

                myDict=request.form
                date1=(myDict['date1'])
                print(date1)
                print(type(date1))
                model_final=pd.read_csv('prediction (1).csv')
                date_time = date1
                x=model_final[model_final['Date']==date_time]
                print(x)
                print("Active")
                a=x.iloc[0][2]
                print(a)
                print("death")
                b=x.iloc[0][3]
                print(b)
                print("recovered")
                c=x.iloc[0][4]
                print(c)	
                return render_template('outbreak.html',inf=round(a),b=round(b),c=round(c))
	
	return render_template('outbreak.html',inf=0,b=0,c=0)

@app.route('/probability',methods=["GET","POST"])
def probability():

	if request.method=="POST":
                #print(request.form)
                myDict=request.form
                fever=int(myDict['fever'])
                age=int(myDict['age'])
                pain=int(myDict['pain'])
                runnynose=int(myDict['runnynose'])
                diffbreath=int(myDict['diffbreath'])
                inputFeatures=[fever,pain,age,runnynose,diffbreath]
                infProb=lr.predict_proba([inputFeatures])[0][1]
                print(infProb)
                return render_template('probability.html',inf="The probability of person infectious to corona virus is {}".format(round(infProb*100)))
	return render_template('probability.html')

@app.route('/doctors',methods=["GET","POST"])
def doctors():
	return render_template('doctors.html')
@app.route('/trends',methods=["GET","POST"])
def trends():
	return render_template('trends.html')		

if __name__=="__main__":
    app.run(debug="True")