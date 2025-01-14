const profileDropdown = () => {
    document.getElementById("profile_dropdown").classList.toggle("nav__profile_show");
};

const settingsDropdown = () => {
    document.getElementById("settings_dropdown").classList.toggle("nav__settings_show");
};

window.onclick = (event) => {
    console.log(event.target);
    if (!event.target.matches("#profile_icon")) {
        var dropdowns = document.getElementsByClassName("nav__profile_content");
        for (let i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains("nav__profile_show")) {
                dropdowns[i].classList.remove("nav__profile_show");
            }
        }
    }

    if (!event.target.matches("#settings_icon")) {
        var dropdowns = document.getElementsByClassName("nav__settings_content");
        for (let i = 0; i < dropdowns.length; i++) {
            if (dropdowns[i].classList.contains("nav__settings_show")) {
                dropdowns[i].classList.remove("nav__settings_show");
            }
        }
    }
}