import csv
from pathlib import Path

dataFile='data.csv'
cfgFileDirectory = 'config'

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(cfgFileDirectory).joinpath(dataFile)


placeList=[(i, f'Unter den Linden {i}', 'Berlin', 'NaN', 'NaN') for i in range(1, 21)]

def create_data(db):
    # with open(DATA_FILE, 'w', newline='') as f:
    #     fieldnames = ['id','street','city','lat','lon']
    #     writer = csv.DictWriter(f, fieldnames=fieldnames)
    #     writer.writeheader()
    head=[('id','street','city','lat','lon')]
    db=head + db

    data_file = open(DATA_FILE, 'w', newline='')
    with data_file:
        writer = csv.writer(data_file)
        writer.writerows(db)
    pass


def get_data():
    with open(DATA_FILE, 'r') as f:
        reader = csv.reader(f)
        next(reader)
        data=[tuple(row) for row in reader]
    return data


create_data(placeList)
print([get_data()[0][-1], get_data()[0][0]])
print(get_data())
