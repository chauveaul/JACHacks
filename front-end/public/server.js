"use strict";

const express = require("express");
const path = require("path");

const app = express();

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "/public")));

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "index.html"));
});

app.get("/http://127.0.0.1:5000/position", function (req, res) {
  const response = res;
  console.log(response);
});

app.listen(3000, function () {
  console.log("Server is running on port 3000");
});
