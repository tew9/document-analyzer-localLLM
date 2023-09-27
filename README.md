# Smart Review Insight.
This is an in memory playground for smart review insight powered by GenAI.

## Dependencies
Make sure you place openai key to your .env file
- Use  ``pipenv`` in vscode to create virtual isolated pip environment.
- Run  ```pipenv install``` to install all the depepencies.
- Run ```pipenv shell``` to activate virtual environment
- Run the app using ```strealit run main.py``` or alias it as ```alias run='streamlit run main.py'``` and then run ```run``` in your terminal.


## Troubleshooting
1. "Did not find openai_api_key, please add an environment variable `OPENAI_API_KEY` which contains it, or pass  `openai_api_key` as a named parameter. (type=value_error)"
    - run ```deactivate``` in your terminal and run ```pipenv again```

created by Tango Tew