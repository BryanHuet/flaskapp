FROM debian:bookworm

ENV APACHE_RUN_USER=www-data
ENV APACHE_RUN_GROUP=www-data
ENV APACHE_LOG_DIR=/var/log/apache2
ENV APACHE_RUN_DIR=/var/run/apache2
ENV APACHE_LOCK_DIR=/var/lock/apache2
ENV APACHE_PID_FILE=/var/run/apache2/apache2.pid

RUN apt-get update && \
    apt-get install -y \
		apache2 \
		python3 \
        python3-pip \
		python3-venv \
		libapache2-mod-wsgi-py3 \
        unzip \
		curl \
		ca-certificates && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb


RUN python3 -m venv /wkdir/venv
RUN chmod +x /wkdir/venv/bin/activate

# Upgrade pip and setuptools inside the virtual environment
RUN . /wkdir/venv/bin/activate && pip install --upgrade pip setuptools

# Install required Python packages from requirements.txt
COPY python/requirements.txt .
RUN . /wkdir/venv/bin/activate && pip install -r requirements.txt

ENV PATH="/wkdir/venv/bin:$PATH"


RUN a2enmod rewrite
RUN a2enmod wsgi

COPY apache/custom-apache.conf /etc/apache2/sites-available/000-default.conf
COPY apache/apache2.conf /etc/apache2/apache2.conf

# Create necessary directories
RUN mkdir -p ${APACHE_RUN_DIR} ${APACHE_LOCK_DIR} ${APACHE_LOG_DIR}

STOPSIGNAL SIGWINCH
EXPOSE 8080



CMD ["apache2", "-DFOREGROUND"]
