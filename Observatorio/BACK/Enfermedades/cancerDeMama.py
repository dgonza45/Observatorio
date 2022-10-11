from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'cancerDeMama'
url = 'http://medata.gov.co/node/24344/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
