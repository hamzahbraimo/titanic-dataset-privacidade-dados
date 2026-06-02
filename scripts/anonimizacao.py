
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
        """
        Salva os dados anonimizados em CSV
        
        Parameters:
        filepath (str): Caminho para salvar o arquivo
        """
        self.data.to_csv(filepath, index=False)
        print(f" Dados anonimizados salvos em: {filepath}")
        
        # Salvar metadados
        self._save_metadata(filepath)
    
    def _save_metadata(self, filepath):
        """
        Salva metadados do processo de anonimização
        """
        metadata_path = filepath.replace('.csv', '_metadata.txt')
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE ANONIMIZAÇÃO - DATASET TITANIC\n")
            f.write("="*60 + "\n\n")
            f.write(f"Data do processo: {pd.Timestamp.now()}\n")
            f.write(f"Arquivo original: data/titanic_clean.csv\n")
            f.write(f"Arquivo gerado: {filepath}\n\n")
            
            f.write("TÉCNICAS APLICADAS:\n")
            f.write("1. Remoção de coluna 'Embarked' (porto de embarque)\n")
            f.write("2. Remoção de coluna 'Sex' (gênero do passageiro)\n")
            f.write("3. Hash SHA256 na coluna 'Name' (identificador direto)\n\n")
            
            f.write("DADOS DO DATASET ANONIMIZADO:\n")
            f.write(f"Total de registros: {len(self.data)}\n")
            f.write(f"Total de colunas: {len(self.data.columns)}\n")
            f.write(f"Colunas: {', '.join(self.data.columns)}\n\n")
            
            f.write("HASH UTILIZADO:\n")
            f.write("- Algoritmo: SHA256\n")
            f.write("- Tamanho: 64 caracteres hexadecimais\n")
            f.write("- Propriedade: Irreversível (one-way function)\n")

def process_anonymization():
    """
    Função principal para processar a anonimização
    """
    print("="*60)
    print(" INICIANDO PROCESSO DE ANONIMIZAÇÃO")
    print("="*60)
    
    # Carregar dados limpos
    print("\n Carregando dados limpos...")
    df = pd.read_csv('data/titanic_clean.csv')
    print(f"   Shape original: {df.shape}")
    
    # Criar instância da classe de anonimização
    anonymizer = DataAnonymization(df)
    
    # Aplicar técnicas de anonimização
    print("\n Aplicando técnicas de anonimização...")
    anonymizer.remove_sensitive_columns()
    anonymizer.apply_hash_to_names()
    
    # Obter dados anonimizados
    df_anonimizado = anonymizer.get_anonymized_data()
    
    print(f"\n Dataset após anonimização:")
    print(f"   Shape final: {df_anonimizado.shape}")
    print(f"   Colunas finais: {list(df_anonimizado.columns)}")
    
    # Salvar resultados
    print("\n Salvando resultados...")
    anonymizer.save_anonymized_data('data/titanic_anonimizado.csv')
    
    # Mostrar prévia
    print("\n PRÉVIA DOS DADOS ANONIMIZADOS:")
    print(df_anonimizado.head())
    
    print("\n" + "="*60)
    print(" ANONIMIZAÇÃO CONCLUÍDA COM SUCESSO!")
    print("="*60)
    
    return df_anonimizado

# Executar se o script for rodado diretamente
if __name__ == "__main__":
    df_anonimizado = process_anonymization()