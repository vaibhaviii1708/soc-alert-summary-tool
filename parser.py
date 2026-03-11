import json
from collections import Counter

alert_types = []
levels = []
agents = []

with open("alerts.json", "r") as file:
    for line in file:
        try:
            alert = json.loads(line)

            if "rule" in alert:
                alert_types.append(alert["rule"]["description"])
                levels.append(alert["rule"]["level"])

            if "agent" in alert:
                agents.append(alert["agent"]["name"])

        except:
            continue


print("\nSOC ALERT SUMMARY\n")

print("Total Alerts:", len(alert_types))


print("\nTop Alert Types:")
for alert, count in Counter(alert_types).most_common(5):
    print(alert, "-", count)


print("\nAlert Severity Levels:")
for level, count in Counter(levels).most_common():
    print("Level", level, "-", count)


print("\nAlerts per Agent:")
for agent, count in Counter(agents).most_common():
    print(agent, "-", count)
