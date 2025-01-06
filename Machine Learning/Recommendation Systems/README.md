## Taxonomy
Dimensions to describe a system:
- Domain: Type of content recommended
- Purpose: Objectives quantified by metrics
- Context: Environment where/when recommendations are received
- Personalization level: Data used to target consumers
  - Non-personalized: Based on popularity, revenue generation, editor picks: especially useful in case of cold start or as a backup in case of system/model delays. 
- Interface: 
  - Inputs: Explicit and implicit customer feedback,
  - Outputs: Explainability, UI. 
- Algorithms: Collaborative filtering, content-based, hybrid. 


## User Data
Note: Explicit ratings may not be a true indicator of user's preferences. 

Implicit:
- Various browsing user activities can be tagged as *events* (e.g. scrolling a themed row, viewing additional info, adding to a personalized list, purchasing, etc.). 
- Implicit user feedback can be quantified using a timeline of these events. 
- New events should be given a larger weight. Similarly different events will have different importance, and hence different weights. 
  - ML can be used to figure out the implicit ratings with $Y = f(X) + \epsilon$, where $Y$ is the prediction user-item preference, $X$ is the set of features (input data), and $\epsilon$ is noise that can be modeled. 
- Analyzing social media to identify similar users, user preferences and user attributes. 

Explicit:
- Star-rating on a scale. 
- Written feedback, quantified as the sentiment in comments, weighted by peer votes. 
- Asking user preferences. 


## Metrics
System metrics:
- Number of users using the service (subscriptions, site views, etc.). 
- Items purchased per month. 
- Profit (considering infra, personnel costs). 

Infrastructure metrics:
- Downtime. 
- Latency. 

Model metrics:
- Conversion percentage (e.g. from free to subscribed). 
- Derived from explicit and implicit user feedback. 


## Analytics
- User personas distribution: Categorize users into personas (set of user or item attributes), and analyze model metrics. 
- User interaction with less popular items, although infrequent, can provide good insight into user preferences. 