// Toggle selection on card click
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
    card.classList.toggle('selected');
  });
});

document.getElementById('submitBtn').addEventListener('click', () => {
  const selected = Array.from(document.querySelectorAll('.card.selected'))
    .map(card => card.dataset.source);

  if (selected.length === 0) {
    alert("Please select at least one data source.");
    return;
  }

  // Redirect with selected sources as query params
  const query = encodeURIComponent(selected.join(','));
  window.location.href = `results.html?sources=${query}`;
});
