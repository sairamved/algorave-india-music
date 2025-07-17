def index_template(blocks):
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Algorave India Compilation Tape Vol.1</title>
      <link rel="stylesheet" href="style.css" />
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital@0;1&display=swap" rel="stylesheet">
    </head>
    <body>
      <div class="container" data-barba="container" data-barba-namespace="index">
        <section class="left">
            <div class="heading-wrapper">
                <div class="heading-container">
                  <div class="heading-line" data-text="Algorave India">Algorave India</div>
                  <div class="heading-line" data-text="Compilation Tape">Compilation Tape</div>
                  <div class="heading-line" data-text="Vol.1">Vol.1</div>
                </div>
              </div>  

              <div class="description">
                <p>
                  A compilation of 10 algorithmic music tracks created by artists from the Algorave India community, paired with 10 generative zines by visual artists from the code.drift collective.
                </p>
              </div>
              <div class="logo-row">
                <a href="https://algorave.in/" target="_blank" rel="noopener" class="logo-link">
                  <img src="assets/logos/algorave-india.png" alt="Logo 1" class="landing-logo" />
                </a>
                <a href="https://www.ajaibghar.com/codedrift" target="_blank" rel="noopener" class="logo-link">
                  <img src="assets/logos/codedrift.png" alt="Logo 2" class="landing-logo" />
                </a>
              </div>
              
          <div class="footer-links">
            <a href="about.html" class="left-link">About</a>
            <a href="https://opencollective.com/algorave-india" class="right-link">Contribute</a>
          </div>
        </section>
        <section class="right" id="trackGrid">
            {blocks}
        </section>
      </div>
      <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>
      <script src="https://unpkg.com/barba.js@2.9.7/dist/barba.min.js"></script>
      <script src="script.js"></script>
    </body>
    </html>

    """

def index_block(slug, name):
    return(f"""
        <div class="track-box" onclick="window.location.href='{slug}.html'">
        <img src="assets/{slug}.jpg" alt="{name}" class="track-image" />
        <div class="track-title">{name}</div>
        </div>""")

def track_template(slug, name, number, track_artist, zine_artist, process, zine_link): 
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <title>Algorave India Compilation Tape Vol.1</title>
      <link rel="stylesheet" href="style.css" />
      <link rel="preconnect" href="https://fonts.googleapis.com">
      <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
      <link href="https://fonts.googleapis.com/css2?family=Space+Mono:ital@0;1&display=swap" rel="stylesheet">
    </head>
    <body>
      <div class="container" data-barba="container" data-barba-namespace="{slug}">
        <section class="left">
            <div class="heading-wrapper">
                <div class="heading-container">
                  <a href="index.html" class="heading-link">
                    <div class="heading-line" data-text="Algorave India">Algorave India</div>
                    <div class="heading-line" data-text="Compilation Tape">Compilation Tape</div>
                    <div class="heading-line" data-text="Vol.1">Vol.1</div>
                  </a>
                </div>
              </div>  

              <div class="track-card">
                <img src="assets/{slug}.jpg" alt="{name} Track Cover" class="cover-img" />
              </div>

          <div class="footer-links">
            <a href="about.html" class="left-link">About</a>
            <a href="https://opencollective.com/algorave-india" class="right-link">Contribute</a>
          </div>
        </section>

        <section class="two-column-grid">
          <div class="column">
            <iframe src="{zine_link}" style="border: 0; width: 100%; height: 100vh;" seamless></iframe>  
            <!-- <iframe src="sketch.html" style="border: 0; width: 100%; height: 100%;" seamless></iframe>   -->
        </div>
          <div class="column">
            <div class="track-info">
              <div class="track-header">
                <h1 class="track-title">{name}</h1>
                <div class="track-number">01</div>
              </div>

              <div class="track-actions">
                <button class="play-button" aria-label="Play audio snippet">
                  <span class="button-text">Play Snippet</span>
                  <span class="loading-dots"><span></span></span>
                </button>
                <button class="download-button">Download PDF</button>
              </div>
              <audio id="audioPlayer" preload="metadata">
                <source src="assets/snippets/{slug}.wav" type="audio/wav">
                Your browser does not support the audio element.
              </audio>
              
              <div class="artist-credits">
                <div class="artist-item">
                  <span class="artist-label">Track Artist</span>
                  <span class="artist-name">{track_artist}</span>
                </div>
                <div class="artist-item">
                  <span class="artist-label">Zine Artist</span>
                  <span class="artist-name">{zine_artist}</span>
                </div>
              </div>
              
              <div class="track-process">
                <h3 class="process-title">Process</h3>
                <p class="process-description">
                    {process}
                </p>
              </div>
              
            </div>
          </div>
        </section>
        
      </div>
      <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
      <script src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/SplitText.min.js"></script>
      <script src="https://unpkg.com/barba.js@2.9.7/dist/barba.min.js"></script>
      <script src="script.js"></script>
    </body>
    </html>
    """