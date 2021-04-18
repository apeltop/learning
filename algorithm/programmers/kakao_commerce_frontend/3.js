function solution(next_student) {
    let answer = 0;
    let dict = {}

    for (let i = 0; i < next_student.length; i++) {
        dict[i + 1] = next_student[i]
    }

    const a = (student) => {
        let visited = {[student]: true}
        let count = 1;
        let nextStudent = dict[student];

        while (nextStudent !== 0 && !(nextStudent in visited)) {
            visited[nextStudent] = true;
            nextStudent = dict[nextStudent]
            count += 1;
        }

        return count
    }

    let result = {}
    for (let i = 0; i < next_student.length; i++) {
        result[i + 1] = a(i + 1)
    }

    let maxIndex = 1;
    let maxValue = result[maxIndex];
    for (const elem in result) {
        if (maxValue < result[elem]) {
            maxValue = result[elem];
            maxIndex = elem;
        }
    }

    return maxIndex;
}


//3
// console.log(solution([5, 9, 13, 1, 0, 0, 11, 1, 7, 12, 9, 9, 2]))

//9
console.log(solution([6, 10, 8, 5, 8, 10, 5, 1, 6, 7]))
