from crewai import Task

from agents import thinker

# Define a task with a description and expected output
conflict_task = Task(
    description=(
        "Find if there are any conflicting statement/information in the given text. \n text:{text}"
    ),
    expected_output="Respond with 'conflicting statements' / 'no conflicting statements'",
    agent=thinker,
)

