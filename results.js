const cardInfo = {
  "Transactional": {
    "Fields": ["Order ID", "Customer ID", "Transaction Date", "Amount", "Product ID"],
    "Pros": "Provides reliable revenue signals; good base for lifetime value estimation.",
    "Cons": "Doesn’t explain customer behavior or engagement."
  },
  "Demographic": {
    "Fields": ["Age", "Gender", "Location", "Income Bracket", "Occupation"],
    "Pros": "Adds context for segmentation and targeting.",
    "Cons": "Too static; doesn’t reflect actual purchase behavior."
  },
  "Behavioral": {
    "Fields": ["Page Views", "Clicks", "Session Duration", "Search Terms", "Add to Cart"],
    "Pros": "Gives early signals of interest or churn risk.",
    "Cons": "Not always tied to revenue; may be noisy."
  }
};

const comboData = {
  "Transactional,Behavioral": {
    "Pros": "Combines spend and engagement — strong for predicting future value and churn.",
    "Cons": "Lacks demographic targeting or persona insights."
  },
  "Transactional,Demographic": {
    "Pros": "Helps identify high-value customer groups.",
    "Cons": "Misses future behavior signals."
  },
  "Demographic,Behavioral": {
    "Pros": "Useful for intent-based segmentation before conversion.",
    "Cons": "No actual spend data to support value."
  },
  "Transactional,Demographic,Behavioral": {
    "Pros": "Full-stack visibility — customer profile, actions, and value. Best for holistic CLTV.",
    "Cons": "Requires careful coordination; may be harder to implement cleanly."
  }
};

function getQuerySources() {
  const params = new URLSearchParams(window.location.search);
  const sources = params.get("sources");
  if (!sources) return [];
  return sources.split(",").map(s => s.trim()).filter(Boolean);
}

function renderResult() {
  const selected = getQuerySources();
  const container = document.getElementById("summary");

  if (selected.length === 0) {
    container.innerHTML = "<p>No data sources selected.</p>";
    return;
  }

  container.innerHTML = `<h2>✅ Selected Data Sources</h2><ul>${selected.map(s => `<li>${s}</li>`).join("")}</ul>`;

  // Collect fields
  let allFields = new Set();
  selected.forEach(s => {
    cardInfo[s]?.Fields?.forEach(f => allFields.add(f));
  });

  container.innerHTML += `<h2>📌 Available Fields</h2><ul>${[...allFields].map(f => `<li>${f}</li>`).join("")}</ul>`;

  const sortedKey = selected.slice().sort().join(",");
  if (comboData[sortedKey]) {
    container.innerHTML += `<h2>✅ Pros (Combination View)</h2><p>${comboData[sortedKey].Pros}</p>`;
    container.innerHTML += `<h2>❌ Cons (Combination View)</h2><p>${comboData[sortedKey].Cons}</p>`;
  } else {
    container.innerHTML += `<h2>✅ Pros (Individual)</h2><ul>${selected.map(s => `<li><strong>${s}</strong>: ${cardInfo[s].Pros}</li>`).join("")}</ul>`;
    container.innerHTML += `<h2>❌ Cons (Individual)</h2><ul>${selected.map(s => `<li><strong>${s}</strong>: ${cardInfo[s].Cons}</li>`).join("")}</ul>`;
  }
}

renderResult();
