// Определяем объект Person
function Person(firstName, lastName) {
    this.firstName = firstName;
    this.lastName = lastName;
}

// Определяем функцию сравнения
function comparePeople(person1, person2) {
    // Сравниваем фамилии
    if (person1.lastName < person2.lastName) {
        return -1;
    }
    if (person1.lastName > person2.lastName) {
        return 1;
    }
    // Если фамилии совпадают, сравниваем имена
    if (person1.firstName < person2.firstName) {
        return -1;
    }
    if (person1.firstName > person2.firstName) {
        return 1;
    }
    // Если фамилии и имена совпадают, объекты равны
    return 0;
}

// Создаем объекты Person
let person1 = new Person("John", "Doe");
let person2 = new Person("Jane", "Doe");
let person3 = new Person("Alice", "Smith");
let person4 = new Person("Bob", "Smith");

// Создаем массив объектов Person
let people = [person1, person2, person3, person4];

// Сортируем массив объектов Person
people.sort(comparePeople);

// Выводим отсортированный массив
console.log(people);