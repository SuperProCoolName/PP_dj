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


// ARTICLES SWIPER

const swiperArticles = new Swiper(".articles-slider", {
    spaceBetween: 20,
    slidesPerView: 3,
    pagination: {
        el: ".swiper-pagination",
        clickable: true, // Пользователь сможет кликать по точкам для переключения слайдов
    },
    breakpoints: {
        768: {
            slidesPerView: 3,
        },
        480: {
            slidesPerView: 2,
        },
        390: {
            slidesPerView: 1,
        },
        0: {
            slidesPerView: 1,
        },
    },
});

// Получаем ссылки на элементы
const filtersButton = document.querySelector(".filters-button");
const filtersDetails = document.querySelector(".filters-details");

// Устанавливаем начальные стили
filtersButton.style.visibility = "visible";
filtersButton.style.opacity = "1";
filtersButton.style.transition = "opacity 0.5s ease";

// Обработчик события для filters-details
filtersDetails.addEventListener("click", () => {
	if (filtersButton.style.visibility === "visible") {
		// Устанавливаем opacity на 0
		filtersButton.style.opacity = "0";

		// Задержка перед установкой display: none, чтобы дождаться завершения анимации
		setTimeout(() => {
			filtersButton.style.visibility = "hidden";
			filtersButton.style.display = "none";
		}, 500); // 500ms соответствует времени перехода в transition
	} else {
		// Убираем display: none и задаем visibility и opacity
		filtersButton.style.display = "block";

		// Делаем небольшую задержку перед началом анимации, чтобы браузер успел применить display: block
		setTimeout(() => {
			filtersButton.style.visibility = "visible";
			filtersButton.style.opacity = "1";
		}, 10); // 10ms для завершения изменения display
	}
});
