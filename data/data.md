# Data
## Enum Adaptation
## Enum Movement
## Enum Equipment
## Enum Difficulty
## Enum PeriodType
- Microcycle
- Macrocycle
- Mesocycle
## Volume
- Reps: int
- Weight: double
- Unit: String
## Muscle
## Exercise
- Name: String
- Demonstration: String (URL)
- PrimeMover: Muscle
- Synergists: List<Muscle>
- Adaptation: Adaptation
- Movement: Movement
- Tags: List<Tags>
- Equipment: Equipment
- Difficulty: Difficulty
- Instructions: String
- Description: String
- Notes: String
- Progression: Exercise
- Regression: Exercise
## Line
- id: int
- exercise: Exercise
- cells: List<Cell>
## Block
- Title: String
- Date: DateTime
- Purpose: String
- Description: String
- Lines: List<Line>
- Tags: List<Tags>
## Workout
- Name: String
- Date: Date
- Exercises: List<Exercise>
- Blocks: List<Block>
- Sets: Volume
- Notes: String
## Period - can be thought of as week containing workouts
- Name: String
- PeriodType: PeriodType
- Workouts: List<Workout>
## Program
- Name: String
- Periods: List<Period>
