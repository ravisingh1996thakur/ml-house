from flask import Flask
import sys
from housing.logger import logging 
from housing.exception import HousingException
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("we are esting ustum exception ")
    except Exception as e:
        housing= HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("we are testing logging module")
    return "ML HOUSE REGRESSION CALIFORNIA DATASET "


if __name__=="__main__":
    app.run(debug=True)
