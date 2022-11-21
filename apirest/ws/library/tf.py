import pandas as pd
from tensorflow import keras
import os
from decimal import Decimal
import json

class ClasificacionMultiple:

	def __init__(self):
		module_dir = os.path.dirname(__file__)  
		
		#Carga de estadísticos
		mean = pd.read_csv(os.path.join(module_dir, './files/mean.csv'), index_col=False, header=None)
		std = pd.read_csv(os.path.join(module_dir, './files/std.csv'), index_col=False, header=None)
		self.mean = mean.set_index(0).T.reset_index(drop=True)
		self.std = std.set_index(0).T.reset_index(drop=True)
		
		#Carga del modelo de TF
		self.new_model = keras.models.load_model(os.path.join(module_dir, './files/modelo_final.h5'))
	
	#Función de normalización
	def normalizacion(self, data):
		star_classification = pd.DataFrame([{
			"alpha": float(data["alpha"]), 
			"delta": float(data["delta"]), 
			"u": float(data["u"]), 
			"g": float(data["g"]), 
			"r": float(data["r"]), 
			"i": float(data["i"]), 
			"z": float(data["z"]),
			"redshift": float(data["redshift"])
		}])
		return (star_classification - self.mean) / self.std
	
	def predict(self, data):
		try:
			data = json.loads(data)
			data_norm = self.normalizacion(data)
			prediccion = self.new_model.predict(data_norm)

			pd_prediccion = pd.DataFrame(prediccion, columns=["galaxy", "qso", "star"])
			pd_prediccion["resultado"]="ok"
			resultado = pd_prediccion.to_json(orient="records")
			return json.loads(resultado)[0]
		except Exception as e:
			resultado = pd.DataFrame([{
				"resultado": "not ok", 
				"error": str(e)
			}]).to_json(orient="records")
			return json.loads(resultado)[0]