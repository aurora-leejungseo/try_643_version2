import pandas as pd
from datetime import datetime

def read(file_path):
    df = pd.read_csv(file_path)
    return df

def clean(other, contact):
    # dtype_dic= {'respondent_id': int, 
    #         'job' : str,
    #         'company': str,
    #         'birthdate': str}
    df_other = read(other)
    df_contact = read_csv(contact)

    df = pd.merge(df_contact, df_other, on='respondent_id', how='left')
    df['birthdate'] = df['birthdate'].apply(lambda x: datetime.strptime(x, '%m%d%Y'))

    return df

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('contact_info_file', help='Contact info file (CSV)')
    parser.add_argument('other_info_file', help='Other info file (CSV)')
    parser.add_argument('output_file', help='Joined and cleaned output file (CSV)')
    args = parser.parse_args()

    df = clean(args.other_info_file, args.contact_info_file)

    df.to_csv(args.output_file, index=False)