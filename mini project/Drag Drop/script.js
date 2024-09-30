const dragAndDropItems = document.getElementById("lang-group");

new Sortable(dragAndDropItems,{
    Animation: 350,
    chosenClass: "lang-chosen",
    dragClass: "lang-drag",
})