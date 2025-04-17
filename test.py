from flask import Flask, jsonify, request
import sqlite3, requests
from icecream import ic
import pandas as pd


def test_db_well_content():
    conn = sqlite3.connect("production_data.sqlite3")
    cursor = conn.cursor()

    query = 'SELECT "API WELL  NUMBER" FROM annual_production'
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()

    wells = [row[0] for row in result]
    ic(len(wells))

    set_wells = set(wells)
    ic(len(set_wells))


def xls_unique_api_well_numbers():

    file_path = "data.xls"
    df = pd.read_excel(file_path)

    unique_api_wells = df["API WELL  NUMBER"].unique()
    ic(len(unique_api_wells))


def chk_each_well():

    file_path = "data.xls"
    df = pd.read_excel(file_path)

    unique_api_wells = df["API WELL  NUMBER"].unique().tolist()
    # ic(unique_api_wells)

    existing = {}
    non_existing = {}

    for well in unique_api_wells:

        url = f"http://localhost:8080/data?well={well}"

        try:
            response = requests.get(url)
            if response.status_code == 200:
                existing[well] = response.json()
            else:
                non_existing[well] = response.status_code

        except Exception as e:
            ic(f"Failed to connect for well {well}: {e}")
        
    ic(len(existing))
    ic(len(non_existing))




if __name__ == "__main__":
    print("\n" + "="*70)
    print("Test 1: Check for duplicate 'API WELL NUMBER' entries in DB")
    test_db_well_content()
    print("="*70 + "\n")

    print("="*70)
    print("Test 2: Display count of unique 'API WELL NUMBER' from Excel")
    xls_unique_api_well_numbers()
    print("="*70 + "\n")

    print("="*70)
    print("Test 3: Verify each unique Excel well number against API 'http://localhost:8080/data?well=<well_number>'")
    chk_each_well()
    print("="*70 + "\n")
    print("All tests completed successfully!\n")
