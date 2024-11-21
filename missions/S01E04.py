from S01E01 import get_answer
import json
import re
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

    question = """Propose a path for the robot to reach the goal at F4 from its starting position at A4. The robot must avoid forbidden fields: B1, B3, B4, D2, D3. Don't confuse UP with RIGHT and DOWN with LEFT.
    """

    content = """
    You are a robot navigating a grid. The grid has columns labeled A to F and rows numbered 1 to 4. Your starting position is at the bottom-left corner, A4. The goal is to reach the bottom-right corner, F4. 

    ### Movement Rules:
    1. **UP**: Move up by decreasing the row number. Example: From A4, UP moves you to A3. FROM 1 points You cant go UP because you are at the top of the grid.
    2. **DOWN**: Move down by increasing the row number. Example: From A4, DOWN moves you to A5. FROM 4 points You cant go DOWN because you are at the bottom of the grid.
    3. **RIGHT**: Move right by increasing the column letter. Example: From A4, RIGHT moves you to B4. FROM A points You cant go LEFT because you are the left of the grid.
    4. **LEFT**: Move left by decreasing the column letter. Example: From B4, LEFT moves you to A4. FROM F points You cant go RIGHT because you are the right of the grid.
    For each step provide detailed breakdown of the made decisions

    ### Forbidden Fields:
    The robot must avoid these fields: B1, B3, B4, D2, D3. You cannot move to these positions under any circumstances.

    ### Example Scenarios:
    Start: A4
    Goal: C4
    Forbidden Fields: B4
    Points in Path: A4, A3, B3, C3, C4

    <RESULT> { "steps": "UP, RIGHT, RIGHT, DOWN" } </RESULT>

    Start: A4
    Goal: F4
    Forbidden Fields: B1, B3, B4, D2, D3
    Points in Path: A4, A3, A2, B2, C2, C3, C4, D4, E4, F4


    ### Task:
    Solve the following scenario:
    Start: A4
    Goal: F4
    Forbidden Fields: B1, B3, B4, D2, D3
    Points in Path: A4, A3, A2, B2, C2, C3, C4, D4, E4, F4

    Provide the solution in the following format:
    <RESULT>
    {
    "steps": "..."
    }
    </RESULT>
    """

    

    answer = get_answer(question, content)
    print(answer)