// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyBwJkIalkDU1C_zXcxJAB63pwIKjGSjMOk",
    authDomain: "viagem-965ad.firebaseapp.com",
    projectId: "viagem-965ad",
    storageBucket: "viagem-965ad.appspot.com",
    messagingSenderId: "938784231164",
    appId: "1:938784231164:web:6aee8263995bb0ce4ad179",
    measurementId: "G-J89L2QQMDS"
  };
// Initialize Firebase
const app = firebase.initializeApp(firebaseConfig);
const db = firebase.firestore(app);

// Captura do formulário e envio para o Firestore
document.getElementById('viajando-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Captura os dados do formulário
    const nome = document.getElementById('nome').value;
    const curso = document.getElementById('curso').value;
    const tipoViagem = document.querySelector('input[name="tipo_viagem"]:checked').value;

    // Envia os dados para o Firestore
    db.collection("estudantes").add({
        nome: nome,
        curso: curso,
        tipoViagem: tipoViagem
    })
    .then(() => {
        document.getElementById('resultado').textContent = "Dados enviados com sucesso!";
    })
    .catch((error) => {
        console.error("Erro ao enviar os dados: ", error);
        document.getElementById('resultado').textContent = "Erro ao enviar os dados.";
    });

    // Limpar formulário após envio
    document.getElementById('viajando-form').reset();
});
