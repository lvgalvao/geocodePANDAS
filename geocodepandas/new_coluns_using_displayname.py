import pandas as pd

# Lendo o arquivo CSV
df = pd.read_csv('files/setNewAddress_FULL.csv')

# Função para extrair os elementos -1, -2, -3, -4 e -5
def extrair_elementos(display_name):
    if isinstance(display_name, str):
        items = display_name.split(', ')
        n = len(items)
        return (
            items[-1] if n >= 1 else '',
            items[-2] if n >= 2 else '',
            items[-3] if n >= 3 else '',
            items[-4] if n >= 4 else '',
            items[-5] if n >= 5 else '',
        )
    else:
        return ('', '', '', '', '')


# Aplicar a função na coluna 'display_name' e criar novas colunas
(
    df['elemento_-1'],
    df['elemento_-2'],
    df['elemento_-3'],
    df['elemento_-4'],
    df['elemento_-5'],
) = zip(*df['display_name'].apply(extrair_elementos))

df.to_csv('files/setNewAddress_FULL_EN.csv', index=False)

# Visualizar o DataFrame resultante
print(df.head())
