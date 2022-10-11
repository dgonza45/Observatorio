from BACK.Modulos import creadorMapa, descargaBD, predicciones, subirDatos

enfermedad = 'hepatitisa'
url = 'http://medata.gov.co/node/24347/download'

descargaBD.descarga(url, enfermedad)
subirDatos.subirdatos(enfermedad)
predicciones.predecir(enfermedad)
creadorMapa.generarmapa(enfermedad)
