import express from "express";
import Prisma from "@prisma/client";

const conexion = new Prisma.PrismaClient();
const servidor = express();

servidor.use(express.json());

servidor.post("/registro", async (req, res) => {
    try {
        const data = req.body;
        const resultado = await conexion.usuario.create({
            data, // : { nombre: data.nombre, email: data.email, nickName: data.nickName},
        })
        //ACA PONES TU MENSAJE
        return res.json({
            message: "Usuario creado exitosamente",
            content: resultado,
        });
    } catch (error) {
        if (error instanceof Prisma.Prisma.PrismaClientValidationError) {
            return res.json({
                message: "Error al hacer la petición a la bd",
            })
        }
        return res.json({
            message: "Error al crear el usuario",
        })
    }
});

servidor
    .route("/notas")
    .post(async (req, res) => {
        const data = req.body;
        try {
            const notaCreada = await conexion.nota.create({data});
            return res.json({
                message: "Nota creada existosamente",
                content: notaCreada
            })
        } catch (error) {
            return res.json({
                message: "Error al crear nota"
            });
        }
    })
    
    .get(async (req, res) => {
        const notas = await conexion.nota.findMany();
        return res.json({
            content: notas,
        })
    });

servidor.listen(process.env.PORT, () => {
    console.log(`Servidor corriendo exitosamente en el puerto ${process.env.PORT}`
    );
});
