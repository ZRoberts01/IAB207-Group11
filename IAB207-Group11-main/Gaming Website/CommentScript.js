window.onload = function() {
    function addComment(comment) {
      var Comments = document.querySelectorAll(".Comment");
      var curr = document.createElement("div");
      curr.setAttribute("class", "Comment active");
      var p1 = document.createElement("p");
      p1.setAttribute("class", "Comment");
      p1.innerHTML = comment;
      curr.appendChild(p1);
      if (Comments.length) {
        Comments[Comments.length -1].insertAdjacentHTML("afterEnd", curr.outerHTML)
      } else {
        document.forms[0].insertAdjacentHTML("afterEnd", curr.outerHTML)
      }
    }
  
    var obj = {
      Comment: "",
    };
  
    document.forms[0].onchange = function(e) {
      obj[e.target.name] = e.target.value;
    }

    document.forms[0].onsubmit = function(e) {
      e.preventDefault();
      addComment("14/6/22: " + obj.Comment)
    }
  }