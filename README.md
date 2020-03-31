# Champions-of-ITK
The tabletop-rpg without a game master!

Purpose of this project:
Some time ago I made some simple rules for a tabletop rpg,
the purpose of the rpg was to have all players create and
play a character without a game master. In order to make
the game interesting and more alive a large amount of tables
should provide everything from events to conversations from
NPCs and that is where this project comes in, the main purpose
is to make this a dynamic adventure database management system.

The rules for Champions of ITK are also provided

How to dockerize the webapp bellow.

for development:

without docker:\n
npm run serve

with docker:
docker-compose up -d --build

for the production:
docker build -f Dockerfile-prod -t my-app:prod .
docker run -it -p 80:80 --rm my-app:prod
