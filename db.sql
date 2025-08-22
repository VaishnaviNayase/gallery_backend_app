create table users(
	userId serial  primary key,
       	email varchar(50));

create table breed( 
	breedId serial  primary key,
	name varchar(20));

create table breedImage(
	breedImgId serial  primary key,
	breedId int,
	imageURL varchar(255),
       	foreign key(breedId) references breed(breedId));

CREATE TABLE likes (
    likeId SERIAL PRIMARY KEY,
    userId INT REFERENCES users(userId) ON DELETE CASCADE,
    breedImgId INT REFERENCES breedImage(breedImgId) ON DELETE CASCADE,
    UNIQUE(userId, breedImgId) 
);

create table recentlyViewed(\
	userId int,
	breedId int,
	viewed timestamp default current_timestamp,
	primary key(userId, breedId),
    foreign key(breedId) references breed(breedId),
   	foreign key(userId) references users(userId));

create table subtype(
	breedId int,
	name varchar(20),
       	foreign key(breedId) references breed(breedId));
