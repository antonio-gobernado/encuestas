const getCookie = (name) => {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
};
const csrftoken = getCookie("csrftoken");

// cuerpo

const pollContestada = () => {
  const leidosForms = [...document.getElementsByClassName("leer-forms")];
  // console.log(leidosForms);
  leidosForms.forEach((form) =>
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const clickedId = e.target.getAttribute("data-form-id");
      const clickedlink = document.getElementById(`enlace-${clickedId}`);

      $.ajax({
        type: "POST",
        url: "",
        data: {
          csrfmiddlewaretoken: csrftoken,
          pk: clickedId,
        },

        success: function (response) {
          console.log(response);
          clickedlink.classList.add("disabled");
        },

        error: function (error) {
          console.log(error);
        },
      });
    })
  );
};
