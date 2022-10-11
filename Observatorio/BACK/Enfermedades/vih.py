from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'vih'
url = 'http://medata.gov.co/node/24370/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
