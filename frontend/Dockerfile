# Use the Node.js image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy the frontend code (myapp) to the container
COPY ./myapp /app

# Install dependencies
RUN npm install

# Expose port 3000 for the React app
EXPOSE 3000

# Command to start the React server
CMD ["npm", "start"]
