$("#home").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Главная"));
});
$("#services").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Услуги"));
});
$("#contacts").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Контакты"));
});
$("#requests").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Мои заявки"));
});
$("#account_logout").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Выйти"));
});
$("#sign-up-link").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Регистрация"));
});
$("#log-in-link").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Вход"));
});
$("#button-switch").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Обычная версия"));
});
$("#heading-cards").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Услуги"));
});
$("#card-one").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(
    new SpeechSynthesisUtterance(
      "Уборка квартир. Обученные клинеры. Сертифицированные средства. Гарантия качества. С нами будет чисто. Срочные выезды. Расчет стоимости на сайте. Новым клиентам скидка 10%"
    )
  );
});
$("#card-two").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(
    new SpeechSynthesisUtterance(
      "Чистка ковров. Качественная чистка ковров и паласов требует немало времени, усилий и знаний. Доверьте этот трудоемкий процесс профессионалам с опытом и наслаждайтесь результатом."
    )
  );
});
$("#contact-footer").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Контакты"));
});
$("#conditions").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Условия пользования"));
});
$("#download").on("click", function() {
  let synth = window.speechSynthesis;
  synth.speak(new SpeechSynthesisUtterance("Скачайте приложение"));
});
