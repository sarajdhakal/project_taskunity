document.addEventListener("DOMContentLoaded", function (e) {
    document.querySelectorAll(".selectize").forEach(function (e) {
        NiceSelect.bind(e)
    })
}), document.addEventListener("DOMContentLoaded", function (e) {
    NiceSelect.bind(document.getElementById("search-select"), {
        searchable: !0
    })
});