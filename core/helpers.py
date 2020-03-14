import os
import json
from flask import abort, Response
from flask_sqlalchemy import BaseQuery


def create_folder():
    root = os.getcwd()
    app_name = input("Enter app name: ")
    app_path = os.path.join(root, app_name)
    if not os.path.exists(app_path):
        os.mkdir(app_path)
        return app_name
    else:
        print('{0} already exists in this project'.format(app_name))
        return None


def create_file(filename):
    if not os.path.exists(filename):
        open(filename, 'w')
    else:
        print('{0} already exists in this project'.format(filename))


def create_files(filenames):
    for filename in filenames:
        if not os.path.exists(filename):
            open(filename, 'w')
        else:
            print('{0} already exists in this project'.format(filename))


class CustomBaseQuery(BaseQuery):
    def get_or_404(self, ident):
        model_class_name = ''
        try:
            model_class_name = self._mapper_zero().class_.__name__
        except Exception as e:
            print(e)

        rv = self.get(ident)
        if not rv:
            error_message = json.dumps(
                {'message': model_class_name + ' ' +
                 str(ident) + ' not found'})
            abort(Response(error_message, 404))
        return rv
