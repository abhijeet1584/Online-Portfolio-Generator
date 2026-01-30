function generate() {
  fetch("http://127.0.0.1:5000/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      name: namefl.value,
      email: email.value,
      phone: phone.value,
      summary: summary.value,
      skills: skills.value,
      experience: experience.value,
      education: education.value
    })
  })
  .then(res => res.blob())
  .then(blob => {
    let url = window.URL.createObjectURL(blob);
    let a = document.createElement("a");
    a.href = url;
    a.download = "resume.pdf";
    a.click();
  });
}
