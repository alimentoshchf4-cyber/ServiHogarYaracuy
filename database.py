import streamlit as st

def inicializar_base_datos():
    """Inicializa las tablas y listas en la sesión de Streamlit para el MVP."""
    if 'tecnicos' not in st.session_state:
        st.session_state.tecnicos = [
            {
                "nombre": "Carlos Mendoza",
                "oficio": "Técnico en Refrigeración y Aire Acondicionado",
                "cedula": "V-18.456.789",
                "telefono": "04120582064",
                "direccion": "Avenida Cedeño, San Felipe, Yaracuy",
                "experiencia": "6 años de experiencia instalando y reparando aires split.",
                "foto": "https://api.iconify.design/fluent-emoji-flat:man-mechanic.svg"
            }
        ]

    if 'solicitudes' not in st.session_state:
        st.session_state.solicitudes = [
            {
                "id": 1,
                "cliente": "Luisa Martínez",
                "telefono": "04129998877",
                "municipio": "San Felipe",
                "servicio": "Mantenimiento preventivo de aire acondicionado",
                "estado": "Abierta"
            }
        ]

    if 'catalogo_exito' not in st.session_state:
        st.session_state.catalogo_exito = [
            {
                "cliente": "Pedro Alastre",
                "municipio": "Independencia",
                "comentario": "Excelente servicio de electricidad. El técnico llegó puntual y solucionó el cortocircuito rápido.",
                "estrellas": "⭐⭐⭐⭐⭐"
            }
        ]
