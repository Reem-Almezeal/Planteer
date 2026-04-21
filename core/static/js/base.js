document.addEventListener("DOMContentLoaded", function () {
    const html = document.documentElement;

    const themeToggle = document.getElementById("theme-toggle");
    const langToggle = document.getElementById("lang-toggle");
    const langForm = document.getElementById("lang-form");
    const langInput = document.getElementById("language-input");

    const savedTheme = localStorage.getItem("planteer-theme") || "light";

    function applyTheme(theme) {
        html.setAttribute("data-theme", theme);

        if (themeToggle) {
            themeToggle.textContent = theme === "dark" ? "🌙" : "☀️";
        }

        localStorage.setItem("planteer-theme", theme);
    }

    if (themeToggle) {
        themeToggle.addEventListener("click", function () {
            const currentTheme = html.getAttribute("data-theme") || "light";
            const newTheme = currentTheme === "dark" ? "light" : "dark";
            applyTheme(newTheme);
        });
    }

    applyTheme(savedTheme);

    if (langToggle && langForm && langInput) {
        langToggle.addEventListener("click", function (e) {
            e.preventDefault();

            const currentLang = html.getAttribute("lang") || "en";
            const newLang = currentLang === "ar" ? "en" : "ar";

            langInput.value = newLang;
            langForm.submit();
        });
    }

    if (typeof AOS !== "undefined") {
        AOS.init({
            duration: 900,
            easing: "ease-out-cubic",
            once: true,
            offset: 40
        });
    }
});