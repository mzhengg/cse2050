# Include your answers for this lab in the dictionary below.
# The keys of the dictionary are the pre-numbered algorithms.
# The values are your answers. Use:
#     'bubble'
#     'selction'
#     'insertion'
#     'mergesort'
#     'quicksort'

# #For instance, if you though all the algorithms  were bubble sort (note: they are not), this file should read:
# answers = {'alg_0': 'bubble',
#                 'alg_1': 'bubble',
#                 'alg_2': 'bubble',
#                 'alg_3': 'bubble',
#                 'alg_4': 'bubble'}

# Fill in your answers as the values in the dict below
answers = {'alg_0': '',
           'alg_1': '',
           'alg_2': '',
           'alg_3': '',
           'alg_4': ''
          }

possible_ans = ['bubble', 'selection', 'insertion', 'mergesort', 'quicksort']
# Run this file in terminal to see if you used the correct formatting in your answer.
for k, v in answers.items():
    if v not in possible_ans:
        raise ValueError(f"Value '{v}' for key '{k}' is not 'bubble', 'selection', 'insertion', 'mergesort', or 'quicksort''")

print("Acceptable answer! Find out if it's right after the due date.")