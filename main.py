from datetime import date, datetime
import numpy as np
from bashplotlib.histogram import plot_hist


from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    dt = datetime.now()
    print(f'Сегодня {dt.date()}.', get_employees())
    print(f'Cегодня в {dt.isoweekday()}-й день недели', calculate_salary())

    arr = np.random.normal(size=1000, loc=0, scale=1)
    plot_hist(arr, bincount=25)



