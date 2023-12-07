-- Table created to store valuable results relevant to our analysis
CREATE TABLE Results (
    TotalRespondents int,
    FrequentTTC int,
    FrequentTTCBooleanTrue int,
	FrequentTTCBooleanFalse int,
    FarTTC int,
    AccessTTC int
);

--Total number of respondants in Seniors Survey 2017 including null values: 6939

--Number of respondants selecting TTC as at least one of their modes of transportation to get around Toronto: 3548

--Number of respondants using TTC frequently: 2903

--Number of respondants do not use TTC frequently: 3002

--Among the 3002 respondants who do not use TTC frequently, 299 choose their reason as [The nearest TTC stop/station is too far away]

--Among the 3002 respondants who do not use TTC frequently, 156 choose their reason as [The nearest TTC stop/station is not accessible]

--
INSERT INTO Results (TotalRespondents, FrequentTTC, FrequentTTCBooleanTrue, FrequentTTCBooleanFalse, FarTTC, AccessTTC)

--values were populated by taking the sums from each column in the table
VALUES ((SELECT COUNT(*) FROM seniorsurvey),
		(SELECT COUNT(usettc) FROM seniorsurvey), 
		(SELECT COUNT(frequently) FROM seniorsurvey WHERE frequently = true),
		(SELECT COUNT(frequently) FROM seniorsurvey WHERE frequently = false),
		(SELECT COUNT(ttcfaraway) FROM seniorsurvey),
		(SELECT COUNT(ttcnotaccessible) FROM seniorsurvey));