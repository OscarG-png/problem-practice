function gradingStudents(grades) {
    let result = [];

    for (let grade of grades) {
        if (grade < 38) {
            result.push(grade);
        } else {
            const multipleOfFive = Math.ceil(grade / 5) * 5;
            if (multipleOfFive - grade < 3) {
                result.push(multipleOfFive);
            } else {
                result.push(grade);
            }
        }
    }
    return result;
}


// my solution so far for this problem. I want to come back to this to see if i can refactor it.
