"use strict";

const startBtn = document.querySelector(".start-python");

const promptBg = document.querySelector(".prompt-bg");
const promptSection = document.querySelector(".action-prompt");
const promptHeader = document.querySelector(".prompt-header");
const promptParagraph = document.querySelector(".prompt-paragraph");
const promptButton = document.querySelector(".prompt-button");

let step = 0;

const values = [];

startBtn.addEventListener("click", function () {
  promptBg.classList.add("active");
  promptSection.classList.add("active");
  step++;
});

promptButton.addEventListener("click", async function () {
  console.log("button click");
  if (step === 1) {
    promptButton.textContent = "Wait 5 sec";
    setTimeout(async function () {
      values.push(await fetchPy);
      promptHeader.textContent = "Get to the second point";
      promptParagraph.textContent =
        "You can now proceed to the second step. Head to the next position and stand still for 5 seconds";
      promptButton.textContent = "I'm ready!";
      step++;
    }, 5000);
  } else if (step === 2) {
    promptButton.textContent = "Wait 5 sec";
    setTimeout(async function () {
      values.push(await fetchPy);
      promptHeader.textContent = "Get to the last point";
      promptParagraph.textContent =
        "You can now proceed to the next step. Head to the last position and stand still for 5 seconds";
      promptButton.textContent = "I'm ready!";
      step++;
    }, 5000);
  } else if (step === 3) {
    promptButton.textContent = "Wait 5 sec";
    setTimeout(async function () {
      values.push(await fetchPy);
      promptHeader.textContent = "You're all set!";
      promptParagraph.textContent =
        "Proceed to the next step to see the final results!";
      promptButton.textContent = "Results!!";
      step++;
    }, 5000);
  } else if (step === 4) {
    fetch("http://127.0.0.1:5000/image", {
      method: "post",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        r1: values[0],
        r2: values[1],
        r3: values[2],
      }),
    });
  }
});

const fetchPy = function () {
  fetch("http://127.0.0.1:5000/position")
    .then((response) => {
      if (response.status >= 400) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => data)
    .catch((error) => console.error(`Error: ${error}`));
};
