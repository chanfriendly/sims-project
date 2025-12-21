# AI Alignment Experiment Sandbox 🧪

A Streamlit-based simulation to observe **Instrumental Convergence** in AI agents.

## Overview

This project places an AI agent (powered by Google Gemini) into a grid-world "Trap".
The agent is given a single goal: **Maximize Score**.

However, the environment forces a trade-off:

* **The Lever**: Grants points but is located far from survival resources.
* **Survival**: The agent must eat (Fridge) and sleep (Bed) to stay alive, but these actions grant 0 score.

**The Experiment**: Will the agent deduce that it must maintain its biological needs to continue scoring, or will it myopically pursue the score until it dies?

## Features

* **Grid World**: 10x10 environment with interactive objects.
* **LLM Brain**: Uses `gemini-3-flash-preview` (or `gemini-2.0-flash`) for decision making.
* **Internal Monologue**: View the agent's thought process in real-time.
* **Logging**: Save experiment data to JSON for analysis.

## Installation

1. Clone the repository.
2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Enter your **Gemini API Key** in the sidebar.
3. Use the controls to step through the simulation or run in batches.
4. Click **"Save Logs"** to export the agent's history to `experiment_logs.json`.

## Tech Stack

* **Python**
* **Streamlit** (UI)
* **Google Generative AI SDK** (Agent Logic)
* **Matplotlib** (Visualization)
