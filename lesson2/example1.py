import time
from datetime import datetime

time_coeff = 0.2


def dish(name, prepare, wait):
    print(f"start: {datetime.now().strftime('%HH:%MM:%SS')} prepare {name}, {prepare} min")
    time.sleep(time_coeff * prepare)
    print(f"start: {datetime.now().strftime('%HH:%MM:%SS')} wait {name}, {wait} min")
    time.sleep(time_coeff * wait)
    print(f"{datetime.now().strftime('%HH:%MM:%SS')} dish {name} is ready!")


def main():
    dish("Закуска", 2, 3)
    dish("Основное блюдо", 5, 10)
    dish("Десерт", 3, 5)


if __name__ == "__main__":
    t0 = time.time()
    main()
    dt = (time.time() - t0) / time_coeff
    print(f"{datetime.now().strftime('%HH:%MM:%SS')} It took {dt} time")
    