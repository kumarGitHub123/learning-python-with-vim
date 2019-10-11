import converters
import utils
# we can also import just parts of a module, rther than the whole module
from converters import lbs_to_kg


print(converters.kg_to_lbs(70))
print(lbs_to_kg(70))

numbers = [10, 3, 6, 2]
print(utils.find_max(numbers))


