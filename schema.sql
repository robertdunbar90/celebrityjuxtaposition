drop table if exists questions;
create table questions (
  id integer primary key autoincrement,
  question text not null,
  answerA text not null,
  descriptionA text not null,
  answerB text not null,
  descriptionB text not null,
  aCount integer not null,
  bCount integer not null
);