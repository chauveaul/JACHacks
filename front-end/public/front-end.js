"use strict";

fetch("192.168.55.255:5000/position")
  .then((response) => {
    if (response.status >= 400) {
      throw new Error("Network response was not ok");
    }
    return response.json();
  })
  .then((data) => console.log(data))
  .catch((error) => console.error(`Error: ${error}`));
