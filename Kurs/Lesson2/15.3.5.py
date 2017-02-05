# 5. Страны и города
# Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.

Countries = dict(zip(["Minsk", "Krakov", "London", "Chicago", "Rome", "Murmansk", "Erevan", "Kaliningrad"],
                  ["Belarus", "Poland", "England", "USA", "Italy", "Russia", "Armenia", "Russia"]))
for key in Countries.keys():
    print(key + " is located in " + Countries.get(key))
