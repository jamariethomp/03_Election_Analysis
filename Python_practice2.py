#counties = ["Arapahoe","Denver","Jefferson"]
# if "Arapahoe" in counties or "El Paso" in counties:
#     print("Arapahoe or El Paso is in the list of counties")
# else:
#     print("Arapahoe or El Paso is not in the list of counties")

# if "Arapahoe" in counties and "El Paso" not in counties:
#     print("Only Arapahoe is in the list of counties")
# else:
#     print("Arapahoe is in the list of counties but Else Paso is not")
# for county in counties:
#     print(county)
# numbers = [0, 1, 2, 3, 4]
# for i in range(len(counties)):
#     print(counties[i])
#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():
#     print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

# for i in range(len(voting_data)):
#     print(voting_data[i]['county'])

for county_dict in voting_data:
    print(county_dict["county"])
