const output = document.querySelector(".output");
output.textContent = "";

for (let i = 10; i >= 0; i--) {
  const para = document.createElement("p");
  if (i == 0) {
    para.textContent = `${i} Blast off`;
    output.appendChild(para);
    // console.log(i + " end")
    continue;
  }
  para.textContent = `${i} Countdown`;
  output.appendChild(para);
  // console.log(i + " start")
}
