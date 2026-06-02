# CODSOFT
Rule-Based  Chatbot production-ready, modular Python command-line conversational agent designed to route user queries using advanced pattern matching. The architecture implements Regular Expressions (Regex) for robust intent classification, manages active response routing through structured conditional logic, and features a built-in automated NLP evaluation test suite to verify classification accuracy.

System Prerequisites
--
Python Version: Python 3.10 or higher.

Dependencies: None. This system uses pure, standard library Python utilities (re, random, datetime) to guarantee optimal execution speed and zero third-party vulnerability risk.

Installation & Local Usage
--
Clone or Download the Script:
Save the provided Python code into a local file named chatbot.py.

Execute the Application:
--
Run the terminal instance via your command prompt or terminal window:python chatbot.py

Architecture Overview:-
--
The codebase is split into four strict operational sections to keep data separate from execution:
 1. Knowledge Base (Training Data)  --> Dict objects containing static responses and precompiled regex patterns.
 2. Core Conversation Engine      --> Normalization functions and the main if-else classification router.
 3. NLP Evaluation Test Suite      --> Pipeline simulation verifying actual vs. expected intent classification.
 4. Runtime System Interface       --> Low-latency command-line input-output l

Evaluation Test Suite Output Example
--
When you run the file, the built-in validation layer processes test data against your patterns and prints a performance report directly to the terminal console:-text

=== RUNNING AUTOMATED NLP EVALUATION TESTS ===

✅ PASSED | Input: 'Hey there bot!' -> Detected: greet

✅ PASSED | Input: 'What time is it right now?' -> Detected: time

✅ PASSED | Input: 'Recommend a good sci-fi movie' -> Detected: movie
...

=== TEST COMPLETE | Intent Detection Accuracy: 100.0% ===

--- Real-Time chatbot Engine Activated ---

Type 'exit' or 'bye' to close the terminal session.
