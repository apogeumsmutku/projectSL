from flask import make_response, render_template, request
from flask_restful import Resource

from models import Praca, Zgloszenie

#api
class Index(Resource):
    def get(self):
        zgloszenia = Zgloszenie.select()
        for i in zgloszenia:
            print(i.__dict__)
        return make_response(render_template('index.html'))


class PraceList(Resource):
    def get(self):
        prace = Praca.select()
        return make_response(render_template('prace.html', prace=prace))
    
    def post(self):
        Praca.create(
            nazwa=request.form.get('nazwa'),
            opis=request.form.get('opis'),
            deadline=request.form.get('deadline')
        )
        

class PracaAdd(Resource):
    def get(self):
        return make_response(render_template('praca_form.html'))
    
class PracaEdit(Resource):
    def get(self, praca_id):
        praca = Praca.get(id=praca_id)
        return make_response(render_template('praca_form.html', praca=praca))

        
class PraceDetail(Resource):
    def get(self, praca_id):
        praca = Praca.get(id=praca_id)
        return make_response(render_template('praca_form.html', praca=praca))
    
    def delete(self, praca_id):
        praca = Praca.get(id=praca_id)
        praca.delete_instance()
        prace = Praca.select()
        return make_response(render_template('prace.html', prace=prace))
        
    def put(self, praca_id):
        praca = Praca.get(id=praca_id)
        praca.nazwa = request.form.get('nazwa')
        praca.opis = request.form.get('opis')
        praca.deadline = request.form.get('deadline')
        praca.save()
        return make_response(render_template('praca_form.html'))


class ZgloszeniaList(Resource):
    def get(self):
        zgloszenia = Zgloszenie.select()
        return make_response(render_template('zgloszenia.html', zgloszenia=zgloszenia))
    
    def post(self):
        Zgloszenie.create(
            praca=request.form.get('praca'),
            email=request.form.get('email'),
            wiadomosc=request.form.get('wiadomosc'),
            nr_telefonu=request.form.get('nr_telefonu')
        )
        
        praca = Praca.get(id = request.form.get('praca'))
        praca.taken = True
        praca.save()
        

class ZgloszeniaAdd(Resource):
    def get(self):
        prace = Praca.select()
        return make_response(render_template('zgloszenie_form.html', prace=prace))
    
class ZgloszeniaEdit(Resource):
    def get(self, zgloszenie_id):
        prace = Praca.select()
        zgloszenie = Zgloszenie.get(id=zgloszenie_id)
        return make_response(render_template('zgloszenie_form.html', zgloszenie=zgloszenie, prace=prace))

        
class ZgloszeniaDetail(Resource):
    def get(self, zgloszenie_id):
        zgloszenie = Zgloszenie.get(id=zgloszenie_id)
        return make_response(render_template('zgloszenie_form.html', zgloszenie=zgloszenie))
    
    def delete(self, zgloszenie_id):
        zgloszenie = Zgloszenie.get(id=zgloszenie_id)
        praca_free = zgloszenie.praca
        praca_free.taken = False
        praca_free.save()
        zgloszenie.delete_instance()
        zgloszenia = Zgloszenie.select()
        return make_response(render_template('zgloszenia.html', zgloszenia=zgloszenia))
        
    def put(self, zgloszenie_id):
        
        zgloszenie = Zgloszenie.get(id=zgloszenie_id)
        praca_free = zgloszenie.praca
        praca_free.taken = False
        praca_free.save()
        
        zgloszenie.praca = request.form.get('praca')
        zgloszenie.email = request.form.get('email')
        zgloszenie.wiadomosc = request.form.get('wiadomosc')
        zgloszenie.nr_telefonu = request.form.get('nr_telefonu')
        zgloszenie.save()
        
        praca = Praca.get(id = request.form.get('praca'))
        praca.taken = True
        praca.save()
        
        return make_response(render_template('zgloszenie_form.html'))
