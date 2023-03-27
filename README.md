# DeepPavlov Dream

**Arabic distribution**
This distribution consists of **dff-arabic-greeting-skill**, **ar-odqa** service, and **dff-ar-odqa-skill**.
For Open-Domain Question Answering model we trained SQuAD model on [Arabic Question Answering Datasets](https://github.com/WissamAntoun/Arabic_QA_Datasets) using [BERT multilingual base model (cased)](https://huggingface.co/bert-base-multilingual-cased), and TF-IDF ranker and reader for Wikipedia texts.


# Quick Start

### Clone the repo

```
https://github.com/Kpetyxova/dream_ar.git
```

### Switch the branch

```
git checkout add/arabic_dist
```

### Install [docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/)

If you get a "Permission denied" error running docker-compose, make sure to [configure your docker user](https://docs.docker.com/engine/install/linux-postinstall/) correctly.

### Run the distribution


```
docker-compose -f docker-compose.yml -f assistant_dists/dream_arabic/docker-compose.override.yml -f assistant_dists/dream_arabic/dev.yml up --build
```

### Let's chat

DeepPavlov Agent provides several options for interaction: a command line interface, an HTTP API, and a Telegram bot 

#### CLI

In a separate terminal tab run:

```
docker-compose exec agent python -m deeppavlov_agent.run agent.channel=cmd agent.pipeline_config=assistant_dists/dream_arabic/pipeline_conf.json
```

Enter your username and have a chat with Dream!

#### HTTP API

Once you've started the bot, DeepPavlov's Agent API will run on `http://localhost:4242`.
You can learn about the API from the [DeepPavlov Agent Docs](https://deeppavlov-agent.readthedocs.io/en/latest/intro/overview.html#http-api-server).

A basic chat interface will be available at `http://localhost:4242/chat`.

#### Telegram Bot
Currently, Telegram bot is deployed **instead** of HTTP API.
Edit `agent` `command` definition inside `docker-compose.override.yml` config:
```
agent:
  command: sh -c 'bin/wait && python -m deeppavlov_agent.run agent.channel=telegram agent.telegram_token=<TELEGRAM_BOT_TOKEN> agent.pipeline_config=assistant_dists/dream_arabic/pipeline_conf.json'
```
**NOTE:** treat your Telegram token as a secret and do not commit it to public repositories!

                                                                                         

# License

DeepPavlov Dream is licensed under Apache 2.0.

Program-y (see `dream/skills/dff_program_y_skill`, `dream/skills/dff_program_y_wide_skill`, `dream/skills/dff_program_y_dangerous_skill`)
is licensed under Apache 2.0.
Eliza (see `dream/skills/eliza`) is licensed under MIT License.
