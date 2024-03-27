import pydicom
import dicom
import models
import os

models.createDatabase()

files = 'E:\\AURORA-002839\\OFFLOAD\\FILES'
for pasta_atual, sub_pastas, arquivos in os.walk(files):
  for arquivo in arquivos:
    try:
      dcm = pydicom.dcmread(os.path.join(pasta_atual, arquivo))
      ano = dicom.verificar_ou_inserir_ano(dcm.StudyDate[0:4])
      mes = dicom.verificar_ou_inserir_mes(dcm.StudyDate[4:6])
      dia = dicom.verificar_ou_inserir_dia(dcm.StudyDate[6:8])
      hora = dicom.verificar_ou_inserir_hora(dcm.StudyTime[:2])
      modalidade = dicom.verificar_ou_inserir_modalidade(dcm.Modality)
      estudo = dicom.verificar_ou_inserir_estudo(d_estudo=dcm.StudyInstanceUID, fk_ano=ano, fk_mes=mes, fk_dia=dia, fk_hora=hora, fk_modalidade=modalidade)
      dicom.verificar_ou_inserir_file(d_estudo=estudo, d_file=os.path.join(pasta_atual, arquivo), size=os.path.getsize(os.path.join(pasta_atual, arquivo)))
    except (pydicom.errors.InvalidDicomError, AttributeError):
      continue
      
models.closeConexao()