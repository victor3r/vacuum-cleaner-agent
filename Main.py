import numpy as np

from VacuumCleaner import VacuumCleaner

world = np.array([[1, 0], 
                  [0, 1]])

vacuum_cleaner = VacuumCleaner(world)
vacuum_cleaner.aspirate()
print('\nNúmero de quadrados que foram aspirados: {}'.format(vacuum_cleaner.getScore()))