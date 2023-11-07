// 3.1
function createPoint(x, y) {
    // Приватные переменные для хранения координат
    let pointX = x;
    let pointY = y;
  
    // get X/Y
    function getX() {
      return pointX;
    }
    function getY() {
      return pointY;
    }
  
    // Перенос точки
    function translate(dx, dy) {
      pointX += dx;
      pointY += dy;
    }
  
    // Масштабирование точки
    function scale(factor) {
      pointX *= factor;
      pointY *= factor;
    }
  
    // Возвращаем объект с публичными методами
    return {
      getX,
      getY,
      translate,
      scale,
    };
  }
  
  
  const point = createPoint(2, 3); // Примерчик
  console.log(point.getX()); // Выведет 2
  console.log(point.getY()); // Выведет 3
  // И т.д. и т.п. 


// 3.2
class Point {
    constructor(x, y) {
      this.x = x;
      this.y = y;
    }
  
    getX() {
      return this.x;
    }
  
    getY() {
      return this.y;
    }
  
    translate(dx, dy) {
      this.x += dx;
      this.y += dy;
    }
  
    scale(factor) {
      this.x *= factor;
      this.y *= factor;
    }
  }
  

  const tochka = new Point(2, 3); // Примерчик
  tochka.scale(2);

  console.log(tochka.getX()); // Выведет 6
  console.log(tochka.getY()); // Выведет 10


// 3.3
class Random {
    static nextDouble(low, high) {
      return Math.random() * (high - low) + low;
    }
  
    static nextInt(low, high) {
      return Math.floor(Math.random() * (high - low + 1)) + low;
    }
  
    static nextElement(array) {
      const randomIndex = Math.floor(Math.random() * array.length);
      return array[randomIndex];
    }
  }
  
  // Использование
  const low = 1;
  const high = 10;
  const array = [1, 2, 3, 4, 5];
  
  const randomDouble = Random.nextDouble(low, high);
  const randomInt = Random.nextInt(low, high);
  const randomElement = Random.nextElement(array);
  
  console.log(randomDouble); // Выведет случайное число с плавающей точкой в диапазоне [low, high]
  console.log(randomInt); // Выведет случайное целое число в диапазоне [low, high]
  console.log(randomElement); // Выведет случайный элемент из заданного массива