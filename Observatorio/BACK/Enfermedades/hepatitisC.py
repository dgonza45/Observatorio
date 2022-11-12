from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'hepatitisc'
url = 'http://medata.gov.co/node/24349/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
for i in range(3):
    creadorMapa.generarmapa(enfermedad, i)
