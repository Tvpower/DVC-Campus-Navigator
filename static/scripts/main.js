// import data from './canvas_coordinates.js';
// var jsondata = require('../scripts/canvas_coordinates');
// import jsonData from '../scripts/canvas_coordinates';

text1 = " "

// Function to travel from Node A to Node B:
// nAx + (oBx - oAx)*scale,  nAy + (oBy - oAy)*scale

// var path;
// readTextFile("../static/path.json", function(text){
//     path = JSON.parse(text); //parse JSON
//     console.log(path);
// });

// var path = pathJsonData["path"]

// Get all elements with the button class (It's just one)
const search_buttons = document.getElementsByClassName("search-button")

// Create event listener
search_buttons[0].addEventListener("click", canvasFunctions)


// Holds all the functions whenever the search button is pressed
function canvasFunctions(){
    let all_functions = function(){
        wipeCanvas()
        fetch_and_draw()
        wipeCanvas()
    }
    window.setTimeout(all_functions, 50)
}
    const canvas = document.getElementById('DrawCanvas');
    const draw = canvas.getContext('2d');
// Important Note: fetch_and_draw() cannot return
function fetch_and_draw() {
    // Wait for python to write to the path.txt file
     fetch('static/file.txt')
        .then(response => response.text())
        .then(text => {
            let target_path = []
            let text1 = text

            // Find all node entries within text string (0 to n-2)
            while(text.indexOf(" ") !== -1){
                let next_space = text.indexOf(" ")
                text1 = text.substring(0, next_space)
                target_path.push(text1)
                text = text.substring(next_space + 1)
                // console.log(tmax= ", tmax, ", next_space index=", next_space)
            }

            // let i = 0, length = text.length;
            // // Parse through text file
            // for (; i < length; i += 3) {
            //     text1 = text.substring(i, i + 3).replace(/ /g, '')
            //     target_path.push(text1)
            // }

            draw.linewidth = 20;
            draw.strokeStyle = 'red';
           for (const element of target_path) {
               console.log(element)
           }

            // drawPath() Function
            let the_node = target_path[0]
            draw.beginPath();
            draw.moveTo(jsonData[the_node][0], jsonData[the_node][1]);

            for(let index = 0 ; index < target_path.length ; index++)
            {
                let the_node = target_path[index]
                console.log(the_node, "the_node raw: ", target_path[index])
                draw.lineTo(jsonData[the_node][0], jsonData[the_node][1]);
                draw.moveTo(jsonData[the_node][0], jsonData[the_node][1]);
                draw.stroke()
            }
            draw.closePath()
        });
}

function wipeCanvas(){
    draw.save();
    draw.setTransform(1, 0, 0, 1, 0, 0);
    draw.clearRect(0, 0, canvas.width, canvas.height);
    draw.restore();
}

// function drawPath(target_path){
//     console.log("drawPath called!")
//     // Delete anything with pcount when we finish when we finish
//     let the_path = target_path
//     console.log(the_path)
//
//     draw.moveTo(jsonData[the_path[0]][0], jsonData[the_path[0]][1]);
//
//     for(let index = 0 ; index < the_path.length ; index++)
//     {
//         let the_node = the_path[index]
//
//         draw.lineTo(jsonData[the_node][0], jsonData[the_node][1]);
//         draw.moveTo(jsonData[the_node][0], jsonData[the_node][1]);
//     }
//     draw.closePath();
//     draw.stroke();
// }

