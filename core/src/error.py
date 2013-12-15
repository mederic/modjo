class ModjoSyntaxError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Uncorrect syntax : " + self.reason

class ModjoTemplateError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Invalid template : " + self.reason

class XMLParseError(Exception):

    def __init__(self, filePath):
        self.filePath = filePath

    def __str__(self):
        return filePath + " is not a valid xml file..."


class ModjoDownloaderError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'Cannot download template: ' + self.reason


class ModjoConfigError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return 'Invalid config file: ' + self.reason
