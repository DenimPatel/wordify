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

// example chips
document.querySelectorAll('.example-chip').forEach(chip => {
  chip.addEventListener('click', () => {
    const panel = chip.closest('.demo-panel');
    const form = panel.querySelector('form');
    const input = form.querySelector('.demo-input');
    input.value = chip.dataset.value;
    form.requestSubmit ? form.requestSubmit() : form.dispatchEvent(new Event('submit', { cancelable: true }));
  });
});

// trie search animation
(function () {
  const svg = document.querySelector('.trie-svg');
  if (!svg) return;

  const trieQueryEl = document.getElementById('trieQuery');
  const trieResultEl = document.getElementById('trieResult');

  const edgesByStep = {
    'root-c': 'edge-root-c', 'c-a': 'edge-c-a', 'a-r': 'edge-a-r', 'r-d1': 'edge-r-d1',
    'a-t': 'edge-a-t', 'root-d2': 'edge-root-d2', 'd2-o': 'edge-d2-o', 'o-g': 'edge-o-g',
  };

  const searches = [
    { word: 'CAR', nodes: ['root', 'c', 'a', 'r'], edges: ['root-c', 'c-a', 'a-r'], found: true },
    { word: 'CARD', nodes: ['root', 'c', 'a', 'r', 'd1'], edges: ['root-c', 'c-a', 'a-r', 'r-d1'], found: true },
    { word: 'CARS', nodes: ['root', 'c', 'a', 'r'], edges: ['root-c', 'c-a', 'a-r'], found: false },
    { word: 'CAT', nodes: ['root', 'c', 'a', 't'], edges: ['root-c', 'c-a', 'a-t'], found: true },
    { word: 'DOG', nodes: ['root', 'd2', 'o', 'g'], edges: ['root-d2', 'd2-o', 'o-g'], found: true },
  ];

  function resetTrie() {
    svg.querySelectorAll('.trie-node').forEach(n => n.classList.remove('active', 'found', 'notfound'));
    svg.querySelectorAll('.trie-edge').forEach(e => e.classList.remove('active'));
    trieResultEl.textContent = '';
    trieResultEl.classList.remove('found', 'notfound');
  }

  let cancelled = false;
  let timeouts = [];

  function clearTimers() {
    timeouts.forEach(t => clearTimeout(t));
    timeouts = [];
  }

  function runSearch(entry, onDone) {
    resetTrie();
    trieQueryEl.textContent = entry.word;
    const stepDelay = 450;
    entry.nodes.forEach((nodeId, i) => {
      const t = setTimeout(() => {
        if (cancelled) return;
        if (i > 0) {
          const edgeEl = document.getElementById(edgesByStep[entry.edges[i - 1]]);
          if (edgeEl) edgeEl.classList.add('active');
        }
        const nodeEl = document.getElementById('node-' + nodeId);
        const isLast = i === entry.nodes.length - 1;
        if (isLast) {
          nodeEl.classList.add(entry.found ? 'found' : 'notfound');
          trieResultEl.textContent = entry.found ? `✓ "${entry.word}" found` : `✗ "${entry.word}" not in dictionary`;
          trieResultEl.classList.add(entry.found ? 'found' : 'notfound');
          timeouts.push(setTimeout(onDone, 1400));
        } else {
          nodeEl.classList.add('active');
        }
      }, i * stepDelay);
      timeouts.push(t);
    });
  }

  function loop(index) {
    if (cancelled) return;
    runSearch(searches[index % searches.length], () => loop(index + 1));
  }

  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (prefersReducedMotion) {
    const entry = searches[0];
    entry.nodes.forEach(nodeId => document.getElementById('node-' + nodeId).classList.add('active'));
    entry.edges.forEach(edgeKey => document.getElementById(edgesByStep[edgeKey]).classList.add('active'));
    document.getElementById('node-' + entry.nodes[entry.nodes.length - 1]).classList.replace('active', 'found');
    trieQueryEl.textContent = entry.word;
    trieResultEl.textContent = `✓ "${entry.word}" found`;
    trieResultEl.classList.add('found');
  } else if ('IntersectionObserver' in window) {
    let started = false;
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting && !started) {
          started = true;
          cancelled = false;
          loop(0);
        } else if (!e.isIntersecting && started) {
          started = false;
          cancelled = true;
          clearTimers();
          resetTrie();
        }
      });
    }, { threshold: 0.3 });
    io.observe(svg);
  } else {
    loop(0);
  }
})();
