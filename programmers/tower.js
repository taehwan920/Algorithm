function solution(heights) {
    const answer = [0]
    for (let i = 1; i < heights.length; i++) {
        const sliced = heights.slice(0, i)
        if (sliced.filter(tower => tower > heights[i]).length === 0) {
            answer.push(0)
        } else {
            for (let j = i; j > -1; j--) {
                if (sliced[j] > heights[i]) {
                    answer.push(j + 1)
                    break
                }
            }
        }
    }
    return answer
}

//다른 사람의 풀이
function solution2(heights) {
    return heights.map((v, i) => {
        while (i) {
            i--;
            if (heights[i] > v) {
                return i + 1;
            }
        }
        return 0;
    });
}
