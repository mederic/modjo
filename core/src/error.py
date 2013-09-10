class ModjoSyntaxError(Exception):

    def __init__(self, reason):
        self.reason = reason

    def __str__(self):
        return "Uncorrect syntax : " + reason
        
class XMLParseError(Exception):

    def __init__(self, filePath):
        self.filePath = filePath

    def __str__(self):
        return filePath + " is not a valid xml file..."