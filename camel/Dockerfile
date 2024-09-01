# Use an official Gradle image as a build environment
FROM gradle:8.1.1-jdk17 as build

# Set the working directory inside the container
WORKDIR /app

# Copy the project files to the container
COPY . .

# Build the project using Gradle
# RUN gradle clean build -x test
RUN gradle clean shadowJar


# Use an official OpenJDK image as the runtime environment
FROM openjdk:17-jdk-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the built application from the build stage
COPY --from=build /app/build/libs/camel-1.0-SNAPSHOT.jar /app/app.jar

# Expose the port on which the application will run
EXPOSE 8080

# Define the command to run your application
CMD ["java", "-jar", "/app/app.jar"]
