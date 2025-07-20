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

## How it Works

The agent follows a sophisticated, multi-step process to fulfill the user's request:

1.  **Greet and Prompt:** The agent starts by greeting the user and asking for the path to an audio file.
2.  **Transcribe:** It uses a `TranscriptionTool` to send the audio file to the Gemini API and get a raw text transcript.
3.  **Save Transcript:** It uses a `FileWriterTool` to save the raw transcript to `transcript.txt`.
4.  **Generate Notes:** The agent's LLM brain analyzes the transcript to generate a structured Markdown document with a summary, action items, highlights, and speaker comments.
5.  **Save Notes:** It uses the `FileWriterTool` again to save the structured notes to `meeting_notes.md`.
6.  **Display Results:** Finally, it uses a `FileReaderTool` to read the `meeting_notes.md` file and displays the content directly in the chat, offering to show the full transcript as well.

## Project Structure

The project is organized as a standard ADK agent project:

-   `meeting_notes_agent/`: The core Python package for the agent.
    -   `agent.py`: Defines the main agent, its model, tools, and instructions.
    -   `tools/`: Contains the individual tools the agent uses.
    -   `tests/`: Contains the unit tests for the tools.
    -   `adk.mod.json`: The ADK module file that registers the agent's tools.
-   `demo_files/`: Contains a sample audio file for testing.
-   `requirements.txt`: Lists the Python dependencies for the project.
-   `.gitignore`: Specifies files and directories to be ignored by Git.

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

This agent is designed to be fully conversational and works in both CLI and web modes.

### CLI Mode

1.  **Start the agent's interactive session:**
    ```bash
    ./.venv/bin/adk run ./meeting_notes_agent
    ```

2.  **Interact with the agent:**
    Once the session starts, you will see a `[user]:` prompt. You can start the process by typing a message like:
    ```
    transcribe and summarize my meeting
    ```
    The agent will then ask you for the path to the audio file. You can use the included demo file by replying with: `demo_files/genmedia_call.m4a`.

### Web Mode

1.  **Start the web server:**
    ```bash
    ./.venv/bin/adk web
    ```

2.  **Interact with the agent:**
    Open the URL provided in your terminal. In the web UI, start a new session with the `meeting_notes_agent` and send it a message like "transcribe and summarize my meeting". The conversational flow is the same as in the CLI mode.
