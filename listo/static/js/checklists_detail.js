/* globals dragula */

for (const link of document.querySelectorAll('.item-edit-link')) {
  link.addEventListener('click', event => {
    link.parentElement.querySelector('.checklist-item-body').style.display = 'none'
    link.parentElement.querySelector('.item-edit-form').style.display = 'inline-block'
  })
}

const checklistReorderingLink = document.getElementById('checklist-reorder-link')
let drake

checklistReorderingLink.addEventListener('click', (event) => {
  event.preventDefault()
  const itemList = document.getElementById('checklist-items')

  if (checklistReorderingLink.dataset.reordering === 'true') {
    itemList.classList.remove('checklist-reordering')
    drake.destroy()
    checklistReorderingLink.classList.remove('button')
    checklistReorderingLink.innerText = 'Reorder'
    checklistReorderingLink.dataset.reordering = 'false'

    const items = itemList.querySelectorAll('.checklist-item')
    const ids = []
    for (const item of items) {
      ids.push(item.dataset.pk)
    }
    console.log(ids)
    fetch(`/lists/${checklistPk}/reorder/`, {
      method: 'POST',
      body: JSON.stringify(ids)
    }).then(res => res.json()).then(data => console.log(data))
  } else {
    itemList.classList.add('checklist-reordering')
    drake = dragula([itemList])

    checklistReorderingLink.classList.add('button')
    checklistReorderingLink.innerText = 'Save order'
    checklistReorderingLink.dataset.reordering = 'true'
  }
})
