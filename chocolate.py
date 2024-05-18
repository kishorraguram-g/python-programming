"""def distribute_chocolates_equally(chocolates, people):
    if people == 0:
        return "Number of people cannot be zero."
    
    chocolates_per_person = chocolates // people
    remaining_chocolates = chocolates % people
    
    distribution = [chocolates_per_person] * people  # Everyone gets an equal share
    distribution[0] += remaining_chocolates  # Add any remaining chocolates to the first person
    
    return distribution

# Example usage
total_chocolates = 97
total_people = 5
print(distribute_chocolates_equally(total_chocolates, total_people))
"""





































def distribute_chocolates_by_performance(chocolates, scores):
    total_score = sum(scores)
    if total_score == 0:
        return "Total score cannot be zero."
    
    factor = chocolates / total_score
    distribution = [round(score * factor) for score in scores]
    
    return distribution

# Example usage
scores = [10, 22, 30]
total_chocolates = 50
print(distribute_chocolates_by_performance(total_chocolates, scores))

































"""
import random
def distribute_chocolates_randomly(chocolates, people):
    distribution = [0] * people
    for _ in range(chocolates):
        person = random.randint(0, people - 1)
        distribution[person] += 1
    
    return distribution

# Example usage
total_chocolates = 100
total_people = 5
print(distribute_chocolates_randomly(total_chocolates, total_people))

"""
