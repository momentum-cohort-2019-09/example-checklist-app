for (const link of document.querySelectorAll('.item-edit-link')) {
  link.addEventListener('click', event => {
    link.parentElement.querySelector('.checklist-item-body').style.display = 'none'
    link.parentElement.querySelector('.item-edit-form').style.display = 'inline-block'
  })
}
