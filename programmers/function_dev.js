function solution(progresses, speeds) {
    const remained = []
    for (let i = 0; i < speeds.length; i++) {
        let temp = Math.ceil((100 - progresses[i]) / speeds[i]);
        remained.push(temp);
    }; /* 이 부분은 map을 사용해도 됐을 것. */

    let dep_day = remained[0]
    let count = 1;
    const answer = []
    for (let i = 1; i < remained.length; i++) {
        if (dep_day >= remained[i]) {
            count++;
        } else {
            answer.push(count);
            count = 1;
            dep_day = remained[i]
        }
    };
    answer.push(count)
    return answer
}