import requests
import pandas as pd

def fetch_fda_reports(total_records=10000, batch_size=100):
    """
    Fetch drug adverse event reports from OpenFDA API in batches,
    extract key fields, and return as a pandas DataFrame.
    No data cleaning applied.
    """
    all_records = []

    for skip in range(0, total_records, batch_size):
        url = f"https://api.fda.gov/drug/event.json?limit={batch_size}&skip={skip}"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch data at skip={skip}. Status code: {response.status_code}")
            continue

        data = response.json()
        for event in data.get('results', []):
            try:
                patient = event['patient']

                age = patient.get('patientonsetage')
                sex = patient.get('patientsex')
                drug = None
                if 'drug' in patient and len(patient['drug']) > 0:
                    drug = patient['drug'][0].get('medicinalproduct')

                reaction = None
                if 'reaction' in patient and len(patient['reaction']) > 0:
                    reaction = patient['reaction'][0].get('reactionmeddrapt')

                hospitalized = event.get('seriousnesshospitalization', 0)

                record = {
                    'age': age,
                    'sex': sex,
                    'drug': drug,
                    'reaction': reaction,
                    'hospitalized': hospitalized
                }

                all_records.append(record)
            except:
                continue

    df = pd.DataFrame(all_records)
    return df

if __name__ == "__main__":
    df = fetch_fda_reports(total_records=10000, batch_size=1000)
    df.to_csv('dataset.csv', index=False)
    print("Data saved to dataset.csv")
    
    print(df.head(10))
