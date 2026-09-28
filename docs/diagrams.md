# Quiz Master Diagrams

## Use Case Diagram — Player Actions and Quiz Services

```mermaid
flowchart LR
  Player([Player])
  subgraph QuizMaster[Quiz Master]
    Play((Play quiz))
    Stats((View performance))
    Board((View leaderboard))
    Browse((Browse categories and difficulty))
    Help((Read rules))
    Exit((Exit safely))
    Persist[(JSON storage)]
  end
  Player --> Play
  Player --> Stats
  Player --> Board
  Player --> Browse
  Player --> Help
  Player --> Exit
  Play --> Persist
  Stats --> Persist
  Board --> Persist
```

## Component Diagram — Module Collaborations

```mermaid
classDiagram
  class MainWorkflow
  class UserInterface
  class QuizEngine
  class QuestionManager
  class Scoring
  class Performance
  class Leaderboard
  class JsonStorage
  MainWorkflow --> UserInterface
  MainWorkflow --> QuizEngine
  QuizEngine --> QuestionManager
  QuizEngine --> Scoring
  MainWorkflow --> Performance
  MainWorkflow --> Leaderboard
  QuestionManager --> JsonStorage
  Performance --> JsonStorage
  Leaderboard --> JsonStorage
```

## Data Storage Design — Local JSON Records

```mermaid
erDiagram
  QUESTION ||--o{ QUIZ_ATTEMPT : appears_in
  PLAYER ||--o{ QUIZ_ATTEMPT : makes
  QUESTION {
    string id
    string question
    object options_ABCD
    string answer
    string category
    string difficulty
  }
  PLAYER {
    string player_name
  }
  QUIZ_ATTEMPT {
    int questions_attempted
    int correct
    int incorrect
    int score
    int max_score
    float accuracy
    string timestamp_utc
    string category
    string difficulty
  }
```

The diagram names mirror the actual JSON fields and Python module boundaries. The JSON files are arrays of question or attempt objects; there is no separate player database.
