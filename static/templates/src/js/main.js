const burger = document.querySelector(".menu-icon");
const menu = document.querySelector(".menu");
const body = document.body;

if (burger && menu) {
	burger.addEventListener("click", () => {
		burger.classList.toggle("_active");
		menu.classList.toggle("_active");
		body.classList.toggle("_lock");
	});
}

// swiper

const swiper = new Swiper(".new-slider", {
	// spaceBetween: 20,
	slidesPerView: 4,
	pagination: {
		el: ".swiper-pagination",
	},

	breakpoints: {
		768: {
			slidesPerView: 4,
		},

		480: {
			slidesPerView: 3,
		},

		390: {
			slidesPerView: 2,
		},

		0: {
			slidesPerView: 1.5,
		},
	},
});

// Получаем ссылки на элементы
const filtersButton = document.querySelector(".filters-button");
const filtersDetails = document.querySelector(".filters-details");

// Обработчик события для filters-details
filtersDetails.addEventListener("click", () => {
	// Если filtersButton видим, устанавливаем opacity на 0
	if (filtersButton.style.opacity !== "0") {
		filtersButton.style.opacity = "0";
		filtersButton.style.transition = "opacity 0.5s ease"; // Плавная анимация
	} else {
		// Иначе, устанавливаем opacity на 1, чтобы показать filtersButton
		filtersButton.style.opacity = "1";
	}
});
