# Data Deduplication Mindgraph Hackathon

## Description and steps on how the files work: 

Change the path name for all the files while using. 


### Deduplication File(MU deduplication_data.ipynb):

For the defuzzication of the names of the participants, organizers and club data, 
thefuzz and leveinstein's distance to map the respective names to their ID's from the 
metadata. 
For every dataset, usage of Fuzzy matching has been done several times to get most of
the data mapped to their roll numbers, so run all the cells under the headers for 
obtaining the final processed dataset.
Note: The headers are Partcipation dataset preprocessing, Organizers preprocessing, clubs data
processing.

### Data Analysis File(Analysis.ipynb):

After obtaining the mapping of rollnumbers and their names in the datasets, we have 
obtained insights from the data in terms of the participation rate, fests and events.
Explanation of the insights will be done in the presentation.

### JSON File(convert to json_profile.ipynb):

In this we read the deduped datasets and make profiles for each unique roll number in Metadata.csv
The code in the above python notebook will create multiple json profiles for each unique person.
