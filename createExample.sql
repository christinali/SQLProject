----------------------------------------------------------------------
-- (a) and (b): you can just edit the CREATE TABLE statements below.

-- Primary keys: person_ssn, accountID, stockSymbol, 
-- Foreign keys: managerSSN (but that can be Null and doesn't have to be unique), accountManagingBrokerSSN (should not be Null, but doesn't need to be unique),
-- 

CREATE TABLE Person
(ssn DECIMAL(10,0) NOT NULL,
 name VARCHAR(256) NOT NULL,
 address VARCHAR(256) NOT NULL,
 PRIMARY KEY(ssn));

CREATE TABLE Broker
(ssn DECIMAL(10,0) NOT NULL,
 phone DECIMAL(10,0) NOT NULL,
 manager DECIMAL(10,0),
 Primary Key (ssn),
 Foreign Key(ssn) references Person(ssn),
 Foreign Key(manager) references Broker(ssn));

CREATE TABLE Account
(aid INTEGER NOT NULL,
 brokerssn DECIMAL(10,0) NOT NULL,
 Primary Key(aid),
 Foreign Key (brokerssn) references Broker(ssn));

CREATE TABLE Owns
(ssn DECIMAL(10,0) NOT NULL,
 aid INTEGER NOT NULL,
 Primary Key(ssn, aid),
 Foreign Key(ssn) references Person(ssn),
 Foreign Key(aid) references Account(aid));

CREATE TABLE Stock
(sym CHAR(5) NOT NULL,
 price DECIMAL(10,2) NOT NULL,
 Primary Key(sym));

CREATE TABLE Holds
(aid INTEGER NOT NULL,
 sym CHAR(5) NOT NULL,
 amount DECIMAL(10,2) NOT NULL,
 Primary Key(aid, sym),
 Foreign Key(aid) references Account(aid),
 Foreign Key(sym) references Stock(sym));

CREATE TABLE Trade
(aid INTEGER NOT NULL,
 seq INTEGER NOT NULL,
 type CHAR(4) NOT NULL,
 timestamp TIMESTAMP NOT NULL,
 sym CHAR(5) NOT NULL,
 shares DECIMAL(10,2) NOT NULL,
 price DECIMAL(10,2) NOT NULL,
 Primary Key(aid, seq),
 Foreign Key(aid) references Account(aid),
 Foreign Key(sym) references Stock(sym),
 check (type='buy' or type='sell'));

----------------------------------------------------------------------
-- (c): trade table is append-only (i.e., no DELETE or UPDATE is
-- allowed); furthermore, within each account, trades must be recorded
-- sequentially over time.  Implement the trigger function below; do
-- not modify the CREATE TRIGGER statement that follows.

CREATE FUNCTION TF_TradeSeqAppendOnly() RETURNS TRIGGER AS $$
BEGIN
  -- YOUR IMPLEMENTATION GOES HERE
  IF (TG_OP = 'DELETE' or TG_OP = 'UPDATE') THEN
	RAISE EXCEPTION 'Cannot update or delete from Trade table';
  end if;
  IF (Exists (Select * from Trade where seq>=NEW.seq and NEW.aid = aid)) then
	RAISE EXCEPTION 'New sequence number must be strictly greater than all previous ones';
  end if;
  IF (Exists (Select * from Trade where timestamp>NEW.timestamp and NEW.aid = aid)) then
	RAISE EXCEPTION 'New timestamp must be greater than or equal to all previous ones';
  end if;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_TradeSeqAppendOnly
  BEFORE INSERT OR UPDATE OR DELETE ON Trade
  FOR EACH ROW
  EXECUTE PROCEDURE TF_TradeSeqAppendOnly();

----------------------------------------------------------------------
-- (d): brokers cannot own accounts, either by themselves or jointly
-- with others.  Implement the trigger function below; do not modify
-- the CREATE TRIGGER statements that follow.

CREATE FUNCTION TF_BrokerNotAccountOwner() RETURNS TRIGGER AS $$
BEGIN
  -- YOUR IMPLEMENTATION GOES HERE
  IF (Exists (Select * from Owns where NEW.ssn in (Select ssn from Broker))) then
	RAISE EXCEPTION 'Broker cannot own an account';
  end if;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_BrokerNotAccountOwner_Broker
  BEFORE INSERT OR UPDATE OF ssn ON Broker
  -- note that DELETE won't cause a violation
  FOR EACH ROW
  EXECUTE PROCEDURE TF_BrokerNotAccountOwner();

CREATE TRIGGER TG_BrokerNotAccountOwner_Owns
  BEFORE INSERT OR UPDATE OF ssn ON Owns
  -- note that DELETE won't cause a violation
  FOR EACH ROW
  EXECUTE PROCEDURE TF_BrokerNotAccountOwner();

----------------------------------------------------------------------
-- (e): no broker reports (directly or indirectly) to him/herself.
-- Implement the view that returns all pairs of brokers (broker1,
-- broker2) where broker1 reports directly or indirectly to broker2;
-- do not modify the CREATE FUNCTION and CREATE TRIGGER statements
-- that follow.

CREATE VIEW ReportsToRecursive(broker1, broker2) AS 
  WITH RECURSIVE brokerPairs (ssn, manager) as(
	(Select ssn, manager from Broker where manager is not null)

	UNION

	(Select b1.ssn, b2.manager from 
    brokerPairs as b1, Broker as b2
    where b1.manager = b2.ssn
	)
)
	select * from brokerPairs;

CREATE FUNCTION TF_NoSelfReport() RETURNS TRIGGER AS $$
BEGIN
  IF EXISTS(SELECT * FROM ReportsToRecursive WHERE broker1 = broker2) THEN
    RAISE EXCEPTION 'broker % now reports to him/herself, directly or indirectly',
                    (SELECT MIN(broker1) FROM ReportsToRecursive WHERE broker1 = broker2);
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER TG_NoSelfReport
  AFTER INSERT OR UPDATE ON Broker
  FOR EACH STATEMENT
  EXECUTE PROCEDURE TF_NoSelfReport();
