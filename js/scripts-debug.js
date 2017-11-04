// Setup
document.addEventListener("DOMContentLoaded", function() {
	// Populate email
	var span = document.getElementById("email-container");
	span.textContent = "hello" + "@" + "laxmidas.com";
	// Say hello!
	console.log("Well hello! I see you're poking around.");
	console.log("I'm always looking to work with curious, self-motivated people.");
	console.log("Want to start a conversation? Shoot me an email!");
});

window.sr = ScrollReveal();
sr.reveal('.body-section', { duration: 600, scale: 1, delay: 80});

particlesJS.load('particles-js', 'particles.json', function() {
});