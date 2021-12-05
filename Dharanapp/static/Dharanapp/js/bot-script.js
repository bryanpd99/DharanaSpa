var botui = new BotUI("reserva-bot");

botui.message
  .add({
    delay: 500,
    loading: true,
    content: "Hola ! Gracias por preferir Dharana SPA",
  })
  .then(function () {
    return botui.message.add({
      delay: 500,
      loading: true,
      content: "Dime , cómo puedo ayudarte?",
    });
  })
  .then(function () {
    return botui.action.button({
      action: [
        {
          text: "Que servicio dispone?",
          value: "hours",
        },
        {
          text: "Quisiera una cita?",
          value: "do",
        },
      ],
    });
  })
  .then(function (res) {
    var message;

    if (res.value === "hours") {
      message = "That’s a good one! This is a website, it’s always open.";
    } else if (res.value === "do") {
      message =
        "I’m a product-focused Scrum master<br><br>I also have a keen interest in chatbots and web analytics";
    }

    return botui.message.add({
      type: "html",
      delay: 1000,
      loading: true,
      content: message,
    });
  })
  .then(function (index) {
    return botui.action.button({
      action: [
        {
          text: "Cool!",
          value: "cool",
        },
      ],
    });
  })
  .then(function (index) {
    return botui.action.text({
        action: {
            placeholder: 'INGRESA TU NOMBRE Y APELLIDO'
          }
    }).then(function(res){

        console.log(res.value)
    });


  });
