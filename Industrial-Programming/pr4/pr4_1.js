//1

function findDegree(num) {
    let degree = 0;
    if (num >= 1) {
        while(num >= 10) {
            num /= 10;
            degree++;
        }
        return degree;
    }
    
    if (num < 1) {
        while(num < 1) {
            num *= 10;
            degree--;
        }
        return degree;
    }
    
}

console.log(findDegree(6156461774.51451));