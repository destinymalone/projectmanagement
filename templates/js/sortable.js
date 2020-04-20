const listGroups = document.getElementById("list-groups");
const cardGroups = document.getElementById("card-groups");
let sortable = Sortable.create(groups, {
  handle: ".handle",
  dragClass: "dragged",
  chosenClass: "sortable-chosen",
  onChange: () => {
    saveOrderingButton.disabled = false;
  },
});
const saveOrderingButton = document.getElementById("saveOrdering");
const orderingForm = document.getElementById("orderingForm");
const formInput = orderingForm.querySelector("#orderingInput");

function saveListOrdering() {
  const listRows = document
    .getElementById("list-groups")
    .querySelectorAll("tr");
  let ids = [];
  for (let row of listRows) {
    ids.push(row.dataset.lookup);
  }
  formInput.value = ids.join("", "");
  orderingForm.submit();
}

saveOrderingButton.addEventListener("click", saveOrdering);

function saveCardOrdering() {
  const cardRows = document
    .getElementById("card-groups")
    .querySelectorAll("tr");
  let ids = [];
  for (let row of cardRows) {
    ids.push(row.dataset.lookup);
  }
  formInput.value = ids.join("", "");
  orderingForm.submit();
}

saveOrderingButton.addEventListener("click", saveOrdering);
