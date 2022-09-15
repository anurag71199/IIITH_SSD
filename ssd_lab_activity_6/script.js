
            function ValidateEmail() 
                {
                    var mail = document.getElementById("email").value;
                    if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(myForm.emailAddr.value))
                    {
                        return (true)
                    }
                    alert("You have entered an invalid email address!")
                    return (false)
                }

                var myInput = document.getElementById("server_password");

                myInput.onfocus = function() {
  document.getElementById("message").style.display = "block";
}

// When the user clicks outside of the password field, hide the message box
myInput.onblur = function() {
  document.getElementById("message").style.display = "none";
}

                myInput.onkeyup = function() {
                    var upperCaseLetters = new RegExp("[A-Z]");
  if(myInput.value.match(upperCaseLetters)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }
                }
                var numbers = /[0-9]/g;
  if(myInput.value.match(numbers)) {  
    capital.classList.remove("invalid");
    capital.classList.add("valid");
  } else {
    capital.classList.remove("valid");
    capital.classList.add("invalid");
  }


        
  function dragstartHandler(evt) {
  evt.dataTransfer.setData("MyDraggedElementId", evt.target.id);
}
const arr = [];
//drag an drop functionality
function dragHandler(evt) {
   showLog("The p element is being dragged");
}

function ondragenterHandler()  {
   showLog("The p element enter drop-target");
}

function dragoverHandler(evt) {
    evt.preventDefault(); // Important!!
}

function dropHandler(evt) {
   evt.preventDefault(); // Important!!
   var elementId = evt.dataTransfer.getData("MyDraggedElementId");
   evt.target.appendChild(document.getElementById(elementId));
   arr.push(elementId);
   showLog("The p element was dropped");
}

// -------------------------------------------------------

function showLog(text)  {
   document.getElementById("log-div").innerHTML = text;
}

window.onload = function(){
   document.getElementById('submit').onclick = function(e){
       alert(document.getElementById("manager_name").value);
       return false;
   }
}
function display()
{
var x=document.details.manager_name.value;
alert("FIRST NAME:"+x);
}
       
myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
  }
  
  // When the user clicks outside of the password field, hide the message box
  myInput.onblur = function() {
    document.getElementById("message").style.display = "none";
  }

  function fofunc() {
    var x = document.getElementById("server_password");
    var y = document.getElementById("confirm_password");
    let result = x.localeCompare(y);
    if(result!=0){
        alert("You have entered an invalid email address!")
    }
    else{
        alert("You have ente")
    }
    // x.value = x.value.toUpperCase();
  }