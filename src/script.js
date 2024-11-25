function mmToCm(value) {
  return value / 10;
}

function cmToMm(value) {
  return value * 10;
}

function cmToM(value) {
  return value / 100;
}

function mToCm(value) {
  return value * 100;
}

function mToKm(value) {
  return value / 1000;
}

function kmToM(value) {
  return value * 1000;
}

function ftToM(value) {
  return value * 0.3048;
}

function mToFt(value) {
  return value / 0.3048;
}

function inToFt(value) {
  return value / 12;
}

function ftToIn(value) {
  return value * 12;
}

function inToCm(value) {
  return value * 2.54;
}

function cmToIn(value) {
  return value / 2.54;
}

function showError(message) {
  const resultContainer = document.getElementById("result-container");
  const resultText = document.getElementById("result");

  resultText.innerText = message;
  resultContainer.classList.add("show", "error");
  resultContainer.style.backgroundColor = "#ffe6e6"; 
  resultContainer.style.color = "#cc0000"; 
}

function clearError() {
  const resultContainer = document.getElementById("result-container");
  resultContainer.classList.remove("error");
  resultContainer.style.backgroundColor = "#e9f7ff"; 
  resultContainer.style.color = "#007BFF";
}

function convert() {
  const valueInput = document.getElementById("value");
  const conversionType = document.getElementById("conversion-type").value;
  // Validacion
  const value = parseFloat(valueInput.value);
  if (valueInput.value.trim() === "") {
      showError("El campo 'Valor' no puede estar vacío.");
      return;
  }
  if (isNaN(value)) {
      showError("Por favor, ingrese un valor numérico válido.");
      return;
  }

  if (value > Number.MAX_VALUE || value > 1e100) {
      showError("El valor es demasiado grande para ser procesado.");
      return;
  }

  if (value === 0) {
      showError("La conversión de 0 no tiene sentido en unidades de medida de distancia.");
      return;
  }

  valueInput.disabled = true;

  // Conversiones
  let result;
  let unit;

  switch (conversionType) {
      case "mmToCm":
          result = mmToCm(value);
          unit = "cm";
          break;
      case "cmToMm":
          result = cmToMm(value);
          unit = "mm";
          break;
      case "cmToM":
          result = cmToM(value);
          unit = "m";
          break;
      case "mToCm":
          result = mToCm(value);
          unit = "cm";
          break;
      case "mToKm": 
          result = mToKm(value);
          unit = "km";
          break;
      case "kmToM":
          result = kmToM(value);
          unit = "m";
          break;
      case "ftToM":
          result = ftToM(value);
          unit = "m";
          break;
      case "mToFt":
          result = mToFt(value);
          unit = "ft";
          break;
      case "inToFt":
          result = inToFt(value);
          unit = "ft";
          break;
      case "ftToIn":
          result = ftToIn(value);
          unit = "in";
          break;
      case "inToCm":
          result = inToCm(value);
          unit = "cm";
          break;
      case "cmToIn":
          result = cmToIn(value);
          unit = "in";
          break;
      default:
          showError("Por favor, seleccione un tipo de conversión válido.");
          return;
  }

  clearError();
  const resultContainer = document.getElementById("result-container");
  const resultText = document.getElementById("result");

  resultText.innerText = `Resultado: ${result.toFixed(3)} ${unit}`;
  resultContainer.classList.add("show");
  
  resultContainer.classList.remove("animate");
  setTimeout(() => {
      resultContainer.classList.add("animate");
  }, 10);
}

function clearForm() {
  document.getElementById("value").value = "";
  document.getElementById("value").disabled = false; 
  document.getElementById("conversion-type").selectedIndex = 0; 
  clearError();
  const resultContainer = document.getElementById("result-container");
  resultContainer.classList.remove("show");
}