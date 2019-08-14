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
let previousLength = "";
let unstripped = "";
let courseName = "";
let coursesBefore = [];

function drop(ev) {
  ev.preventDefault();
  data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  column = document.getElementById(ev.srcElement.id).children;
  course = document.getElementById(data).id;
  for (counter = 0; counter < columnOrder.length; counter++){
    if (columnOrder[counter] == ev.target.id){
      break;
    }
    else {
      previous = document.getElementById(columnOrder[counter]);
      previousLength = previous.getElementsByTagName('p').length;
      console.log(previousLength);
      for (count = 0; count < previousLength; count++){
        unstripped = previous.getElementsByTagName('p')[count];
        console.log(unstripped);
        coursesBefore.push(unstripped.innerHTML)
      }
    }
  }
}
