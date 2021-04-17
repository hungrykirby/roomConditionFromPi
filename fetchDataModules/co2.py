import subprocess
import re

class MHZ19CO2Fetcher:
    def __init__(self):
        pass

    def fetchData(self):
        try:
            out = subprocess.check_output(['sudo', 'python', '-m', 'mh_z19'])
            if not out:
                return False, 'Not Found Matched Int'
            return True, int(self.extractCO2FromOutput(out))
        except:
            return False, 'subprocess error'

    def extractCO2FromOutput(self, out):
        try:
            d = out.decode().strip().split('\n')[0]
            pattern = '{"co2": (\d+)}'
            result = re.match(pattern, d)
            return result.group(1)
        except:
            return False