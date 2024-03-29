CREATE TABLE address (
id INT(11) NOT NULL AUTO_INCREMENT,
contact_id INT(11) NOT NULL,
street1 VARCHAR(100),
street2 VARCHAR(100),
suburb VARCHAR(64),
city VARCHAR(64),
post_code VARCHAR(16),
PRIMARY KEY(id),
CONSTRAINT fk_addr_contact_id
FOREIGN KEY (contact_id)
  REFERENCES contact(id)
);
