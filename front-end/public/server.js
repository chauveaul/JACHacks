"use strict";

const express = require("express");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(cors());
app.options('*', cors());

app.use(express.json());
app.use(express.static(path.join(__dirname, "..", "/public")));

app.get("/", function (req, res) {
  res.sendFile(path.join(__dirname, "..", "index.html"));
});

app.get("/test", function (req, res) {
  fetch("http://127.0.0.1:5000/position")
})

app.get("./192.168.55.92:5000/position", function (req, res) {
  const response = res;
  console.log(response);
});

app.listen(3000, function () {
  console.log("Server is running on port 3000");
});
