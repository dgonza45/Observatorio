from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'intentoSuicidio'
url = 'http://medata.gov.co/node/24445/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
