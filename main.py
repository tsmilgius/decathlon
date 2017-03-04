import math
from helpers import to_seconds
from readinput import read_csv
#
# class Event:
#     def __init__(self, name, a, b, c, result):
#         self.name = name
#         self.a = a
#         self.b = b
#         self.c = c
#         self.result = result
#
#     def track_event_score(self):
#         """ calculates score for track events"""
#         return int(self.a * math.pow((self.b - self.result), self.c))
#
#     def field_event_jump_score(self):
#         """ calculates score for field jumping events"""
#         return int(self.a * math.pow((self.result*100 - self.b), self.c))
#
#     def field_event_throw_score(self):
#         """ calculates score for field throwing events"""
#         return int(self.a * math.pow((self.result - self.b), self.c))


class Athlete:

    result = 0;
    hundred_meters = (25.4347, 18, 1.81)
    long_jump = (0.14354, 220, 1.4)
    shot_put = (51.39, 1.5, 1.05)
    hih_jump = (0.8465, 75, 1.42)
    four_hundred = (1.53775, 82, 1.81)
    hurdles= (5.74352, 28.5, 1.92)
    discus = (12.91, 4, 1.1)
    pole =  (10.14, 7, 1.08)
    javelin = (10.14, 7, 1.08)
    fifteen_hundred = (0.03768, 480, 1.85)

    def __init__(self, result_set):
        self.result_set = result_set

    def track_event_score(self):
        """ calculates score for track events"""
        return int(self.a * math.pow((self.b - self.result), self.c))

    def field_event_jump_score(self):
        """ calculates score for field jumping events"""
        return int(self.a * math.pow((self.result*100 - self.b), self.c))

    def field_event_throw_score(self):
        """ calculates score for field throwing events"""
        return int(self.a * math.pow((self.result - self.b), self.c))

    def print_athlete_result(self):

        for key, value in self.result_set.items():
            if key == '100m':
                result +=  int(hundred_meters[0] * math.pow((hundred_meters[1] - float(self.result_set[key]) ), hundred_meters[2]))
            if key == 'Long jump':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == 'Shot put':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == 'High jump':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == '400m':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == '110m hurdles':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == 'Discus throw':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == 'Pole vault':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == 'Javelin throw':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))
            if key == '1500m':
                result += int(long_jump[0] * math.pow((float(self.result_set[key])*100 - long_jump[1]), long_jump[2]))

        return result




athl = Athlete(read_csv()[0])

print(athl.print_athlete_result())


# first_event = Event('100 m', 25.4347, 18, 1.81, 10.23)
# second_event = Event('Long Jump', 0.14354, 220, 1.4, 7.88)
# third_event = Event('Shot Put', 51.39, 1.5, 1.05, 14.52)
# fourth_event = Event('High Jump', 0.8465, 75, 1.42, 2.01)
# fifth_event = Event('400 m', 1.53775, 82, 1.81, 45.00)
# sixth_event = Event('110 m hurdles', 5.74352, 28.5, 1.92, 13.69)
# seventh_event = Event('Discus Throw', 12.91, 4, 1.1, 43.34)
# eight_event = Event('Pole Vault', 0.2797, 100, 1.35, 5.20)
# ninth_event = Event('Javelin Throw', 10.14, 7, 1.08, 63.63)
# tenth_event = Event('1500 m', 0.03768, 480, 1.85, float(to_seconds('4.17.52')))
#
#
# # print(first_event.track_event_score() + second_event.field_event_jump_score() + third_event.field_event_throw_score() + fourth_event.field_event_jump_score() + fifth_event.track_event_score() + sixth_event.track_event_score() + seventh_event.field_event_throw_score() + eight_event.field_event_jump_score() + ninth_event.field_event_throw_score() + tenth_event.track_event_score())
# # print(second_event.field_event_jump_score())
# print(to_seconds('4.17.52'))
# print(tenth_event.track_event_score())
