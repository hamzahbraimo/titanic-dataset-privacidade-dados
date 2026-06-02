from scripts.data_cleaning import DataCleaning
import secrets

class PseudoMask:

    def __init__(self):
        self.dc = DataCleaning(None)
        self.data = self.dc.get_clean_data()

    def pseudo_id(self):
        token_map: dict[int, str] = {}

        for element in self.data['PassengerId']:
            if element not in token_map:
                token_map[element] = secrets.token_hex(4)
                self.data['PassengerId'] = self.data['PassengerId'].replace(element, token_map[element])
                
    def mask_ticket(self):
        for element in self.data['Ticket']:
            self.data['Ticket'] = self.data['Ticket'].str[:3] + '****'  

    def mask_cabin(self):
        for element in self.data['Cabin']:
            if element != 'Desconhecido':
                self.data['Cabin'] = self.data['Cabin'].str[0]

    def save_masked_data(self):
        self.data.to_csv('data/titanic_masked.csv', index=False)    


    def mask_data(self):
        self.pseudo_id()
        self.mask_ticket()
        self.mask_cabin()   
        self.save_masked_data() 