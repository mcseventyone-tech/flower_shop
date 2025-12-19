function order(bouquet) {
    const name = prompt("Введите ваше имя:");
    const phone = prompt("Введите ваш телефон:");

    if (!name || !phone) {
        alert("Имя и телефон обязательны!");
        return;
    }

    fetch('http://127.0.0.1:5001/order', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({name, phone, bouquet})
    });

    alert(`Спасибо! Ваш заказ на "${bouquet}" принят.`);
}
