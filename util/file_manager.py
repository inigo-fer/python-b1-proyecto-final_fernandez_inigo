import pandas as pd
class CSVFileManager:
  def __init__(self,path: str):
    self.path = path
  
  def read(self) -> str:
    ''' La función lee el CSV y devuelve un Data Frame '''
    return pd.read_csv(self.path)  
  
  def write(self,dataFrame):
    ''' La función convierte un Data Frame en un archivo CSV
    Esta es una función opcional, se deja al estudiante la implementación '''
    pass