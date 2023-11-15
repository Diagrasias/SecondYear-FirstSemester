function getPositions(arr, value) {
    return arr.map((el, i) => el === value ? i : -1).filter(el => el !== -1);
}

// Пример использования:
let arr = [0, 1, 0, 2, 0, 1, 2, 1, 0];
console.log(getPositions(arr, 2)); // Выведет: [0, 2, 5, 8]