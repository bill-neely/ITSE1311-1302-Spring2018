function setup() {
  for (i = 0; i < students.length; i++) {
    option = buildSelectOptions(students[i]);
    document.getElementById('studentSelector').appendChild(option);
  }
}

function buildSelectOptions(student) {
  option = document.createElement('option');
  option.setAttribute('value', student.idNumber);
  option.innerHTML = student.lastName + ", " + student.firstName;
  return option;
}

function chooseStudent() {
  document.getElementById('reportCard').className = "hide";
  choice = document.getElementById('studentSelector');
  chosenID = choice[choice.selectedIndex].value;
  for (i = 0; i < students.length; i++) {
    if (students[i].idNumber == chosenID) {
      buildReportCard(students[i]);
      break;
    }
  }
}

function buildReportCard(student) {
  document.getElementById('name').innerHTML = student.lastName + ", " + student.firstName;
  document.getElementById('street').innerHTML = student.streetAddress;
  document.getElementById('city').innerHTML = student.city + ", " + student.state + " " + student.zipCode;
  document.getElementById('avatar').src = student.avatar;
  document.getElementById('courseList');
  courseRows = document.getElementById('courseRows');
  courseRows.innerHTML = "";
  student.courses.forEach(function (course) {
    document.getElementById('courseRows').appendChild(makeRow(course));
  });
  document.getElementById('idNumber').innerHTML = student.idNumber;
  document.getElementById('reportCard').className = "";
}

function makeRow(course) {
  row = document.createElement('tr');
  row.appendChild(makeTD(course.courseName));
  row.appendChild(makeTD(course.instructor));
  row.appendChild(makeTD(course.termGrades[0]));
  row.appendChild(makeTD(course.termGrades[1]));
  row.appendChild(makeTD(course.termGrades[2]));
  row.appendChild(makeTD(course.termGrades[3]));
  row.appendChild(makeTD(average(course.termGrades)));
  return row;
}

function makeTD(data) {
  cell = document.createElement('td');
  cell.innerHTML = data
  return cell;
}

function average(anArray) {
  sum = 0;
  anArray.forEach(function (elem) {
    sum += elem;
  });
  return sum / anArray.length;
}
