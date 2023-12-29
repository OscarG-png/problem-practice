function calcDroneMinEnergy(route) {
    let maxAltitude = route[0][2];

    for (let i = 1; i < route.length; i++) {
        const altitude = route[i][2];

        maxAltitude = Math.max(maxAltitude, altitude);
        }
        return Math.max(0, maxAltitude - route[0][2]);
    }
