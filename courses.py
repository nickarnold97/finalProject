__author__ = 'NicholasArnold'


class Course:
    def __init__(self, title='Class', course=('College','Department', 'Course'),section='A1', typ='Lecture',
                 instructor='Professor', cred=0, location=('Building','Room'), days=['Monday','Wednesday','Friday'],
                 time=('12:00am','1:00pm'),notes=None):

        self.title = title
        self.course = course
        self.section = section
        self.Typ = typ

        self.instructor = instructor

        self.cred_hrs = cred

        self.location = location
        self.day_time = {}
        for day in days:
            self.day_time[day]= (self.to_twentyfour(time[0]), self.to_twentyfour(time[1]))

        self.notes = notes

    def to_twentyfour(self,time):
        """Converts a time given as a string in format 'HR:MINam/pm'
        to an integer between 0 and 2400"""
        hours = 0
        hour_min = time[0:-2].split(':')
        afternoon = time[-2:] == 'pm'
        hours += int(hour_min[0]) * 100 + int(hour_min[1])
        if afternoon:
            hours += 1200
        return hours

    def to_twelve(self,time):
        "Converts an integer time value between 0 and 2400 to HR:MIN am/pm format"
        afternoon = False
        tod = 'am'
        if time >= 1200:
            time -= 1200
            afternoon = True
            tod = 'pm'
        if time == 0:
            time += 1200
        hour = str(time)[0:-2]
        minute = str(time)[-2:]
        return "{}:{} {}".format(hour, minute, tod)

python = Course()
print(type(python))
print(python.day_time)