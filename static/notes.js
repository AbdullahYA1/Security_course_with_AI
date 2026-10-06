// A developer mistakenly placed the service key in browser code.
// This is an inert classroom value, never a credential for a real provider.
const AI_SERVICE_KEY = "demo_classroom_key_v1_not_real";

document.getElementById('summarize').addEventListener('click', async () => {
  const result = document.getElementById('result');
  result.textContent = 'جاري إعداد الملخص...';
  try {
    const response = await fetch('/api/summary', {
      method: 'POST',
      headers: {'X-Demo-Key': AI_SERVICE_KEY}
    });
    const data = await response.json();
    result.textContent = data.summary || data.error;
  } catch {
    result.textContent = 'تعذر إنشاء الملخص. حاول مرة ثانية.';
  }
});
