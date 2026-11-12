// 1) 키·몸무게로 BMI 계산 (몸무게 ÷ 키(m)²)
function calcBmi() {
    const h = Number(document.querySelector('#height').value) / 100;
    const w = Number(document.querySelector('#weight').value);
    if (h <= 0 || w <= 0) return 0;
    return Math.round((w / (h * h)) * 10) / 10;
}

// 키·몸무게를 바꿀 때마다 BMI 표시 갱신
document.querySelector('#height').addEventListener('input', () => {
    document.querySelector('#bmi').textContent = calcBmi();
});
document.querySelector('#weight').addEventListener('input', () => {
    document.querySelector('#bmi').textContent = calcBmi();
});

// 2) 달러 표시 형식 : 12345 → $12,345
function money(v) {
    return '$' + Number(v).toLocaleString('en-US');
}

// 3) 예측하기 버튼
document.querySelector('#form').addEventListener('submit', async (e) => {
    e.preventDefault();   // 폼 기본 동작(새로고침) 막기

    // 입력값 → 서버로 보낼 객체 (열 이름은 학습 데이터와 같게)
    const item = {
        age:      Number(document.querySelector('#age').value),
        sex:      document.querySelector('#sex').value,
        bmi:      calcBmi(),
        children: Number(document.querySelector('#children').value),
        smoker:   document.querySelector('#smoker').value,
        region:   document.querySelector('#region').value
    };

    // 학습 데이터 범위 밖이면 예측하지 않음 (나이 18~64 , BMI 16~53 , 자녀 0~5)
    if (item.age < 18 || item.age > 64) {
        alert('나이는 18~64세 사이로 입력해 주세요.');
        return;
    }
    if (item.bmi < 16 || item.bmi > 53) {
        alert('BMI가 ' + item.bmi + '입니다. 키·몸무게를 확인해 주세요. (BMI 16~53 범위만 예측 가능)');
        return;
    }
    if (item.children < 0 || item.children > 5) {
        alert('자녀 수는 0~5명 사이로 입력해 주세요.');
        return;
    }

    const btn = document.querySelector('button');
    btn.disabled = true;
    btn.textContent = '예측 중...';

    try {
        // POST 로 본문(JSON) 전송 (axios : 객체를 넣으면 JSON으로 자동 변환)
        const response = await axios.post("http://127.0.0.1:8000/api/predict", item);
        const data = response.data;

        // 결과 표시
        document.querySelector('#charge').textContent = money(data.charge);
        document.querySelector('#monthly').textContent = '월 평균 ' + money(data.monthly);
        document.querySelector('#metric').textContent =
            '모델 성능 : 테스트 R² ' + data.r2 + ' · 교차검증 R² ' + data.cv_r2;
        document.querySelector('#result').classList.remove('hidden');
    } catch (err) {
        alert('서버와 연결할 수 없습니다. AppStart.py 가 실행 중인지 확인하세요.');
    }

    btn.disabled = false;
    btn.textContent = '예측하기';
});