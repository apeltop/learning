function solution(n) {
    let answer = 0;

    let strN = n.toString()
    let numSet = new Set()
    for (let i = 0 ; i < strN.length ; i++) {
        if (strN[i] !== '0') {
            numSet.add(strN[i])
        }
    }

    let setIter = numSet[Symbol.iterator]();
    while (setIter) {
        let {value, done} = setIter.next();
        let v = Number.parseInt(value);
        if (done) {
            break
        }
        if (n % v === 0) {
            answer++
        }
    }

    return answer;
}

console.log(solution(2322)) //2
console.log(solution(1234)) //2
console.log(solution(1034)) //1
console.log(solution(1000)) //1
console.log(solution(2222)) //1
console.log(solution(0)) //-1
