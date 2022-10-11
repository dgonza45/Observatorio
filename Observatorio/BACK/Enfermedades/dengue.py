from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'dengue'
url = 'http://medata.gov.co/node/24364/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
