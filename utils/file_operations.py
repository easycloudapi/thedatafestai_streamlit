def convert_to_json(df):
    process_df_json = df.copy()
    return process_df_json.to_json()

def convert_to_csv(df):
    process_df_csv = df.copy()
    return process_df_csv.to_csv(index=False).encode('utf-8')

def convert_to_excel(df):
    pass