function hackerlandRadioTransmitters(x, k) {
    x = x.sort((a, b) => a - b);
    let transmitters = 0;
    let i = 0;

    while (i < x.length) {
        let location = x[i];

        while (i < x.length && x[i] <= location + k) {
            i++;
        }

        let transmitterLocation = x[i - 1];

        while (i < x.length && x[i] <= transmitterLocation + k) {
            i++;
        }

        transmitters++;
    }

    return transmitters;
}

/* this one took a minute to figure out. Had to play around with the while loops to make sure i didn't
* exceed the time limit.
*/
