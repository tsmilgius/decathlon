import math, json, io, codecs
from collections import OrderedDict
from operator import itemgetter
from helpers import to_seconds
from readinput import read_input


class Athlete:

        
    def __init__(self, result_set):
        self.result_set = result_set


    def athlete_result(self):
        """calculates athletes result, returns an integer"""
        result = 0
        hundred_meters = (25.4347, 18, 1.81)
        long_jump = (0.14354, 220, 1.4)
        shot_put = (51.39, 1.5, 1.05)
        high_jump = (0.8465, 75, 1.42)
        four_hundred = (1.53775, 82, 1.81)
        hurdles = (5.74352, 28.5, 1.92)
        discus = (12.91, 4, 1.1)
        pole = (0.2797, 100, 1.35)
        javelin = (10.14, 7, 1.08)
        fifteen_hundred = (0.03768, 480, 1.85)

        ## TO DO: rewrite this part: create three different cases/methods and call them when needed

        for key, value in self.result_set.items():
            if key == '100m':
                result += int(
                    hundred_meters[0] * math.pow((hundred_meters[1] - float(self.result_set[key])), hundred_meters[2]))
            if key == 'Long jump':
                result += int(long_jump[0] * math.pow((float(self.result_set[key]) * 100 - long_jump[1]), long_jump[2]))
            if key == 'Shot put':
                result += int(shot_put[0] * math.pow((float(self.result_set[key]) - shot_put[1]), shot_put[2]))
            if key == 'High jump':
                result += int(high_jump[0] * math.pow((float(self.result_set[key]) * 100 - high_jump[1]), high_jump[2]))
            if key == '400m':
                result += int(
                    four_hundred[0] * math.pow((four_hundred[1] - float(self.result_set[key])), four_hundred[2]))
            if key == '110m hurdles':
                result += int(hurdles[0] * math.pow((hurdles[1] - float(self.result_set[key])), hurdles[2]))
            if key == 'Discus throw':
                result += int(discus[0] * math.pow((float(self.result_set[key]) - discus[1]), discus[2]))
            if key == 'Pole vault':
                result += int(pole[0] * math.pow((float(self.result_set[key]) * 100 - pole[1]), pole[2]))
            if key == 'Javelin throw':
                result += int(javelin[0] * math.pow((float(self.result_set[key]) - javelin[1]), javelin[2]))
            if key == '1500m':
                result += int(
                    fifteen_hundred[0] * math.pow((fifteen_hundred[1] - float(to_seconds(self.result_set[key]))),
                                                  fifteen_hundred[2]))
        return result

    def list_results():
        """returns the list of all results"""
        res_li = []
        for athl in range(len(read_input())):
            res_li.append(Athlete(read_input()[athl]).athlete_result())

        return res_li

    def add_score_position():
        """ adds 'result' key and according value to a dictionary
        also sorts the list by the result in descending order and
        assigns the 'position to the athlete"""
        listas = read_input()
        for athl in range(len(Athlete.list_results())):
            listas[athl]['result'] = Athlete.list_results()[athl]
        sortedlist = sorted(listas, key=itemgetter('result'), reverse=True)
        for ath in range(len(sortedlist)):
            sortedlist[ath]['position'] = str(ath + 1)
        for d in range(len(sortedlist) - 1):
            if sortedlist[d]['result'] == sortedlist[d + 1]['result']:
                sortedlist[d]['position'] = str(sortedlist[d]['position']) + '-' + str(sortedlist[d + 1]['position'])
                sortedlist[d + 1]['position'] = str(sortedlist[d]['position'])
        return sortedlist


def save_to_file():
    """saves the result to pretty printed *.json file"""
    final_dict = OrderedDict()
    final_dict['Competition scores'] = Athlete.add_score_position()

    with codecs.open('uploads/data.json', 'w', 'utf8') as f:
        f.write(json.dumps(final_dict, indent=4, sort_keys=True, ensure_ascii=False))
