<svg width="1200" height="300" viewBox="0 0 1200 300" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0d1117">
        <animate attributeName="stop-color" values="#0d1117;#131a2e;#0d1117" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="50%" stop-color="#161b33">
        <animate attributeName="stop-color" values="#161b33;#1c2140;#161b33" dur="6s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#0d1117">
        <animate attributeName="stop-color" values="#0d1117;#131a2e;#0d1117" dur="6s" repeatCount="indefinite"/>
      </stop>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7aa2f7"/>
      <stop offset="50%" stop-color="#bb9af7"/>
      <stop offset="100%" stop-color="#7dcfff"/>
    </linearGradient>
    <radialGradient id="glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#7aa2f7" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#7aa2f7" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="1200" height="300" rx="18" fill="url(#bgGrad)"/>

  <circle cx="1000" cy="80" r="140" fill="url(#glow)">
    <animate attributeName="r" values="140;170;140" dur="5s" repeatCount="indefinite"/>
  </circle>
  <circle cx="180" cy="240" r="120" fill="url(#glow)" opacity="0.6">
    <animate attributeName="r" values="120;150;120" dur="7s" repeatCount="indefinite"/>
  </circle>

  <g opacity="0.7">
    <circle cx="120" cy="60" r="2.5" fill="#7dcfff">
      <animate attributeName="cy" values="60;40;60" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.2;0.7" dur="4s" repeatCount="indefinite"/>
    </circle>
    <circle cx="220" cy="100" r="1.8" fill="#bb9af7">
      <animate attributeName="cy" values="100;75;100" dur="5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.15;0.6" dur="5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="1050" cy="220" r="2.2" fill="#7aa2f7">
      <animate attributeName="cy" values="220;195;220" dur="4.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.7;0.2;0.7" dur="4.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="950" cy="60" r="1.6" fill="#7dcfff">
      <animate attributeName="cy" values="60;35;60" dur="6s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.1;0.6" dur="6s" repeatCount="indefinite"/>
    </circle>
    <circle cx="60" cy="180" r="2" fill="#ff9e64">
      <animate attributeName="cy" values="180;155;180" dur="5.5s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.6;0.15;0.6" dur="5.5s" repeatCount="indefinite"/>
    </circle>
  </g>

  <g font-family="Consolas, 'Courier New', monospace">
    <text x="600" y="140" text-anchor="middle" font-size="42" font-weight="700" fill="url(#textGrad)">
      Hi, I'm Aayush Aade
      <animate attributeName="opacity" values="0;1" dur="1s" fill="freeze"/>
    </text>
    <text x="600" y="140" text-anchor="middle" font-size="42" font-weight="700" fill="none" stroke="#7aa2f7" stroke-width="0.5" opacity="0">
      <animate attributeName="opacity" values="0;0.5;0" dur="2.4s" begin="0.2s" fill="freeze"/>
    </text>

    <text x="600" y="185" text-anchor="middle" font-size="19" fill="#a9b1d6" opacity="0">
      AI &amp; Data Science Student · Building Real-Time AI Systems
      <animate attributeName="opacity" values="0;1" dur="1s" begin="0.9s" fill="freeze"/>
    </text>

    <text x="600" y="220" text-anchor="middle" font-size="15" fill="#7dcfff" opacity="0">
      Computer Vision &#8226; Machine Learning &#8226; Backend
      <animate attributeName="opacity" values="0;1" dur="1s" begin="1.5s" fill="freeze"/>
    </text>
  </g>

  <rect x="500" y="245" width="0" height="2" rx="1" fill="url(#textGrad)">
    <animate attributeName="width" values="0;200" dur="1.2s" begin="1.8s" fill="freeze"/>
    <animate attributeName="x" values="600;500" dur="1.2s" begin="1.8s" fill="freeze"/>
  </rect>

  <rect x="0" y="0" width="1200" height="300" rx="18" fill="none" stroke="#3b4261" stroke-width="1" opacity="0.5"/>
</svg>
