//1.1
function sumAngles(angle1, angle2) {
  angle1 = angle1 % 360;
  angle2 = angle2 % 360;
  return (angle1 + angle2) % 360;
}
console.log(sumAngles(135, 270));  // Выводить будет 135, т.к. 135 + 270 = 405, а 405 % 360 = 45


//1.2
alphabets = 'abcdefghijklmnopqrstuvwxyz'.split("");
const isPangram = (string) => {
    string = string.toLowerCase();
    return alphabets.every(x => string.includes(x));
}
console.log(isPangram("Detect Pangram"));
console.log(isPangram("abcd efgh ijkl mnop qrst uvwx yz"));


//1.3
function getMiddle(s) {
  var even, odd, centerLetter, arrLetter;
  if (s.length % 2 == 0) {
    centerLetter = (Math.round(s.length / 2));
  } else {
    centerLetter = (Math.round(s.length / 2)) - 1;
  }
  arrLetter = s.split("");
  if (s.length % 2 == 0) {
    return arrLetter[centerLetter - 1] + arrLetter[centerLetter];
  } else {
    return arrLetter[centerLetter];
  }
}
console.log(getMiddle("test")); //es
console.log(getMiddle("testing")); //t
console.log(getMiddle("middle")); //dd
console.log(getMiddle("A")); //A


//1.4
const arr = [1,2,'aasf','1','123',123];
const numbers = arr.filter( element => typeof element === 'number');
console.log(numbers);


//1.5
function solution(string) {
  let splitStr = string.split("");
  let newStr = string.split("");
  let capStr = string.toUpperCase().split("");
  for (i = 0; i < splitStr.length; i++) {
    if (splitStr[i] === capStr[i]) {
      newStr.splice(i, 0, ' ');
    }
  }
  return newStr.join("");
}
console.log('camelCasing: ', solution('camelCasing'));
console.log('camelCasingTest: ', solution('camelCasingTest'));