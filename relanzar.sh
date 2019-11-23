sudo docker-compose -f docker/config/base.yml rm -sfv
sudo docker-compose -f docker/config/base.yml build
sudo docker-compose -f docker/config/base.yml up -d
