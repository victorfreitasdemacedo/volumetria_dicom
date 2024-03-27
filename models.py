from peewee import *

database = MySQLDatabase('dicom', host = '10.1.4.71', port = 3306, user = 'root', password = 'qwe456')

class ano(database.Model):
  id = PrimaryKeyField()
  ano = CharField()

class mes(database.Model):
  id = PrimaryKeyField()
  mes = CharField()

class dia(database.Model):
  id = PrimaryKeyField()
  dia = CharField()

class hora(database.Model):
  id = PrimaryKeyField()
  hora = CharField()

class modalidade(database.Model):
  id = PrimaryKeyField()
  modalidade = CharField()

class estudo(database.Model):
  id = BigAutoField(primary_key=True)
  fk_id_ano = ForeignKeyField(ano, backref='id_ano')
  fk_id_mes = ForeignKeyField(mes, backref='id_mes')
  fk_id_dia = ForeignKeyField(dia, backref='id_dia')
  fk_id_hora = ForeignKeyField(hora, backref='id_hora')
  fk_id_modalidade = ForeignKeyField(modalidade, backref='id_modalidade')
  estudo = CharField()

class file(database.Model):
  id = BigAutoField(primary_key=True)
  fk_id_estudo = ForeignKeyField(estudo, backref='id_estudo')
  files = CharField()
  files_size = BigIntegerField()


database.connect()

def createDatabase():
  database.create_tables([ano, mes, dia, hora, modalidade, estudo, file])

def closeConexao():
  database.close()


