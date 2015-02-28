from avwx.models import MetarSet, TafSet, WeatherStation


class WeatherSummary(object):
    station = None

    def __init__(self, station_id):
        self.station = WeatherStation(station_id)
        self.metars = MetarSet(station_id)
        self.tafs = TafSet(station_id)

        self.refresh()

    def refresh(self):
        self.metars.refresh()
