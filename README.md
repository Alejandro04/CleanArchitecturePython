# Clean Architecture usando Python y Flask

He desarrollado un pequeño ejemplo que trabaja con una db en mysql (adapter) llamada shipping y una tabla llamada providers.

#### La tabla se puede crear con el siguiente comando:

```sql
CREATE TABLE providers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Las pruebas unitarias y e2e se pueden ejecutar con el siguiente comando:

```bash
    python3 -m pytest
```

# Estructura de carpetas en una aplicación utilizando Clean Architecture

Tiene como objetivo principal lograr una separación clara de responsabilidades y facilitar el mantenimiento y la evolución del código.

## Domain
La carpeta "domain" contiene las entidades y reglas de negocio fundamentales de la aplicación. Aquí se definen las clases y estructuras que representan los conceptos centrales del dominio de la aplicación. Estas entidades encapsulan la lógica y los comportamientos específicos de la aplicación.

El objetivo de la carpeta "domain" es ser independiente de cualquier tecnología o infraestructura externa. No debe tener dependencias de frameworks, bases de datos u otros componentes externos. Esto permite que el código del dominio sea portátil y reutilizable en diferentes contextos.

## Adapters
La carpeta "adapters" contiene los adaptadores o implementaciones concretas de las interfaces definidas en el dominio. Estos adaptadores son responsables de interactuar con los componentes externos, como bases de datos, servicios web o interfaces de usuario.

Los adaptadores se encargan de traducir las operaciones y los datos del dominio a un formato que sea compatible con las tecnologías o infraestructuras específicas. También proporcionan una capa de abstracción que permite desacoplar el dominio de las implementaciones concretas, lo que facilita el cambio o la actualización de los componentes externos sin afectar el código del dominio.

## Use Cases
La carpeta "use_cases" contiene las implementaciones de los casos de uso de la aplicación. Estos casos de uso definen las acciones o funcionalidades principales que la aplicación debe proporcionar a los usuarios. Cada caso de uso se implementa como una clase o función que encapsula la lógica necesaria para cumplir con ese caso de uso específico.

Los casos de uso se comunican con el dominio a través de las interfaces definidas en el dominio. Utilizan las entidades y las reglas de negocio del dominio para llevar a cabo las operaciones requeridas. Además, pueden utilizar los adaptadores para interactuar con los componentes externos necesarios para completar el caso de uso.

## Beneficios de la separación
La separación de responsabilidades en domain, adapters y use_cases trae varios beneficios:

### Legibilidad y mantenibilidad: 
La estructura clara y organizada facilita la comprensión y el mantenimiento del código. Cada componente tiene una responsabilidad específica y se puede modificar o reemplazar sin afectar a los demás.

### Reutilización y portabilidad: 
El código del dominio en la carpeta "domain" puede ser reutilizado en diferentes contextos o proyectos, ya que no tiene dependencias externas. Además, la separación de adaptadores permite cambiar o actualizar las tecnologías o infraestructuras sin afectar al código del dominio.

### Testabilidad: 
La separación de capas facilita la escritura de pruebas unitarias y de integración. Se pueden probar las reglas de negocio en el dominio de forma aislada, y los adaptadores y casos de uso se pueden probar por separado utilizando mocks o stubs.
