function indexOf(arr, func) {
    let indices = [];
    for(let i = 0; i < arr.length; i++) {
        if(func(arr[i])) {
            indices.push(i);
        }
    }
    return indices;
}

let arr = [-1, 2, -3, 4, -5];
let indices = indexOf(arr, x => x > 0);
console.log(indices); // [1, 3]