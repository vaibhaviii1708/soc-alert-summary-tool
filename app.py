from flask import Flask, render_template
import json
from collections import Counter

app = Flask(__name__)

def analyze_alerts():

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

    return {
        "total": len(alert_types),
        "top_alerts": Counter(alert_types).most_common(5),
        "levels": Counter(levels),
        "agents": Counter(agents)
    }


@app.route("/")
def dashboard():

    data = analyze_alerts()

    return render_template(
        "dashboard.html",
        total=data["total"],
        alerts=data["top_alerts"],
        levels=data["levels"],
        agents=data["agents"]
    )


if __name__ == "__main__":
    app.run(debug=True)
