function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
  ev.dataTransfer.setData("text", ev.target.id);
}

let columnOrder = ["1A", "1W", "1S"]

function drop(ev) {
  ev.preventDefault();
  var data = ev.dataTransfer.getData("text");
  ev.target.appendChild(document.getElementById(data));
  let column = document.getElementById(ev.srcElement.id).children;
  let course = document.getElementById(data).id;
  console.log(course);
  console.log(ev.target.id);
  // console.log(course.getAttribute("hidden"));
  // for (child = 0; child < column.length; child++) {
  //   console.log(column[child]);
  // }
  for (counter = 0; counter < columnOrder.length; counter++){
    if (columnOrder[counter] == ev.target.id){
      break;
    }
    else {
      console.log(document.getElementById(columnOrder[counter]));
    }
  }
}
