#!/usr/bin/env python

import requests
import json
import time
import datetime
import turtle

__author__ = """
    https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
    Ybrayy Abamov
    Doug Enas
    Piero Madarp
            """


base_url = 'http://api.open-notify.org'


def astro_members():
    r = requests.get(base_url + '/astros.json')
    return r.json()['people']


def astro_position():
    r = requests.get(base_url + '/iss-now.json')
    positions = r.json()['iss_position']
    return positions


def astro_time():
    r = requests.get(base_url + '/iss-now.json')
    iss_time = r.json()['timestamp']
    iss_time = iss_time % (24 * 3600)
    hour = iss_time // 3600
    iss_time %= 3600
    minutes = iss_time // 60
    iss_time %= 60
    return '%d:%02d:%02d' % (hour, minutes, iss_time)


def astro_graph():
    t = turtle.Turtle()
    screen = turtle.Screen()
    screen.register_shape("iss.gif")
    screen.setup(720, 360, startx=0, starty=0)
    screen.bgpic("map.gif")
    screen.setworldcoordinates(-180, -90, 180, 90)
    t.penup()
    t.goto(float(astro_position()['longitude']),
           float(astro_position()['latitude']))
    t.shape('iss.gif')
    # turtle.done() # uncomment it to see the actual map and ISS space-craft's location on the map


def astro_future(lon, lat):
    """ Will get the future lat/lon coordinates
    of the space-craft to the specified location
    """
    params = {'lat': lat, 'lon': lon}
    r = requests.get(base_url + '/iss-pass.json', params=params)
    risetime = time.ctime(r.json()['response'][0]['risetime'])
    return risetime


def main():
    astro_dict = astro_members()
    print(f'\n Current number of astronauts in space is: {len(astro_dict)}')
    print("\n The astronauts' full-names and the space-craft which they're on:")
    for d in astro_dict:
        print(f' {"   "} {d["name"]} in space-craft --> {d["craft"]}')

    astro_p = astro_position()
    print(
        f' \n The latitude point of the space-craft is {astro_p["latitude"]} and longitude point of the space-craft is {astro_p["longitude"]}')

    print(f' The timestamp is {astro_time()} \n ')

    astro_graph()

    pred_time = astro_future(-86.1581, 39.7684)
    print('The ISS will be passing Indianpolis at: ' + str(pred_time))


if __name__ == '__main__':
    main()
