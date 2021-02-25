import json
import logging

from flask import Flask, request
import os, sys, csv

#################################
########## MAIN APP #############
#################################

try:
    app = Flask(__name__)

    # open file
    def open_file(file_path):
        file = open(file_path, 'r')

        def csv_process(file):
            dict_items = csv.DictReader(file)
            anylist = []
            for row in dict_items:
                anylist.append(row)
            return anylist

        return csv_process(file)

    # write to file
    def write_to_file(file_path, values):
        try:
            file = open(file_path, 'a')
            somestring = ",".join(str(item) for item in values)
            file.write('\n')
            file.write(somestring)
        except Exception as err:
            raise err

    class AppContext:
    # DAO to csv file

        def __init__(self, file):
            self.items = file

    context = AppContext(open_file('./payload-sample.csv'))

    # show all items
    @app.route('/items')
    def items():
        logging.info(context.items)
        return json.dumps(context.items), 200

    # show item by id
    @app.route('/item/<id>')
    def item(id):
        logging.info(id)
        for item in context.items:
            if item['id'] == id:
                return item

    # add item
    @app.route('/add_item', methods=['POST'])
    def item_post():
        data = request.json
        logging.info(data)

        write_to_file('./payload-sample.csv', data['items'])
        return json.dumps({'success': True}), 200

    print('Startup!!!')
    app.run()

#################################
########## MAIN APP #############
#################################
except KeyboardInterrupt:
    print('EXIT')
    sys.exit()