from flask import Flask
from flask_restful import Api
from resources import  Index, PracaAdd, PracaEdit, PraceDetail, PraceList, ZgloszeniaAdd, ZgloszeniaDetail, ZgloszeniaEdit, ZgloszeniaList

app = Flask(__name__)
app.config.from_object('config.Config')

api = Api(app)

api.add_resource(Index, '/', '/home')

api.add_resource(PraceList,'/prace')
api.add_resource(PracaAdd,'/prace/new-praca')
api.add_resource(PracaEdit,'/prace/<uuid:praca_id>/edit')
api.add_resource(PraceDetail,'/prace/<uuid:praca_id>')

api.add_resource(ZgloszeniaList,'/zgloszenia')
api.add_resource(ZgloszeniaAdd,'/zgloszenia/new-zgloszenie')
api.add_resource(ZgloszeniaEdit,'/zgloszenia/<uuid:zgloszenie_id>/edit')
api.add_resource(ZgloszeniaDetail,'/zgloszenia/<uuid:zgloszenie_id>')

if __name__ == '__main__':
    app.run()