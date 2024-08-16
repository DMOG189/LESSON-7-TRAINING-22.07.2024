# TRAINING 4 COMPLEX LOOP B


# COMPLEX LOOP:

# 2. United Nations Voting Simulation

# START

# 2. United Nations Voting Simulation:

votes = []
votes_in_favor = 0
votes_against = 0
abstentions = 0
veto_detected = False

print("Enter the topic of the vote:")
topic = input()

print("Enter the votes (1 for In Favor, 2 for Against, 3 for Abstain, 4 for Veto):")

first_in_favor = None
last_against = None

for i in range(44):
    while True:
        try:
            vote = int(input(f"Enter the vote for country {i + 1}: "))

            if vote not in [1, 2, 3, 4]:
                print("Invalid vote. Please enter a number between 1 and 4.")
                continue

            votes.append(vote)

            if vote == 1:
                votes_in_favor += 1
                if first_in_favor is None:
                    first_in_favor = i + 1
            elif vote == 2:
                votes_against += 1
                last_against = i + 1
            elif vote == 3:
                abstentions += 1
            elif vote == 4:
                print(f"Veto detected by country {i + 1}. Voting stopped.")
                veto_detected = True
                break

            break

        except ValueError:
            print("Invalid input, please enter a numeric value.")

    if veto_detected:
        break

print("\nVoting Results:")
print(f"Votes in favor: {votes_in_favor}")
print(f"Votes against: {votes_against}")
print(f"Abstentions: {abstentions}")

if first_in_favor:
    print(f"The first country to vote in favor was country {first_in_favor}.")
if last_against:
    print(f"The last country to vote against was country {last_against}.")

# END