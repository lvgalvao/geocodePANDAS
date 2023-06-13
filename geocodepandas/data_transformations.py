import pandas as pd


def extract_city(df):
    df['city'] = df['display_name'].str.split(',').str[-4].str.strip()
    return df


def extract_state(df):
    df['state'] = df['display_name'].str.split(',').str[-3].str.strip()
    return df


# Exemplo de uso
if __name__ == '__main__':
    # Exemplo de uso
    data = {
        'display_name': [
            """Roque Saenz Peña, Cóndor Bajo, Barrio Cumbres, Villa Allende, Municipio de Villa Allende,
            Pedanía Calera Norte, Departamento Colón, Córdoba, X5111, Argentina"""
        ]
    }
    df = pd.DataFrame(data)

    df = extract_city(df)

    print(df['city'].values[0])
