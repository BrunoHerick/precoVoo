# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as grafico

dados = pd.read_csv("/home/brunohelghast/PROFISSIONAL/PYTHON/SCIKIT_LEARN/precoVoo/Clean_Dataset.csv")

tempoDepArr = dados.iloc[:,[4,6,11]]

manhaManha = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaManha = manhaManha[manhaManha["arrival_time"] == "Morning"]

manhaCedo = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaCedo = manhaCedo[manhaCedo["arrival_time"] == "Early_Morning"]

manhaTarde = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaTarde = manhaTarde[manhaTarde["arrival_time"] == "Afternoon"]

manhaEvening = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaEvening = manhaEvening[manhaEvening["arrival_time"] == "Evening"]

manhaNight = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaNight = manhaNight[manhaNight["arrival_time"] == "Night"]

manhaLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Morning"]
manhaLateNight = manhaLateNight[manhaLateNight["arrival_time"] == "Late_Night"]

cedoManha = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoManha = cedoManha[cedoManha["arrival_time"] == "Morning"]

cedoCedo = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoCedo = cedoCedo[cedoCedo["arrival_time"] == "Early_Morning"]

cedoTarde = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoTarde = cedoTarde[cedoTarde["arrival_time"] == "Afternoon"]

cedoEvening = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoEvening = cedoEvening[cedoEvening["arrival_time"] == "Evening"]

cedoNight = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoNight = cedoNight[cedoNight["arrival_time"] == "Night"]

cedoLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Early_Morning"]
cedoLateNight = cedoLateNight[cedoLateNight["arrival_time"] == "Late_Night"]

tardeManha = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeManha = tardeManha[tardeManha["arrival_time"] == "Morning"]

tardeCedo = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeCedo = tardeCedo[tardeCedo["arrival_time"] == "Early_Morning"]

tardeTarde = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeTarde = tardeTarde[tardeTarde["arrival_time"] == "Afternoon"]

tardeEvening = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeEvening = tardeEvening[tardeEvening["arrival_time"] == "Evening"]

tardeNight = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeNight = tardeNight[tardeNight["arrival_time"] == "Night"]

tardeLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Afternoon"]
tardeLateNight = tardeLateNight[tardeLateNight["arrival_time"] == "Late_Night"]

eveningManha = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningManha = eveningManha[eveningManha["arrival_time"] == "Morning"]

eveningCedo = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningCedo = eveningCedo[eveningCedo["arrival_time"] == "Early_Morning"]

eveningTarde = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningTarde = eveningTarde[eveningTarde["arrival_time"] == "Afternoon"]

eveningEvening = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningEvening = eveningEvening[eveningEvening["arrival_time"] == "Evening"]

eveningNight = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningNight = eveningNight[eveningNight["arrival_time"] == "Night"]

eveningLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Evening"]
eveningLateNight = eveningLateNight[eveningLateNight["arrival_time"] == "Late_Night"]

nightManha = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightManha = nightManha[nightManha["arrival_time"] == "Morning"]

nightCedo = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightCedo = nightCedo[nightCedo["arrival_time"] == "Early_Morning"]

nightTarde = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightTarde = nightTarde[nightTarde["arrival_time"] == "Afternoon"]

nightEvening = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightEvening = nightEvening[nightEvening["arrival_time"] == "Evening"]

nightNight = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightNight = nightNight[nightNight["arrival_time"] == "Night"]

nightLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Night"]
nightLateNight = nightLateNight[nightLateNight["arrival_time"] == "Late_Night"]

lateManha = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateManha = lateManha[lateManha["arrival_time"] == "Morning"]

lateCedo = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateCedo = lateCedo[lateCedo["arrival_time"] == "Early_Morning"]

lateTarde = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateTarde = lateTarde[lateTarde["arrival_time"] == "Afternoon"]

lateEvening = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateEvening = lateEvening[lateEvening["arrival_time"] == "Evening"]

lateNight = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateNight = lateNight[lateNight["arrival_time"] == "Night"]

lateLateNight = tempoDepArr[tempoDepArr["departure_time"] == "Late_Night"]
lateLateNight = lateLateNight[lateLateNight["arrival_time"] == "Late_Night"]

""" manhaManha = manhaManha.sample(73)
manhaCedo = manhaCedo.sample(73)
manhaTarde = manhaTarde.sample(73)
manhaEvening = manhaEvening.sample(73)
manhaNight = manhaNight.sample(73)
manhaLateNight = manhaLateNight.sample(73)
cedoManha = cedoManha.sample(73)
cedoCedo = cedoCedo.sample(73)
cedoTarde = cedoTarde.sample(73)
cedoEvening = cedoEvening.sample(73)
cedoNight = cedoNight.sample(73)
cedoLateNight = cedoLateNight.sample(73)
tardeManha = tardeManha.sample(73)
tardeCedo = tardeCedo.sample(73)
tardeTarde = tardeTarde.sample(73)
tardeEvening = tardeEvening.sample(73)
tardeNight = tardeNight.sample(73)
tardeLateNight = tardeLateNight.sample(73)
eveningManha = eveningManha.sample(73)
eveningCedo = eveningCedo.sample(73)
eveningTarde = eveningTarde.sample(73)
eveningEvening = eveningEvening.sample(73)
eveningNight = eveningNight.sample(73)
eveningLateNight = eveningLateNight.sample(73)
nightManha = nightManha.sample(73)
nightCedo = nightCedo.sample(73)
nightTarde = nightTarde.sample(73)
nightNight = nightNight.sample(73)
nightLateNight = nightLateNight.sample(73)
nightEvening = nightEvening.sample(73)
lateManha = lateManha.sample(73)
lateCedo = lateCedo.sample(73)
lateTarde = lateTarde.sample(73)
lateEvening = lateEvening.sample(73)
lateNight = lateNight.sample(73)
lateLateNight = lateLateNight.sample(73) """

manhaManhaMed = np.mean(manhaManha["price"])
manhaManhaVar = np.var(manhaManha["price"])

manhaCedoMed = np.mean(manhaCedo["price"])
manhaCedoVar = np.var(manhaCedo["price"])

manhaTardeMed = np.mean(manhaTarde["price"])
manhaTardeVar = np.var(manhaTarde["price"])

manhaEveningMed = np.mean(manhaEvening["price"])
manhaEveningVar = np.var(manhaEvening["price"])

manhaNightMed = np.mean(manhaNight["price"])
manhaNightVar = np.var(manhaNight["price"])

manhaLateNightMed = np.mean(manhaLateNight["price"])
manhaLateNightVar = np.var(manhaLateNight["price"])

cedoManhaMed = np.mean(cedoManha["price"])
cedoManhaVar = np.var(cedoManha["price"])

cedoCedoMed = np.mean(cedoCedo["price"])
cedoCedoVar = np.var(cedoCedo["price"])

cedoTardeMed = np.mean(cedoTarde["price"])
cedoTardeVar = np.var(cedoTarde["price"])

cedoEveningMed = np.mean(cedoEvening["price"])
cedoEveningVar = np.var(cedoEvening["price"])

cedoNightMed = np.mean(cedoNight["price"])
cedoNightVar = np.var(cedoNight["price"])

cedoLateNightMed = np.mean(cedoLateNight["price"])
cedoLateNightVar = np.var(cedoLateNight["price"])

tardeManhaMed = np.mean(tardeManha["price"])
tardeManhaVar = np.var(tardeManha["price"])

tardeCedoMed = np.mean(tardeCedo["price"])
tardeCedoVar = np.var(tardeCedo["price"])

tardeTardeMed = np.mean(tardeTarde["price"])
tardeTardeVar = np.var(tardeTarde["price"])

tardeEveningMed = np.mean(tardeEvening["price"])
tardeEveningVar = np.var(tardeEvening["price"])

tardeNightMed = np.mean(tardeNight["price"])
tardeNightVar = np.var(tardeNight["price"])

tardeLateNightMed = np.mean(tardeLateNight["price"])
tardeLateNightVar = np.var(tardeLateNight["price"])

eveningManhaMed = np.mean(eveningManha["price"])
eveningManhaVar = np.var(eveningManha["price"])

eveningCedoMed = np.mean(eveningCedo["price"])
eveningCedoVar = np.var(eveningCedo["price"])

eveningTardeMed = np.mean(eveningTarde["price"])
eveningTardeVar = np.var(eveningTarde["price"])

eveningEveningMed = np.mean(eveningEvening["price"])
eveningEveningVar = np.var(eveningEvening["price"])

eveningNightMed = np.mean(eveningNight["price"])
eveningNightVar = np.var(eveningNight["price"])

eveningLateNightMed = np.mean(eveningLateNight["price"])
eveningLateNightVar = np.var(eveningLateNight["price"])

nightManhaMed = np.mean(nightManha["price"])
nightManhaVar = np.var(nightManha["price"])

nightCedoMed = np.mean(nightCedo["price"])
nightCedoVar = np.var(nightCedo["price"])

nightTardeMed = np.mean(nightTarde["price"])
nightTardeVar = np.var(nightTarde["price"])

nightEveningMed = np.mean(nightEvening["price"])
nightEveningVar = np.var(nightEvening["price"])

nightNightMed = np.mean(nightNight["price"])
nightNightVar = np.var(nightNight["price"])

nightLateNightMed = np.mean(nightLateNight["price"])
nightLateNightVar = np.var(nightLateNight["price"])

lateManhaMed = np.mean(lateManha["price"])
lateManhaVar = np.var(lateManha["price"])

lateCedoMed = np.mean(lateCedo["price"])
lateCedoVar = np.var(lateCedo["price"])

lateTardeMed = np.mean(lateTarde["price"])
lateTardeVar = np.var(lateTarde["price"])

lateTardeMed = np.mean(lateTarde["price"])
lateTardeVar = np.var(lateTarde["price"])

lateEveningMed = np.mean(lateEvening["price"])
lateEveningVar = np.var(lateEvening["price"])

lateNightMed = np.mean(lateNight["price"])
lateNightVar = np.var(lateNight["price"])

lateLateNightMed = np.mean(lateLateNight["price"])
lateLateNightVar = np.var(lateLateNight["price"])

medias = [manhaManhaMed,manhaCedoMed,manhaTardeMed,manhaEveningMed,manhaNightMed,manhaLateNightMed,cedoManhaMed,cedoCedoMed,cedoTardeMed,cedoEveningMed,cedoNightMed,cedoLateNightMed,tardeManhaMed,tardeCedoMed,tardeTardeMed,tardeEveningMed,tardeNightMed,tardeLateNightMed,eveningManhaMed,eveningCedoMed,eveningTardeMed,eveningEveningMed,eveningNightMed,eveningLateNightMed,nightManhaMed,nightCedoMed,nightTardeMed,nightNightMed,nightLateNightMed,nightEveningMed,lateManhaMed,lateCedoMed,lateTardeMed,lateEveningMed,lateNightMed,lateLateNightMed]

variancias = [manhaManhaVar,manhaCedoVar,manhaTardeVar,manhaEveningVar,manhaNightVar,manhaLateNightVar,cedoManhaVar,cedoCedoVar,cedoTardeVar,cedoEveningVar,cedoNightVar,cedoLateNightVar,tardeManhaVar,tardeCedoVar,tardeTardeVar,tardeEveningVar,tardeNightVar,tardeLateNightVar,eveningManhaVar,eveningCedoVar,eveningTardeVar,eveningEveningVar,eveningNightVar,eveningLateNightVar,nightManhaVar,nightCedoVar,nightTardeVar,nightNightVar,nightLateNightVar,nightEveningVar,lateManhaVar,lateCedoVar,lateTardeVar,lateEveningVar,lateNightVar,lateLateNightVar]

filtro = [manhaManha,manhaCedo,manhaTarde,manhaEvening,manhaNight,manhaLateNight,cedoManha,cedoCedo,cedoTarde,cedoEvening,cedoNight,cedoLateNight,tardeManha,tardeCedo,tardeTarde,tardeEvening,tardeNight,tardeLateNight,eveningManha,eveningCedo,eveningTarde,eveningEvening,eveningNight,eveningLateNight,nightManha,nightCedo,nightTarde,nightNight,nightLateNight,nightEvening,lateManha,lateCedo,lateTarde,lateEvening,lateNight,lateLateNight]

grafico.boxplot([manhaManha["price"],manhaCedo["price"],manhaTarde["price"],manhaEvening["price"],manhaNight["price"],manhaLateNight["price"],cedoManha["price"],cedoCedo["price"],cedoTarde["price"],cedoEvening["price"],cedoNight["price"],cedoLateNight["price"],tardeManha["price"],tardeCedo["price"],tardeTarde["price"],tardeEvening["price"],tardeNight["price"],tardeLateNight["price"],eveningManha["price"],eveningCedo["price"],eveningTarde["price"],eveningEvening["price"],eveningNight["price"],eveningLateNight["price"],nightManha["price"],nightCedo["price"],nightTarde["price"],nightNight["price"],nightLateNight["price"],nightEvening["price"],lateManha["price"],lateCedo["price"],lateTarde["price"],lateEvening["price"],lateNight["price"],lateLateNight["price"]])
grafico.grid()
grafico.show()

mediaDasVariancias = np.mean(variancias)
varianciaDasMedias = np.var(medias)
varianciaEntreMedias = ((varianciaDasMedias*8337)/mediaDasVariancias)

print(varianciaEntreMedias/mediaDasVariancias)