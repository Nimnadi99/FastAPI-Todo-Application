<h1>📝 FastAPI Todo Application</h1>
<br/>
<i>This project is a comprehensive CRUD (Create, Read, Update, Delete) application built with FastAPI. It allows users to manage tasks with features such as adding, updating, deleting, and retrieving tasks from a SQLite database. The application also includes secure authentication using JWT tokens for user management.</i>
<br/>

<h3>🌟 Features</h3>
<ul>
  <li>➕ <b>Create Tasks</b>: Add new tasks with a task description and completion status.</li>
  <li>📖 <b>Read Tasks</b>: View all tasks or a specific task by its ID.</li>
  <li>✏️ <b>Update Tasks</b>: Modify task details such as description and completion status.</li>
  <li>🗑️ <b>Delete Tasks</b>: Remove tasks either individually or all at once.</li>
  <li>🔐 <b>User Authentication</b>: Secure endpoints with JWT token-based authentication.</li>
  <li>🔄 <b>Task Management</b>: Manage tasks with the option to mark them as completed or ongoing.</li>
</ul>

<br/>
<h3>📁 Project Structure</h3>
<ul>
  <li>📂 <b>todo/database.py</b>: Contains database connection logic and SQLAlchemy configurations. This file initializes the SQLite database and sets up the session for querying tasks and users.</li>
  <li>📂 <b>todo/models.py</b>: Defines the database models for users and tasks. The <code>Task</code> model represents the tasks, and the <code>User</code> model is for storing user credentials.</li>
  <li>📂 <b>todo/schemas.py</b>: Defines the Pydantic schemas for validating request data. This includes input validation for creating and updating tasks, user registration, and login.</li>
  <li>📂 <b>todo/main.py</b>: Contains the FastAPI application with routes for CRUD operations on tasks and authentication endpoints. It integrates all the routes and ensures the application runs properly.</li>
  <li>📁 <b>todo/routers/</b>: Contains route handlers for:
    <ul>
      <li>🔑 <b>authentication.py</b>: Handles JWT-based login and authentication endpoints.</li>
      <li>👤 <b>user.py</b>: Manages user-related actions like registration, login.</li>
      <li>📋 <b>todo.py</b>: Manages task-related routes such as creating, updating, deleting, and retrieving tasks.</li>
    </ul>
  </li>
  <li>💾 <b>todo.db</b>: SQLite database file for storing tasks and user information.</li>
  <li>📜 <b>requirements.txt</b>: Lists the dependencies required for the project, including FastAPI, SQLAlchemy, Passlib, Python-Jose, and others.</li>
</ul>

<br/>
<h3>⚙️ Installation and Setup</h3>
<ul>
  <li>📥 Clone the repository</li>  
  
  <li>📂 Navigate to the project directory</li>
  
  <li>🔧 Install the required dependencies</li>
  
  <li>🚀 Run the FastAPI application</li>
  
  <li>🌐 The application will be running at: <b>http://127.0.0.1:8000</b></li>
</ul>

<br/>
<h3>💡 Usage</h3>
<ul>
  <li>🌍 Once the application is running, you can interact with the API using tools like <b>Swagger UI</b> (automatically available at <b>http://127.0.0.1:8000/docs</b>).</li>
  
  <li>🔑 For accessing secure endpoints, you must authenticate with a JWT token. You can obtain a token by making a POST request to the <code>/login</code> endpoint with your username and password.</li>
  
  <li>📝 Example of authentication:</li>
  <pre>POST http://127.0.0.1:8000/login</pre>
  <pre>
  {
    "username": "user1",
    "password": "password123"
  }
  </pre>
  
  <li>✅ Upon successful authentication, the API will return a JWT token, which you can use in the <code>Authorization</code> header for further requests.</li>
</ul>

<h3>📑 API Endpoints</h3>
<ul>
  <li>📝 <b>POST /register</b>: Register a new user.</li>
  <li>🔑 <b>POST /login</b>: Login with a username and password to receive a JWT token.</li>
  <li>📋 <b>GET /tasks</b>: Retrieve all tasks. Requires JWT authentication.</li>
  <li>🔍 <b>GET /tasks/{task_id}</b>: Retrieve a specific task by ID. Requires JWT authentication.</li>
  <li>➕ <b>POST /tasks</b>: Create a new task. Requires JWT authentication.</li>
  <li>✏️ <b>PUT /tasks/{task_id}</b>: Update an existing task by ID. Requires JWT authentication.</li>
  <li>🗑️ <b>DELETE /tasks/{task_id}</b>: Delete a specific task by ID. Requires JWT authentication.</li>
  <li>🗑️ <b>DELETE /tasks</b>: Delete all tasks. Requires JWT authentication.</li>
</ul>

<br/>
<h3>🙏 Acknowledgments</h3>
<ul>
  <li>🌐 Thanks to the <b>FastAPI</b> community for providing an efficient and easy-to-use framework for building APIs.</li>
  <li>🔧 Special thanks to the <b>SQLAlchemy</b> team for creating a robust ORM for database management.</li>
  <li>💾 Gratitude to the <b>Passlib</b> and <b>Python-Jose</b> libraries for their contributions to password hashing and JWT handling, respectively.</li>
</ul>
