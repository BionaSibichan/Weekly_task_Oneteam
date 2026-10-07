let students = [];

let form = document.getElementById("studentForm");
let table = document.getElementById("table");

function displayStudents() {

    table.innerHTML = "";

    students.forEach(function(student) {

        let row = document.createElement("tr");

        row.innerHTML =
            "<td>" + student.name + "</td>" +
            "<td>" + student.subject + "</td>" +
            "<td>" + student.marks + "</td>" +
            "<td>" + (student.marks >= 50 ? "Pass" : "Fail") + "</td>";

        if (student.marks < 50) {
            row.style.backgroundColor = "red";
        }

        table.appendChild(row);
    });
}

form.addEventListener("submit", function(event) {

    event.preventDefault();

    let name = document.getElementById("name").value;
    let subject = document.getElementById("subject").value;
    let marks = document.getElementById("marks").value;

    if (name == "" || subject == "" || marks == "") {
        alert("Please enter all details");
        return;
    }

    let student = {
        name: name,
        subject: subject,
        marks: Number(marks)
    };

    students.push(student);

    displayStudents();

    form.reset();
});

document.getElementById("avgBtn").addEventListener("click", function() {

    if (students.length == 0) {
        document.getElementById("average").innerHTML = "No students";
        return;
    }

    let total = students.reduce(function(sum, student) {
        return sum + student.marks;
    }, 0);

    let avg = total / students.length;

    document.getElementById("average").innerHTML =
        "Average Marks: " + avg;
});

document.getElementById("removeBtn").addEventListener("click", function() {

    let name = prompt("Enter student name:");

    students = students.filter(function(student) {
        return student.name != name;
    });

    displayStudents();
});

displayStudents();