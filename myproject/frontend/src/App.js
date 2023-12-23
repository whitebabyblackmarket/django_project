import React, { useState } from 'react';

function App() {
  const [prompt, setPrompt] = useState('');
  const [negativePrompt, setNegativePrompt] = useState('');
  const [selectedImage, setSelectedImage] = useState(null);
  const [generatedImage, setGeneratedImage] = useState(null);

  const handleImageUpload = event => {
    setSelectedImage(URL.createObjectURL(event.target.files[0]));
  };

  const handleFormSubmit = async event => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('prompt', prompt);
    formData.append('negative_prompt', negativePrompt);
    formData.append('image', selectedImage);

    const response = await fetch('/predict/', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      console.error('Image generation failed:', response.statusText);
      return;
    }

    const data = await response.text();
    const parser = new DOMParser();
    const htmlDocument = parser.parseFromString(data, 'text/html');
    const imageUrl = htmlDocument.querySelector('img').src;
    setGeneratedImage(imageUrl);
  };

  return (
    <div>
      <h1>Welcome to the Stable Diffusion Integration!</h1>
      <form onSubmit={handleFormSubmit} encType="multipart/form-data">
        <label htmlFor="prompt">Prompt:</label><br />
        <input
          type="text"
          id="prompt"
          name="prompt"
          value={prompt}
          onChange={e => setPrompt(e.target.value)}
        /><br />
        <label htmlFor="negative_prompt">Negative Prompt:</label><br />
        <input
          type="text"
          id="negative_prompt"
          name="negative_prompt"
          value={negativePrompt}
          onChange={e => setNegativePrompt(e.target.value)}
        /><br />
        <label htmlFor="image">Upload Image:</label><br />
        <input
          type="file"
          id="image"
          name="image"
          accept="image/*"
          onChange={handleImageUpload}
        /><br />
        <input type="submit" value="Generate" />
      </form>
      {generatedImage && (
        <>
          <h2>Generated Image:</h2>
          <img src={generatedImage} alt="Generated" />
        </>
      )}
    </div>
  );
}

export default App;