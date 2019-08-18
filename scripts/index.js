function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

let columnOrder = ["1A", "1W", "1S"];
let data = "";
let column = "";
let course = "";
let previous = "";
let prereqs = "";
let temp = "";
let start="";
let end="";
let previousLength = "";
let unstripped = "";
let courseName = "";
let coursesBefore = [];
let prereqsMade = false;

function drop(ev) {
  ev.preventDefault();
  data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  column = document.getElementById(ev.srcElement.id).children;
  temp = document.getElementById(data).getElementsByClassName('button');
  prereqs = temp[0].innerHTML.toString();
  start = prereqs.indexOf("Pre-reqs: ")
  end = prereqs.indexOf("data-original-title")
  temp = prereqs.substring(start+10, end-2);
  prereqs = temp.split(" ");
  course = document.getElementById(data).id;
  for (counter = 0; counter < columnOrder.length; counter++){
    if (columnOrder[counter] == ev.target.id){
      break;
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
  // TODO: check for case when there are no prereqs
  for (counter = 0; counter < prereqs.length; counter++) {
    prereqsMade = false;
    for (counter1 = 0; counter1 < coursesBefore.length; counter1++){
      if (prereqs[counter] == coursesBefore[counter1]) {
        prereqsMade = true;
        break;
      }
    }
    if (prereqsMade == false){
      alert("the pre-reqs of this class have not been fulfilled");
    }
  }
}
