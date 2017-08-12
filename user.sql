BEGIN TRANSACTION;
CREATE TABLE `user` (
	`firstName`	VARCHAR(10),
	`lastName`	VARCHAR(20),
	`userName`	VARCHAR(20),
	`education`	VARCHAR(15),
	`email`	VARCHAR(50),
	`password`	VARCHAR(20),
	`keys`	VARCHAR(5)
);
COMMIT;
