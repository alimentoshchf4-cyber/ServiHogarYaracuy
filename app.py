import streamlit as st
import urllib.parse
from database import inicializar_base_datos

# Configuración inicial de la página
st.set_page_config(
    page_title="YaracuyServicios | Plataforma Digital",
    page_icon="🛠️",
    layout="wide"
)

# Inicializar datos
inicializar_base_datos()

# Número de WhatsApp base de soporte/coordinación
WHATSAPP_CONTACTO = "584120582064"

def generar_link_whatsapp(mensaje):
    """Genera un enlace directo para abrir WhatsApp con un mensaje preconfigurado."""
    mensaje_codificado = urllib.parse.quote(mensaje)
    return f"https://wa.me/{WHATSAPP_CONTACTO}?text={mensaje_codificado}"

# Barra Lateral de Navegación
st.sidebar.title("🛠️ YaracuyServicios")
st.sidebar.markdown("**Estado Yaracuy - Venezuela**")
menu = st.sidebar.selectbox(
    "Seleccione un Módulo",
    [
        "🏠 Inicio y Catálogo de Éxito", 
        "👤 Registro de Técnicos (Postulación)", 
        "📋 Solicitar Servicio & Elegir Experto", 
        "💳 Pasarela de Pago (Pago Móvil, Zinli, Wally)"
    ]
)

# ==========================================
# MÓDULO 1: INICIO Y CATÁLOGO DE TRABAJOS
# ==========================================
if menu == "🏠 Inicio y Catálogo de Éxito":
    st.title("🌟 YaracuyServicios: Mercado de Profesionales del Hogar")
    st.markdown("Conectamos hogares en San Felipe, Independencia, Cocorote y todo Yaracuy con técnicos calificados de confianza.")
    
    st.image("https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
    
    st.markdown("---")
    st.header("🏆 Trabajos Realizados y Clientes Satisfechos")
    st.markdown("Conoce las opiniones reales de hogares que ya confiaron en nuestra plataforma.")

    for item in st.session_state.catalogo_exito:
        with st.container():
            st.info(f"""
            **Cliente:** {item['cliente']} ({item['municipio']})  
            **Opinión:** "{item['comentario']}"  
            **Calificación:** {item['estrellas']}
            """)
            
    st.markdown("---")
    st.success("💬 ¿Necesitas atención inmediata? Contáctanos directamente por WhatsApp haciendo clic abajo:")
    msg_w = "Hola, necesito asistencia urgente con un servicio para el hogar en Yaracuy."
    st.markdown(f'<a href="{generar_link_whatsapp(msg_w)}" target="_blank"><button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">📱 Escribir al WhatsApp (0412-0582064)</button></a>', unsafe_allow_html=True)

# ==========================================
# MÓDULO 2: REGISTRO DE TÉCNICOS / PROFESIONALES
# ==========================================
elif menu == "👤 Registro de Técnicos (Postulación)":
    st.title("👷 Postulación de Profesionales y Técnicos")
    st.markdown("Llena el siguiente formulario tipo perfil profesional para unirte a nuestra red en Yaracuy.")
    
    with st.form("form_registro_tecnico"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre y Apellido")
            cedula = st.text_input("Cédula de Identidad (Ej. V-20123456)")
            telefono = st.text_input("Número de Teléfono / WhatsApp", value="0412")
        with col2:
            oficio = st.selectbox("Especialidad principal", ["Electricista", "Plomero", "Técnico de Aires Acondicionados", "Albañil / Construcción", "Técnico en Línea Blanca"])
            direccion = st.text_input("Dirección / Municipio de Residencia (Ej. San Felipe)")
            
        experiencia = st.text_area("Resumen de Experiencia Profesional y Trayectoria")
        
        btn_postular = st.form_submit_button("Enviar Postulación")
        
        if btn_postular:
            if nombre and cedula and telefono:
                nuevo_tecnico = {
                    "nombre": nombre,
                    "oficio": oficio,
                    "cedula": cedula,
                    "telefono": telefono,
                    "direccion": direccion,
                    "experiencia": experiencia,
                    "foto": "https://api.iconify.design/fluent-emoji-flat:technologist.svg"
                }
                st.session_state.tecnicos.append(nuevo_tecnico)
                st.success("¡Postulación enviada con éxito! Tu perfil ya está disponible para que los clientes te elijan.")
            else:
                st.warning("Por favor completa los campos obligatorios (Nombre, Cédula y Teléfono).")

# ==========================================
# MÓDULO 3: SOLICITUD Y ELECCIÓN DE TÉCNICOS
# ==========================================
elif menu == "📋 Solicitar Servicio & Elegir Experto":
    st.title("🛒 Mercado de Solicitudes y Selección de Expertos")
    st.markdown("Publica tu requerimiento o selecciona directamente al profesional calificado que prefieras según su experiencia y cédula verificada.")
    
    tab1, tab2 = st.tabs(["📝 Publicar Necesidad", "🔍 Directorio de Técnicos Verificados"])
    
    with tab1:
        st.subheader("Solicita un Servicio Doméstico")
        with st.form("form_solicitud_cliente"):
            c_nombre = st.text_input("Tu Nombre")
            c_telefono = st.text_input("Tu Teléfono de Contacto")
            c_muni = st.selectbox("Municipio", ["San Felipe", "Independencia", "Cocorote", "Yaritagua", "Nirgua"])
            c_desc = st.text_area("Describe detalladamente el servicio que necesitas (Ej. Fuga de agua en tubería principal de baño)")
            
            btn_enviar_sol = st.form_submit_button("Publicar Solicitud")
            if btn_enviar_sol:
                if c_nombre and c_telefono and c_desc:
                    nueva_sol = {
                        "id": len(st.session_state.solicitudes) + 1,
                        "cliente": c_nombre,
                        "telefono": c_telefono,
                        "municipio": c_muni,
                        "servicio": c_desc,
                        "estado": "Abierta"
                    }
                    st.session_state.solicitudes.append(nueva_sol)
                    st.success("¡Solicitud publicada en el mercado con éxito!")
                else:
                    st.error("Rellena todos los campos para continuar.")
                    
    with tab2:
        st.subheader("Directorio de Profesionales (Puja y Experiencia)")
        st.markdown("Elige al especialista que mejor se adapte a tus necesidades y confírmalo directamente por WhatsApp al **04120582064**.")
        
        for tec in st.session_state.tecnicos:
            with st.container():
                col_img, col_info = st.columns([1, 4])
                with col_img:
                    st.image(tec["foto"], width=90)
                with col_info:
                    st.markdown(f"### {tec['nombre']} - *{tec['oficio']}*")
                    st.write(f"🆔 **Cédula:** {tec['cedula']} | 📍 **Ubicación:** {tec['direccion']}")
                    st.write(f"📞 **Contacto:** {tec['telefono']}")
                    st.write(f"💼 **Experiencia:** {tec['experiencia']}")
                    
                    # Botón dinámico para confirmar contratación vía WhatsApp
                    texto_ws = f"Hola, deseo contratar al técnico {tec['nombre']} ({tec['oficio']}) de la plataforma YaracuyServicios. Mi número es..."
                    link_ws = generar_link_whatsapp(texto_ws)
                    st.markdown(f'<a href="{link_ws}" target="_blank"><button style="background-color:#007bff; color:white; padding:8px 16px; border:none; border-radius:4px; font-weight:bold; cursor:pointer;">👉 Contratar / Consultar por WhatsApp</button></a>', unsafe_allow_html=True)
                st.markdown("---")

# ==========================================
# MÓDULO 4: PASARELA DE PAGO (PAGO MÓVIL, ZINLI, WALLY)
# ==========================================
elif menu == "💳 Pasarela de Pago (Pago Móvil, Zinli, Wally)":
    st.title("💳 Pasarela de Pagos Digitales")
    st.markdown("Selecciona tu método de pago preferido para cancelar el servicio o la tarifa de conexión en YaracuyServicios.")
    
    metodo_pago = st.selectbox("Elige método de pago", ["Pago Móvil (Bancos Nacionales)", "Zinli", "Wally Tech"])
    
    col_p1, col_p2 = st.columns(2)
    
    with col_p1:
        st.info(f"Has seleccionado: **{metodo_pago}**")
        monto_ref = st.number_input("Monto a cancelar (USD / Ref)", min_value=5.0, value=15.0, step=5.0)
        concepto = st.text_input("Concepto o Código de Solicitud", value="Servicio técnico hogar")
        
        if metodo_pago == "Pago Móvil (Bancos Nacionales)":
            st.markdown("""
            **Datos para Pago Móvil:**
            * **Banco:** Mercantil / Banesco (0105 / 0134)
            * **Teléfono:** 0412-0582064
            * **Cédula:** V-18.456.789
            """)
        elif metodo_pago == "Zinli":
            st.markdown("""
            **Datos para Zinli:**
            * **Correo electrónico:** pagos@yaracuyservicios.com
            * **Beneficiario:** YaracuyServicios C.A.
            """)
        else:
            st.markdown("""
            **Datos para Wally:**
            * **Wally Tag / Cuenta:** @YaracuyServicios
            """)
            
    with col_p2:
        st.subheader("Validación de Transacción")
        num_referencia = st.text_input("Número de Referencia del Pago / Captura ID")
        banco_emisor = st.text_input("Banco emisor o correo de origen")
        
        if st.button("Reportar y Validar Pago"):
            if num_referencia:
                st.success("¡Pago reportado con éxito! El equipo verificará la transacción y activará la garantía de servicio.")
                
                # Mensaje automático vía WhatsApp para notificar el pago al operador
                msg_pago = f"Hola, reporto un pago por {metodo_pago} por un monto de ${monto_ref}. Referencia: {num_referencia}. Concepto: {concepto}"
                st.markdown(f'<a href="{generar_link_whatsapp(msg_pago)}" target="_blank"><button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">✅ Notificar comprobante por WhatsApp</button></a>', unsafe_allow_html=True)
            else:
                st.warning("Por favor ingresa el número de referencia del pago.")
