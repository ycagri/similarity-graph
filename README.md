# Similarity Graph Creator

This is a simple similarity graph creator using `OpenAi` and `GraphCommons` apis. Inspired by Yigitalp Ertem's blog[https://yalpertem.com/blog/2023/01/05/500-film-directors-in-a-graph-i-chatgpt/], I decided to create a more generic and automated version. In order to run the scripts, you have to get an `OpenAI` api key from [here](https://platform.openai.com/) and create an account using email and password on [GraphCommons](https://graphcommons.com/).

The way script works:
1 - Sends general prompt to OpenAi GPT such as `I want you to list me 100 historical battles all around the world. I just want the names line by line, no extra text, no number or bullet in the beginning.`.
2 - Sends another prompt for each line recieved from the previous step such as `Now forget everything and give me 5 similar battles to Battle of Cannae. I just want the names line by line, no extra text, no number or bullet in the beginning.`.
3 - Creates a graph using [GraphCommons](https://graphcommons.com/) api.

[Here](https://graphcommons.com/graphs/94e785c8-cf2e-4fb0-aac1-2b1ad014f026) is the sample output graph.

## Setup Environment

- Install Python
- Install `virtualenv`: `pip install virtualenv`
- Create a virtual environment: `virtualenv env`
- Start virtual environment: `source env/bin/activate`
- Install requirements: `pip3 install -r requirements.txt`
- In order to use apis, create `.env` file in the root directory. Please see [.env.example](./.env.example) file for the format.


## Run Scripts

Script has four parameters:
- `name`: A name for the graph. This name is also used to create a directory and files for the answers received from OpenAI.
- `description`: A brief description for the graph.
- `skip_prompt`: This option is defined to skip OpenAI prompt file and run graph generation using previously created answer file.
- `question_file`: A simple json file contains just two keys: `general` and `similarity`. `general` contains the first question generate some amount of data. `similarity` is used to get similar suggestions for the generated data. This file has to be created in `files` directory. Please see [battle.json](./files/battle.json).

Here is the sample runs:
- `python3 main.py --name battle --description "A similarity graph for historical battles" --question_file files/battle.json`
- `python3 main.py --name battle --description "A similarity graph for historical battles" --skip_promt`
