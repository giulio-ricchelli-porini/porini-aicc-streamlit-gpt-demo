 # Streamlit Demo: OpenAI chatbot

This project demonstrates the [Open AI](https://platform.openai.com/docs/guides/gpt) GPT model capabilities into an interactive [Streamlit](https://streamlit.io) app.

## Assignment steps
* Prepare an environment and run the app:
    * As done in the first assignment, clone this repo in the "GitClass" folder ("C:\Users\\%yourUsername%\Visual Studio Code\GitClass"); you should then have a new project folder in the "GitClass" folder dedicated to this project
    * In a terminal window, go into the project folder: ```cd %yourProjectFolder%```
    * Create a Python virtual env: ```python -m venv porini-gitclass-env-2```
    * Activate the new virtual env: ```"porini-gitclass-env-2/Scripts/activate.bat"```
    * Install requirements: ```pip install -r requirements.txt```
    * Run the app: ```streamlit run main.py```
    * After having verified that it works, stop the app (ctrl+C from the terminal window, or kill the terminal window)
* Create a new branch:
    * Create a new branch: ```git branch develop```
    * Switch to the new branch: ```git checkout develop```
    * Check that the current branch is "develop": ```git branch```
* Update the code:
    * Add a button to the main page, with label "Use example chat", that inserts the example chat text in the input text box, so that the user can use this button to load the example through a simple click
        * To accomplish this, you can use the Streamlit session_state, combined with the on_click event on the new button and the value attribute on the text_input (check the Streamlit documentation)
        * Remember to initialize the state on page load!
* Push your changes and merge to the "main" branch:
    * By using the integrated "Source Control" tab in VSCode, commit and push your changes by publishing the "develop" branch to the remote
    * From the browser, open the repository, go to the "develop" branch and create a pull request to merge your changes to the "main" branch: complete and merge it to align "main" to "develop"; in this way, you aligned commits from the "develop" branch to the "main" branch
* Update your local project "main" branch:
    * From your local project, from the terminal window go to the "main" branch: ```git checkout main```
    * Pull the changes applied by the pull request you completed: ```git pull```; in this way, your local project is aligned with the "main" from the remote
* Delete the "develop" branch, both locally and remotely:
    * Delete your local "develop" branch: ```git branch -d develop```; in this way, the "develop" branch has been deleted locally but it still exists on the remote
    * Check that the "develop" local branch has been deleted: ```git branch```
    * Check from the browser that the "develop" branch still exists on the remote, even of you reload the page
    * Delete the "develop" branch from the remote: ```git push origin --delete develop```
    * Check from the browser that the "develop" branch no longer exists on the remote: now the repository branch list shows only the "main" branch, and the repository url with "/develop" as final subpath gives a "404 Not Found" error

By editing the "develop" branch and bringing its changes to the "main" branch through a pull request, you've also simulated the situation in which another developer working on your same repository brings changes to the remote "main" branch (through the pull request you performed), and you have to align your local "main" branch to the remote one, in order to be syncronized with the changes from the other developer: the pull command is the way to keep your local branches updated with your team colleagues!

You completed the assignment! Please notify us when you have done!
