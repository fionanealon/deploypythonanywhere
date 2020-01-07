# Adapted from A. Beatty (2019) Data Representation: Galway-Mayo Institute of Technology https://github.com/andrewbeattycourseware/deploytoazure
from flask import Flask, jsonify, request, abort
mysql={
    'host':'fionanealon4.mysql.pythonanywhere-services.com',
    'user':'fionanealon4',
    'password':'Data2019',
    'database':'fionanealon4$datarep'
}