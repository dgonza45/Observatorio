from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'parotiditis'
url = 'http://medata.gov.co/node/24362/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
