<h1>📝 FastAPI Todo Application</h1>
<br/>
<i>This project is a comprehensive CRUD (Create, Read, Update, Delete) application built with FastAPI. It enables users to manage tasks with features such as adding, updating, deleting, and retrieving tasks from a SQLite database. The application also includes JWT token-based authentication for secure user login and task management.</i>
<br/>

<h3>🌟 Features <br/></h3>
<ul>
  <li>Create Tasks ➕: Add new tasks with a task description and completion status.</li>
  <li>Read Tasks 📖: View all tasks or a specific task by its ID.</li>
  <li>Update Tasks ✏️: Modify task details such as description and completion status.</li>
  <li>Delete Tasks 🗑️: Remove tasks either individually or all at once.</li>
  <li>User Authentication 🔐: Secure user login and JWT token-based authentication for protected routes.</li>
</ul>

<br/>
<h3>📁 Project Structure<br/></h3>
<ul>
  <li><b>todo/database.py</b>: Contains database connection logic and SQLAlchemy configurations.</li>
  <li><b>todo/models.py</b>: Defines the database models for users and tasks.</li>
  <li><b>todo/schemas.py</b>: Defines the Pydantic schemas for validating request data.</li>
  <li><b>todo/main.py</b>: Contains the FastAPI application with routes for CRUD operations and user authentication.</li>
  <li><b>todo/routers/</b>: Contains route handlers for authentication (`authentication.py`), user management (`user.py`), and task management (`todo.py`).</li>
  <li><b>todo.db</b>: SQLite database file for storing tasks and user information.</li>
  <li><b>requirements.txt</b>: Lists the dependencies required for the project.</li>
</ul>

<br/>
<h3>🙏 Acknowledgments<br/></h3>
<ul>
  <li>Thanks to the FastAPI community for providing an efficient and easy-to-use framework for building APIs.</li>
  <li>Special thanks to the SQLAlchemy team for creating a robust ORM for database management.</li>
  <li>Gratitude to the Passlib and Python-Jose libraries for their contributions to password hashing and JWT handling, respectively.</li>
</ul>
