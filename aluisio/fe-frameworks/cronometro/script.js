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
      // Computed é uma propriedade usada para formatar o tempo de exibição
      formattedTime() {
        // Formata horas, minutos e segundos com dois dígitos: 00:00:00
        let h = this.hours < 10 ? '0' + this.hours : this.hours;
        let m = this.minutes < 10 ? '0' + this.minutes : this.minutes;
        let s = this.seconds < 10 ? '0' + this.seconds : this.seconds;
        return `${h}:${m}:${s}`;
      }
    },
    methods: {
      // Método para iniciar o cronômetro
      startTimer() {
        if (!this.isRunning) { //inicia o cronometro apenas se ele ja nao estiver rodando
          this.isRunning = true; //ele define isRunning como true para controlar o estado
          this.interval = setInterval(() => { 
            this.incrementTime(); //usando o setInterval para incrementar o tempo a cada segundo
          }, 1000); 
        }
      },
      // Método para parar o cronômetro
      stopTimer() {
        clearInterval(this.interval); //para o cronometro usando o setInterval
        this.isRunning = false; //define isRunning como false
      },
      // Método para zerar o cronômetro
      resetTimer() { //para o cronometro e muda o estado do contador para zero
        this.stopTimer();
        this.seconds = 0;
        this.minutes = 0;
        this.hours = 0;
      },
      // Método para incrementar o tempo
      incrementTime() { //é chamado a cada segundo quando o cronometro esta rodando 
        this.seconds++;
        if (this.seconds === 60) {
          this.seconds = 0;
          this.minutes++;
        } //incrementando os segundos e ajustando caso necessário
        if (this.minutes === 60) {
          this.minutes = 0;
          this.hours++;
        }
      }
    }
  });
  
