from core.src.error import *
import os
import sys
import urllib2
from zipfile import ZipFile

class TemplateDownloader:

    def __init__(self, ref_template, config):
        self.ref_template = ref_template
        self.config = config

        splitted = ref_template.split(':', 1)
        repos_name = splitted[0]
        template_id = splitted[1]

        self.repos = self.config.repos.get(repos_name)
        if self.repos is None:
           raise ModjoSyntaxError('unknown repos : \'' + repos_name + '\'')

        if not self.repos.is_local:
            self.local_path = config.template_folder
            self.local_path = os.path.join(self.local_path, repos_name)

            if not os.path.exists(self.local_path):
                os.makedirs(self.local_path)

            self.local_path = os.path.join(self.local_path, template_id)

            if not os.path.exists(self.local_path):
                self.download(repos_name, template_id)
        else:
            self.local_path = self.repos.uri + template_id

    def download(self, repos_name, template_id):
        zip_url = self.repos.uri + 'template/'
        zip_url += template_id
        zip_url += '.zip'

        print 'Start downloading \'' + template_id + '\' from repos \'' + repos_name + '\'\n'

        try:
            u = urllib2.urlopen(zip_url)
        except:
            raise ModjoDownloaderError('Cannot access to ' + zip_url)

        f = open(self.local_path + '.zip', 'w')
        meta = u.info()
        file_size = int(meta.getheaders('Content-length')[0])

        file_size_dl = 0
        block_size = 512
        while True:
            buffer = u.read(block_size)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            p = float(file_size_dl) / file_size
            self.print_progress(p)

        print '\n'
        f.close()
        # We have now to unzip template...

        zip_file = ZipFile(self.local_path + '.zip')
        os.makedirs(self.local_path)
        zip_file.extractall(self.local_path)
        zip_file.close()
        os.remove(self.local_path + '.zip')

    def print_progress(self, progress):
        int_progress = int(progress * 100)
        str_progress = '  [{0}] {1}%'.format('=' * (int_progress / 5), int_progress)
        sys.stdout.write('\r' + str_progress)

    def getLocalPath(self):
        return self.local_path
