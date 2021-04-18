function solution(grades) {
    let answer = [];
    let classDict = {}
    let classIndex = {}

    const gradeList = {
        'A+': 12,
        'A0': 11,
        'A-': 10,
        'B+': 9,
        'B0': 8,
        'B-': 7,
        'C+': 6,
        'C0': 5,
        'C-': 4,
        'D+': 3,
        'D0': 2,
        'D-': 1,
        'F': 0
    }

    for (let i = 0 ; i < grades.length ; i++) {
        let [cls, grade] = grades[i].split(' ');
        if (cls in classDict) {
            if (gradeList[classDict[cls]] < gradeList[grade]) {
                classDict[cls] = grade;
                classIndex[cls] = i
            }
        } else {
          classDict[cls] = grade;
          classIndex[cls] = i
        }
    }

    for (const [key, value] of Object.entries(classDict)) {
        answer.push(`${key} ${value}`);
    }

    answer.sort(function (a, b) {
        let [cls1, grade1] = a.split(' ');
        let [cls2, grade2] = b.split(' ');

        grade1 = gradeList[grade1];
        grade2 = gradeList[grade2];

        if (grade1 < grade2) {
            return 1;
        }
        if (grade1 > grade2) {
            return -1;
        }

        if (classIndex[cls1] < classIndex[cls2]) {
            return -1
        }

        if (classIndex[cls1] > classIndex[cls2]) {
            return 1
        }

        return 0;
    });

    return answer;
}

console.log(solution(["DS7651 A0", "CA0055 D+", "AI5543 C0", "OS1808 B-", "DS7651 B+", "AI0001 F", "DB0001 B-", "AI5543 D+", "DS7651 A+", "OS1808 B-"]))
//["DS7651 A+", "OS1808 B-", "DB0001 B-", "AI5543 C0", "CA0055 D+", "AI0001 F"]
console.log(solution(["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]))
//["GP0000 A0", "PL6677 B+", "DM0106 B+"]
