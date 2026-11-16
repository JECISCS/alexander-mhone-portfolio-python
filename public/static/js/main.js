const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('.nav');
if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('nav-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.textContent = isOpen ? '×' : '☰';
  });
  nav.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    nav.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.textContent = '☰';
  }));
}

const portraitToggle = document.querySelector('[data-portrait-toggle]');
if (portraitToggle) {
  const orbit = portraitToggle.closest('.hero-orbit');
  let portraitTimer;

  portraitToggle.addEventListener('click', () => {
    window.clearTimeout(portraitTimer);
    orbit.classList.add('is-portrait-expanded');
    portraitToggle.setAttribute('aria-pressed', 'true');
    portraitToggle.setAttribute('aria-label', 'Portrait expanded');

    portraitTimer = window.setTimeout(() => {
      orbit.classList.remove('is-portrait-expanded');
      portraitToggle.setAttribute('aria-pressed', 'false');
      portraitToggle.setAttribute('aria-label', 'Show full portrait briefly');
    }, 2600);
  });
}

document.querySelectorAll('[data-gallery]').forEach(gallery => {
  const track = gallery.querySelector('.gallery-track');
  if (!track) return;

  const slides = Array.from(track.querySelectorAll('img'));
  const progress = gallery.querySelector('.gallery-progress');
  const progressBar = gallery.querySelector('.gallery-progress-bar');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let activeIndex = 0;
  let autoplayTimer;
  let isHovered = false;
  let isFocused = false;

  if (!slides.length || !progress || !progressBar) return;

  if (slides.length > 1) slides[1].loading = 'eager';

  const canAutoplay = () => (
    slides.length > 1 &&
    !reducedMotion &&
    !document.hidden &&
    !isHovered &&
    !isFocused
  );

  const scheduleAutoplay = () => {
    window.clearTimeout(autoplayTimer);
    progress.classList.remove('is-running');
    if (!canAutoplay()) return;

    slides[(activeIndex + 1) % slides.length].loading = 'eager';
    void progress.offsetWidth;
    progress.classList.add('is-running');
    autoplayTimer = window.setTimeout(() => {
      const nextIndex = (activeIndex + 1) % slides.length;
      track.scrollTo({ left: nextIndex * track.clientWidth, behavior: 'smooth' });
    }, 5000);
  };

  const updateGallery = () => {
    const index = Math.max(0, Math.min(
      slides.length - 1,
      Math.round(track.scrollLeft / track.clientWidth)
    ));
    if (index === activeIndex) return;

    activeIndex = index;
    scheduleAutoplay();
  };

  track.addEventListener('scroll', updateGallery, { passive: true });
  window.addEventListener('resize', updateGallery);
  gallery.addEventListener('mouseenter', () => {
    isHovered = true;
    scheduleAutoplay();
  });
  gallery.addEventListener('mouseleave', () => {
    isHovered = false;
    scheduleAutoplay();
  });
  gallery.addEventListener('focusin', () => {
    isFocused = true;
    scheduleAutoplay();
  });
  gallery.addEventListener('focusout', event => {
    if (!gallery.contains(event.relatedTarget)) {
      isFocused = false;
      scheduleAutoplay();
    }
  });
  document.addEventListener('visibilitychange', scheduleAutoplay);
  scheduleAutoplay();
});

const projectDialog = document.querySelector('.project-dialog');
if (projectDialog) {
  const dialogImage = projectDialog.querySelector('[data-dialog-image]');
  const dialogCaption = projectDialog.querySelector('[data-dialog-caption]');
  const dialogCount = projectDialog.querySelector('[data-dialog-count]');
  const previous = projectDialog.querySelector('[data-dialog-prev]');
  const next = projectDialog.querySelector('[data-dialog-next]');
  const liveLink = projectDialog.querySelector('[data-dialog-live]');
  let slides = [];
  let slideIndex = 0;
  let activeTrigger = null;

  const updateProjectSlide = () => {
    const slide = slides[slideIndex];
    dialogImage.src = slide.src;
    dialogImage.alt = slide.caption;
    dialogCaption.textContent = slide.caption;
    dialogCount.textContent = `${String(slideIndex + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    previous.disabled = slideIndex === 0;
    next.disabled = slideIndex === slides.length - 1;
  };

  document.querySelectorAll('[data-project-details]').forEach(trigger => {
    trigger.addEventListener('click', () => {
      const card = trigger.closest('.project-card');
      const title = card.querySelector('h3').textContent.trim();
      const description = card.querySelector('.project-copy p').textContent.trim();
      const stage = card.querySelector('.project-stage');
      const type = card.querySelector('.project-meta span:last-child');
      const technologies = card.querySelector('.project-tech');

      slides = Array.from(card.querySelectorAll('.gallery-track img'), image => ({
        src: image.getAttribute('src'),
        caption: image.dataset.caption || image.alt
      }));
      if (!slides.length) return;

      slideIndex = 0;
      activeTrigger = trigger;
      projectDialog.querySelector('[data-dialog-title]').textContent = title;
      projectDialog.querySelector('[data-dialog-type]').textContent = type.textContent.trim();
      projectDialog.querySelector('[data-dialog-description]').textContent = description;
      const dialogStage = projectDialog.querySelector('[data-dialog-stage]');
      dialogStage.textContent = stage ? stage.textContent.trim() : '';
      dialogStage.hidden = !stage;

      const dialogTechnologies = projectDialog.querySelector('[data-dialog-technologies]');
      dialogTechnologies.replaceChildren();
      if (technologies) {
        technologies.querySelectorAll('li').forEach(technology => {
          const item = document.createElement('li');
          item.textContent = technology.textContent;
          dialogTechnologies.append(item);
        });
      }
      dialogTechnologies.hidden = !dialogTechnologies.childElementCount;

      const projectUrl = trigger.dataset.projectUrl;
      liveLink.hidden = !projectUrl;
      if (projectUrl) liveLink.href = projectUrl;

      updateProjectSlide();
      projectDialog.showModal();
    });
  });

  projectDialog.querySelector('[data-dialog-close]').addEventListener('click', () => {
    projectDialog.close();
  });
  previous.addEventListener('click', () => {
    if (slideIndex > 0) {
      slideIndex -= 1;
      updateProjectSlide();
    }
  });
  next.addEventListener('click', () => {
    if (slideIndex < slides.length - 1) {
      slideIndex += 1;
      updateProjectSlide();
    }
  });
  projectDialog.addEventListener('click', event => {
    if (event.target === projectDialog) projectDialog.close();
  });
  projectDialog.addEventListener('keydown', event => {
    if (event.key === 'Escape') {
      event.preventDefault();
      projectDialog.close();
    }
  });
  projectDialog.addEventListener('close', () => {
    activeTrigger?.focus();
  });
}

const revealTargets = document.querySelectorAll(
  '.hero-kicker, .hero-grid, .hero-bottom, .section-heading, .project-card, ' +
  '.expertise-card, .experience-group, .education-card, .about-copy > *, .contact-row, .contact-details'
);
const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if ('IntersectionObserver' in window && !reducedMotion) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        observer.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.12,
    rootMargin: '0px 0px -36px 0px'
  });

  revealTargets.forEach(target => {
    target.classList.add('scroll-reveal');
    revealObserver.observe(target);
  });
}
