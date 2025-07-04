if (document.getElementById("trackGrid")) {
  const isMobile = window.innerWidth <= 768;
  const trackBoxes = document.querySelectorAll('.track-box');
  
  trackBoxes.forEach((box) => {
    const img = box.querySelector('.track-image');
    const label = box.querySelector('.track-title');
    
    if (!isMobile) {
      const applyHoverEffect = (e) => {
        const rect = box.getBoundingClientRect();
        const x = e.clientX - rect.left - rect.width / 2;
        const y = e.clientY - rect.top - rect.height / 2;

        gsap.to(img, {
          duration: 0.05,
          x: x / 10,
          y: y / 10,
          rotateY: x / 15,
          rotateX: -y / 15,
          ease: "power2.out",
        });

        gsap.to(box, {
          duration: 0.1,
          backgroundColor: "#F5EF69",
          ease: "power2.out",
        });

        gsap.to(label, {
          duration: 0.3,
          color: "#000000",
          ease: "power2.out",
        });
      };

      const removeHoverEffect = () => {
        gsap.to(img, {
          duration: 0.4,
          x: 0,
          y: 0,
          rotateY: 0,
          rotateX: 0,
          ease: "power2.in",
        });

        gsap.to(box, {
          duration: 0.4,
          backgroundColor: "#000000",
          ease: "power2.in",
        });

        gsap.to(label, {
          duration: 0.4,
          color: "#FFFFFF",
          ease: "power2.in",
        });
      };

      box.addEventListener("mousemove", applyHoverEffect);
      box.addEventListener("mouseleave", removeHoverEffect);
    }
  });
}
  
  function autoSizeHeadings() {
    const lines = document.querySelectorAll('.heading-line');
    const leftColumn = document.querySelector('.left');
  
    if (!leftColumn) return;
  
    const leftColumnStyle = window.getComputedStyle(leftColumn);
    const leftPadding = parseFloat(leftColumnStyle.paddingLeft) + parseFloat(leftColumnStyle.paddingRight);
    const leftMargin = parseFloat(leftColumnStyle.marginLeft) + parseFloat(leftColumnStyle.marginRight);
    const availableWidth = Math.min(leftColumn.getBoundingClientRect().width - leftPadding - leftMargin, window.innerWidth);
  
    lines.forEach(line => {
        // line.style.visibility = 'hidden';
        const text = line.textContent;
        const font = 'Faction';
        const context = document.createElement('canvas').getContext('2d');
  
        let fontSize = 10;
        let measuredWidth = 0;
  
        while (true) {
            context.font = `${fontSize}px ${font}`;
            measuredWidth = context.measureText(text).width;
            if (measuredWidth >= availableWidth || fontSize > 1000) break;
            fontSize += 1;
        }
  
        if (measuredWidth > availableWidth) fontSize -= 1;
  
        line.style.fontSize = `${fontSize}px`;
        line.style.visibility = 'visible'; 
    });
  }
  
  
  window.addEventListener('load', () => {
    document.fonts.ready.then(() => {
      requestAnimationFrame(autoSizeHeadings);
    });
  });
  
  
  async function fullyReady() {
    await new Promise((resolve) => {
      if (document.readyState === 'complete' || document.readyState === 'interactive') {
        resolve();
      } else {
        document.addEventListener('DOMContentLoaded', resolve, { once: true });
      }
    });
  
    await document.fonts.ready;
  }
  
  function forceLayoutReflow() {
    document.body.offsetHeight;
    window.dispatchEvent(new Event('resize'));
  }
  
  async function runLayoutFix() {
    await fullyReady();
    autoSizeHeadings();
    forceLayoutReflow();
  
    requestAnimationFrame(() => {
      // initHeadlineSplit();
    });
  }
  
  runLayoutFix();
  
  
  
  window.addEventListener('resize', autoSizeHeadings);
  
  gsap.registerPlugin(SplitText);
  
  function initHeadlineSplit() {
    const splitted = SplitText.create('.heading-line', {
      type: 'chars',
      preserveSpaces: true
    });
  
    splitted.chars.forEach((char) => {
      char.addEventListener('mouseenter', () => {
        gsap.to(char, {
          duration: 0.4,
          ease: 'power2.out',
          fontFamily: "'Faction','FactionOutline',sans-serif",
          color: '#F5EF69'
        });
      });
      char.addEventListener('mouseleave', () => {
        gsap.to(char, {
          duration: 0.4,
          ease: 'power2.in',
          delay: 0.2,
          fontFamily: "'FactionOutline','Faction',sans-serif",
          color: '#FFFFFF'
        });
      });
    });
  
    //kerning for specific pairs in Faction
    splitted.chars.forEach((char, i) => {
      const current = char.textContent || '';
      const next = splitted.chars[i + 1]?.textContent || '';
      if (
        (current === 'r' && next === 'a') ||
        (current === 'a' && next === 'v') ||
        (current === 'v' && next === 'e') 
      ) {
        char.style.marginRight = '-0.02em';
      }
      if (
        (current === 'V' && next === 'o')  ||
        (current === '.' && next === '1')
      ) {
        char.style.marginRight = '-0.040em';
      }
      if (
        (current === 'T' && next === 'a')
      ) {
        char.style.marginRight = '-0.08em';
      }
    });
  }
  
  window.addEventListener('DOMContentLoaded', () => {
    document.fonts.ready.then(() => {
    initHeadlineSplit();
    setTimeout(() => {
      autoSizeHeadings();
      forceLayoutReflow();
    }, 100);
  
    });
  });