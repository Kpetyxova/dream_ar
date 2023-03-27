# FROM python:3.9.1
# RUN pip install --upgrade pip && pip install git+https://github.com/Kpetyxova/DeepPavlov.git

# ARG CONFIG
# ARG PORT
# ARG SED_ARG=" | "

# ENV CONFIG=$CONFIG
# ENV PORT=$PORT


# COPY ./requirements.txt /src/requirements.txt
# RUN pip install -r /src/requirements.txt

# COPY . /src

# WORKDIR /src

# CMD gunicorn --workers=1 server:app -b 0.0.0.0:8139 --timeout 500


FROM python:3.9.1
# ###################### IMMUTABLE SECTION ######################################
# Do not change anything in this section 
WORKDIR /src

# ###################### CUSTOM SECTION ######################################
# Here you can make changes 

ARG SERVICE_NAME
ENV SERVICE_NAME ${SERVICE_NAME}

COPY services/${SERVICE_NAME}/requirements.txt .
RUN pip install -r requirements.txt
RUN pip install git+https://github.com/Kpetyxova/DeepPavlov.git

COPY services/${SERVICE_NAME}/ ./

ARG SERVICE_PORT
ENV SERVICE_PORT ${SERVICE_PORT}
ARG CONFIG
ENV CONFIG ${CONFIG}

# wait for a server answer ( INTERVAL + TIMEOUT ) * RETRIES seconds after that change stutus to unhealthy
# HEALTHCHECK --interval=5s --timeout=5s --retries=3 CMD curl --fail 127.0.0.1:${SERVICE_PORT}/healthcheck || exit 1


CMD gunicorn --workers=1 server:app -b 0.0.0.0:${SERVICE_PORT}
