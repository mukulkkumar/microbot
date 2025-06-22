from db_test import TestDB


class TestModule(object):

    scripts = {
        'test-script': TestDB
    }

    def __init__(self, script, optional_arg=None):
        if script in self.scripts:
            if optional_arg:
                self.scripts[script](optional_arg)
            else:
                self.scripts[script]()
        else:
            print("Invalid Script")
