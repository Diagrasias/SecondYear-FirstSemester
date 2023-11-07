//2.1
function calculateAverage(data) {
    if (data.length === 0) {
      return 0;
    }
  
    var sum = 0;
    for (var i = 0; i < data.length; i++) {
      sum += data[i];
    }
  
    var average = sum / data.length;
    return average;
  }


  //2.2
  const checkEvenOdd = (data) => (data % 2 === 0 ? "Even" : "Odd");


  //2.3
  const getCentury = (data) => Math.ceil(data / 100);


  //2.4
  const reverseDigits = (data) => {
    const digits = String(data).split('');
    return digits.reverse().map(Number);
  };


  //2.5
  const countDivisors = (data) => {
    let count = 0;
    for (let i = 1; i <= data; i++) {
      if (data % i === 0) {
        count++;
      }
    }
    return count;
  };


  //2.6
  const divisors = (data) => {
    const result = [];
    
    for (let i = 2; i < data; i++) {
      if (data % i === 0) {
        result.push(i);
      }
    }
  
    if (result.length === 0) {
      return `${data} является простым`;
    } else {
      return result;
    }
  };


  //2.7
  const findNextSquare = (data) => {
    const squareRoot = Math.sqrt(data);
    if (Number.isInteger(squareRoot)) {
      const nextSquare = Math.pow(squareRoot + 1, 2);
      return nextSquare;
    } else {
      return -1;
    }
  };


//2.8
const isTriangle = (data) => {
    const [a, b, c] = data;
    if (a + b > c && a + c > b && b + c > a) {
      return true;
    } else {
      return false;
    }
  };


//2.9
const isMountainLinear = (data) => {            // Функция для проверки, является ли массив горным с помощью линейного поиска
    const arr = data;
    const n = arr.length;

    if (n < 3) {
      return false;
    }
    let i = 0;
    
    while (i < n - 1 && arr[i] < arr[i + 1]) {          // Поиск пика
      i++;
    }
    
    if (i === 0 || i === n - 1) {           // Проверка условий для горного массива
      return false;
    }
    
    while (i < n - 1 && arr[i] > arr[i + 1]) {
      i++;
    }
    
    return i === n - 1;
  };


const findMountainPeakBinary = (data) => {          // Функция для нахождения индекса пика в горном массиве с помощью бинарного поиска
    const arr = data;
    const n = arr.length;
    
    let left = 0;
    let right = n - 1;
    
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      
      if (arr[mid] < arr[mid + 1]) {
        left = mid + 1;
      } else {
        right = mid;
      }
    }
    
    return left;
  };

  
  //2.10
  const countSmallerElements = (data) => {          
    const nums = data;
    const n = nums.length;
    const counts = new Array(n).fill(0);
    const sortedNums = [];
  
    for (let i = n - 1; i >= 0; i--) {
      const num = nums[i];
      const insertionIndex = findInsertionIndex(sortedNums, num);
      counts[i] = insertionIndex;
      sortedNums.splice(insertionIndex, 0, num);
    }
  
    return counts;
  };
  
  const findInsertionIndex = (arr, target) => {
    let left = 0;
    let right = arr.length;
  
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (arr[mid] >= target) {
        right = mid;
      } else {
        left = mid + 1;
      }
    }
  
    return left;
  };


  //Важное примечание:

 //         _._     _,-'""`-._
 //         (,-.`._,'(       |\`-/|
 //             `-.-' \ )-`( , o o)
 //                  `-    \`_`"'-