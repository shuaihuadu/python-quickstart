# sum = 1 + 2
# product = sum * 2
# print(product)
# print("show this in the console")

# plants_in_solar_system = 8
# distance_to_alpha_centauri = 4.367
# can_liftoff = True
# shuttle_landed_on_the_moon = "Apollo 11"
# type(distance_to_alpha_centauri)

# from datetime import date
# print(date.today())
# print("Today's date is: " + str(date.today()))

# parsecs = 11
# lightyears = parsecs * 3.26
# print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

# 命令行输入
# import sys
# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])

# 使用数字
# print("calculator program")
# first_number = input("first number:")
# second_number = input("second number:")
# print(first_number + second_number)
# print(int(first_number) + int(second_number))

# print("1" + 2)

# 使用布尔逻辑
# a = 97
# b = 55
# if a < b:
#     print(b)
# elif a == b:
#     print(0)
# else:
#     print(a)


# if a == 9 or b == 55:
#     print(b)

# if a == 10 and b == 55:
#     print(a)

# 字符串
# fact = "The Moon has no atmosphere."

# print(fact)

# moon_radius = 'The "Near side" is the part of the Moon that faces the Earth.'

# print(moon_radius)

# moon_radius = "We only see about 60% of the Moon's surface."

# print(moon_radius)

# moon_radius = (
#     """We only see about 60% of the Moon's surface, this is known as the "near side"."""
# )
# print(moon_radius)

# multiline = "Facts about the Moon:\n There is no atomsphere.\n There is no sound."
# print(multiline)


# multiline = """Facts about the Moon:
#  There is no atomsphere.
#  There is no sound."""

# print(multiline)

# print("temperatures and facts about the moon".title())


# heading = "temperatures and facts about the moon"

# heading_upper = heading.title()

# print(heading_upper)

# temperatures = "Daylight: 260 F\n Nighttime: -280 F"

# temperatures_list = temperatures.split("\n")

# print(temperatures_list)


# print("Moon" in "This text will describe facts and challenges with space travel")
# print("Moon" in "This text will describe facts about the Moon")

# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Moon"))
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.find("Mars"))
# temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
# print(temperatures.count("Mars"))
# print(temperatures.count("Moon"))
# temperatures = "Mars Average Temperature: -60 C"
# parts = temperatures.split(":")
# print(parts)
# print(parts[-1])

# mars_temperature = "The highest temperature on Mars is about 30 C"
# for item in mars_temperature.split():
#     if item.isnumeric():
#         print(item)
# print("-60".startswith("-"))
# if "30 C".endswith("C"):
#     print("This temperature is in Celsius")

# print(
#     "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace(
#         "Celsius", "C"
#     )
# )

# text = "Temperatures on the Moon can vary wildly."
# print("temperatures" in text)

# text = "Temperatures on the Moon can vary wildly."
# print("temperatures" in text.lower())

# moon_facts = [
#     "The Moon is drifting away from the Earth.",
#     "On average, the Moon is moving about 4cm every year.",
# ]
# print(" ".join(moon_facts))

# mass_percentage = "1/6"
# print(
#     "On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage
# )

# print(
#     """Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s."""
#     % ("Moon", "Earth", "Moon", "Earth")
# )

# mass_percentage = "1/6"
# print(
#     "On the Moon, you would weigh about {0} of your weight on Earth.".format(
#         mass_percentage
#     )
# )

# print(
#     """You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format(
#         "Moon", mass_percentage
#     )
# )

# mass_percentage = "1/6"
# print(
#     """You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(
#         moon="Moon", mass=mass_percentage
#     )
# )

# mass_percentage = "1/6"
# print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
# print(round(100 / 6, 1))
# print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

# subject = "interesting facts about the moon"
# heading = f"{subject.title()}"
# print(heading)

# 数学计算
# seconds = 1042

# display_minutes = 1042 // 60

# print(display_minutes)

# display_minutes = 1042 % 60

# print(display_minutes)

# 列表

# planets = [
#     "Mercury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune",
# ]
# print("The first planet is", planets[0])
# print("The second planet is", planets[1])
# print("The third planet is", planets[2])


# planets[3] = "Red Planet"
# print("Mars is also known as", planets[3])

# number_of_planets = len(planets)
# print("There are", number_of_planets, "planets in the solar system.")

# planets.append("Pluto")
# number_of_planets = len(planets)
# print("There are actually", number_of_planets, "planets in the solar system.")

# planets.pop()
# number_of_planets = len(planets)
# print("No, there are definitely", number_of_planets, "planets in the solar system.")

# print("The last planet is", planets[-1])
# print("The penultimate planet is", planets[-2])

# jupiter_index = planets.index("Jupiter")
# print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
# bus_weight = 124054  # in Newtons, on Earth

# print("On Earth, a double-decker bus weighs", bus_weight, "N")
# print(
#     "The lightest a bus would be in the solar system is",
#     bus_weight * min(gravity_on_planets),
#     "N",
# )
# print(
#     "The heaviest a bus would be in the solar system is",
#     bus_weight * max(gravity_on_planets),
#     "N",
# )

# planets = [
#     "Mercury",
#     "Venus",
#     "Earth",
#     "Mars",
#     "Jupiter",
#     "Saturn",
#     "Uranus",
#     "Neptune",
# ]
# planets_before_earth = planets[0:2]
# print(planets_before_earth)
# planets_after_earth = planets[3:]
# print(planets_after_earth)

# amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
# galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

# regular_satellite_moons = amalthea_group + galilean_moons
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# regular_satellite_moons.sort()
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# regular_satellite_moons.sort(reverse=True)
# print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# 使用“while”和“for”循环
# user_input = ""

# while user_input.lower() != "done":
#     user_input = input("Enter a new value, or done when done")

# user_input = ""

# inputs = []

# while user_input.lower() != "done":
#     if user_input:
#         inputs.append(user_input)

#     print(inputs)

#     user_input = input("Enter a new value, or done when done")

# from time import sleep

# countdown = [4, 3, 2, 1, 0]

# for number in countdown:
#     print(number)
#     sleep(1)  # Wait 1 second
# print("Blast off!! 🚀")

# 使用字典
# planet = {"name": "Earth", "moons": 1}

# print(planet.get("name"))
# print(planet["name"])

# planet.update({"name": "Makemake"})
# print(planet.get("name"))

# planet["name"] = "Jupiter"
# print(planet.get("name"))

# planet["orbital period"] = 4333
# print(planet.get("orbital period"))

# planet.pop("orbital period")
# print(planet.get("orbital period"))
# print(plant["orbital period"])


# planet["diameter (km)"] = {"polar": 133709, "equatorial": 142984}

# print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')

# for key in planet.keys():
#     print(f"{key}: {planet[key]}")

# if "key1" in planet:
#     planet["key1"] = planet["key1"] + 1
# else:
#     planet["key1"] = 1

# for value in planet.values():
#     print(value)


# 函数
# def rocket_parts():
#     return "payload, propellant, structure"


# output = rocket_parts()

# print(output)

# any = any([True, False, False])
# print(any)

# any = any([False, False, False])
# print(any)


# def distance_from_earth(destination):
#     if destination == "Moon":
#         return "238,855"
#     else:
#         return "Unable to compute to that destination"


# print(distance_from_earth("Moon"))

# print(distance_from_earth("Saturn"))


# def days_to_complete(distance, speed):
#     hours = distance / speed
#     return hours / 24


# total_days = days_to_complete(238855, 75)

# print(round(total_days))
# print(round(days_to_complete(238855, 75)))


# from datetime import timedelta, datetime


# def arrival_time(hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime("Arrival: %A %H:%M")


# print(arrival_time())
# print(arrival_time(hours=0))


# def arrival_time(destination, hours=51):
#     now = datetime.now()
#     arrival = now + timedelta(hours=hours)
#     return arrival.strftime(f"{destination} Arrival: %A %H:%M")


# print(arrival_time("Moon"))
# print(arrival_time("Orbit", hours=0.13))


# def variable_length(*args):
#     print(args)


# variable_length()
# variable_length("one", "two")
# variable_length(None)


# def sequence_time(*args):
#     total_minutes = sum(args)
#     if total_minutes < 60:
#         return f"Total time to launch is {total_minutes} minutes"
#     else:
#         return f"Total time to launch is {total_minutes/60} hours"


# print(sequence_time(4, 14, 18))
# print(sequence_time(4, 14, 48))


# def variable_length(**kwargs):
#     print(kwargs)


# variable_length(tanks=1, day="Wednesday", pilots=3)


# def crew_members(**kwargs):
#     print(f"{len(kwargs)} astronauts assigned for this mission:")
#     for title, name in kwargs.items():
#         print(f"{title}: {name}")


# crew_members(
#     captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"
# )


# 引发异常
# def water_left(astronauts, water_left, days_left):
#     daily_usage = astronauts * 11
#     total_usage = daily_usage * days_left
#     total_water_left = water_left - total_usage
#     if total_water_left < 0:
#         raise RuntimeError(
#             f"There is not enough water for {astronauts} astronauts after {days_left} days!"
#         )
#     return f"Total water left after {days_left} days is: {total_water_left} liters"


# # water_left(5, 100, 2)
# water_left("3", "200", None)
def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type
            # Raise the same exception but with a better error message
            raise TypeError(
                f"All arguments must be of type int, but received: '{argument}'"
            )
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(
            f"There is not enough water for {astronauts} astronauts after {days_left} days!"
        )
    return f"Total water left after {days_left} days is: {total_water_left} liters"


water_left("3", "200", None)
