
function addFields(){
    // Number of inputs to create
    var number = document.getElementById("input_n").value;
    // Container <div> where dynamic content will be placed
    var container = document.getElementById("container");
    // Clear previous contents of the container
    while (container.hasChildNodes()) {
        container.removeChild(container.lastChild);
    }
    var action = document.createElement("input");
    action.type = "submit";
    action.name = "submit";
    action.id = "submit";
    //action.onclick = "buildData()"
    
    for (i=0;i<number;i++){
        // Append a node with a random text
        container.appendChild(document.createTextNode((i+1) + " RPN expression to evaluate "));
        // Create an <input> element, set its type and name attributes
        var input = document.createElement("input");
        input.type = "text";
        input.name = "exp" + i;
        container.appendChild(input);
        // Append a line break 
        container.appendChild(document.createElement("br"));
    }
    container.appendChild(action);
}


