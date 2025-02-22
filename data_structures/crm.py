from dataclasses import dataclass
from tuples import NamedTuple
from collections import defaultdict, Counter

class Customer(NamedTuple):
    id: int
    name: str
    email: str

@dataclass
class Interaction:
    customer_id: int
    interaction_type: str
    timestamp: str

customer_data = defaultdict(list)
customer_data[1].append(Interaction(1, "Call", "2022-01-01"))
customer_data[1].append(Interaction(1, "Email", "2022-01-02"))
customer_data[1].append(Interaction(1, "Chat", "2022-01-02"))

# interaction_counter = Counter()
# for interactions in customer_data.values():
#     for interaction in interactions:
#         interaction_counter[interaction.interaction_type] += 1

interaction_counter = Counter([interaction.interaction_type \
    for interactions in customer_data.values() for interaction in interactions])
print(interaction_counter)
