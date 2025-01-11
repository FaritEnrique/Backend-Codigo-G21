import express from 'express';

const servidor = express();
servidor.use(express.json());
// servidor.use(express.urlencoded());
servidor.use(express.text());

servidor.get("/", (req, res) => {
    res.json({
        message: 'Bienvenido a mi Api'
    });
});

servidor.post("/crear-usuario", (req, res) => {
    console.log(req.body);
    res.json({
        message: 'Usuario creado exitosamentesss',
    })
})

servidor.listen(3000, () => {
    console.log("Servidor corriendo exitosamente");
});