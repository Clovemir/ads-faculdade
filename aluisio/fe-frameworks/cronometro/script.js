new Vue({
    el: '#app',
    data: {
      seconds: 0,
      minutes: 0,
      hours: 0,
      interval: null,
      isRunning: false
    },
    computed: {
      // Computed property para formatar o tempo de exibição
      formattedTime() {
        // Formata horas, minutos e segundos com dois dígitos
        let h = this.hours < 10 ? '0' + this.hours : this.hours;
        let m = this.minutes < 10 ? '0' + this.minutes : this.minutes;
        let s = this.seconds < 10 ? '0' + this.seconds : this.seconds;
        return `${h}:${m}:${s}`;
      }
    },
    methods: {
      // Método para iniciar o cronômetro
      startTimer() {
        if (!this.isRunning) {
          this.isRunning = true;
          this.interval = setInterval(() => {
            this.incrementTime();
          }, 1000);
        }
      },
      // Método para parar o cronômetro
      stopTimer() {
        clearInterval(this.interval);
        this.isRunning = false;
      },
      // Método para zerar o cronômetro
      resetTimer() {
        this.stopTimer();
        this.seconds = 0;
        this.minutes = 0;
        this.hours = 0;
      },
      // Método para incrementar o tempo
      incrementTime() {
        this.seconds++;
        if (this.seconds === 60) {
          this.seconds = 0;
          this.minutes++;
        }
        if (this.minutes === 60) {
          this.minutes = 0;
          this.hours++;
        }
      }
    }
  });  
  