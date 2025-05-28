import duckdb
from flask import Flask

app = Flask(__name__)

@app.route("/tripcount")
def returndata():
  cursor = duckdb.connect()
  try:
    count = cursor.execute("select count(*) from read_parquet('/data/*.parquet')").fetchall()[0][0]
    return f"Total trips: {count}"
  except duckdb.duckdb.IOException:
    return f"Data files are not present", 503

@app.route("/first")
def returnfirst():
  cursor = duckdb.connect()
  try:
    first = cursor.execute("select min(tpep_pickup_datetime) from read_parquet('/data/*.parquet')").fetchall()[0][0]
    return f"First pickup: {first:%Y/%m/%d}" 
  except duckdb.duckdb.IOException:
    return f"Data files are not present", 503

@app.route("/last")
def returnlast():
  cursor = duckdb.connect()
  try:
    last = cursor.execute("select max(tpep_pickup_datetime) from read_parquet('/data/*.parquet')").fetchall()[0][0]
    return f"Last pickup: {last:%Y/%m/%d}" 
  except duckdb.duckdb.IOException:
    return f"Data files are not present", 503
