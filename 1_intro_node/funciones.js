const sumar = (numero1, numero2) => {
    const resultado = numero1 + numero2;
    return resultado;
};

function restar(numero1, numero2) {
    const resultado = numero1 - numero2;
    return resultado;
};

const multiplicar = (numero1, numero2) => (numero1 * numero2);

module.exports = {
    sumar: sumar,
    restar,
    multiplicar,
};
