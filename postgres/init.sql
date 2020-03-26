CREATE TABLE public."user" (
	id serial NOT NULL,
	fullname varchar NOT NULL,
	"password" varchar NOT NULL,
	email varchar NOT NULL,
	CONSTRAINT user_email_key UNIQUE (email),
	CONSTRAINT user_pkey PRIMARY KEY (id)
);

CREATE TABLE public.board (
	id serial NOT NULL,
	name varchar NULL,
	master int4 NULL,
	CONSTRAINT board_name_key UNIQUE (name),
	CONSTRAINT board_pkey PRIMARY KEY (id)
);


-- public.board foreign keys

ALTER TABLE public.board ADD CONSTRAINT board_master_fkey FOREIGN KEY (master) REFERENCES "user"(id);

CREATE TABLE public.article (
	id serial NOT NULL,
	board int4 NULL,
	writer int4 NULL,
	title varchar NOT NULL,
	"content" varchar NOT NULL,
	pub_date timestamp NULL,
	CONSTRAINT article_pkey PRIMARY KEY (id)
);


-- public.article foreign keys

ALTER TABLE public.article ADD CONSTRAINT article_board_fkey FOREIGN KEY (board) REFERENCES board(id);
ALTER TABLE public.article ADD CONSTRAINT article_writer_fkey FOREIGN KEY (writer) REFERENCES "user"(id);