
import pandas as pd
import hashlib

class DataAnonymization:
    def __init__(self, data):
        self.data = data.copy()
    
    def remove_sensitive_columns(self):
        # Remover coluna Embarked
        if 'Embarked' in self.data.columns:
            self.data = self.data.drop('Embarked', axis=1)
            print(" Coluna 'Embarked' removida")
        else:
            print(" Coluna 'Embarked' não encontrada")
            
        # Remover coluna Sex
        if 'Sex' in self.data.columns:
            self.data = self.data.drop('Sex', axis=1)
            print(" Coluna 'Sex' removida")
        else:
            print(" Coluna 'Sex' não encontrada")
        
        return self
    
    def apply_hash_to_names(self):
        """Aplica hash SHA256 na coluna Name"""
        def hash_name(name):
            if pd.isna(name):
                return None
            # Converter para string e aplicar hash
            name_str = str(name)
            hash_obj = hashlib.sha256(name_str.encode('utf-8'))
            return hash_obj.hexdigest()
        
        if 'Name' in self.data.columns:
            # Aplicar hash nos nomes
            self.data['Name_Hash'] = self.data['Name'].apply(hash_name)
            # Remover coluna original
            self.data = self.data.drop('Name', axis=1)
            print(" Hash SHA256 aplicado na coluna 'Name'")
            print(f"  - Nova coluna: 'Name_Hash'")
        else:
            print(" Coluna 'Name' não encontrada")
        
        return self
    
    def get_anonymized_data(self):
        """
        Retorna o DataFrame anonimizado
        """
        return self.data
    
    def save_anonymized_data(self, filepath='data/titanic_anonimizado.csv'):
        self.data.to_csv(filepath, index=False)
        print(f" Dados anonimizados salvos em: {filepath}")

    def anonimizar(self):
    
        # Carregar dados limpos
        print("\n Carregando dados limpos...")
        df = pd.read_csv('data/titanic_clean.csv')
        print(f"   Shape original: {df.shape}")
        
        # Criar instância da classe de anonimização
        # anonymizer = DataAnonymization(df)
        
        # Aplicar técnicas de anonimização
        print("\n Aplicando técnicas de anonimização...")
        self.remove_sensitive_columns()
        self.apply_hash_to_names()
        
        # Obter dados anonimizados
        df_anonimizado = self.get_anonymized_data()
        
        print(f"\n Dataset após anonimização:")
        print(f"   Shape final: {df_anonimizado.shape}")
        print(f"   Colunas finais: {list(df_anonimizado.columns)}")
        
        # Salvar resultados
        print("\n Salvando resultados...")
        self.save_anonymized_data('data/titanic_anonimizado.csv')
        
        return df_anonimizado

# Executar se o script for rodado diretamente
# if __name__ == "__main__":
#     df_anonimizado = anonimizar()