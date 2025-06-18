const fs = require('fs');
const csv = require('csv-parser');
const neo4j = require('neo4j-driver');

const uri = "neo4j://localhost:7687";
const user = "neo4j";
const password = "neo4j_contraseña";

const driver = neo4j.driver(uri, neo4j.auth.basic(user, password));
const session = driver.session();

async function cargarDatos() {
  const registros = [];

  fs.createReadStream('../archivo.csv')
    .pipe(csv())
    .on('data', (data) => registros.push(data))
    .on('end', async () => {
      try {
        for (const d of registros) {
          await session.run(`
            MERGE (a:Aspirante {correlativo: $correlativo})
            SET a.sexo = $sexo,
                a.anio_nacimiento = toInteger($anio_nacimiento),
                a.fecha_asignacion = date($fecha_asignacion),
                a.anio_ingreso = toInteger($anio_ingreso),
                a.numero_de_fecha = toInteger($numero_de_fecha),
                a.aprobacion = $aprobacion = 'true'

            MERGE (c:Carrera {nombre: $carrera})
            MERGE (m:Materia {nombre: $materia})
            MERGE (i:Institucion {
              tipo: $tipo_institucion,
              municipio: $municipio,
              departamento: $departamento
            })

            MERGE (a)-[:BUSCA_CARRERA]->(c)
            MERGE (a)-[:REALIZA]->(m)
            MERGE (a)-[:ESTUDIA_EN]->(i)
            MERGE (i)-[:OFRECE]->(c)
          `, {
            correlativo: d.correlativo_aspirante,
            sexo: d.sexo,
            anio_nacimiento: d.anio_nacimiento,
            fecha_asignacion: d.fecha_asignacion,
            anio_ingreso: d.anio_de_ingreso,
            numero_de_fecha: d.numero_de_fecha_de_evaluaci,
            aprobacion: d.aprobacion,
            carrera: d.carrera_objetivo,
            materia: d.materia,
            tipo_institucion: d.tipo_institucion_educativa,
            municipio: d.municipio_institucion_,
            departamento: d.departamento_institucion_ed
          });
        }
        console.log('Datos cargados correctamente');
      } catch (err) {
        console.error('Error al cargar datos:', err);
      } finally {
        await session.close();
        await driver.close();
      }
    });
}

cargarDatos();
