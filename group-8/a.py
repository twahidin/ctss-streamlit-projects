
import json

data = {
    "11/05/2026": {
        "1": {
            "1": {
                "movie": "Night of the Day of the Dawn of the SOn of the Bride of the Return of the Revenge of the Terror of the Attack of the Evil, Mutant, Alien, Flesh Eating, Hellbound, Zombiefied Living Dead Part 2: In shocking 2D",
                "seats": {
                    "A": [0, 0, 0],
                    "B": [0, 0, 0],
                    "C": [0, 0, 0]
                }
            },
            "image_link": "https://images.pexels.com/photos/28344947/pexels-photo-28344947.jpeg"
        }
    },
    "ADMINS": {
        "ADMIN": "1234",
        "KOSHER": "5678"
    },
    "MEMBERS": {
        "JOHN": {"password": "0000", "tickets": [], "birth date": "01/01/2000", "email": "NaN"},
        "DOE": {"password": "1111", "tickets": [], "birth date": "02/02/2000", "email": "NaN"}
    }
}

with open("file.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

