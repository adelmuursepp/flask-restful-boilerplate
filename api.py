from flask import Flask
from flask_restful import Api
from controllers import helloController
from controllers import predictController
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# model =  {'A': fields.Float(required = True,
#   description="A",
#   help="A cannot be blank"),
#  'C': fields.Float(required = True,
#   description="C",
#   help="C cannot be blank"),
#  'D': fields.Float(required = True,
#   description="D",
#   help="D cannot be blank"),
#  'G': fields.Float(required = True,
#   description="G",
#   help="G cannot be blank"),
#  'H': fields.Float(required = True,
#   description="H",
#   help="H cannot be blank"),
#  'I': fields.Float(required = True,
#   description="I",
#   help="I cannot be blank"),
#  'J': fields.Float(required = True,
#   description="J",
#   help="J cannot be blank"),
#  'K': fields.Float(required = True,
#   description="K",
#   help="K cannot be blank"),
#  'N': fields.Float(required = True,
#   description="N",
#   help="N cannot be blank"),
#  'O': fields.Float(required = True,
#   description="O",
#   help="O cannot be blank"),
#  'P': fields.Float(required = True,
#   description="P",
#   help="P cannot be blank"),
#  'S': fields.Float(required = True,
#   description="S",
#   help="S cannot be blank"),
#  'U': fields.Float(required = True,
#   description="U",
#   help="U cannot be blank"),
#  'V': fields.Float(required = True,
#   description="V",
#   help="V cannot be blank"),
#  'X': fields.Float(required = True,
#   description="X",
#   help="X cannot be blank"),
#  'Y': fields.Float(required = True,
#   description="Y",
#   help="Y cannot be blank"),
#  'Z': fields.Float(required = True,
#   description="Z",
#   help="Z cannot be blank"),
#   'Z': fields.Float(required = True,
#   description="Z",
#   help="Z cannot be blank")}



api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/db/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

api.add_resource(helloController.HelloController, '/api/hello')
api.add_resource(predictController.PredictController, '/api/predict')

if __name__ == '__main__':
    app.run(debug=True)
