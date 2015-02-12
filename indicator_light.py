import sys

from avwx.models import Metar, SkyCondition

from colorama import Fore, Back, Style

class Indicator(object):
    color = None
    reason = None

    def __init__(self, color, reason=None):
        if color not in ['red', 'yellow', 'green']:
            raise Exception("Invalid color: %s" % color)
        self.color = color
        self.reason = reason

    def __str__(self):
        if self.color == 'red':
            term_str = Fore.WHITE + Back.RED + Style.BRIGHT
        elif self.color == 'yellow':
            term_str = Fore.BLACK + Back.YELLOW
        elif self.color == 'green':
            term_str = Fore.BLACK + Back.GREEN
        else:
            raise Exception("Unexpected color")
        return term_str + " %s LIGHT%s " % (self.color.upper(), (' (%s)' % self.reason) if self.reason else '') \
                + Fore.RESET + Back.RESET + Style.RESET_ALL




def get_bad_indicators(metar):
    indicators = []
    if metar.flight_category not in ['VFR']:
        indicators.append(Indicator('red', "Flight Category: %s" % metar.flight_category))
    if metar.visibility < 8:
        indicators.append(Indicator('red', "Visibility: %.2f sm" % metar.visibility))
    cloud_base = metar.get_base_cloud_layer()
    if cloud_base is not None:
        if cloud_base.height <= 3500:
            indicators.append(Indicator('red', "Cloud Base: %s AGL" % cloud_base))
        elif cloud_base.height <= 6000:
            indicators.append(Indicator('red', "Cloud Base: %s AGL" % cloud_base))
    if metar.wind_speed > 20:
        indicators.append(Indicator('red', "High Winds: %s kts" % metar.wind_speed))
    elif metar.wind_speed > 10:
        indicators.append(Indicator('yellow', "Wind: %s kts" % metar.wind_speed))
    # Gusts
    if metar.wind_gust is not None:
        gust_diff = metar.wind_gust - metar.wind_speed
        if gust_diff >= 10:
            indicators.append(Indicator('red', "High Wind Gusts: %s kts" % metar.wind_gust))
        elif gust_diff >= 5:
            indicators.append(Indicator('yellow', "Wind Gusting: %s kts" % metar.wind_gust))
    if metar.temp <= 0:
        indicators.append(Indicator('yellow', "It's chilly: %.0fC (%.0fF)" % (metar.temp, (metar.temp * 9 / 5 + 32))))
    return indicators

metar = Metar("%s" % sys.argv[1]) #, fake='mock.xml')
#metar = Metar('KAPA', fake='mock.xml')
metar.refresh()
bad_indicators = get_bad_indicators(metar)
print metar.raw_text
if len(bad_indicators) == 0:
    print Indicator('green')
else:
    for indicator in bad_indicators:
        print indicator
