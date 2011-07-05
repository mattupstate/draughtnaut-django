INSERT INTO beer_beer VALUES(1,'Sierra Nevada Celebration Ale',6.8,2,1,0,'2011-07-05 11:04:28.704847','2011-07-05 11:04:28.704874');
INSERT INTO beer_beer VALUES(2,'Sierra Nevada Bigfoot Barleywine Style Ale',9.6,3,1,0,'2011-07-05 11:05:11.451387','2011-07-05 11:05:11.451414');
INSERT INTO beer_beer VALUES(3,'Sierra Nevada Pale Ale',5.6,4,1,0,'2011-07-05 12:36:48.160297','2011-07-05 12:36:48.160325');
INSERT INTO beer_beer VALUES(4,'Sierra Nevada Summerfest Lager',5,6,1,0,'2011-07-05 12:37:04.995455','2011-07-05 12:37:04.995485');
INSERT INTO beer_beer VALUES(5,'Sierra Nevada Porter',5.6,7,1,0,'2011-07-05 12:37:24.748000','2011-07-05 12:37:24.748030');
INSERT INTO beer_beer VALUES(6,'Sierra Nevada Stout',5.8,8,1,0,'2011-07-05 12:37:43.956221','2011-07-05 12:37:43.956254');

INSERT INTO beer_beerontap VALUES(1,'',1,4,2,'2011-07-05 12:41:35.841701');
INSERT INTO beer_beerontap VALUES(2,'',1,5,2,'2011-07-05 12:41:39.370159');

INSERT INTO beer_beerstyle VALUES(1,'ale','Ale','',NULL);
INSERT INTO beer_beerstyle VALUES(2,'american-ipa','American IPA','',1);
INSERT INTO beer_beerstyle VALUES(3,'american-barleywine','American Barleywine','',1);
INSERT INTO beer_beerstyle VALUES(4,'american-pale-ale','American Pale Ale','',1);
INSERT INTO beer_beerstyle VALUES(5,'lager','Lager','',NULL);
INSERT INTO beer_beerstyle VALUES(6,'czech-pilsener','Czech Pilsener','',5);
INSERT INTO beer_beerstyle VALUES(7,'america-porter','American Porter','',1);
INSERT INTO beer_beerstyle VALUES(8,'american-stout','American Stout','',1);

INSERT INTO venues_venue VALUES(1,'sierra-nevada-brewing-co','Sierra Nevada Brewing Co.','1075 E. 20th Street','','Chico','California',95928,'United States','','','',1,'',NULL,NULL,'2011-07-05 11:03:26.620900','2011-07-05 11:03:26.620928');
INSERT INTO venues_venue VALUES(2,'mission-dolores','Mission Dolores','249 4th Ave','','Brooklyn','New York',11215,'United States','','','',2,'',NULL,NULL,'2011-07-05 12:34:44.557305','2011-07-05 12:34:44.557333');

INSERT INTO venues_venuetype VALUES(1,'brewery','Brewery');
INSERT INTO venues_venuetype VALUES(2,'bar','Bar');