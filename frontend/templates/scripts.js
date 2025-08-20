const footer = document.getElementById("footer");
const topicSelect = document.getElementById("topicSelect");
const statisticsGroup = document.getElementById("statisticsGroup");

topicSelect.addEventListener("change", () => {
  if (topicSelect.value === "statistics") {
    statisticsGroup.style.display = "block";
  } else {
    statisticsGroup.style.display = "none";
  }
});

const currentYear = new Date().getFullYear();
footer.innerHTML = `&copy; ${currentYear} MathSolver | Powered by BrainTech`;
