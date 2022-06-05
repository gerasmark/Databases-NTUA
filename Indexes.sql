CREATE INDEX researcher_fullname_idx ON `researcher`(`first_name`,`last_name`);
CREATE INDEX org_name_idx ON `organization`(`name`);
CREATE INDEX project_name_idx ON `project`(`title`);
CREATE INDEX scientific_field_idx ON `scientific_field`(`name`);
CREATE INDEX program_name_idx ON `program`(`name`);
