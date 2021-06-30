// document.addEventListener('DOMContentLoaded', function(){
// });

const changeBtn = document.querySelectorAll(".changeBtn"),
  deleteBtn = document.querySelectorAll(".deleteBtn");

changeBtn.forEach(item => {
  item.addEventListener("click", () => {
    const parent = item.parentNode.parentNode,
      orderId = parent.id,
      clientName = parent.querySelector(".clientName"),
      clientPhone = parent.querySelector(".clientPhone"),
      clientComment = parent.querySelector(".clientComment"),
      saveBtn = parent.querySelector(".saveBtn"),
      deleteBtn = parent.querySelector(".deleteBtn");
    clientName.disabled = false;
    clientPhone.disabled = false;
    clientComment.disabled = false;
    item.classList.add("d-none");
    saveBtn.classList.remove("d-none");

    saveBtn.addEventListener("click", async () => {
      const data = {
        client_name: clientName.value,
        client_phone: clientPhone.value,
        client_comment: clientComment.value
      };

      try {
        await fetch(`/api/v1/orders/${orderId}`, {
          method: "PUT",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify(data)
        });
        clientName.disabled = true;
        clientPhone.disabled = true;
        clientComment.disabled = true;
        item.classList.remove("d-none");
        saveBtn.classList.add("d-none");
      } catch (e) {
        throw new Error(e);
      }
    });
  });
});

deleteBtn.forEach(item => {
  item.addEventListener("click", async () => {
    const orderId = item.parentNode.parentNode.id;

    try {
      await fetch(`/api/v1/orders/${orderId}`, {
        method: "DELETE"
      });
      document.location.reload();
    } catch (e) {
      throw new Error(e);
    }
  });
});
