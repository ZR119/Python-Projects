# Python-Projects
My favorite projects from ap csp

Project 1: nicknames
A smart, lightweight Python application that recommends music bands based on user input. Whether you feed it your favorite genres, specific musical attributes (tempo, mood, era), or existing bands you love, this engine analyzes the characteristics and outputs personalized recommendations to expand your sonic horizons.

### 🚀 Features
* **Multi-Criteria Matching:** Recommend bands based on sub-genres, moods, acoustic traits, or historical eras.
* **Similarity Scoring:** Uses vector distance / text similarity models to find the closest matches to your favorite artists.
* **Extensible Database:** Easily add or update band profiles via a structured JSON/CSV data layer.
* **Interactive CLI:** A simple, intuitive command-line interface for rapid discovery.

### 💻 Usage Example
```text
[?] Enter a band you like, or a style (e.g., '90s grunge, fast tempo, melancholic'): 
> Tool, atmospheric, heavy riffs

[!] Analyzing sonic profiles...

🎯 Top 3 Recommendations for you:
1. ISIS (Post-Metal) - Match Score: 94%
   👉 Why: Shares deep, atmospheric arrangements and progressive, heavy guitar riffs.
2. Soen (Progressive Metal) - Match Score: 89%
   👉 Why: Heavily inspired by intricate polyrhythms and clean, emotive vocal delivery.
3. Karnivool (Alternative Progressive) - Match Score: 87%
   👉 Why: Dynamic shifts between atmospheric melodies and complex heavy rhythmic structures.

Project 2: pokemon
A classic, 2D turn-based monster battling game inspired by retro Pokémon mechanics. Built using clean, modular code, this project serves as a foundational engine for turn-based combat, party management, and elemental type-matching mechanics.

### 🚀 Features
* **Turn-Based Battle System:** Fully functional turn loop (Fight, Bag, Switch, Run) with speed-based move order calculations.
* **Elemental Type Advantages:** Complete type-matching matrix (e.g., Fire beats Grass, Water beats Fire) including critical hits and damage modifiers.
* **Creature Stat Progression:** Experience point (XP) scaling, leveling up, and proportional stat increases (HP, Attack, Defense, Speed).
* **Stat-Changing Moves & Status Effects:** Moves that buff/debuff stats or inflict status alignments like Burn, Paralysis, or Sleep.

### 🎮 Battle Gameplay Example
```text
--------------------------------------------------
WILD FLARION APPEARED! (Lv. 14)
--------------------------------------------------
Go! AQUATERRA (Lv. 15) [HP: 45/45]

What will AQUATERRA do?
1. FIGHT      2. POKÉMON
3. BAG        4. RUN

> 1

Choose a move:
1. Hydro Pump [WATER] - 10/10 PP
2. Tackle     [NORMAL] - 35/35 PP

> 1

--------------------------------------------------
AQUATERRA used Hydro Pump!
It's super effective!
Wild FLARION took 32 damage!

Project 3: preds
### 🇺🇸 US Presidents Information API & CLI

A comprehensive Python utility and data engine that provides instant access to detailed historical data, timelines, political affiliations, and key milestones for every United States President from George Washington onwards. 

This project works perfectly as a local command-line reference tool, an educational script, or a micro-backend for history applications.

### 🚀 Features
* **Complete Historical Database:** Includes structural data for all 47 presidencies—covering full names, terms in office, political parties, vice presidents, key historical events, and lifespans.
* **Advanced Querying & Filtering:** Filter presidents easily by political party, century, state of birth, or specific historical milestones.
* **Chronological Timelines:** Generate clean, ordered lists or search for specific succession orders (e.g., "Who was the 16th president?").
* **JSON Export/Integration:** Built with a clean data separation layer, making it trivial to extract JSON data or hook it up to a web API.

### 🔍 Usage Examples
```text
$ python query_presidents.py --number 16

==================================================
16th PRESIDENT OF THE UNITED STATES
==================================================
Name:          Abraham Lincoln
Term:          March 4, 1861 – April 15, 1865
Party:         Republican / National Union
Vice Pres:     Hannibal Hamlin, Andrew Johnson
Birth State:   Kentucky

Key Events:
- Presided over the American Civil War
- Issued the Emancipation Proclamation (1863)
==================================================

Project 4: race
### 🐢 The Tortoise and the Hare Simulation Engine 🐇

An interactive, algorithm-driven simulation of the classic Aesop's fable, *The Tortoise and the Hare*. Written in Python, this project uses probabilistic modeling and tick-based event handling to simulate the famous race, complete with random events (like the Hare taking a nap or the Tortoise finding a steady rhythm). 

It serves as an engaging educational tool for understanding state machines, random distributions, and game loop design.

### 🚀 Features
* **Dynamic Race Mechanics:** Tick-by-tick simulation where the Tortoise and Hare have different speed baselines, burst mechanics, and fatigue thresholds.
* **Stochastic (Random) Events:**
  * The Hare has a high chance of sprinting ahead, but a randomized risk of falling asleep if its lead gets too large.
  * The Tortoise moves slowly but consistently, with occasional "steady determination" bursts that slightly elevate its baseline speed.
* **Real-time Terminal Track Animation:** A visual ASCII-art racetrack updates live in your console to display their positions side-by-side.
* **Configurable Parameters:** Easily adjust track length, nap probabilities, terrain factors, and base speeds via a configurations layer.

### 🏁 Terminal Live-View Example
```text
==================================================
        THE GREAT RACE IS UNDERWAY!
==================================================
Track Length: 50 meters
[Tick 18]

🐢 Tortoise: [-------------------🐢------------------------] (19m)
🐇 Hare:     [-------------------------💤------------------] (25m)

[STATUS] The Hare is overconfident and has fallen asleep!
[STATUS] The Tortoise keeps moving forward with a steady pace.
--------------------------------------------------

project 5: weather
### 🧥 Smart Wardrobe Advisor (Weather-to-Wear Engine)

A hyper-localized, rules-based context engine that analyzes the current outdoor temperature (and secondary weather factors like wind chill or precipitation) to recommend the optimal outfit combinations. No more stepping outside under-dressed or overheating—this script ensures you pick the perfect layers every single time.

### 🚀 Features
* **Temperature-Tiered Logic:** Dynamically categorizes weather into 5 structural profiles (Freezing, Crisp, Mild, Warm, Scorching) to deliver precise layering advice.
* **Secondary Modifier Index:** Factors in rain/snow status, wind speeds, and activity levels to append necessary accessories (umbrellas, windbreakers, thermal socks).
* **API or Manual Input Modes:** Can be run completely standalone via a CLI manual prompt, or integrated with an OpenWeatherMap API key to fetch real-time live metrics.
* **Highly Customizable Manifest:** Outfits and thresholds are separated cleanly into a config layer, allowing you to tailor recommendations to your personal tolerance for cold or heat.

### 🧣 Example CLI Interaction
```text
$ python advisor.py --temp 42 --unit F --rain True

[🔍] Processing meteorological data...
--------------------------------------------------
🌡️  CURRENT WEATHER ANALYSIS
--------------------------------------------------
Temperature: 42°F (5.5°C)
Classification: Crisp / Chili
Precipitation: Active Rain

👔 RECOMMENDED WARDROBE MANIFEST:
Top Layer:     Waterproof Rain Jacket / Trenchcoat
Base Layer:    Heavy knit sweater or long-sleeve thermal
Bottoms:       Thick denim jeans or chinos
Footwear:      Water-resistant leather boots or rain boots

🎒 OPTIONAL ACCESSORIES:
- Compact Umbrella (Required: Rain detected)
--------------------------------------------------
