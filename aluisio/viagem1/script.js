// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyAlQA523ozDdeibuaytsbOqIVmWHI95Bcw",
    authDomain: "viajando-e35cd.firebaseapp.com",
    databaseURL: "https://viajando-e35cd-default-rtdb.firebaseio.com",
    projectId: "viajando-e35cd",
    storageBucket: "viajando-e35cd.appspot.com",
    messagingSenderId: "467759795258",
    appId: "1:467759795258:web:4b3a7bb6718a1ae3ae7903",
    measurementId: "G-V8KMHMM9NV"
  };
// Initialize Firebase
const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);

// Captura do formulário e envio para o Firestore
document.getElementById('viagem-form').addEventListener('submit', function(event) {
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
    document.getElementById('viagem-form').reset();
});
