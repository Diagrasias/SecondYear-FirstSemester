 //2

function nextFloat(f) {
    var bitRepr = floatToBits(f);
    bitRepr++;
    return bitsToFloat(bitRepr);
}

function floatToBits(f) {
    var buf = new ArrayBuffer(4);
    (new Float32Array(buf))[0] = f;
    return (new Uint32Array(buf))[0];
}

function bitsToFloat(b) {
    var buf = new ArrayBuffer(4);
    (new Uint32Array(buf))[0] = b;
    return (new Float32Array(buf))[0];
}

let f = parseInt(prompt("Enter a number:"));
console.log(`The smallest representable floating-point number next to ${f} is ${nextFloat(f)}`);
