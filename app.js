(() => {
  'use strict';

  // ==================== Constants & State ====================
  const STORAGE_KEY = 'routineTrackerData';
  const today = new Date().toISOString().slice(0, 10);

  // ==================== DOM References ====================
  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => ctx.querySelectorAll(sel);

  const views = {
    dashboard: $('#dashboard'),
    gym: $('#gym'),
    study: $('#study'),
    sleep: $('#sleep'),
  };

  const dateEl = $('#current-date');
  const themeToggle = $('#theme-toggle');
  const toastEl = $('#toast');

  // Gym
  const gymForm = $('#gym-form');
  const exercisesContainer = $('#exercises-container');
  const addExerciseBtn = $('#add-exercise-btn');
  const gymCalories = $('#gym-calories');

  // Study
  const studyForm = $('#study-form');
  const studySubject = $('#study-subject');
  const studyDuration = $('#study-duration');
  const studyNotes = $('#study-notes');
  const studyFocus = $('#study-focus');
  const starRating = $('#star-rating');

  // Sleep
  const sleepForm = $('#sleep-form');
  const sleepBedtime = $('#sleep-bedtime');
  const sleepWaketime = $('#sleep-waketime');
  const sleepDurationValue = $('#sleep-duration-value');
  const sleepQuality = $('#sleep-quality');
  const qualityRating = $('#quality-rating');
  const sleepNotes = $('#sleep-notes');

  // Checks
  const checkGym = $('#check-gym');
  const checkStudy = $('#check-study');
  const checkSleep = $('#check-sleep');

  // ==================== LocalStorage Helpers ====================
  function loadData() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY)) || {};
    } catch {
      return {};
    }
  }

  function saveData(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  function getTodayData() {
    return loadData()[today] || {};
  }

  function saveTodayModule(module, moduleData) {
    const data = loadData();
    if (!data[today]) data[today] = {};
    data[today][module] = moduleData;
    saveData(data);
    updateChecks();
  }

  // ==================== Theme ====================
  function initTheme() {
    const saved = localStorage.getItem('routineTrackerTheme');
    if (saved === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      $('.theme-icon').textContent = '☀️';
    }
  }

  themeToggle.addEventListener('click', () => {
    const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
    if (isDark) {
      document.documentElement.removeAttribute('data-theme');
      $('.theme-icon').textContent = '🌙';
      localStorage.setItem('routineTrackerTheme', 'light');
    } else {
      document.documentElement.setAttribute('data-theme', 'dark');
      $('.theme-icon').textContent = '☀️';
      localStorage.setItem('routineTrackerTheme', 'dark');
    }
  });

  // ==================== Date Display ====================
  dateEl.textContent = new Date().toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric',
  });

  // ==================== View Navigation ====================
  function showView(viewName) {
    Object.values(views).forEach((v) => {
      v.classList.remove('active');
    });
    const target = views[viewName];
    // Trigger reflow for animation
    target.classList.add('entering');
    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        target.classList.add('active');
        target.classList.remove('entering');
      });
    });
  }

  $$('.card[data-module]').forEach((card) => {
    card.addEventListener('click', () => {
      showView(card.dataset.module);
    });
  });

  $$('[data-back]').forEach((btn) => {
    btn.addEventListener('click', () => showView('dashboard'));
  });

  // ==================== Dashboard Checks ====================
  function updateChecks() {
    const todayData = getTodayData();
    checkGym.classList.toggle('visible', !!todayData.gym);
    checkStudy.classList.toggle('visible', !!todayData.study);
    checkSleep.classList.toggle('visible', !!todayData.sleep);
  }

  // ==================== Toast ====================
  function showToast(message) {
    toastEl.textContent = message;
    toastEl.classList.add('show');
    setTimeout(() => toastEl.classList.remove('show'), 2500);
  }

  // ==================== Gym Module ====================
  let exerciseCount = 0;

  function createExerciseBlock(name = '', sets = []) {
    exerciseCount++;
    const id = exerciseCount;
    const block = document.createElement('div');
    block.className = 'exercise-block';
    block.dataset.exerciseId = id;

    block.innerHTML = `
      <div class="exercise-header">
        <input type="text" placeholder="Exercise name (e.g. Bench Press)" value="${escapeHtml(name)}" data-exercise-name>
        <button type="button" class="btn-danger" data-remove-exercise>Remove</button>
      </div>
      <div class="sets-container" data-sets></div>
      <button type="button" class="add-set-btn" data-add-set>+ Add Set</button>
    `;

    // Wire up remove exercise
    $('[data-remove-exercise]', block).addEventListener('click', () => block.remove());

    // Wire up add set
    $('[data-add-set]', block).addEventListener('click', () => {
      addSetRow($('[data-sets]', block));
    });

    // Pre-fill sets
    const setsContainer = $('[data-sets]', block);
    if (sets.length > 0) {
      sets.forEach((s) => addSetRow(setsContainer, s.reps, s.weight));
    } else {
      addSetRow(setsContainer);
    }

    exercisesContainer.appendChild(block);
  }

  let setCount = 0;

  function addSetRow(container, reps = '', weight = '') {
    setCount++;
    const setNum = container.children.length + 1;
    const row = document.createElement('div');
    row.className = 'set-row';
    row.innerHTML = `
      <span class="set-label">Set ${setNum}</span>
      <input type="number" placeholder="Reps" min="0" value="${reps}" data-reps>
      <input type="number" placeholder="Weight" min="0" value="${weight}" data-weight>
      <button type="button" class="btn-danger" data-remove-set>✕</button>
    `;

    $('[data-remove-set]', row).addEventListener('click', () => {
      row.remove();
      renumberSets(container);
    });

    container.appendChild(row);
  }

  function renumberSets(container) {
    $$('.set-row', container).forEach((row, i) => {
      $('.set-label', row).textContent = `Set ${i + 1}`;
    });
  }

  addExerciseBtn.addEventListener('click', () => createExerciseBlock());

  gymForm.addEventListener('submit', (e) => {
    e.preventDefault();

    const exerciseBlocks = $$('.exercise-block', exercisesContainer);
    if (exerciseBlocks.length === 0) {
      showToast('Add at least one exercise');
      return;
    }

    const exercises = [];
    let valid = true;

    exerciseBlocks.forEach((block) => {
      const name = $('[data-exercise-name]', block).value.trim();
      if (!name) {
        valid = false;
        $('[data-exercise-name]', block).style.borderColor = 'var(--danger)';
        return;
      }
      $('[data-exercise-name]', block).style.borderColor = '';

      const sets = [];
      $$('.set-row', block).forEach((row) => {
        const reps = parseInt($('[data-reps]', row).value) || 0;
        const weight = parseInt($('[data-weight]', row).value) || 0;
        if (reps > 0 || weight > 0) {
          sets.push({ reps, weight });
        }
      });

      exercises.push({ name, sets });
    });

    if (!valid) {
      showToast('Please name all exercises');
      return;
    }

    const calories = parseInt(gymCalories.value) || 0;
    saveTodayModule('gym', { calories, exercises });
    showToast('Workout saved!');
  });

  // ==================== Study Module ====================
  // Star rating interaction
  $$('.star', starRating).forEach((star) => {
    star.addEventListener('click', () => {
      const val = parseInt(star.dataset.value);
      studyFocus.value = val;
      updateStars(val);
    });

    star.addEventListener('mouseenter', () => {
      const val = parseInt(star.dataset.value);
      highlightStars(val);
    });
  });

  starRating.addEventListener('mouseleave', () => {
    updateStars(parseInt(studyFocus.value));
  });

  function updateStars(rating) {
    $$('.star', starRating).forEach((s) => {
      s.classList.toggle('active', parseInt(s.dataset.value) <= rating);
    });
  }

  function highlightStars(upTo) {
    $$('.star', starRating).forEach((s) => {
      s.classList.toggle('active', parseInt(s.dataset.value) <= upTo);
    });
  }

  studyForm.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors(studyForm);

    let hasError = false;
    if (!studySubject.value.trim()) {
      setError(studySubject, 'Subject is required');
      hasError = true;
    }
    if (!studyDuration.value || parseInt(studyDuration.value) < 1) {
      setError(studyDuration, 'Enter time spent');
      hasError = true;
    }
    if (hasError) return;

    saveTodayModule('study', {
      subject: studySubject.value.trim(),
      duration: parseInt(studyDuration.value),
      notes: studyNotes.value.trim(),
      focus: parseInt(studyFocus.value) || 0,
    });
    showToast('Study session saved!');
  });

  // ==================== Sleep Module ====================
  function calcSleepDuration() {
    const bed = sleepBedtime.value;
    const wake = sleepWaketime.value;
    if (!bed || !wake) {
      sleepDurationValue.textContent = '--';
      return;
    }

    const [bh, bm] = bed.split(':').map(Number);
    const [wh, wm] = wake.split(':').map(Number);

    let bedMins = bh * 60 + bm;
    let wakeMins = wh * 60 + wm;

    // If wake is before or equal to bed, assume crossing midnight
    if (wakeMins <= bedMins) {
      wakeMins += 24 * 60;
    }

    const diff = wakeMins - bedMins;
    const hours = Math.floor(diff / 60);
    const mins = diff % 60;
    const durationStr = `${hours}h ${mins}m`;

    sleepDurationValue.textContent = durationStr;
    return durationStr;
  }

  sleepBedtime.addEventListener('change', calcSleepDuration);
  sleepWaketime.addEventListener('change', calcSleepDuration);
  sleepBedtime.addEventListener('input', calcSleepDuration);
  sleepWaketime.addEventListener('input', calcSleepDuration);

  // Quality rating
  $$('.quality-btn', qualityRating).forEach((btn) => {
    btn.addEventListener('click', () => {
      $$('.quality-btn', qualityRating).forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');
      sleepQuality.value = btn.dataset.value;
    });
  });

  sleepForm.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors(sleepForm);

    let hasError = false;
    if (!sleepBedtime.value) {
      setError(sleepBedtime, 'Bedtime is required');
      hasError = true;
    }
    if (!sleepWaketime.value) {
      setError(sleepWaketime, 'Wake time is required');
      hasError = true;
    }
    if (hasError) return;

    const duration = calcSleepDuration() || '0h 0m';

    saveTodayModule('sleep', {
      bedtime: sleepBedtime.value,
      wakeTime: sleepWaketime.value,
      duration,
      quality: sleepQuality.value || 'Not rated',
      notes: sleepNotes.value.trim(),
    });
    showToast('Sleep log saved!');
  });

  // ==================== Form Validation Helpers ====================
  function setError(input, message) {
    const group = input.closest('.form-group');
    if (!group) return;
    group.classList.add('error');
    let msg = $('.error-msg', group);
    if (!msg) {
      msg = document.createElement('div');
      msg.className = 'error-msg';
      group.appendChild(msg);
    }
    msg.textContent = message;
  }

  function clearErrors(form) {
    $$('.form-group.error', form).forEach((g) => {
      g.classList.remove('error');
      const msg = $('.error-msg', g);
      if (msg) msg.textContent = '';
    });
  }

  // ==================== HTML Escaping ====================
  function escapeHtml(str) {
    const div = document.createElement('div');
    div.textContent = str;
    return div.innerHTML;
  }

  // ==================== Pre-fill From Storage ====================
  function prefillData() {
    const todayData = getTodayData();

    // Gym
    if (todayData.gym) {
      const g = todayData.gym;
      gymCalories.value = g.calories || '';
      if (g.exercises && g.exercises.length > 0) {
        g.exercises.forEach((ex) => createExerciseBlock(ex.name, ex.sets || []));
      }
    }

    // Study
    if (todayData.study) {
      const s = todayData.study;
      studySubject.value = s.subject || '';
      studyDuration.value = s.duration || '';
      studyNotes.value = s.notes || '';
      studyFocus.value = s.focus || 0;
      updateStars(s.focus || 0);
    }

    // Sleep
    if (todayData.sleep) {
      const sl = todayData.sleep;
      sleepBedtime.value = sl.bedtime || '';
      sleepWaketime.value = sl.wakeTime || '';
      sleepNotes.value = sl.notes || '';
      if (sl.quality) {
        sleepQuality.value = sl.quality;
        $$('.quality-btn', qualityRating).forEach((btn) => {
          btn.classList.toggle('active', btn.dataset.value === sl.quality);
        });
      }
      calcSleepDuration();
    }
  }

  // ==================== Init ====================
  initTheme();
  prefillData();
  updateChecks();
})();
