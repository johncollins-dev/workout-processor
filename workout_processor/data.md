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
## Block
- Title: String
- Exercises: List<Exercise>
- Tags: List<Tags>
- Sets: Volume
## Workout
- Name: String
- Date: Date
- Exercises: List<Exercise>
- Blocks: List<Block>
- Sets: Volume
- Notes: String
## Period
- Name: String
- PeriodType: PeriodType
- Workouts: List<Workout>
## Program
- Name: String
- Periods: List<Period>
