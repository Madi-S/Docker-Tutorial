FROM node:alpine

WORKDIR /app

EXPOSE 3000

# Copy package.json and package-lock.json
COPY package*.json ./

RUN npm install

# Recommended to run dependencies before copying scripts for faster image building (cached dependencies)
COPY . ./

CMD ["npm", "start"]