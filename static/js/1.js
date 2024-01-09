const contenedores = document.querySelectorAll('.item');
contenedores.forEach((contenedor) => {
  const imagen = contenedor.querySelector('#imagen');
  const containerRect = contenedor.getBoundingClientRect();
  const initialTransform = imagen.style.transform;
  contenedor.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX - containerRect.left;
    const mouseY = event.clientY - containerRect.top + window.scrollY; // Ajuste para tener en cuenta el desplazamiento vertical
    const scaleX = 1.1; // Ajusta este valor para controlar el nivel de agrandamiento horizontal
    const scaleY = 1.1; // Ajusta este valor para controlar el nivel de agrandamiento vertical
    const translateX = ((mouseX - containerRect.width / 2) / containerRect.width) * 50;
    const translateY = ((mouseY - containerRect.height / 2) / containerRect.height) * 50;
    const verticalOffset = (mouseY - containerRect.height / 2) * 0.1; // Ajuste el factor de desplazamiento vertical
    const horizontalOffset = (mouseX - containerRect.width / 2) * 0.3; // Ajuste el factor de desplazamiento horizontal
    imagen.style.transform = `translate(${translateX - horizontalOffset}px, ${translateY - verticalOffset}px) scale(${scaleX}, ${scaleY})`;
  });
  contenedor.addEventListener('mouseleave', () => {
    imagen.style.transform = initialTransform;
  });
});