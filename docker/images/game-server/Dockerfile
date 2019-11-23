FROM dms1920-base:latest

VOLUME /tmp
VOLUME /tmp/src
VOLUME /tmp/data

ADD scripts /tmp/scripts
RUN chmod a+x /tmp/scripts/*
RUN pip3 install requests numpy

ENTRYPOINT [ "/tmp/scripts/bootstrap.sh" ]
