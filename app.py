import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse

# Configuración inicial de la página
st.set_page_config(
    page_title="YaracuyServicios | Plataforma Digital Segura",
    page_icon="🛠️",
    layout="wide"
)

# Inicialización de Estados Globales
if 'tecnicos' not in st.session_state:
    st.session_state.tecnicos = [
        {
            "nombre": "Carlos Mendoza",
            "oficio": "Técnico en Refrigeración y Aire Acondicionado",
            "cedula": "V-18.456.789",
            "telefono": "04120582064",
            "direccion": "Avenida Cedeño, San Felipe, Yaracuy",
            "experiencia": "6 años de experiencia instalando y reparando aires split.",
            "estado": "Disponible",
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

# Datos Únicos de Pago del Administrador
ADMIN_PAGO_MOVIL = {
    "banco": "Banco de Venezuela (0102)",
    "telefono": "04120582064",
    "cedula": "V-15.642.481",
    "beneficiario": "Carlos Pacheco"
}
WHATSAPP_ADMIN = "584120582064"

def generar_link_whatsapp(mensaje):
    """Genera enlace exclusivo para comunicarse con el Administrador/Soporte."""
    return f"https://wa.me/{WHATSAPP_ADMIN}?text={urllib.parse.quote(mensaje)}"

# ---------------------------------------------------------
# TASA DE CAMBIO DIARIA (ACTUALIZABLE CADA 24 HORAS)
# ---------------------------------------------------------
hoy = datetime.now().date()

if 'fecha_tasa_activa' not in st.session_state:
    st.session_state.fecha_tasa_activa = hoy
    st.session_state.tasa_dolar_diaria = 36.50  # Tasa inicial por defecto

if st.session_state.fecha_tasa_activa != hoy:
    st.session_state.fecha_tasa_activa = hoy

TASA_DOLAR = st.session_state.tasa_dolar_diaria

# Barra Lateral de Navegación
st.sidebar.title("🛠️ YaracuyServicios")
st.sidebar.markdown(f"**Fecha del Sistema:** {hoy}")
st.sidebar.markdown(f"**Tasa del Dólar Vigente:** Bs. {TASA_DOLAR:.2f} *(Válida por 24h)*")
st.sidebar.markdown("---")

menu = st.sidebar.selectbox(
    "Seleccione Módulo",
    [
        "🌟 Inicio y Catálogo de Éxito", 
        "👤 Registro de Técnicos (Perfiles)", 
        "📋 Solicitar Servicio & Cotización PDF", 
        "🔒 Panel de Adjudicación (Administrador)",
        "💳 Pasarela de Pago & Contrato (50% / 50%)"
    ]
)

# ==========================================
# MÓDULO 1: INICIO Y CATÁLOGO DE ÉXITO (Neuromarketing + Logos)
# ==========================================
if menu == "🌟 Inicio y Catálogo de Éxito":
    # Layout de 3 columnas para colocar los logos a los lados y el título en el centro
    col_logo_izq, col_titulo, col_logo_der = st.columns([1, 4, 1])
    
    with col_logo_izq:
        try:
            st.image("Logo Servihogar1.png", use_container_width=True)
        except:
            st.write("🛡️ [Logo 1]")
            
    with col_titulo:
        st.markdown("<h1 style='text-align: center; color: #004080; font-size: 28px;'>🏡 Tu Hogar en Yaracuy Merece Paz y Confianza Absoluta</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #555; font-size: 16px;'>Recupera la tranquilidad con expertos verificados y garantizados por contrato.</h3>", unsafe_allow_html=True)
        
    with col_logo_der:
        try:
            st.image("Logo Servihogar2.png", use_container_width=True)
        except:
            st.write("⭐ [Logo 2]")
    
    st.markdown("---")
    
    col_l1, col_l2, col_l3, col_l4 = st.columns(4)
    with col_l1:
        st.markdown("<div style='text-align: center;'><h2>🛡️</h2><h4>100% Verificados</h4><p style='font-size:12px; color:gray;'>Cédula y antecedentes comprobados.</p></div>", unsafe_allow_html=True)
    with col_l2:
        st.markdown("<div style='text-align: center;'><h2>🤝</h2><h4>Contrato y Garantía</h4><p style='font-size:12px; color:gray;'>Respaldo legal y seguridad total.</p></div>", unsafe_allow_html=True)
    with col_l3:
        st.markdown("<div style='text-align: center;'><h2>⚡</h2><h4>Rapidez y Eficiencia</h4><p style='font-size:12px; color:gray;'>Soluciones puntuales sin demoras.</p></div>", unsafe_allow_html=True)
    with col_l4:
        st.markdown("<div style='text-align: center;'><h2>🔒</h2><h4>Pago Protegido</h4><p style='font-size:12px; color:gray;'>Esquema seguro 50/50 centralizado.</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.image("https://images.unsplash.com/photo-1581578731548-c64695cc6952?q=80&w=1200&auto=format&fit=crop", use_container_width=True)
    
    st.markdown("---")
    st.header("🏆 Trabajos Garantizados y Clientes Satisfechos en Yaracuy")
    
    if st.session_state.catalogo_exito:
        for item in st.session_state.catalogo_exito:
            st.info(f"""
            **Cliente:** {item['cliente']} ({item['municipio']})  
            **Servicio:** {item['comentario']}  
            **Calificación:** {item['estrellas']}
            """)

# ==========================================
# MÓDULO 2: REGISTRO DE TÉCNICOS
# ==========================================
elif menu == "👤 Registro de Técnicos (Perfiles)":
    st.title("👷 Registro y Perfil Profesional del Técnico")
    st.markdown("Al registrarte, aceptas cumplir estrictamente con los **estándares de calidad, rapidez y seguridad** bajo contrato con la administración.")
    
    with st.form("form_registro_tecnico"):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("Nombre y Apellido")
            cedula = st.text_input("Cédula de Identidad (Ej. V-20123456)")
            telefono = st.text_input("Número de Teléfono Personal")
        with col2:
            oficio = st.selectbox("Especialidad principal", ["Electricista", "Plomero", "Técnico de Aires Acondicionados", "Albañil", "Línea Blanca"])
            direccion = st.text_input("Municipio / Dirección de Residencia")
            
        experiencia = st.text_area("Experiencia Profesional y Certificaciones")
        acepta_contrato = st.checkbox("Acepto los términos de calidad, seguridad y la comisión de servicio del administrador.")
        
        btn_postular = st.form_submit_button("Registrar Perfil Profesional")
        
        if btn_postular:
            if acepta_contrato and nombre and cedula:
                nuevo_tecnico = {
                    "nombre": nombre,
                    "oficio": oficio,
                    "cedula": cedula,
                    "telefono": telefono,
                    "direccion": direccion,
                    "experiencia": experiencia,
                    "estado": "Disponible",
                    "foto": "https://api.iconify.design/fluent-emoji-flat:technologist.svg"
                }
                st.session_state.tecnicos.append(nuevo_tecnico)
                st.success("¡Perfil registrado con éxito! El administrador evaluará tus credenciales.")
            else:
                st.warning("Debes completar los campos obligatorios y aceptar el contrato de calidad.")

# ==========================================
# MÓDULO 3: SOLICITUD DE SERVICIO & COTIZACIÓN PDF
# ==========================================
elif menu == "📋 Solicitar Servicio & Cotización PDF":
    st.title("📋 Módulo de Solicitud y Cotización de Servicios")
    st.warning("🔒 **Aviso de Seguridad:** La clienta NO tiene acceso telefónico directo al técnico. La selección se realiza por perfil profesional, y el Administrador adjudica y genera la cotización/contrato oficial.")
    
    tab1, tab2, tab3 = st.tabs(["📝 Publicar Necesidad", "👥 Elegir Perfil Profesional", "📄 Generar Cotización Formato PDF"])
    
    with tab1:
        with st.form("form_solicitud_cliente"):
            c_nombre = st.text_input("Tu Nombre y Apellido")
            c_telefono = st.text_input("Tu Teléfono de Contacto")
            c_muni = st.selectbox("Municipio", ["San Felipe", "Independencia", "Cocorote", "Yaritagua", "Nirgua"])
            c_desc = st.text_area("Detalla la falla o servicio requerido en el hogar")
            
            btn_enviar_sol = st.form_submit_button("Registrar Solicitud en el Sistema")
            if btn_enviar_sol:
                if c_nombre and c_telefono and c_desc:
                    nueva_sol = {
                        "id": len(st.session_state.solicitudes) + 1,
                        "cliente": c_nombre,
                        "telefono": c_telefono,
                        "municipio": c_muni,
                        "servicio": c_desc,
                        "estado": "Pendiente de Adjudicación por Admin"
                    }
                    st.session_state.solicitudes.append(nueva_sol)
                    st.success("¡Solicitud registrada! El Administrador la revisará.")
                else:
                    st.error("Por favor completa los campos requeridos.")
                    
    with tab2:
        st.subheader("Directorio de Expertos (Evaluación por Experiencia y Perfil)")
        if st.session_state.tecnicos:
            for i, tec in enumerate(st.session_state.tecnicos):
                with st.container():
                    col1, col2 = st.columns([1, 4])
                    with col1:
                        st.image(tec["foto"], width=80)
                    with col2:
                        st.markdown(f"### {tec['nombre']} - *{tec['oficio']}*")
                        st.write(f"🆔 **Cédula Verificada:** {tec['cedula']} | 📍 **Municipio:** {tec['direccion']}")
                        st.write(f"💼 **Experiencia:** {tec['experiencia']}")
                        
                        if st.button(f"Seleccionar Perfil de {tec['nombre']}", key=f"sel_{i}"):
                            st.session_state.tecnico_seleccionado_cot = tec['nombre']
                            st.success(f"¡Has seleccionado a {tec['nombre']}! Ya puedes generar tu cotización formal.")
                st.markdown("---")
        else:
            st.info("No hay técnicos disponibles en este momento.")

    with tab3:
        st.subheader("📄 Generador de Cotización y Contrato de Servicio")
        st.markdown("Genera el documento oficial detallado con la tasa del día, desglose 50/50 y condiciones de garantía.")
        
        with st.form("form_cotizacion"):
            cot_cliente = st.text_input("Nombre del Cliente Solicitante", value="María Pérez")
            cot_servicio = st.text_input("Descripción breve del servicio", value="Mantenimiento y revisión general")
            cot_monto_usd = st.number_input("Monto Total Estimado del Servicio (USD)", min_value=10.0, value=40.0, step=5.0)
            
            btn_generar_cot = st.form_submit_button("Generar Documento de Cotización")
            
            if btn_generar_cot:
                monto_bs_total = cot_monto_usd * TASA_DOLAR
                inicial_usd = cot_monto_usd * 0.50
                inicial_bs = inicial_usd * TASA_DOLAR
                restante_usd = cot_monto_usd * 0.50
                restante_bs = restante_usd * TASA_DOLAR
                
                st.markdown("---")
                st.markdown(f"""
                ### 🛠️ YARACUYSERVICIOS - COTIZACIÓN Y CONTRATO OFICIAL
                **Fecha de Emisión:** {hoy}  
                **Tasa BCV Aplicada (Fija 24h):** Bs. {TASA_DOLAR:.2f} per USD  
                ------------------------------------------------------------  
                **Cliente:** {cot_cliente}  
                **Servicio Solicitado:** {cot_servicio}  
                ------------------------------------------------------------  
                #### 💰 DESGLOSE FINANCIERO:
                * **Monto Total del Contrato:** ${cot_monto_usd:.2f} (Bs. {monto_bs_total:.2f})
                * **Inicial Requerida (50% para inicio):** ${inicial_usd:.2f} (Bs. {inicial_bs:.2f})
                * **Pago Final (50% al culminar):** ${restante_usd:.2f} (Bs. {restante_bs:.2f})
                
                #### 🔒 DATOS ÚNICOS PARA PAGO MÓVIL (ADMINISTRADOR):
                * **Banco:** {ADMIN_PAGO_MOVIL['banco']}
                * **Teléfono:** {ADMIN_PAGO_MOVIL['telefono']}
                * **Cédula:** {ADMIN_PAGO_MOVIL['cedula']} ({ADMIN_PAGO_MOVIL['beneficiario']})
                
                > **Cláusula de Garantía y Calidad:** Al realizar el pago del 50% inicial a las cuentas del administrador, se activa la póliza de cumplimiento, rapidez y seguridad técnica bajo supervisión de YaracuyServicios.
                ------------------------------------------------------------
                """)
                
                texto_cotizacion = f"""YARACUYSERVICIOS - COTIZACION OFICIAL
Fecha: {hoy} | Tasa: {TASA_DOLAR}
Cliente: {cot_cliente}
Servicio: {cot_servicio}
Total: ${cot_monto_usd} (Bs. {monto_bs_total})
Inicial 50%: ${inicial_usd} (Bs. {inicial_bs})
Pago Final 50%: ${restante_usd} (Bs. {restante_bs})
Pago Movil: {ADMIN_PAGO_MOVIL['telefono']} - {ADMIN_PAGO_MOVIL['cedula']} ({ADMIN_PAGO_MOVIL['banco']})
"""
                st.download_button(
                    label="📥 Descargar Cotización en TXT / Formato Digital",
                    data=texto_cotizacion,
                    file_name=f"Cotizacion_YaracuyServicios_{cot_cliente.replace(' ', '_')}.txt",
                    mime="text/plain"
                )

# ==========================================
# MÓDULO 4: PANEL DE ADJUDICACIÓN & TASA PROTEGIDA (ADMIN)
# ==========================================
elif menu == "🔒 Panel de Adjudicación (Administrador)":
    st.title("🔒 Panel de Control del Administrador")
    st.markdown("Área exclusiva para la gerencia. Aquí se adjudican los contratos y se controla de forma segura la tasa cambiaria diaria.")
    
    admin_clave = st.text_input("Clave de Acceso Administrador", type="password")
    
    if admin_clave == "admin1234":
        st.success("Acceso Autorizado como Administrador.")
        
        st.markdown("---")
        st.subheader("⚙️ Módulo Protegido: Actualización de Tasa Diaria (24 Horas)")
        st.markdown(f"Tasa actual en sistema: **Bs. {TASA_DOLAR:.2f}**")
        
        nueva_tasa = st.number_input("Ingresar Nueva Tasa BCV / Paralelo", value=float(TASA_DOLAR), step=0.10)
        if st.button("Fijar Tasa por 24 Horas (Seguro Admin)"):
            st.session_state.tasa_dolar_diaria = nueva_tasa
            st.success(f"¡Tasa actualizada correctamente a Bs. {nueva_tasa:.2f} por las próximas 24 horas!")
            st.rerun()
            
        st.markdown("---")
        st.subheader("📋 Listado de Solicitudes y Adjudicación de Contratos")
        if st.session_state.solicitudes:
            for idx, sol in enumerate(st.session_state.solicitudes):
                with st.expander(f"Solicitud #{sol['id']} - Cliente: {sol['cliente']} ({sol['municipio']})"):
                    st.write(f"**Servicio:** {sol['servicio']}")
                    st.write(f"**Teléfono Cliente:** {sol['telefono']}")
                    st.write(f"**Estado Actual:** {sol['estado']}")
                    
                    nuevo_estado = st.selectbox(f"Actualizar Estado Contrato #{sol['id']}", ["Pendiente de Adjudicación", "Adjudicado (En Proceso)", "Culminado con Éxito"], key=f"est_{idx}")
                    if st.button(f"Guardar Estado #{sol['id']}", key=f"btn_est_{idx}"):
                        sol['estado'] = nuevo_estado
                        st.success("¡Estado de contrato actualizado correctamente!")
        else:
            st.info("No hay solicitudes pendientes.")
        
        st.markdown("---")
        st.subheader("💰 Cálculo y Liquidación de Pagos a Técnicos")
        monto_contrato = st.number_input("Monto Total del Contrato en USD ($)", min_value=10.0, value=50.0)
        comision_admin = monto_contrato * 0.10
        pago_tecnico = monto_contrato * 0.90
        st.write(f"🔹 **Retención plataforma (10%):** ${comision_admin:.2f} (Bs. {comision_admin * TASA_DOLAR:.2f})")
        st.write(f"🔹 **Monto a liquidar al técnico (90%):** ${pago_tecnico:.2f} (Bs. {pago_tecnico * TASA_DOLAR:.2f})")
        
    elif admin_clave != "":
        st.error("Clave de administrador incorrecta.")

# ==========================================
# MÓDULO 5: PASARELA DE PAGO & CONTRATO (50% / 50%)
# ==========================================
elif menu == "💳 Pasarela de Pago & Contrato (50% / 50%)":
    st.title("💳 Pasarela de Pagos Centralizada (Esquema 50% / 50%)")
    st.markdown("Todo pago se realiza **únicamente** a través de las cuentas oficiales del Administrador.")
    
    st.info(f"""
    **DATOS OFICIALES ÚNICOS PARA PAGO MÓVIL:**
    * **Banco:** {ADMIN_PAGO_MOVIL['banco']}
    * **Teléfono:** {ADMIN_PAGO_MOVIL['telefono']}
    * **Cédula:** {ADMIN_PAGO_MOVIL['cedula']}
    * **Beneficiario:** {ADMIN_PAGO_MOVIL['beneficiario']}
    * **Tasa del Dólar Actual (Fija 24h):** Bs. {TASA_DOLAR:.2f}
    """)
    
    tipo_pago_etapa = st.selectbox("Seleccione Etapa del Contrato", ["1. Pago Inicial (50%)", "2. Pago Final / Culminación (50%)"])
    metodo = st.selectbox("Método de Pago", ["Pago Móvil (Banco de Venezuela)", "Zinli", "Wally Tech"])
    
    monto_ref = st.number_input("Monto en Divisas (USD)", min_value=5.0, value=25.0, step=5.0)
    monto_bs = monto_ref * TASA_DOLAR
    
    if "Pago Móvil" in metodo:
        st.warning(f"Equivalente exacto a pagar en Bolívares según tasa del día (Bs. {TASA_DOLAR:.2f}): **Bs. {monto_bs:.2f}**")
        
    ref_pago = st.text_input("Número de Referencia de la Transferencia / Pago Móvil")
    
    if st.button("Reportar Transacción al Administrador"):
        if ref_pago:
            st.success("¡Pago reportado con éxito! El administrador verificará la referencia.")
            
            msg_pago = f"Hola Carlos Pacheco, reporto pago de {tipo_pago_etapa} por ${monto_ref} ({metodo}). Ref: {ref_pago}. Tasa aplicada: {TASA_DOLAR}."
            st.markdown(f'<a href="{generar_link_whatsapp(msg_pago)}" target="_blank"><button style="background-color:#25D366; color:white; padding:10px 20px; border:none; border-radius:5px; font-weight:bold; cursor:pointer;">📱 Notificar Comprobante al Administrador por WhatsApp</button></a>', unsafe_allow_html=True)
        else:
            st.error("Por favor ingrese el número de referencia del pago.")
