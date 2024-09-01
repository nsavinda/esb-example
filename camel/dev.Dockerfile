# Use an official Gradle image with JDK as the environment
FROM gradle:8.1.1-jdk17

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Install additional dependencies or perform setup
# You might want to add configurations or scripts here if needed

# Expose the port on which the application will run
EXPOSE 8080

# Set up the command to run your application with Gradle's continuous build
ENTRYPOINT ["gradle", "--continuous", "run", "--args='--server.port=8080'"]
