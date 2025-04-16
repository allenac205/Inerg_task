# Inerg_task
A Flask-based API to serve annual oil, gas, and brine production data from a SQLite database.

## ⚙️ Setup Instructions

1. **Clone the repo**
```bash
git clone https://github.com/your-username/production-data-api.git

cd inerg_task
```


2. **Create and activate a virtual environment **
```bash
python3 -m venv venv

source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Process the Excel data (Optional)**
```bash
python3 load_db_data.py
```
This will read the .xls file, group the data by api well number, and store the annual production data in production_data.sqlite3.


3. **Run the API**
```bash
python3 main.py
```
Server will start on http://localhost:8080


## 🔍 API Usage
GET /data

Query Parameters:
  well (required): API Well Number

Example:
```bash
http://localhost:8080/data?well=34059242540000
```

Response:
```json
{
  "oil": 381,
  "gas": 108074,
  "brine": 939
}
```


