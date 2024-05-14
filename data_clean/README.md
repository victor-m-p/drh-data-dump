# Database of Religious History (DRH) data dump

(some description of the DRH)

## <a name="table-valuescsv"></a>Table [answerset.csv](./answerset.csv)

This table lists the complete answerset for published entries in the Database of Religious History (DRH). Connected to other tables through `question_id`, `entry_id`, `region_id` columns. Table has no primary key since the answerset is across questions (`question_id`) and entries (`entry_id`); additionally, distinct answers can be given for particular date ranges (`year_from`, `year_to`), regions (`region_id`), and `branching_questions`, different experts (`expert_id`) can provide different answers, or the same expert might provide different answers (to the same question for the same entry). 

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
question_id | `int` | xxx
question_name | `string` | xxx
parent_question_id | `float` | xxx
parent_question | `string` | xxx
entry_id | `int` | xxx
answer | `string` | xxx
answer_value | `int` | xxx
parent_answer | `string` | xxx
parent_answer_value | `int` | xxx
notes | `string` | xxx
year_from | `int` | xxx
year_to | `int` | xxx
branching_question | `string` | xxx
region_id | `int` | xxx
expert_id | `int` | xxx
expert_name | `string` | xxx
editor_id | `int` | xxx
editor_name | `string` | xxx
date_published | `string` | xxx
date_created | `string` | xxx
date_modified | `string` | xxx

## <a name="table-entry_datacsv"></a>Table [entry_data.csv](./entry_data.csv)

This table lists metadata for entries published in the Database of Religious History (DRH). Connected to other tables through `entry_id`, `region_id` columns.

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
entry_id | `int` | Primary key
entry_name | `string` | xxx
poll_id | `int` | xxx 
poll_name | `string` | xxx
description | `string` | xxx
year_from | `int` | xxx
year_to | `int` | xxx
region_id | `int` | xxx
expert_id | `int` | xxx
expert_name | `string` | xxx
date_created | `string` | xxx
date_modified | `string` | xxx
data_source | `string` | xxx

## <a name="table-region_data"></a>Table [region_data.csv](./region_data.csv)

Some description goes here...

### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
`region_id` | `int` | Primary key
`region_name` | `string` | xxx
`region_description` | `string` | xxx
`gis_region` | `string` | multipolygon
`completed` | `bool` | `gis_region` completed (True/False)
`world_region` | `string` | coded into 10 values (cite)
