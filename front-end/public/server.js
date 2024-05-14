"use strict";

const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(cors());
app.options("*", cors());

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "/public")));

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "index.html"));
});

app.get("/position", async function (req, res) {
  const pos = await fetch("http://127.0.0.1:5000/position")
    .then((response) => {
      if (response.status >= 400) {
        throw new Error("Network response was not ok");
      }
      return response.json();
    })
    .then((data) => data)
    .catch((error) => console.error(`Error: ${error}`));

  return res.status(200).json({
    success: true,
    position: pos,
  });
});

app.listen(3000, function () {
  console.log("Server is running on port 3000");
});
