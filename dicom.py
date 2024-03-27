import models

def verificar_ou_inserir_ano(d_ano):
  try:
    tmp_ano = models.ano.get(ano=d_ano)
  except models.ano.DoesNotExist:
    tmp_ano = models.ano.create(ano=d_ano)
  return tmp_ano   

def verificar_ou_inserir_mes(d_mes):
  try:
    tmp_mes = models.mes.get(mes=d_mes)
  except models.mes.DoesNotExist:
    tmp_mes = models.mes.create(mes=d_mes)
  return tmp_mes

def verificar_ou_inserir_dia(d_dia):
  try:
    tmp_dia = models.dia.get(dia=d_dia)
  except models.dia.DoesNotExist:
    tmp_dia = models.dia.create(dia=d_dia)
  return tmp_dia

def verificar_ou_inserir_hora(d_hora):
  try:
    tmp_hora = models.hora.get(hora=d_hora)
  except models.hora.DoesNotExist:
    tmp_hora = models.hora.create(hora=d_hora)
  return tmp_hora

def verificar_ou_inserir_modalidade(d_modalidade):
  try:
    tmp_modalidade = models.modalidade.get(modalidade=d_modalidade)
  except models.modalidade.DoesNotExist:
    tmp_modalidade = models.modalidade.create(modalidade=d_modalidade)
  return tmp_modalidade

def verificar_ou_inserir_estudo(d_estudo, fk_ano, fk_mes, fk_dia, fk_hora, fk_modalidade):
  try:
    tmp_estudo = models.estudo.get(estudo=d_estudo, fk_id_ano=fk_ano, fk_id_mes=fk_mes, fk_id_dia=fk_dia, fk_id_hora=fk_hora, fk_id_modalidade=fk_modalidade)
  except models.estudo.DoesNotExist:
    tmp_estudo = models.estudo.create(estudo=d_estudo, fk_id_ano=fk_ano, fk_id_mes=fk_mes, fk_id_dia=fk_dia, fk_id_hora=fk_hora, fk_id_modalidade=fk_modalidade)
  return tmp_estudo

def verificar_ou_inserir_file(d_file, size, d_estudo):
  try:
    tmp_file = models.file.get(fk_id_estudo=d_estudo, files=d_file)
  except models.file.DoesNotExist:
    tmp_file = models.file.create(fk_id_estudo=d_estudo, files=d_file, files_size=size)
  return tmp_file

