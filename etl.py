import pandas as pd
from app.logger import logger

def process(file):
    logger.info(f'Processing {file}')
    if file.endswith('.csv'):
        df=pd.read_csv(file)
    elif file.endswith('.xlsx'):
        df=pd.read_excel(file)
    elif file.endswith('.json'):
        df=pd.read_json(file)
    else:
        raise Exception('Unsupported format')
    df.fillna(0,inplace=True)
    return df.describe()
