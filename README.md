# Tic_Tac_ToeAI
Tic-Tac-Toe AI: Implement an AI agent that plays Tic-Tac-Toe optimally using game tree search algorithms such as Minimax with alpha-beta pruning. Explore different heuristic functions to improve the AI's performance.

<h1 align="center"> Tic-Tac-Toe: AI with Minimax & Alpha-Beta Pruning </h1>
<p align="center">
<img alt="Languages" src="https://img.shields.io/github/languages/count/mubtasim-fuad/Tic_Tac_ToeAI">
<img alt="Repository size" src="https://img.shields.io/github/repo-size/mubtasim-fuad/Tic_Tac_ToeAI">
<img alt="Contributors" src="https://img.shields.io/github/contributors/mubtasim-fuad/Tic_Tac_ToeAI">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/mubtasim-fuad/Tic_Tac_ToeAI">
</p>

## Project Overview
This project implements a classic command-line Tic-Tac-Toe game featuring an unbeatable Artificial Intelligence (AI) opponent. It serves as a practical demonstration of fundamental AI search algorithms, specifically Minimax with Alpha-Beta Pruning, and the application of heuristic evaluation for performance optimization. Players can engage in a game against an optimally playing AI and explore the impact of search depth and heuristics on decision-making efficiency.

## Core AI Concepts & Features
This project highlights the following key AI principles and features:

Human vs. AI Gameplay: Facilitates a standard Tic-Tac-Toe match against an intelligent opponent.

Minimax Algorithm: Constitutes the AI's decision-making core, ensuring optimal play through exhaustive search of the game tree to determine the most advantageous move.

Alpha-Beta Pruning: An optimization technique applied to the Minimax algorithm, significantly reducing the number of nodes evaluated in the game tree without compromising the optimality of the final decision. This demonstrates efficiency improvements in state-space search.

Optional Heuristic Evaluation: Provides an adjustable mode enabling the AI to utilize a heuristic function for accelerated decision-making by limiting search depth. This feature illustrates the inherent trade-off between computational speed and absolute optimality.

Command-Line Interface (CLI): Offers a straightforward and direct interface for user interaction.

Modular Design: Employs a clean and well-structured codebase, ensuring clear separation of game logic from AI algorithms.

## 📦 Project Structure
```
project/
│
├── main.py
├── support/
│   ├── game.py
│   └── ai.py
├── presentation/
│   ├── Update Report.docx
│   ├── update presentation.pptx
````
### 
main.py
Game Orchestration: Manages the overall game flow, encompassing initialization, user input prompts (e.g., choosing X or O), and turn-based execution.

Heuristic Mode Control: Prompts the user to enable or disable the heuristic-based AI evaluation, thereby demonstrating flexibility in AI strategy selection.

### Support/game.py
print_board(board): Responsible for the console-based visual representation of the Tic-Tac-Toe board, ensuring clear display of the current game state.

player_move(board, human_player): Handles human player input, including validation to ensure moves are placed on valid, unoccupied tiles.

ai_move(board, ai_player, use_heuristic=False): Interfaces with the AI module (support/ai.py) to determine and execute the AI's move, conditionally applying the heuristic strategy.

### Support/ai.py
check_winner(board): A utility function that evaluates the current board state to ascertain the presence of a winner, a draw, or if the game remains ongoing. This function is fundamental for terminal state detection within the Minimax algorithm.

heuristic(board, player): Implements the heuristic evaluation function. This function assigns a numerical score to a given board state, providing an estimated desirability for a specific player without requiring a full search. It is crucial for the optional heuristic mode.

minimax(board, depth, is_maximizing_player, alpha, beta, use_heuristic): Represents the core of the AI's intelligence. This function recursively explores the game tree:

It evaluates all feasible future moves.

It employs Alpha-Beta Pruning to efficiently truncate branches of the search tree that cannot yield a superior outcome, thereby significantly accelerating the decision-making process.

It integrates the heuristic function when use_heuristic is set to true, limiting the search depth and providing a faster, though potentially sub-optimal, move.

## 🚀 How to Run
1. Clone the repository
git clone https://github.com/mubtasim-fuad/Tic_Tac_ToeAI.git
cd Tic_Tac_ToeAI

2. Run the game
python main.py

🕹️ How to Play
Choose Your Side: Upon initiating the game, you will be prompted to select your desired marker: X or O.

Board Reference: The game board is visually presented using numerical positions 1-9 for intuitive input. Consult the following layout for guidance on move placement:

## 🧪 Sample Board Position Reference

```text
Board positions:
 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
```

Make Your Move: During your turn, input a number from 1 to 9 corresponding to the empty tile where you intend to place your marker.

AI's Optimal Play: The AI, driven by the Minimax algorithm, will execute its move optimally, striving for a win or a draw.

##⚙️ Heuristic Mode (Optional)
At the commencement of each game, you will be queried regarding the activation of the heuristic mode:

Limit search depth using a heuristic evaluation? (y/n): y

This option facilitates observation of the performance implications associated with employing a heuristic:

Select y to enable heuristic-based evaluation at a constrained search depth. This significantly expedites the AI's decision-making, illustrating how heuristics can achieve satisfactory performance in larger state spaces where exhaustive full-depth search is computationally prohibitive.

Select n to instruct the AI to perform full-depth Minimax with Alpha-Beta Pruning. This guarantees perfect play but may result in marginally longer processing times, particularly in scenarios with larger game trees.

## 📚 Requirements
Python 3.6+

No reliance on third-party libraries; utilizes solely the Python standard library, ensuring high portability.

## 📈 Future Improvements
Graphical User Interface (GUI): Enhance the user experience by developing a visual interface utilizing libraries such as pygame or tkinter.

Online Multiplayer Mode: Implement network capabilities to enable two human players to compete over a network.

Difficulty Levels: Introduce varied AI difficulty levels by adjusting the search depth for Minimax or refining the heuristic function.

Score Tracking: Integrate persistent score tracking functionality to record wins, losses, and draws across multiple game sessions.

## Team Members

| Student ID   | Name                        |
|--------------|-----------------------------|
| 2131200042   | Miwan Sariana Saqib           |
| 2022122042   | Md. Mubtasim Fuad Arnob       |
| 2121025642   | Redwan Hossain                |
| 2122119642   | Md. Naimul Hasan Munna        |


**Faculty Supervisor**: Mohammad Shifat-E-Rabbi  
**Department**: Department of Electrical and Computer Engineering  
**University**: North South University
</div>
