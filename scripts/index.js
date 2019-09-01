function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

let columnOrder = ["1A", "1W", "1S", "2A", "2W", "2S", "3A", "3W", "3S", "4A", "4W", "4S",];
let data = "";
let column = "";
let course = "";
let previous = "";
let prereqs = "";
let neededFor = "";
let temp = "";
let temp1 = "";
let start="";
let start1="";
let end="";
let end1="";
let previousLength = "";
let unstripped = "";
let courseName = "";
let coursesBefore = [];
let coursesAfter = [];
let prereqsMade = false;
let neededMade = false;

function drop(ev) {
  ev.preventDefault();
  data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  temp = document.getElementById(data).getElementsByClassName('button');
  prereqs = temp[0].innerHTML.toString();
  start = prereqs.indexOf("Pre-reqs: ");
  start1 = prereqs.indexOf("Needed for: ");
  end1 = prereqs.indexOf("data-original-title");
  end = prereqs.indexOf(". Needed");
  temp = prereqs.substring(start+10, end);
  temp1 = prereqs.substring(start1+12, end1-2);
  prereqs = temp.split(" ");
  neededFor = temp1.split(" ");
  course = document.getElementById(data).id;

  for (let i = 0; i < columnOrder.length; i++) {
    if (columnOrder[i] == ev.target.id){
      column = i;
    }
  }

  // creates list of coursesBefore and coursesAfter the moved course
  for (counter = 0; counter < columnOrder.length; counter++) {
    if (counter == column){
      continue;
    }
    else if (counter > column){
      previous = document.getElementById(columnOrder[counter]);
      previousLength = previous.getElementsByTagName('p').length;
      for (count = 0; count < previousLength; count++){
        unstripped = previous.getElementsByTagName('p')[count];
        coursesAfter.push(unstripped.innerHTML)
      }
    }
    else {
      previous = document.getElementById(columnOrder[counter]);
      previousLength = previous.getElementsByTagName('p').length;
      for (count = 0; count < previousLength; count++){
        unstripped = previous.getElementsByTagName('p')[count];
        coursesBefore.push(unstripped.innerHTML)
      }
    }
  }

  // checks if the prereqs of course are met
  if ((prereqs == "none") == false) {
    for (counter = 0; counter < prereqs.length; counter++) {
      prereqsMade = false;
      for (counter1 = 0; counter1 < coursesBefore.length; counter1++){
        if (prereqs[counter] == coursesBefore[counter1]) {
          prereqsMade = true;
          break;
        }
      }
      if (prereqsMade == false){
        alert("The pre-reqs of this class have not been fulfilled. Please move it back.");
      }
    }
  }

  // checks to make sure that other classes previous in schedule do not need this course as a pre-req
  if ((neededFor == "none") == false) {
    for (counter = 0; counter < neededFor.length; counter++) {
      neededMade = false;
      for (counter1 = 0; counter1 < coursesAfter.length; counter1++){
        if (neededFor[counter] == coursesAfter[counter1]) {
          neededMade = true;
          break;
        }
      }
      if (neededMade == false){
        alert("This class is a pre-req for another course. Please move it back.");
      }
    }
  }
  coursesBefore=[];
  coursesAfter=[];
}
