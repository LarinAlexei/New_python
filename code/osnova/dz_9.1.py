import time
import itertools


class TrafficLight:
    __color = [['red', [7, 31]], ['yellow', [3, 33]], ['green', [15, 32]], ['yellow', [3, 33]]]


    def go(self):
        for light in itertools.cycle(self.__color):
            print(f'\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m', end='')
            time.sleep(light[1][0])


trafficlight_1 = TrafficLight()
trafficlight_1.go()