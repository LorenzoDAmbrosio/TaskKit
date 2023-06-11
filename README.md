# TaskKit

TaskKit is a task management system with social networking capabilities developed by Lorenzo D'Ambrosio. This system allows users to create an account from the index page and then navigate to the community screen, where they can view all the communities. In the account section, users can create new communities using the provided form. Once a community is created, users can add projects to it. Each project serves as a container for tasks, which can be viewed either in the containers or organized based on their status using the progress bar in the Planner page.

TaskKit is developed using HTML, JavaScript, Bootstrap, CSS, Python, Django framework, and utilizes an SQLite database.

## Features

- **User Registration:** Users can create an account by providing the required information.

- **Community Management:** Users can view all the communities and create new communities from the account section.

- **Project Management:** Users can add projects to communities, providing a way to organize tasks within a specific context.

- **Task Containers:** Tasks are organized within project containers, allowing users to easily manage and track progress.

- **Customizable Task Status:** For each project, users can add or delete task statuses, allowing for customized progression states.

- **Task Status Tracking:** Tasks can be viewed and organized based on their status using the progress bar in the Planner page. This helps users monitor task completion.

## Technologies Used

- Frontend: HTML, JavaScript, Bootstrap, CSS
- Backend: Python, Django framework
- Database: SQLite

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/LorenzoDAmbrosio/TaskKit.git
   ```

2. Navigate to the project directory:

   ```shell
   cd TaskKit
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Configure the database settings in the `settings.py` file to use SQLite.

5. Run the database migrations:

   ```shell
   python manage.py migrate
   ```

6. Start the development server:

   ```shell
   python manage.py runserver
   ```

7. Open your web browser and visit `http://localhost:8000` to access TaskKit.

## Usage

1. Register a new user account from the index page.

2. Log in with your credentials.

3. Navigate to the Community screen to view all the communities.

4. In the Account section, create a new community using the provided form.

5. Once a community is created, go to the Projects section and add projects to it.

6. Within each project, you can manage tasks in containers or organize them based on their status using the progress bar in the Planner page.

7. Customize the task statuses for each project as needed, allowing for personalized progression states.

## Default Users

TaskKit comes with two default users:

1. **LorenzoDambrosio** (Common User)
   - Username: LorenzoDambrosio
   - Password: StudLNZ2001

2. **Admin** (System Administrator)
   - Username: Admin
   - Password: StudLNZ2001

You can use these credentials to log in and explore the features of TaskKit.

## Contributing

Contributions to the TaskKit project are always welcome. If you find any issues or have suggestions for improvements, please open an issue on the GitHub repository. If you'd like to contribute code, you can fork the repository and create a pull request with your changes.

When contributing to this project, please follow the existing coding style and guidelines. Make sure to test your changes thoroughly before submitting a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

##

 Contact

For any questions or further assistance, please feel free to contact Lorenzo D'Ambrosio at lorenzo.dambrosio@stud.unifi.it.
