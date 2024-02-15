const calculateBtn = document.getElementById('calculate-btn');
const timeInput = document.getElementById('time-input');
const timesContainer = document.getElementById('times-container');

calculateBtn.addEventListener('click', () => {
  const inputTime = timeInput.value;
  if (inputTime !== '') {
    fetch(`/sleepytime?input_time=${inputTime}`)
      .then(response => response.json())
      .then(times => {
        timesContainer.innerHTML = '';
        times.forEach(time => {
          const timeBox = document.createElement('div');
          timeBox.classList.add('time-box');
          timeBox.innerHTML = `
            <p class="wake-up-time">${time[0]}</p>
            <p class="cycle-info">${time[1]}</p>
            <p class="cycle-hours">${time[2]} hours of sleep</p>
          `;
          timesContainer.appendChild(timeBox);
        });
      })
      .catch(error => console.error(error));
  }
});
