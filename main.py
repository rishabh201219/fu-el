import pickle
from flask import Flask, request, jsonify,render_template

from model_files.ml_model import predict_mpg
app = Flask(__name__)




model = pickle.load(open('model.pkl', 'rb')) 

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    if request.method =='POST': 
      Cylinders = request.form['Cylinders']
      Cylinders= int(Cylinders)

      Cylinder = request.form['Cylinder']
      Cylinder = int(Cylinder)

      Cylinde = request.form['Cylinde']
      Cylinde = int(Cylinde)

      Displacement =request.form['Displacement']
      Displacement = int(Displacement)

      Displacemen = request.form['Displacemen']
      Displacemen = int(Displacemen)

      Displaceme = request.form['Displaceme']
      Displaceme = int(Displaceme)

      Horsepower =request.form['Horsepower']
      Horsepower = int(Horsepower)

      Horsepowe =request.form['Horsepowe']
      Horsepowe = int(Horsepowe)

      Horsepow = request.form['Horsepow']
      Horsepow = int(Horsepow)

      Weight = request.form['Weight']
      Weight = int(Weight)

      Weigh = request.form['Weigh']
      Weigh = int(Weigh)

      Weig = request.form['Weig']
      Weig = int(Weig)

      Acceleration =request.form['Acceleration']
      Acceleration = int(Acceleration)

      Acceleratio = request.form['Acceleratio']
      Acceleratio = int(Acceleratio)

      Accelerati =request.form['Accelerati']
      Accelerati = int(Accelerati)

      Model_Year = request.form['Model Year']
      Model_Year = int(Model_Year)

      Model_Yea = request.form['Model Yea']
      Model_Yea = int(Model_Yea)

      Model_Ye = request.form['Model Ye']
      Model_Ye = int(Model_Ye)
      
      Origin =request.form['Origin']
      Origin = int(Origin)
      
      Origi = request.form['Origi']
      Origi = int(Origi)
      
      Orig = request.form['Orig']
      Orig = int(Orig)
      vehicle_config = [[Cylinders, Cylinder, Cylinde], [Displacement, Displacemen, Displaceme], [
          Horsepower, Horsepowe, Horsepow], [Weight, Weigh, Weig], [Acceleration, Acceleratio, Accelerati], [Model_Year, Model_Yea, Model_Ye], [Origin, Origi, Orig]]
    
      predictions = predict_mpg(vehicle_config, model)
      return render_template('home.html',prediction_text="miles per gallon of car1,car2,car3={}".format(predictions)) 
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)
