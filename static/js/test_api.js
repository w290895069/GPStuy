// divvy = document.getElementById("test_div");
// fetch('/api_path/', {'loc1':131, 'loc2': 230})
//   .then(function(response) {
//       console.log("hello");
//       console.log();
//     divvy.innerHTML =  response.JSON;
//   });
var pic1 = document.getElementById("vimage1");
var pic2 = document.getElementById("vimage2");

var divvy = document.getElementById("test_div");
var divvy2 = document.getElementById("test_div2");

function do_stuff(maze,pic) {
    var dim1 = [maze.length, maze[0].length];
    pic.setAttribute("height", dim1[0] * 20);
    pic.setAttribute("width", dim1[1] * 20);
    for (var i = 0; i < maze.length; i++) {
        for (var j = 0; j < maze[0].length; j++) {
            var c = document.createElementNS("http://www.w3.org/2000/svg", "rect");
            // console.log(c);
            c.setAttribute("height", 20);
            c.setAttribute("width", 20);
            c.setAttribute("rx", 5);
            c.setAttribute("x", 20 * j);
            c.setAttribute("y", 20 * i);
            c.setAttribute("stroke", "black");
            // console.log(maze[i][j]);
            // if (!maze[i][j]){
            //     console.log("FDSFDSF")
            // }
            switch (maze[i][j]) {
                case "@":
                    c.setAttribute("fill", "green");
                    break;
                case "#":
                    c.setAttribute("fill", "tan");
                    break;
                case " ":
                    c.setAttribute("fill", "white");
                    break;
                case ".":
                    c.setAttribute("fill", "white");
                    break;
                case "S":
                    c.setAttribute("fill", "blue");
                    break;
                case "E":
                    c.setAttribute("fill", "purple");
                    break;
                default:
                    c.setAttribute("fill", "red");
            }
            pic.appendChild(c)
        }
    }
}


var promise = new Promise(function (resolve, reject) {
    $.get("/api_path/", {'loc1': 131, 'loc2': 230})
        .done(function (response) {
            resolve(response);
        })
        .fail(function () {
            reject();
        });
});

promise.then(function (result) {
        var maze = JSON.parse(result);
        var floor1 = maze['f1'];
        var floor2 = maze['f2'];
        console.log("DFSFDS");
        console.log(maze);
        console.log(floor1);
        console.log(floor2);
        for (var i = 0; i < floor1.length; i++) {
            for (var j = 0; j < floor1[0].length; j++) {
                divvy.innerHTML += floor1[i][j];
            }
            // console.log(divvy)
            // divvy.innerHTML+=floor1[i];
            divvy.innerHTML += "<br>";
        }
        for (var i = 0; i < floor2.length; i++) {
            for (var j = 0; j < floor2[0].length; j++) {
                divvy2.innerHTML += floor2[i][j];
            }
            // divvy.innerHTML+=floor2[i];
            divvy2.innerHTML += "<br>";
        }
        // divvy.innerHTML.replace(" ", ".");
        // divvy2.innerHTML.replace(" ", ".");
        do_stuff(floor1,pic1);
        do_stuff(floor2,pic2);
        gen
    },

    function (err) {
        console.log(err);
    }
);

function gendirections(map) {
    var directions = [(0,1),(-1,0),(0,-1),(1,0)];
    var map = document.getElementById("test_div");
    console.log(map)
    var res = map.split("</br>")
// function dirgen(map){

// }
// mapArr = [[cor for cor in row] in map.split('<br>')]
//     cur_xcor = []
// 	for dir in directions:
// 		#keep going in correct way 
//         #once you hit a ! stop and then loop through directions again
//         #first check if it is stairs or dest; if it is you have arrived/ take the stairs 
    
};