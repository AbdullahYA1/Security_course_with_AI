document.getElementById('summarize').addEventListener('click', async () => {
  const result = document.getElementById('result');
  result.textContent = 'جاري إعداد الملخص...';
  try {
    const response = await fetch('/api/v2/summary', {method: 'POST'});
    const data = await response.json();
    result.textContent = data.summary || data.error;
  } catch {
    result.textContent = 'تعذر إنشاء الملخص. حاول مرة ثانية.';
  }
});
