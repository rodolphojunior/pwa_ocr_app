document.getElementById('upload-form').addEventListener('submit', async function(e) {
  e.preventDefault(); // Previne o comportamento padrão de recarregar a página

  const fileInput = document.getElementById('nota-fiscal');
  const formData = new FormData();
  formData.append('nota-fiscal', fileInput.files[0]);

  try {
    const response = await fetch('http://127.0.0.1:5000/upload', {  
      method: 'POST',
      body: formData
    });
    const result = await response.json();
    document.getElementById('status').textContent = result.message;
  } catch (error) {
    document.getElementById('status').textContent = "Erro ao enviar a nota fiscal.";
  }
});


