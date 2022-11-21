# MU Hiring 2022 Dataset
1. Prepare a customer data platform from the activity data provided
    <br>a. Will be validated aganist masked source data
2. Pitch a business solution using analysis of the CDP built
    <br>a. Judged by a panel
## General information
- Number of clubs: 3
- Number of fests: 2
## Dataset description
- College provided source truth: [Metadata](Metadata.csv)
- All club events data: [Clubs_data](Clubs_data.csv)
- All Organizers for fests: [Organisers_In_Fests](Organisers_In_Fests.csv)
- Participation list from all fest related events: [Participants_In_Fests](Participants_In_Fests.csv)

## Mandatory tech features
1. Plotly Dash
2. Profile JSON should be submitted before presentation
3. Pluggable format



## Sample Profile json format
```
[
    {'name': 'Dummy',
 'id': 'id000',
 'clubs': {'club_i': {'isOrganiser': 'Organiser',
            'club_i_event_j': {'participated': False},
            },
        },
 'fests': {'fest_i': {'isOrganiser': '',
            'fest_i_event_j': {'participated': True},
            },
        }
    }
]


```