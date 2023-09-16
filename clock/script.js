var minInput = document.getElementById("min");
        var secInput = document.getElementById("sec");
        var minutes = document.getElementById("minutes_tick");
        var seconds = document.getElementById("seconds_tick");
        var timer;
        var totalTime = 0;

        document.getElementById("set").addEventListener("click", function() {
            var inputMinutes = parseInt(minInput.value) || 0;
            var inputSeconds = parseInt(secInput.value) || 0;
            totalTime = inputMinutes * 60 + inputSeconds;
            startTimer(totalTime);
        });

        document.getElementById("reset").addEventListener("click", function() {
            clearInterval(timer);
            minutes.innerHTML = "00";
            seconds.innerHTML = "00";
        });

        function startTimer(time) {
            clearInterval(timer);

            timer = setInterval(function() {
                var minutesLeft = Math.floor(time / 60);
                var secondsLeft = time % 60;

                minutes.innerHTML = String(minutesLeft).padStart(2, "0");
                seconds.innerHTML = String(secondsLeft).padStart(2, "0");

                if (time <= 0) {
                    clearInterval(timer);
                    alert("Time is over!");
                }

                time--;
            }, 1000);
        }