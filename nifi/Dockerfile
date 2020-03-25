FROM apache/nifi

USER root

RUN apt-get install python -y
RUN apt-get install host -y
RUN apt-get install net-tools -y
RUN apt-get install telnet

ENV PATH="/opt/nifi/nifi-toolkit-1.11.1/bin:${PATH}"

RUN mkdir -p /opt/nifi/nifi-current/dependencies
RUN chown nifi:nifi /opt/nifi/nifi-current/dependencies

COPY --chown=nifi:nifi ./dependencies/flow.xml.gz /opt/nifi/nifi-current/conf
COPY --chown=nifi:nifi ./dependencies/bootstrap.conf /opt/nifi/nifi-current/conf

COPY --chown=nifi:nifi ./dependencies/gcp-poc-256203-ecfe5e053d80.json /opt/nifi/nifi-current/dependencies

USER nifi