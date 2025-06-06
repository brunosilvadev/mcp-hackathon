# rules.py

RULES = {
    "judo": [
        {
            "keyword": "leg grab",
            "aliases": ["touching the leg", "grabbed the leg", "leg penalty"],
            "explanation": "Touching or grabbing an opponent’s leg is prohibited in judo and will result in a penalty ('Shido')."
        },
        {
            "keyword": "ippon",
            "aliases": ["full point", "thrown on back", "ending throw"],
            "explanation": "An Ippon is scored when a competitor throws their opponent onto their back with force and control, ending the match immediately."
        },
        {
            "keyword": "golden score",
            "aliases": ["overtime", "sudden death", "tie breaker"],
            "explanation": "If a judo match is tied after regular time, it goes into 'Golden Score'—the first to score any point wins."
        }
    ],
    "handball": [
        {
            "keyword": "goal area",
            "aliases": ["box", "crease", "inside the area", "in the box", "goal box", "six-meter line"],
            "explanation": "Only the goalkeeper is allowed in the goal area (aka 'the box'). Field players cannot step into or touch the goal area."
        },
        {
            "keyword": "passive play",
            "aliases": ["stalling", "time wasting", "not attacking"],
            "explanation": "Teams must attempt to attack; stalling (passive play) can be penalized by referees."
        },
        {
            "keyword": "dribble fault",
            "aliases": ["double dribble", "traveling", "steps", "walk"],
            "explanation": "Double dribbling or taking more than three steps without dribbling results in a turnover."
        }
    ],
    "modern pentathlon": [
        {
            "keyword": "laser run",
            "aliases": ["shooting and running", "run and shoot"],
            "explanation": "The Laser Run combines running and shooting. Athletes must complete several laps, stopping to hit targets with a laser pistol."
        },
        {
            "keyword": "fencing bonus",
            "aliases": ["sudden death fencing", "bonus round"],
            "explanation": "The fencing bonus round allows athletes to score extra points with single-bout sudden death matches."
        },
        {
            "keyword": "swimming penalty",
            "aliases": ["time penalty", "slow swimming"],
            "explanation": "Exceeding the designated swimming time adds penalty seconds to an athlete’s total time."
        }
    ],
    "table tennis": [
        {
            "keyword": "edge ball",
            "aliases": ["edge shot", "corner ball"],
            "explanation": "If the ball hits the edge of the table during play, it is considered in and the rally continues."
        },
        {
            "keyword": "let serve",
            "aliases": ["net serve", "replay serve"],
            "explanation": "A serve that touches the net but lands in the correct box is called a 'let' and is replayed."
        },
        {
            "keyword": "service toss",
            "aliases": ["throw up serve", "toss serve", "serve height"],
            "explanation": "When serving, the ball must be tossed at least 16cm vertically before being struck."
        }
    ],
    "water polo": [
        {
            "keyword": "ordinary foul",
            "aliases": ["minor foul", "regular foul"],
            "explanation": "Ordinary fouls are common and result in a free throw for the opposing team."
        },
        {
            "keyword": "exclusion foul",
            "aliases": ["major foul", "kick out", "player ejected"],
            "explanation": "For major infractions, a player receives an exclusion foul and must leave the pool for 20 seconds."
        },
        {
            "keyword": "goalkeeper",
            "aliases": ["keeper out of box", "goalie scored", "goalie half line"],
            "explanation": "Goalkeepers cannot cross the half-line or attempt to score a goal."
        }
    ]
}
