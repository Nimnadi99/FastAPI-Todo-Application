<h1>📝 FastAPI Todo Application</h1>
<br/>
<i>This project is a simple CRUD (Create, Read, Update, Delete) application built with FastAPI. It allows users to manage tasks with features such as adding, updating, deleting, and retrieving tasks from a SQLite database.</i>
<br/>

<h3>🌟 Features <br/></h3>
<ul>
  <li>Create Tasks ➕: Add new tasks with a task description and completion status.</li>
  <li>Read Tasks 📖: View all tasks or a specific task by its ID.</li>
  <li>Update Tasks ✏️: Modify task details such as description and completion status.</li>
  <li>Delete Tasks 🗑️: Remove tasks either individually or all at once.</li>
</ul>

<br/>
<h3>📁 Project Structure<br/></h3>
<ul>
  <li><b>todo/database.py</b>: Contains database connection logic and SQLAlchemy configurations.</li>
  <li><b>todo/models.py</b>: Defines the database model for the tasks.</li>
  <li><b>todo/schemas.py</b>: Defines the Pydantic schema for validating request data.</li>
  <li><b>todo/main.py</b>: Contains the FastAPI application with routes for CRUD operations.</li>
  <li><b>todo.db</b>: SQLite database file for storing tasks.</li>
  <li><b>requirements.txt</b>: Lists the dependencies required for the project.</li>
</ul>

<br/>
<h3>🙏 Acknowledgments<br/></h3>
<ul>
  <li>Thanks to the FastAPI community for providing an efficient and easy-to-use framework for building APIs.</li>
  <li>Special thanks to the SQLAlchemy team for creating a robust ORM for database management.</li>
</ul>
