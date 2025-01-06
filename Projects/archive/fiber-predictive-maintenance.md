# Predictive Maintenance for Optical Fiber Draws

## Goals and Objectives
Preventative Maintenance (PM) leads to:
- Over-maintenance of machines, i.e. performing maintenance when machine is in a good health state and have no signs of wear. This leads to additional man-hours and machine downtime which incur cost. 
- Under-maintenance of machine, i.e. machine shows signs of wear but is not caught manually by the process engineers and hence leads to unexpected downtimes. 

Goals are:
- To implement a data-driven strategy to machine maintenance so as to avoid over- and under-maintenance. 
- To derive a metric for machine health which not only represents confidence in available data, but also incorporates domain knowledge expertise from plant engineers. 
- To predict optimal failure times for the machines so that maintenance can be scheduled in advance accordingly by plant management. 
- To follow a six-sigma approach to system design so that the system is maintainable, repeatable, can be implemented at-scale, improves customer satisfaction, and is metrics-driven. 

### DMAIC
Six-Sigma DMAIC stages are: Define, Measure, Analyze, Implement and Control. 
- *Define*: Voice of Customer, define requirements and project goals. 
- *Measure*: Collect data and domain knowledge on the process, and create data engineering pipelines if not present. 
- *Analyze*: Analyze the data to investigate root-cause and effect, determine data correlations and relationships, and determine process KPIs. 
- *Implement*: Design and implement the improvement system, conduct experiments, and establish system capability using a pilot. 
- *Control*: Implement control limits on process deviations, downstream process is these limits are exceeded, and visualize results and KPIs. Thorough documentation. 

## Data Engineering
- Time-series data is already hosted on PI servers, which collects data from various draw sensors such as Pressure, Temperature, Humidity, Draw Speed, etc. 
- Using python APIs, this data is extracted for offline studies as dataframes. 
- For deployment, data pipelines are built using python so that this data is ingested/refreshed into a SQL server periodically. DB is chosen such that one year's worth of data can be hosted at any given time in the DB. 
- Integration is done with the maintenance activity server where important events such as maintenance times and schedules are logged. 

## Feature Engineering
- Sensor data is smoothed using a polynomial window method. 
- Outlier time periods are identified and not used for training. 
- Six condition indicators are identified after doing a slope analysis near machine failure times. 

## Training Data
To build a regression model for machine health, we need to identify instances of good and bad health on the sensor data (labeling). This identification is done in a ad-hoc way for each machine in collaboration with process engineers. 

## Literature Review


## Model Development
### Health Metric
Given historical run-to-failure feature data for the draw (+similar draws), objective is to create a model for the health of the draw, which will be used as a condition indicator for the draw. Following steps are taken:
- We define a linear regression model such that: $h_t = \beta_0 + \beta_1T_t + \beta_2P_t + ...$, where $T_t, P_t$ are temperature and pressure sensor measurements at time $t$, and the '$...$' indicates that several other sensor measurements were utilized as identified in the feature selection phase. 
  - Can be written as $H = B^TX$, where $H$ and $X$ include the entire time-series data till failure. 
  - For training, we identify the response as the linear line segment connecting the start of the draw process ($H=1$) to the draw failure ($H=0$). We define $X$ to be the feature matrix with rows corresponding to the same time stamps. 
  - Drawbacks of this method are that prior domain knowledge on $\beta_i$ is not utilized, and the heath point estimates do not convey the uncertainty due to very limited data present. 
- Hence a Bayesian approach is used such that:
  - $h_t \sim N(B^TX_t, \sigma^2)$, where $B^TX_t$ is the OLS estimate for health. 
  - Parameter Posterior $P(B|X_t,h_t) \sim P(h_t|X_t,B).P(B)$, where $P(h_t|X_t,B))$ is the data likelihood and $P(B)$ is the model parameter prior distribution. 
- After training, we obtain the estimates $\hat{B}$ as the means of the posteriors. 
  - Priors for the parameters are modeled as normal distributions with mean and variance coming from plant engineer intuitions and historical data. 
- Hence, at inference time with new data samples $X_t$, we can show the normal health distribution $P(H_t)$ to the plant personnel on a dashboard using mean posterior estimates of $B$ and $\sigma$.

### Remaining Useful Life
Using the mean health model parameter estimates, we create a repository of health models for all draws which have run to failure. Note that this repository will increase over time, and hence the parameter estimates will improve. Following steps are then taken to estimate RUL:
- For the particular draw, we fit polynomial degradation models $h_t = a + bt + ct^2$ using OLS on the health model repository. 
- At inference:
  - Let the new sensor data be $X_t$. We obtain the current machine health as $h_t$ as the mean of the distribution $P(H_t) = N(\hat{B}^TX_t, \hat{\sigma}^2)$. This distribution is visualized on the dashboard. 
  - Find top $k$ trajectories (from the model repository) which are similar to the current health trajectory, where the similarity score is the exponential of the $L_1$ norm.
  - For the top $k$ exponential trajectories identified, get the distribution of RULs. 
  - Mean of this distribution is the RUL for current draw. This distribution is visualized on the dashboard. 


## Model Evaluation
Offline:
- Case study is done to test 6 draws which are near failure times, to not go to preventative maintenance and let them run to failure. In parallel, the designed PdM system is run (along with visualizations on the dashboard) to check if actual failure times match with predicted in real-time. 

Online:
- After getting buy-in from stakeholders, the developed system is rolled out to the entire fleet of draws (across US) in a phased approach to minimize risk and ensuring stable operations. 

Metrics used (over a 12-month rolling average period):  
- *PdM Effectiveness*: Number of identified PdM instances divided by the number of preventative maintenance (PM) scheduled instances. 
- *PdM Schedule Adherence*: Number of times maintenance implemented with a PdM flag divided by number of instances where PdM flagged a machine health to be less than the specified threshold. 
- *Labor Hours*: Percentage of worker's time spent on PdM routines. 
- *PdM System Maintenance*: Software engineering hours spent on debugs and maintenance of PdM software. PowerBI issues tracked separately. 
- *Machine Utilization*: Number of machine hours in uptime divided by total time. 
- *PdM Failure Rate*: Number of times maintenance implemented without a PdM flag divided by total number of maintenance instances. 

## Model Deployment
On-prem deployment with:
- PostgreSQL DB to store incoming recent data, model parameters and results. 
- Stand alone virtual server machine executing a python application. 
  - Application auto-start is built in, in case the server is disconnected. 
- Time series data stored in PI data servers, and then pulled to a temporary server for storage, and then to application server in-memory for processing. 

## Model Monitoring
- PowerBI dashboard for customers
- Log files generated for developer access. 
  - Database logs,
  - Application logs, 
  - Process logs. 