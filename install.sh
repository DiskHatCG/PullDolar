#!/bin/bash
# DiskHat Computing Group 


if [[ ! -f "./main.py" ]]; then
    echo "No se encontro el archivo inicial (main.py)."
    exit 1
fi
cp "./main.py" "/usr/local/bin/pulldolar.py"
echo "#!/bin/bash" > "/usr/local/bin/pulldolar"
echo "python3 /usr/local/bin/pulldolar.py \"\$@\"" >> "/usr/local/bin/pulldolar"
chmod +x "/usr/local/bin/pulldolar"
echo "✅ | Instalación realizada. Prueba utilizando el comando "pulldolar"."