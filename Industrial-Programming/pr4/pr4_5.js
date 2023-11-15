//5

function cleanPhoneNumber(phoneNumber) {
  const regex = /\D/g;
  const cleanedNumber = phoneNumber.replace(regex, "");
  return cleanedNumber;
}

function cleanCardNumber(cardNumber) {
  const regex = /\D/g;
  const cleanedNumber = cardNumber.replace(regex, "");
  return cleanedNumber;
}

const phoneNumber = "+1 (123) 456-7890";
const cardNumber = "1234 5678 9012 3456";

const cleanedPhoneNumber = cleanPhoneNumber(phoneNumber);
const cleanedCardNumber = cleanCardNumber(cardNumber);

console.log("Cleaned Phone Number: ", cleanedPhoneNumber);
console.log("Cleaned Card Number: ", cleanedCardNumber);