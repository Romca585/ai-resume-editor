'''

The idea:
    It wouldn't be the first time I heard someone tell me I need to tailor my resume for each job description in order to increase the chances my resume gets seen.
    While this task is feasible through the use of ChatGPT and manual editing, I thought it would be cool to explore a 1 in many resume editor that allows users to:
        1) Edit their resume, regardless of the file format (pdf, plaintext, docx or LaTex - as my own personal resume is written)
        2) Allow AI to enhance their resume - this will require me to tinker with the prompt - potentially allowing users to select from a category of options on how they want their resume to be edited
        3) Allow for the creation of a brand new resume - again allow users to select the file format. For formats such as LaTex, it would be cool if I can have a more user-friendly UI, rather than pure code.


April 1/2: Initial Commit 
    Started playing around with the AI integration. I have a page that allows me to uplaod a resume and for AI to parse that resume. 
    Added an option to add a job description, this will prompt the AI to edit the resume according the keywords found in the description
        This on its own will be a huge limitation considering how dumb gpt3.5-turbo is. I decided to leave this specific task until the end.
        if the project goes in the direction I want it to, I will change models, especially given the price increase.

    Next Steps:
        I want to shy away from AI tailoring and focus more on the actual resume uploading/editing part. For now this includes:
            - Uploading PDF/plaintext/docx resumes
            - Parsing those resumes into subsections (i.e name, skills, experiences etc.)
            - Allow users to change those sections + glue it back together the way it was.. This might be easier to do on plaintext/docx files first prior to jumping into PDFS
        
