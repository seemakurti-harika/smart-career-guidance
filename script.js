document.getElementById("careerForm").addEventListener("submit", function (e) {
    e.preventDefault();

    let name = document.getElementById("name").value;
    let skills = [];

    document.querySelectorAll("input[type='checkbox']:checked")
        .forEach(skill => skills.push(skill.value));

    let career = "";
    let roadmap = [];

    // Career logic (AUTOMATION)
    if (skills.includes("HTML") && skills.includes("CSS") && skills.includes("JavaScript")) {
        career = "Frontend Developer";
        roadmap = [
            "Master JavaScript",
            "Learn React",
            "Build Responsive Websites",
            "Create Portfolio Projects"
        ];
    }
    else if (skills.includes("Python") && skills.includes("SQL")) {
        career = "Data Analyst";
        roadmap = [
            "Learn Advanced Python",
            "Practice SQL Queries",
            "Learn Data Visualization",
            "Work on Real Datasets"
        ];
    }
    else {
        career = "General IT Career";
        roadmap = [
            "Strengthen Programming Basics",
            "Choose a Specialization",
            "Build Mini Projects",
            "Learn Industry Tools"
        ];
    }

    displayResult(name, career, roadmap);
});

function displayResult(name, career, roadmap) {
    let resultDiv = document.getElementById("result");

    let steps = "";
    roadmap.forEach(step => {
        steps += `<li>${step}</li>`;
    });

    resultDiv.innerHTML = `
        <h3>Hello ${name}</h3>
        <h4>Suggested Career: ${career}</h4>
        <p>Recommended Roadmap:</p>
        <ul>${steps}</ul>
    `;
}
