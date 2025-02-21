prompt_template = ("""You are an expert at creating questions based on coding materials and documentation. 
Your goal is to prepare a coder or programmer for a test or coding exam. You do this asking question based on the below test

-------
{text}
-------

Prepare questions that will prepare the candidate for their test , make sure not lose any informations

Questions:
""")



Refine_template = ("""You are an expert at creating questions based on coding materials and documentation. 
Your goal is to prepare a coder or programmer for a test or coding exam.We have recieved some questions to certain extent : {existing_answer}.
We have option to refine the questions or to add new questions if necessary with some more context below.


---------
{text}
---------

Given the context,refine the questions in English. If context is not helpful give original questions.

Question:
""")