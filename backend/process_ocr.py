from PIL import Image
from transformers import AutoModelForCausalLM, AutoProcessor

class Phi3VisionModel:
    
    def __init__(self, model_id="microsoft/Phi-3-vision-128k-instruct", device="cuda"):
        """
        Inicializa o modelo Phi-3-Vision-128K-Instruct com o ID do modelo e o dispositivo (GPU ou CPU).
        """
        self.model_id = model_id
        self.device = device
        self.model = self.load_model()
        self.processor = self.load_processor()

    def load_model(self):
        """
        Carrega o modelo pré-treinado com capacidades de causal language modeling.
        """
        print("Carregando o modelo...")
        return AutoModelForCausalLM.from_pretrained(
            self.model_id,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True,
            _attn_implementation='flash_attention_2'
        ).to(self.device)

    def load_processor(self):
        """
        Carrega o processador associado ao modelo para lidar com entradas de texto e imagens.
        """
        print("Carregando o processador...")
        return AutoProcessor.from_pretrained(self.model_id, trust_remote_code=True)

    def predict(self, image_path, prompt):
        """
        Realiza a predição utilizando uma imagem local e um prompt textual.
        """
        # Carrega a imagem local
        image = Image.open(image_path)

        # Formata o prompt de entrada para o modelo
        prompt_template = f"<|user|>\n<|image_1|>\n{prompt}<|end|>\n<|assistant|>\n"

        # Processa as entradas (imagem e texto)
        inputs = self.processor(prompt_template, [image], return_tensors="pt").to(self.device)

        # Definição de parâmetros de geração
        generation_args = {
            "max_new_tokens": 500,
            "temperature": 0.7,
            "do_sample": False
        }

        print("Gerando resposta...")
        output_ids = self.model.generate(**inputs, **generation_args)
        output_ids = output_ids[:, inputs['input_ids'].shape[1]:]  # Ignora o prompt na resposta gerada

        # Decodifica a saída gerada pelo modelo
        response = self.processor.batch_decode(output_ids, skip_special_tokens=True)[0]
        return response
