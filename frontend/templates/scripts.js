const footer = document.getElementById("footer");
const topicSelect = document.getElementById("topicSelect");
const statisticsGroup = document.getElementById("statisticsGroup");
const numberBasesGroup = document.getElementById("numberBasesGroup");

topicSelect.addEventListener("change", () => {
  if (topicSelect.value === "statistics") {
    statisticsGroup.style.display = "block";
  } else {
    statisticsGroup.style.display = "none";
  }
});

topicSelect.addEventListener("change", () => {
  if (topicSelect.value === "number-bases") {
    numberBasesGroup.style.display = "block";
  } else {
    numberBasesGroup.style.display = "none";
  }
});

const currentYear = new Date().getFullYear();
footer.innerHTML = `&copy; ${currentYear} MathSolver | Powered by BrainTech`;
