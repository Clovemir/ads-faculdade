new Vue({
    el: '#app',
    data: {
        novaData: '',
        novoHorario: '',
        agendamentos: JSON.parse(localStorage.getItem('agendamentos')) || []
    },
    methods: {
        addAgendamento() {
            if (this.novaData && this.novoHorario) {
                const novoAgendamento = {
                    data: this.novaData,
                    horario: this.novoHorario
                };
                this.agendamentos.push(novoAgendamento);
                this.updateLocalStorage();
                this.novaData = '';
                this.novoHorario = '';
            }
        },
        editAgendamento(index) {
            const novaData = prompt("Editar data (aaaa-mm-dd):", this.agendamentos[index].data);
            const novoHorario = prompt("Editar horário (hh:mm):", this.agendamentos[index].horario);
            if (novaData && novoHorario) {
                this.agendamentos[index].data = novaData;
                this.agendamentos[index].horario = novoHorario;
                this.updateLocalStorage();
            }
        },
        deleteAgendamento(index) {
            this.agendamentos.splice(index, 1);
            this.updateLocalStorage();
        },
        updateLocalStorage() {
            localStorage.setItem('agendamentos', JSON.stringify(this.agendamentos));
        }
    }
});
