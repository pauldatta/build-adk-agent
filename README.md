# Meeting Notes Agent

This project contains an ADK agent that helps you transcribe and summarize audio files into meeting notes.

## Description

The agent is designed to be a helpful assistant for anyone who needs to process audio recordings of meetings. It uses the Gemini 2.5 Pro model to perform the transcription and summarization, and it interacts with the user to get the necessary information.

The agent has the following capabilities:
*   It can ask the user for the path to an audio file.
*   It can transcribe the audio file using the Gemini API.
*   It saves the raw transcript to `transcript.txt`.
*   It generates a structured and detailed meeting notes document.
*   It saves the final meeting notes to `meeting_notes.md`.
*   It proactively displays the generated meeting notes to the user.
*   It can display the full transcript upon request.

## Project Structure

The project is organized as a standard ADK agent project:

-   `meeting_notes_agent/`: The core Python package for the agent.
    -   `agent.py`: Defines the main agent, its model, tools, and instructions.
    -   `tools/`: Contains the individual tools the agent uses.
    -   `tests/`: Contains the unit tests for the tools.
    -   `adk.mod.json`: The ADK module file that registers the agent's tools.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `.gitignore`: Specifies files and directories to be ignored by Git.
-   `development_notes.md`: Contains notes on the development process and lessons learned.
-   `integration_blueprint.md`: The design document for the agent.
-   `tdd_plan.md`: The test-driven development plan.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv .venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate
    ```

4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Set up your API key:**
    Create a copy of the sample environment file:
    ```bash
    cp .env.sample .env
    ```
    Then, open the `.env` file and add your Google API key:
    ```
    GOOGLE_API_KEY="YOUR_API_KEY"
    ```

## How to Run

To run the agent, execute the following command from the project root:

```bash
./.venv/bin/adk run ./meeting_notes_agent "transcribe and summarize my meeting"
```

The agent will then ask you for the path to the audio file. Once you provide the path in a subsequent message, it will process the file, save the transcript and notes, and then display the notes for you.
