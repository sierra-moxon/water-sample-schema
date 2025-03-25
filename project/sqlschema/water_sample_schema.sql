-- # Class: "EnvironmentalSample" Description: "A hypothetical collection of attributes that represent a sample from a specific  location."
--     * Slot: id Description: 
--     * Slot: analysis_type Description: The type of sample
--     * Slot: latitude Description: The latitude of the sample
--     * Slot: longitude Description: The longitude of the sample

CREATE TABLE "EnvironmentalSample" (
	id INTEGER NOT NULL, 
	analysis_type VARCHAR, 
	latitude FLOAT, 
	longitude FLOAT, 
	PRIMARY KEY (id)
);