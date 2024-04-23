// 문자열을 대문자로 변환
let str1 = "Your First String Here".toUpperCase();
let str2 = "Your Second String Here".toUpperCase();

// 공백을 제거
str1 = str1.replace(/\s/g, '');
str2 = str2.replace(/\s/g, '');

// 알파벳이 아닌 문자를 제거
str1 = str1.replace(/[^A-Z]/g, '');
str2 = str2.replace(/[^A-Z]/g, '');

let acount = 0;
let count = 0;

// str1을 순회하며 str2와의 유사도 계산
for (let i = 0; i < str1.length; i++) {
    if (str2.includes(str1[i])) {
        count += 1;
        str2 = str2.replace(str1[i], ''); // str2에서 일치하는 첫 번째 문자를 제거
    }
    acount += 1;
}

// 최종 유사도 계산
let answer = (count / (acount + str2.length)) * 65536;
answer = Math.round(answer);

console.log(answer);