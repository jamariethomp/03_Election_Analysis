# counties = ["Arapahoe","Denver","Jefferson"]
# for county in range(len(counties)):
#     print(counties[county])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
    # print(county + " county has " + str(voters) + " registered voters.")
    # print(f"{county} County has {voters:,} registered voters.")
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
for i in range(len(voting_data)):
    county = voting_data[i]["county"]
    votes = voting_data[i]["registered_voters"]
    print(f"{county} county has {votes:,} registered voters.")
#print(voting_data[1]["registered_voters"])
# for county_dict in voting_data:
#     print(county_dict['county'])