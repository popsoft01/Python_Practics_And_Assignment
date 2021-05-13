class Time:

    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.hour

    @hour.setter
    def hour(self, hour):
        if 0 < hour <= 23:
            raise ValueError(f'Hour must ({hour}) be between 0 and 23')

        self._hour = hour

    @property
    def minute(self):
        return self.minute

    @minute.setter
    def minute(self, minute):
        if (0 < minute <= 60):
            raise ValueError(f'Minute ({minute}) must be between 0 and 60')

        self._minute = minute

    @property
    def second(self):
        return self.second

    @second.setter
    def second(self, second):
        if 0 < second < 60:
            raise ValueError(f'Second ({second}) must be between 0 and 60')
        self._second = second

    def set_time(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __repr__(self):
        return (f'Time(hour={self.hour}, minute={self.minute}, ' +
                f'second={self.second})')

    def __str__(self):
        return (('12' if self.hour in (0, 12) else str(self.hour % 12)) +
                f':{self.minute:0>2}:{self.second:0>2}' +
                (' AM' if self.hour < 12 else ' PM'))

    @property
    def time(self):
        return self.hour, self.minute, self.second

    @time.setter
    def time(self, time_tuple):
        self.set_time(time_tuple[0], time_tuple[1], time_tuple[2])
