const footer = document.getElementById("footer");
const topicSelect = document.getElementById("topicSelect");
const statisticsGroup = document.getElementById("statisticsGroup");
const numberBasesGroup = document.getElementById("numberBasesGroup");
const matricesGroup = document.getElementById("matricesGroup");
const simultaneousGroup = document.getElementById("simultaneousGroup");

function hideAllGroups() {
  statisticsGroup.style.display = "none";
  numberBasesGroup.style.display = "none";
  matricesGroup.style.display = "none";
  simultaneousGroup.style.display = "none";
}


topicSelect.addEventListener("change", () => {
  hideAllGroups(); 
  if (topicSelect.value === "statistics") {
    statisticsGroup.style.display = "block";
  } else if (topicSelect.value === "number-bases") {
    numberBasesGroup.style.display = "block";
  } else if (topicSelect.value === "matrices") {
    matricesGroup.style.display = "block";
  } else if (topicSelect.value === "simultaneous") {
    simultaneousGroup.style.display = "block";
  }
});

const currentYear = new Date().getFullYear();
footer.innerHTML = `&copy; ${currentYear} MathSolver | Powered by BrainTech`;

