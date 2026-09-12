// mobile menu
const menuBtn = document.getElementById('menuBtn');
const navLinks = document.getElementById('navLinks');
menuBtn.addEventListener('click', () => navLinks.classList.toggle('open'));
navLinks.querySelectorAll('a').forEach(a => a.addEventListener('click', () => navLinks.classList.remove('open')));

// footer year
document.getElementById('year').textContent = new Date().getFullYear();

// scroll reveal
const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const revealEls = document.querySelectorAll('.reveal');
if (prefersReduced) {
  revealEls.forEach(el => el.classList.add('is-visible'));
} else if ('IntersectionObserver' in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => io.observe(el));
} else {
  revealEls.forEach(el => el.classList.add('is-visible'));
}

// demo tabs
const demoTabs = document.querySelectorAll('.demo-tab');
const demoPanels = document.querySelectorAll('.demo-panel');
demoTabs.forEach(tab => {
  tab.addEventListener('click', () => {
    demoTabs.forEach(t => t.classList.remove('active'));
    demoPanels.forEach(p => p.classList.remove('active'));
    tab.classList.add('active');
    document.getElementById(tab.dataset.target).classList.add('active');
  });
});

// wordifier setup
let wordifier = null;
const dictionaryReady = fetch('data/words.json')
  .then(res => res.json())
  .then(words => {
    const trie = new Trie();
    words.forEach(word => trie.insert(word));
    wordifier = new Wordifier(trie);
  })
  .catch(err => {
    console.error('Failed to load dictionary', err);
  });

function showError(errorEl, message) {
  errorEl.textContent = message;
  errorEl.classList.add('visible');
}

function clearError(errorEl) {
  errorEl.classList.remove('visible');
  errorEl.textContent = '';
}

// Number -> Words
const numberForm = document.getElementById('numberForm');
const numberInput = document.getElementById('numberInput');
const numberResult = document.getElementById('numberResult');
const numberError = document.getElementById('numberError');

numberForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  clearError(numberError);
  await dictionaryReady;
  if (!wordifier) {
    showError(numberError, 'Dictionary failed to load. Please refresh and try again.');
    return;
  }
  const value = numberInput.value.trim();
  if (!value) return;
  try {
    const best = wordifier.numberToWords(value);
    const all = wordifier.allWordifications(value);
    const unique = [...new Set(all)];
    if (!best && unique.length === 0) {
      numberResult.innerHTML = '<p class="demo-result-empty">No wordification found for this number — try another one.</p>';
      return;
    }
    let html = '';
    if (best) {
      html += `<div class="best-match-label">Best match</div><div class="best-match">${escapeHtml(best)}</div>`;
    }
    if (unique.length > 0) {
      html += `<div class="best-match-label" style="margin-top:24px;">All wordifications (${unique.length})</div>`;
      html += `<div class="all-results">${unique.map(w => `<span class="chip">${escapeHtml(w)}</span>`).join('')}</div>`;
    }
    numberResult.innerHTML = html;
  } catch (err) {
    showError(numberError, err.message || 'Enter a valid phone number (digits after the first two cannot include 0 or 1).');
    numberResult.innerHTML = '';
  }
});

// Words -> Number
const wordsForm = document.getElementById('wordsForm');
const wordsInput = document.getElementById('wordsInput');
const wordsResult = document.getElementById('wordsResult');
const wordsError = document.getElementById('wordsError');

wordsForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  clearError(wordsError);
  await dictionaryReady;
  if (!wordifier) {
    showError(wordsError, 'Dictionary failed to load. Please refresh and try again.');
    return;
  }
  const value = wordsInput.value.trim();
  if (!value) return;
  const number = Wordifier.wordsToNumber(value);
  wordsResult.innerHTML = `<div class="best-match-label">Phone number</div><div class="result-number">${escapeHtml(number)}</div>`;
});

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}
