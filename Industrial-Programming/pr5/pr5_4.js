for (let i = 0; i <= 0x10FFFF; i++) {
    let char = String.fromCodePoint(i);
    if (char.normalize('NFKC').length > 1 || char.normalize('NFKD').length > 1) {
        console.log(char, i.toString(16).toUpperCase());
    }
}