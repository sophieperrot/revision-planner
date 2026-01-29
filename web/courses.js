let coursework = [
    {
        name: "Course 1",
        id: "course-1",
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
                nextRevision: +2,
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
    container.innerHTML = "";
    coursework.forEach((course) => {
        const courseArticle = document.createElement("article");
        container.appendChild(courseArticle);
        courseArticle.classList.add("course");
        courseArticle.setAttribute("id", course.id);
        
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
        const moduleTable = container.querySelector(`#${course.id} > .module`);
        course.modules.forEach(moduleInfo => {
            let moduleEntry = moduleTable.insertRow(-1);

            let proficiencyCell = moduleEntry.insertCell(0);
            proficiencyCell.classList.add("proficiency");
            proficiencyCell.textContent = moduleInfo.proficiency
            moduleEntry.appendChild(proficiencyCell);

            let nameCell = moduleEntry.insertCell(1);
            nameCell.classList.add("module-name");
            nameCell.textContent = moduleInfo.module;
            moduleEntry.appendChild(nameCell);

            let lastRevisionCell = moduleEntry.insertCell(2);
            lastRevisionCell.classList.add("last-revision");
            lastRevisionCell.textContent = moduleInfo.lastRevision;
            moduleEntry.appendChild(lastRevisionCell);

            let nextRevisionCell = moduleEntry.insertCell(3);
            nextRevisionCell.classList.add("next-revision");
            nextRevisionCell.textContent = moduleInfo.nextRevision;
            moduleEntry.appendChild(nextRevisionCell);
        })
    });
}

// ADD COURSES POPUP
const addCoursePopup = document.getElementById("add-course-form")
addCoursePopup.addEventListener("submit", (e) => {
    e.preventDefault();
    let name_text = addCoursePopup.elements[0].value;
    for (let key in coursework) {
        if (coursework[key].name === name_text) {
            console.log("already exists")
        }
    }

    let moduleList = [];
    const modules = addCoursePopup.elements[1].value.split(", ");
    modules.forEach((moduleName) => {
        moduleList.push({
            module: moduleName,
            proficiency: 0,
            lastRevision: 0,
            nextRevision: 0
        });
    });
    coursework.push({
        name: name_text,
        id: name_text.split(/\s+/).join("-"),
        modules: moduleList
    });
    console.log(coursework);
    renderCourses();
})

renderCourses();