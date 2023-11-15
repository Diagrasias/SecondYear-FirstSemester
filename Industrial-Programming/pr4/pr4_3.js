//3

function getUTCDifference() {
    const now = new Date();
    const localHour = now.getHours();
    const utcHour = now.getUTCHours();

    let diff = localHour - utcHour;

    // If the local time is in a time zone different from UTC,
    // the difference may be negative. In this case, we add 24
    // to get a positive number.
    if (diff < 0) {
        diff += 24;
    }

    return diff;
}

console.log("The difference between local time and UTC is " + getUTCDifference() + " hours.");