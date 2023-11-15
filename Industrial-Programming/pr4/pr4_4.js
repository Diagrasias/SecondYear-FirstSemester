//4

const emailRegex = /[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}/;
const urlRegex = /http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+/;

const email = "example@gmail.com";
const url = "https://www.google.com";

if (emailRegex.test(email)) {
  console.log("Email is valid");
} else {
  console.log("Email is not valid");
}

if (urlRegex.test(url)) {
  console.log("URL is valid");
} else {
  console.log("URL is not valid");
}