from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'intentoSuicidio'
url = 'http://medata.gov.co/node/24445/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
for i in range(3):
    creadorMapa.generarmapa(enfermedad, i)
