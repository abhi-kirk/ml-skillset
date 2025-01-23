# Behavioral Questions

## **General Work Experience and Role Fit**
- *Can you walk me through your resume and highlight your most impactful projects?*  
  - STORY: CNN defect classifier
- *Why are you interested in this role at our company?*  
  - Tesla's emphasis on innovation building systems of their own, 
  - Manufacturing data science background (mention pdm if appropriate), 
  - Experience and strong fundamentals in vision and NLP ML, 
  - Good culture fit as opposed to in a bank. 
  - STORY: Chatbot road to prod. 
- *How do you prioritize tasks when managing multiple projects or deadlines?*  
  - Break down projects into smaller components, and set smaller goals and timelines, 
  - Communicate with stakeholders regularly and keep them updated on progress, 
  - Track everything.
  - STORY: Corning - Classifier/PdM/MPC under three different managers.  
- *Describe a challenging project you worked on. How did you overcome the obstacles?*  
  - STORY: Cold start. 
- *Tell me about a time you made a mistake on a project. How did you address it?*  
  - STORY: Small mistake: Chunking, 
  - STORY: Bigger: Over-engineering with RetinaNet and/or GNN. 

---

## **Technical and Problem-Solving**
- *How do you approach debugging a complex machine learning model or software issue?*  
  - Isolate the issue by analyzing logs, telemetry, walking back the dependency graph using EDA tools. 
  - Root cause the issue by possibly recreating it and walking through the code. 
  - Propose multiple solutions with respective trade-offs. 
  - STORY: Chunking. 
- *Describe a situation where you had to make a tradeoff between accuracy/performance and efficiency/speed.*  
  - STORY: GNN vs. Embedding match. Limited the scope of GNN predictions since latency was a concern, at the expense of accuracy. 
- *Tell me about a project where you implemented a new technology or algorithm. Why did you choose it, and what was the outcome?*  
  - STORY: New to me: LTR. 
  - STORY: Innovative: Image occlusion/masking. 
- *Have you ever disagreed with a team member or stakeholder about a technical decision? How did you resolve it?*  
  - STORY: Software change vs. prompt engineeing. 
  - Usecase: Removing hyperlinks from LLM response. 
  - Resolution: Try both and quantify the affects on the overall system. Standardize a rule set for when prompt engineering should be used. 
- *How do you ensure the reproducibility and scalability of your code or models?*  
  - Tracking ML experiments using comet-ml, tracking data with DVC or compressed file versioning. 
  - Write code in a modular way, keeping in mind productionization efforts. 
  - Model checkpointing during training, and good documentation. 
  - STORY: Clustering for search engine. 

---

## **Collaboration and Communication**
- *Describe a time you collaborated with cross-functional teams (e.g., data scientists, software engineers, product managers). What challenges did you face, and how did you address them?*  
  - STORY: Cross-lob collab with product on incident search engine / root-cause analysis. 
  - Gathered requirements, success criterion, testing process, division of responsibilities, frequency of updates and timelines. 
  - DEVUP selection and securing funding. 
- *How do you explain complex technical concepts to non-technical stakeholders?*  
  - Use more intuitive ML metrics and align them with business metrics. 
  - Explain fundamentals and not necessarily the specific tech. 
  - Make models and results as explainable as possible. 
  - STORY: Confusion matrices for CNN classifier + Occlusion heatmap. 
- *Tell me about a time you mentored a colleague or shared knowledge with your team.*  
  - STORY: Mentored: Junior SWE for enhancing graph UI for search engine backend. 
  - STORY: Sharing: GPT-Vader side-project learnings to help understand LLM pretraining process. 
- *How do you handle conflicts or misunderstandings in a team setting?*
  - Not to escalate; be polite and friendly. 
  - Present evidence to back up your claims, but don't disregard other claims/opinions. 
  - Put yourself in their shoes. 
  - 1:1. 
  - STORY: Prompt engineering, CNN explainability. 

---

## **Adaptability and Learning**
- *Tell me about a time you had to quickly learn a new tool, framework, or programming language to complete a project.*  
  - STORY: Start of data science career: python, DS tools, ML/DL, C#, software best practices. 
  - STORY: Transformers. 
- *How do you stay up-to-date with industry trends, especially in machine learning or software development?*  
  - Research on every tech/algorithm for the current task. 
  - Keep an eye out for latest papers on interested tech. 
  - Thinking about how to improve existing processes. 
    - STORY: LTR. 
- *Share an example of how you adapted to a significant change in a project's requirements or scope.*  
  - STORY: Scope change for chatbot: rapid enabling of data ingestion from 5+ sources. 

---

## **Leadership and Initiative**
- *Describe a time when you took the lead on a project or initiative.*  
  - STORY: Defect classifier, Search engine. 
- *Tell me about a time you identified an inefficiency in a system or process. What did you do to improve it?*  
  - STORY: Search engine. 
- *How do you ensure your team stays motivated and aligned toward a project goal?*  
  - Assigning tasks: intersection of what the business needs, individual's skillset, and individual's goals/interests. 
  - Clear roadmap with small deliverables and milestones. 
  - Clear and quantifiable communication on project impact and the resulting positive impact to individual's career goals. 
  - Enthusiastic and positive attitude. 
  - STORY: Clustering for search engine. 

---

## **Results-Oriented Questions**
- *Can you provide an example of a project where your work directly impacted the company’s bottom line or product success?*  
  - STORY: Defect classifier. 
- *How do you measure the success of your projects or contributions?*  
  - Quantitative and qualitative: Business metrics (ROI, KPIs), timely deliverables, collaborative effort, customer satisfaction. 
  - STORY: Chatbot. 
