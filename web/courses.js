let coursework = [
    {
        name: "Course 1",
        modules: [
            {
                module: "Module 1",
                proficiency: 8,
                lastRevision: -10,
                nextRevision: +20,
            }, 
            {
                module: "Module 2",
                proficiency: 3,
                lastRevision: 0,
                nextRevision: 20,
            }]
    },
    // {
    //     name: "Course 2",
    //     modules: [
    //         {
    //             module: "Module 1",
    //             proficiency: 5,
    //             lastRevision: null,
    //             nextRevision: null,
    //         }
    //     ]
    // }
];


// RENDER COURSES
function renderCourses() {
    const container = document.getElementById("courses-display");
    // container.innerHTML = "";
    coursework.forEach(course => {
        const courseArticle = document.createElement("article");
        container.appendChild(courseArticle);
        courseArticle.classList.add("course");
        
        // TODO: need to not use innerHTML but this will do for now
        courseArticle.innerHTML = `
            <h3 class="course-name">${course.name}</h3>
            <table class="module">
                <thead>
                    <tr>
                        <th>Proficiency</th>
                        <th>Module name</th>
                        <th>Last revision</th>
                        <th>Next revision</th>
                    </tr>
                </thead>
                <tbody>
                </tbody>
            </table>
        `;
        const moduleTable = container.querySelector(".module");
        course.modules.forEach(moduleInfo => {
            let moduleEntry = moduleTable.insertRow(-1);

            let proficiencyCell = moduleEntry.insertCell(0);
            proficiencyCell.classList.add("proficiency");
            proficiencyCell.textContent = moduleInfo.proficiency
            moduleEntry.appendChild(proficiencyCell);

            let nameCell = moduleEntry.insertCell(1);
            nameCell.classList.add("module-name");
            moduleEntry.appendChild(nameCell);

            let lastRevisionCell = moduleEntry.insertCell(2);
            lastRevisionCell.classList.add("last-revision");
            moduleEntry.appendChild(lastRevisionCell);

            let nextRevisionCell = moduleEntry.insertCell(3);
            nextRevisionCell.classList.add("next-revision");
            moduleEntry.appendChild(nextRevisionCell);
        })

        // <tr>
        //     <td class="proficiency">8</td>
        //     <td class="module-name">Module 1</td>
        //     <td>-10</td>
        //     <td>+20</td>
        // </tr>
        // <tr>
        //     <td>3</td>
        //     <td>Module 2</td>
        //     <td>0</td>
        //     <td>+2</td>
        // </tr>
    });
}

// ADD COURSES POPUP
// const addCoursePopup = document.getElementById("add-course-form")
// addCoursePopup.addEventListener("submit", e => {
//     let newCourse = prompt("Enter new course name");
//     coursework.push({
//         name: newCourse,
//         modules: []
//     })
//     renderCourses();
// })

renderCourses();