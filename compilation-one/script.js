gsap.registerPlugin(SplitText);

function initHeadlineSplit() {
  const splitted = SplitText.create('.headline-line', {
    type: 'chars',
    preserveSpaces: true
  });

  splitted.chars.forEach((char) => {
    char.addEventListener('mouseenter', () => {
      gsap.to(char, {
        duration: 0.4,
        ease: 'power2.out',
        color: 'transparent',
        webkitTextStroke: '0.1vw white'
      });
    });
    char.addEventListener('mouseleave', () => {
      gsap.to(char, {
        duration: 0.4,
        ease: 'power2.in',
        delay: 0.4,
        color: 'currentColor',
        webkitTextStroke: '0vw'
      });
    });
  });
}

window.addEventListener('DOMContentLoaded', () => {
  document.fonts.ready.then(() => {
    initHeadlineSplit();
  });
});