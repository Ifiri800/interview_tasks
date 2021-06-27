from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgrsql:///ifiri:postgre@localhost:5435/postgres"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class SmartMeter(db.Model):
    _tablename_ = 'meter'
   
    id = db.Column(db.Integer, primary_key=True)
    energy_kwh = db.Column(db.String, unique=True, nullable=False)
    timestamp = db.Column(db.String, unique=True, nullable=False)
    smart_meter_id = db.Column(db.String, unique=True, nullable=False)
    
    
    
    def _init_(self, energy_kwh, timestamp, smart_meter_id):
        self.energy_kwh = energy_kwh ("randomn value between zero and one")
        self.timestamp = timestamp ("time that the energy was measured")
        self.smart_meter_id ("id of the smart meter")
        
    def _repr_(self):
        return f"<meter {self.smart_meter_id}>"
    
    @app.route('/meter', methods=['POST', 'GET'])
    def handle_meter():
        if request.method == 'POST':
            if request.is_json:
                data = request.get_json()
                new_meter = SmartMeter(energy_kwh=data['energy_kwh'], timestamp=data['timestanp'], smart_meter_id=data['smart_meter_id'])
                db.session.add(new_meter)
                db.session.commit()
                return{"message": f"meter {new_meter} has been created successfully."}
        
            else:
                return {"error": "The request payload is not in JSON format"}
        elif request.method == 'GET':
            meters = SmartMeter.query.filter_by(id).first('snart_mter_id')
            results = [
                {
                   "energy_kwh" : meters.energy_kwk,
                    "timestamp": meters.timestanp,
                    "smart_meter_id": meters.smart_meter_id} for meter in meters]
            return { "count": len(results), "meter": results}
        db.session.commit()
        
        
        # Message broker support
        
        from confluent_kafka import Consumer
        c = Consumer
        
        c = Consumer ({
            'bootstap.servers': 'mybroker',
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest'
            })
        
        c.subscribe(['mytopic'])
        
        while True:
            msg = c.poll(1.0)
            
            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}". format(msg.error()))
                continue
            
               
        print('Received message:  {}'. format(msg.value().decode('utf-8')))
  
    
       
        # Dockerfiles to Intall all dependencies
    
app = Flask(__name__)
    
@app.route('/')
def Hello_World():
       return{"Hello Docker"}
   
    
if __name__ == '__main__':
       app.run(debug=True)
      
       
      


        
        
        
        
                


