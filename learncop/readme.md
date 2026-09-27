# Learn Copilot Documentation

## 1. Project Overview

Learn Copilot is an AI-powered personal knowledge assistant. It allows users to upload learning materials (PDFs, Markdown, Text), generates visual knowledge graphs to show connections between concepts, and (in the future) provides adaptive learning paths, assessments, and spaced repetition practice.

## 2. Current Implementation Details
  

### 2.1 Authentication & User Management

*   **Mechanism:** Local Authentication (No backend server).

*   **Storage:** `localStorage` key `learn_copilot_users`.

*   **Logic:**

    *   **Registration:** Checks if username exists. If unique, saves `User` object (id, username, password, avatar).

    *   **Login:** Matches username/password against stored array.

    *   **Session:** State is held in `App.tsx`. Reloading the page requires re-login (for security in this demo), but data persists.

  

### 2.2 Data Persistence

*   **Mechanism:** `localStorage` + JSON Export/Import.

*   **Storage Key:** `learn_copilot_data_{userId}`.

*   **Structure:**

    *   `KnowledgeBase`: Represents a subject (e.g., "Biology"). Contains metadata and a list of `KnowledgeFile`s.

    *   `GraphData`: Stored directly inside the `KnowledgeBase` object to persist the generated node structure.

  

### 2.3 Knowledge Graph Generation (The Core AI Feature)

This feature converts unstructured text into a structured node-link diagram.

  

*   **Step 1: Aggregation:** All text content from files in a Knowledge Base is concatenated.

*   **Step 2: Prompt Engineering:** We send a prompt to **Gemini 1.5 Flash**.

    *   *Prompt Logic:* "Analyze these materials. Identify key concepts as 'nodes' (types: concept, fact, example). Identify relationships as 'edges'. Assign X/Y coordinates for a canvas."

    *   *Schema:* We enforce a JSON response schema ensuring `nodes` have `{id, label, type, x, y}` and `edges` have `{source, target, label}`.

*   **Step 3: Rendering:** The returned JSON is parsed and rendered in `pages/Graph.tsx` using SVG for edges and HTML `div`s for nodes.

  

---

  

## 3. Future Module Implementation Plans

  

### 3.1 Learning Path (`pages/LearningPath.tsx`)

*   **Goal:** Convert the non-linear Knowledge Graph into a linear, step-by-step curriculum.

*   **Implementation Strategy:**

    1.  **Input:** The existing `GraphData` (nodes/edges).

    2.  **Algorithm/AI:**

        *   *Option A (Algorithmic):* Perform a Topological Sort on the Directed Acyclic Graph (DAG) to find dependencies.

        *   *Option B (AI):* Send the Node list to Gemini with the prompt: "Order these concepts from beginner to advanced. Group them into modules."

    3.  **Data Structure:**

        ```typescript

        interface LearningModule {

            id: string;

            title: string; // e.g., "Module 1: Basics"

            nodeIds: string[]; // Concepts covered

            status: 'locked' | 'active' | 'completed';

        }

        ```

    4.  **UI:** A vertical timeline or roadmap view. Clicking a step opens the associated notes/files for that concept.

  

### 3.2 Assessment / Testing (`pages/Assessment.tsx`)

*   **Goal:** Active recall testing for specific concepts.

*   **Implementation Strategy:**

    1.  **Trigger:** User clicks "Test Me" on a specific Node in the graph or Learning Path.

    2.  **Generation:** Send Node context + Source file content to Gemini.

        *   *Prompt:* "Generate a Socratic question about [Concept] based on this text. Do not reveal the answer."

    3.  **Evaluation:**

        *   User types an answer.

        *   System sends (User Answer + Source Text) to Gemini.

        *   *Prompt:* "Grade this answer on a scale of 0-100 based on accuracy to the source text. Provide constructive feedback."

    4.  **Storage:** Save result `{nodeId, score, date}` to `Analytics` storage.

  

### 3.3 Practice / Spaced Repetition (`pages/Practice.tsx`)

*   **Goal:** Ensure long-term retention using Spaced Repetition System (SRS).

*   **Implementation Strategy:**

    1.  **Algorithm:** Use a simplified SM-2 algorithm.

        *   If user answers correctly: Next review interval = Current Interval * Multiplier (e.g., 2.5).

        *   If wrong: Reset interval to 1 day.

    2.  **Queue Generation:**

        *   On app load, check all stored "Assessment Results".

        *   Filter: `Where (LastReviewDate + Interval) <= Today`.

        *   Show these items in the "Due Today" section.

  

### 3.4 Analytics (`pages/Analytics.tsx`)

*   **Goal:** Visualize progress and gaps.

*   **Implementation Strategy:**

    1.  **Data Aggregation:** Calculate stats from the user's saved data.

    2.  **Metrics:**

        *   *Total Study Time:* Sum of time spent in app (needs a timer context).

        *   *Mastery:* Average of most recent test scores for all Nodes.

        *   *Retention:* Percentage of Practice items answered correctly on the first try.

    3.  **Visualization:** Use charts (or simple CSS bars) to show Mastery vs. Time.