const API_URL = "https://snps-hospital.onrender.com";

fetch(`${API_URL}/api/endpoint/`)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));

// Counter Animation
const counters = document.querySelectorAll('.count');
const speed = 200; // Adjust this speed for faster/slower animation

counters.forEach(counter => {
  const updateCount = () => {
    const target = +counter.getAttribute('data-target');
    const count = +counter.innerText;

    // Calculate increment
    const increment = target / speed;

    // Check if the current count is less than the target
    if (count < target) {
      counter.innerText = Math.ceil(count + increment);
      setTimeout(updateCount, 10); // Update every 10 milliseconds
    } else {
      counter.innerText = target; // Set final value once reached
    }
  };

  updateCount();
});
