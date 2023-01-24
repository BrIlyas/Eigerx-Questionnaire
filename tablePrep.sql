 CREATE TABLE DEPARTMENT
  (
     ID       INT,
     NAME     VARCHAR(255),
     LOCATION VARCHAR(255),
	 PRIMARY KEY(ID)
  );

CREATE TABLE EMPLOYEE
  (
     ID      INT,
     NAME    VARCHAR(255),
     SALARY  INT,
     DEPT_ID INT,
	 PRIMARY KEY(ID),
	 FOREIGN KEY (DEPT_ID) REFERENCES DEPARTMENT(ID)
  );
  
INSERT INTO DEPARTMENT
            (ID,
             NAME,
             LOCATION)
VALUES      (1,
             "EXECUTIVE",
             "SYDNEY");

INSERT INTO DEPARTMENT
            (ID,
             NAME,
             LOCATION)
VALUES      (2,
             "PRODUCTION",
             "SYDNEY");

INSERT INTO DEPARTMENT
            (ID,
             NAME,
             LOCATION)
VALUES      (3,
             "RESOURCES",
             "CAPE TOWN");

INSERT INTO DEPARTMENT
            (ID,
             NAME,
             LOCATION)
VALUES      (4,
             "TECHNICAL",
             "TEXAS");

INSERT INTO DEPARTMENT
            (ID,
             NAME,
             LOCATION)
VALUES      (5,
             "MANAGEMENT",
             "PARIS");

INSERT INTO EMPLOYEE
            (ID,
             NAME,
             SALARY,
             DEPT_ID)
VALUES      (1,
             "CANDICE",
             4685,
             1);

INSERT INTO EMPLOYEE
            (ID,
             NAME,
             SALARY,
             DEPT_ID)
VALUES      (2,
             "JULIA",
             2559,
             2);

INSERT INTO EMPLOYEE
            (ID,
             NAME,
             SALARY,
             DEPT_ID)
VALUES      (3,
             "BOB",
             4405,
             4);

INSERT INTO EMPLOYEE
            (ID,
             NAME,
             SALARY,
             DEPT_ID)
VALUES      (4,
             "SCARLET",
             2350,
             1);

INSERT INTO EMPLOYEE
            (ID,
             NAME,
             SALARY,
             DEPT_ID)
VALUES      (5,
             "ILEANA",
             1151,
             4);