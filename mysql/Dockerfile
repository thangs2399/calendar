FROM mysql:latest

COPY ./init.sql /tmp

# command: mysqld --init-file="/tmp/database/install_db.sql"
CMD ["mysqld", "--init-file=/tmp/init.sql"]