-- Task 5. Email validation to sent
-- Write a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed.
CREATE TRIGGER when_email_changes
BEFORE UPDATE
ON users FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    END IF;
END$$

DELIMITER;
