# RiftReport

#### Video Demo: <https://youtu.be/vriuB3u5BQ8>

#### Description

RiftReport is a Python application that analyzes a League of Legends player's profile using the Riot Games API. The program allows users to enter a Riot ID and a server, then automatically retrieves information about the player's ranked status, champion mastery, and recent match history. Using these data, the application calculates useful statistics such as winrate, average KDA, and the champion with the highest KDA over the last ten games.

I decided to build this project because League of Legends is a game I have played for years, and I wanted to create something related to a topic I genuinely enjoy. At the same time, I wanted a project that would push me beyond the basics covered in CS50P. Working with a real-world API seemed like a perfect opportunity to learn how applications communicate with external services and how JSON data can be processed in Python.

## How the program works

The application begins by asking the user for two pieces of information:

- Riot ID in the format `GameName#TAG`
- League of Legends server (for example `eun1` or `euw1`)

The Riot ID is split into the game name and tagline, since these are required by Riot's Account API.

Using this information, the program sends a request to Riot's servers and retrieves the player's account information, including the unique player identifier (`PUUID`). The PUUID is essential because almost every other Riot API endpoint uses it instead of the player's nickname.

Once the PUUID has been obtained, the application performs several independent API requests:

- retrieves the player's Solo Queue rank,
- downloads the player's three highest champion masteries,
- fetches the IDs of the last ten matches,
- downloads detailed information for each match.

The Riot API returns champion IDs rather than champion names. To solve this, the application downloads Riot's Data Dragon champion database and creates a dictionary that maps champion IDs to readable champion names. This makes the final report much easier to understand.

After collecting all required data, the application extracts only the selected player's statistics from each match and calculates:

- overall winrate,
- average KDA,
- the champion on which the player achieved the highest KDA.

Finally, all information is formatted into a clean report displayed in the terminal.

## Design choices

One of the most important design decisions was dividing the program into many small functions instead of writing everything inside `main()`. Every function has a single responsibility.

For example:

- `fetch_account()` only retrieves account information.
- `fetch_rank()` only downloads ranked information.
- `calculate_winrate()` only performs calculations.
- `display_report()` is responsible only for formatting the output.

This approach makes the code much easier to read, test, and extend in the future.

Another design decision was separating data collection from data analysis. Functions beginning with `fetch_` are responsible for communicating with Riot's API, while functions such as `calculate_average_kda()` or `find_best_kda_champion()` work only on already downloaded data. This separation improves readability and follows the principle that each function should have a single responsibility.

## Challenges

The biggest challenge during this project was understanding how REST APIs work.

Before starting the project I had never worked with an external API, so concepts such as HTTP requests, JSON responses, endpoints, and API authentication were completely new to me. Learning how different Riot API endpoints connect with each other was probably the most difficult part of the project.

Another challenge was Riot's routing system. Some endpoints require a platform routing value such as `euw1`, while Match-V5 endpoints require regional routing values like `europe` or `americas`. To solve this problem I implemented the `server_to_region()` helper function, which automatically maps platform servers to the correct regional endpoint.

I also needed to convert champion IDs into champion names. Since Riot only returns numeric champion IDs in the Champion Mastery endpoint, I decided to use Riot's Data Dragon service to build a dictionary that translates IDs into readable names.

Finally, I had to handle situations where invalid data is entered or the Riot API cannot find the requested player. In these cases the program exits gracefully with an appropriate error message instead of crashing unexpectedly.

## Requirements

Before running the application, a Riot Games API key is required.

Create a `.env` file in the project directory containing:

```text
RIOT_API_KEY=your_api_key_here
```

Install the required libraries:

```bash
pip install requests python-dotenv
```

Then simply run:

```bash
python project.py
```

or

```bash
py project.py
```

depending on your Python installation.

## Libraries used

This project uses the following libraries:

- `requests` for sending HTTP requests to Riot's API.
- `python-dotenv` for loading the API key from an environment file.
- `os` for accessing environment variables.
- `sys` for terminating the program when invalid input or API errors occur.

## Future improvements

Although the project fulfills its intended purpose, there are many features that could be added in the future.

Possible improvements include:

- graphical user interface,
- support for additional statistics such as CS per minute or vision score,
- champion performance comparison,
- exporting reports to a text or PDF file,
- caching API responses to reduce unnecessary API requests,
- allowing users to analyze more than the last ten matches.

Overall, this project taught me much more than just Python syntax. It introduced me to working with real-world APIs, processing JSON data, organizing code into reusable functions, and designing a complete application from start to finish.