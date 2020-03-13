import os


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
