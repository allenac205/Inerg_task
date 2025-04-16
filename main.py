from flask import Flask, jsonify, request
import sqlite3
from icecream import ic

app = Flask(__name__)

@app.route("/data", methods=["GET"])
def get_well_data():
   
    well = request.args.get("well")
    ic(well)

    if well:
        
        conn = sqlite3.connect("production_data.sqlite3")
        cursor = conn.cursor()
        ic(cursor)

        query = """
            SELECT OIL, GAS, BRINE FROM annual_production WHERE "API WELL  NUMBER" = ?
        """
        cursor.execute(query, (well,))
        result = cursor.fetchone()
        ic(result)
        conn.close()

        if result:
            out = {
                "oil": result[0],
                "gas": result[1],
                "brine": result[2]
            }
            ic(out)
            return jsonify(out)
            
        else:
            return jsonify({"error": "Well not found"}), 404
    
    else:
        return jsonify({"error": "Missing 'well' query parameter"}), 400


if __name__ == "__main__":
    app.run(port=8080, debug=True)
