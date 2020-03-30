from flask import Flask, render_template, request
app=Flask(__name__)
import pickle



with open("model.pkl", 'rb') as pickle_file:
    clf = pickle.load(pickle_file)



# file=open('model.pkl','rb') #
# clf=pickle.load(file)
# file.close()

@app.route('/',methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        myDict= request.form
        fever = int(myDict['fever'])
        age = int(myDict['age'])
        bodyPain = int(myDict['bodyPain'])
        runnyNose = int(myDict['runnyNose'])
        diffBreath = int(myDict['diffBreath'])
        #code for inference
        inputFeature = [fever,bodyPain,age,runnyNose,diffBreath]
        infProb=clf.predict_proba([inputFeature])[0][1]
        print(infProb)
        return render_template('show.html',inf=round(infProb*100))
    return render_template('index.html')
    # return 'hello, world!' + str(infProb)

if __name__ == "__main__":
    app.run(debug=True)