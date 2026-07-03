import json
from invalid_learn_excp import InvalidLearnException
from invalid_batch import  InvalidBatchCntException
from invalid_episode import InvalidEpisodesException
from name_not_found import NameNotFoundException



class Config:
   def __init__(self,filepath):
      with open(filepath,'r') as cfg_file:
            self.cfg_dict = json.load(cfg_file)
            print(f'file {filepath} loaded successfully')  
      if 'learn_rate' not in self.cfg_dict:
         raise InvalidLearnException("learning rate not found in the config file")  
      if self.cfg_dict['learn_rate']<0 or self.cfg_dict['learn_rate']>1:
         raise InvalidLearnException("learning rate is out of bounds")
      if 'batch_size' not in self.cfg_dict:
         raise InvalidBatchCntException("batch size not found in the config file")
      if self.cfg_dict['batch_size']<=0 :
         raise InvalidBatchCntException("batch size can't be negative or null")
      if 'episodes' not in self.cfg_dict:
         raise InvalidEpisodesException("number of episodes not found in the config file")
      if self.cfg_dict['episodes']<=0:
         raise InvalidEpisodesException("number of episodes can't be negative or null")
      if 'model_name' not in self.cfg_dict:
         raise NameNotFoundException("model name not found in the config file")
      return
   def free(self):
      self.cfg_dict = {}
      return
   
   
      
   






               
   
         
         
         
     
           

            
        
         





     
    