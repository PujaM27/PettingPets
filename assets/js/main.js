// Alert when browsing pets
document.querySelector('a[href="adopt.html"]').addEventListener('click', function () {
    alert('Ready to find your new furry friend!');
});

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth' });
        } else {
            console.error('Target not found for smooth scroll.');
        }
    });
});

// Quiz Functionality
document.addEventListener("DOMContentLoaded", function () {
    const quizQuestions = [
        {
            question: "What is your preferred pet size?",
            options: ["Small", "Medium", "Large"],
            key: "size"
        },
        {
            question: "How much time can you dedicate to grooming?",
            options: ["Minimal", "Moderate", "High"],
            key: "grooming"
        },
        {
            question: "What kind of energy level do you prefer?",
            options: ["Low", "Moderate", "High"],
            key: "energy"
        }
    ];

    let quizIndex = 0;
    const userAnswers = {};

    // Start Quiz
    document.getElementById("quiz-button").addEventListener("click", function () {
        this.style.display = "none";
        showQuestion();
    });

    function showQuestion() {
        const quizSection = document.getElementById("pet-quiz");

        if (quizIndex < quizQuestions.length) {
            const currentQuestion = quizQuestions[quizIndex];

            quizSection.innerHTML = `
                <h3>${currentQuestion.question}</h3>
                ${currentQuestion.options
                    .map(option => `<button class="quiz-option" data-answer="${option}">${option}</button>`)
                    .join("")}
            `;

            // Event delegation for quiz options
            quizSection.addEventListener('click', function (e) {
                if (e.target && e.target.matches('.quiz-option')) {
                    const answer = e.target.getAttribute("data-answer");
                    userAnswers[currentQuestion.key] = answer;
                    quizIndex++;
                    if (quizIndex < quizQuestions.length) {
                        showQuestion();
                    } else {
                        showResult();
                    }
                }
            });
        }
    }

    function showResult() {
        const quizSection = document.getElementById("pet-quiz");
        const petAIRecommendation = determineIdealPet(userAnswers);

        quizSection.innerHTML = `
            <h3>Your ideal pet is:</h3>
            <p>${petAIRecommendation}</p>
            <button id="restart-quiz">Take Quiz Again</button>
        `;

        document.getElementById("restart-quiz").addEventListener("click", () => {
            quizIndex = 0;
            Object.keys(userAnswers).forEach(key => delete userAnswers[key]);
            document.getElementById("quiz-button").style.display = "inline-block";
        });
    }

    function determineIdealPet(answers) {
        if (answers.size === "Small" && answers.grooming === "Minimal" && answers.energy === "Low") {
            return "A cuddly rabbit 🐇";
        } else if (answers.size === "Large" && answers.grooming === "High" && answers.energy === "High") {
            return "An energetic Golden Retriever 🐕";
        } else {
            return "A versatile cat 🐈";
        }
    }
});
