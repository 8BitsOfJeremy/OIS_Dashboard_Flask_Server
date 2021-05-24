from flask import Flask, jsonify, render_template, session, request, Response, redirect, url_for, send_from_directory
import settings
import logging
import json
from logging.handlers import RotatingFileHandler


# ============================================
# Logging
# ============================================

app = Flask(__name__)
formatter = logging.Formatter(settings.LOG_FORMAT)
handler = RotatingFileHandler(
    settings.LOG_FILE,
    maxBytes=settings.LOG_MAX_BYTES,
    backupCount=settings.LOG_BACKUP_COUNT
)
handler.setLevel(logging.getLevelName(settings.LOG_LEVEL))
handler.setFormatter(formatter)
app.logger.addHandler(handler)


# ============================================
# Web Views / Routes
# ============================================


# Home page
@app.route('/', methods=['GET'])
def index():
    return 'not implemented', 200


@app.route('/getDayType', methods=['GET'])
def getDayType():
    return jsonify(dayType='A')


@app.route('/getBellScheduleForRoom', methods=['GET'])
def getBellScheduleForRoom():
    room_info = [
        {
            'className': 'AP CS',
            'teacherName': 'Mr. Anderson',
            'startTime': '13:25pm',
            'endTime': '14:45pm',
            'blockName': 'B4(O)'
        },
        {
            'className': 'Math Something',
            'teacherName': 'Mrs. Africa',
            'startTime': '08:30am',
            'endTime': '09:50am',
            'blockName': 'B1(O)'
        }
    ]
    return jsonify(room_info)

# ============
# Added from https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uswgi-and-nginx-on-ubuntu-18-04
#


if __name__ == "__main__":
    app.run(host='0.0.0.0')
