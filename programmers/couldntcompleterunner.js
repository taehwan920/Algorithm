function solution(participant, completion) {
    participant.sort();
    completion.sort();
    for (let i = 0; i < completion.length; i++) {
        if (participant[i] !== completion[i]) {
            return participant[i]
        }
        if (i === completion.length - 1 && participant[i] === completion[i]) {
            return participant[i + 1]
        }
    }
}

//해쉬를 이용한 풀이
function solution(participant, completion) {
    let ret = []
    let hashed = []
    participant.forEach(entry => {
        hashed[entry] = hashed[entry] ? hashed[entry] + 1 : 1
    })
    completion.forEach(entry => {
        hashed[entry] = hashed[entry] - 1
    })

    for (var key in hashed) {
        if (hashed[key] >= 1) return key
    }
}