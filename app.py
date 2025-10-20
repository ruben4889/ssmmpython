"""
Streamlit App - Social Media Report Generator
Ejecutar: streamlit run app.py
"""

import streamlit as st
import os
from datetime import datetime
from io import BytesIO

# Importar la función de generación (asumiendo que está en report_generator.py)
# Si tu archivo se llama diferente, cambia el nombre aquí
# Configuración de base de datos usando secrets de Streamlit
try:
    DB_CONFIG = {
        'host': st.secrets["database"]["host"],
        'database': st.secrets["database"]["database"],
        'user': st.secrets["database"]["user"],
        'password': st.secrets["database"]["password"]
    }
except:
    # Fallback para desarrollo local
    DB_CONFIG = {
        'host': 'servermcp.postgres.database.azure.com',
        'database': 'DataAvengers',
        'user': 'reche',
        'password': 'Crieff4889'
    }


# Configuración de la página
st.set_page_config(
    page_title="Social Media Report Generator",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado para mejorar la apariencia
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 8px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d1fae5;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #10b981;
        margin: 1rem 0;
    }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 18px;
        font-weight: bold;
        padding: 0.75rem 2rem;
        border-radius: 8px;
        border: none;
        width: 100%;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #5568d3 0%, #653a8f 100%);
        border: none;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>📊 Social Media & Happiness Report Generator</h1>
    <p>Generador automático de reportes PDF con análisis completo</p>
</div>
""", unsafe_allow_html=True)

# Sidebar con información
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2920/2920324.png", width=100)
    st.title("ℹ️ Información")
    
    st.markdown("""
    ### 🎯 ¿Qué hace esta app?
    
    Genera un reporte PDF profesional con:
    - 📈 Análisis estadístico completo
    - 📊 Gráficos y visualizaciones
    - 🔍 Insights y correlaciones
    - ✅ Recomendaciones accionables
    - 🎯 Plan de acción de 30 días
    
    ### 📋 Contenido del Reporte
    
    1. **Executive Summary**
    2. **Key Findings**
    3. **Platform Analysis**
    4. **Screen Time Impact**
    5. **Demographics**
    6. **Correlation Analysis**
    7. **Recommendations**
    8. **30-Day Action Plan**
    9. **Expected Outcomes**
    """)
    
    st.divider()
    
    # Mostrar configuración de BD (ofuscada)
    st.markdown("### 🔐 Configuración")
    st.info(f"""
    **Base de datos:** {DB_CONFIG.get('database', 'N/A')}  
    **Host:** {DB_CONFIG.get('host', 'N/A')}  
    **Usuario:** {DB_CONFIG.get('user', 'N/A')}
    """)
    
    st.caption("© 2025 Data Analytics Project")

# Contenido principal
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="info-box">
        <h3>📄 Generación de Reporte</h3>
        <p>Este reporte analiza datos de usuarios de redes sociales y su impacto en la felicidad. 
        Incluye métricas clave, análisis de plataformas, correlaciones y recomendaciones prácticas.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.metric(label="📊 Páginas del Reporte", value="~15")
    st.metric(label="⏱️ Tiempo estimado", value="~10s")

# Sección de generación
st.markdown("---")
st.subheader("🚀 Generar Reporte")

col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

with col_btn2:
    generate_button = st.button("📥 GENERAR Y DESCARGAR PDF", type="primary", use_container_width=True)

# Lógica de generación
if generate_button:
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        # Paso 1: Conectar a la base de datos
        status_text.text("🔌 Conectando a la base de datos...")
        progress_bar.progress(20)
        
        # Paso 2: Obtener datos
        status_text.text("📊 Obteniendo datos de usuarios...")
        progress_bar.progress(40)
        
        # Paso 3: Generar PDF
        status_text.text("📄 Generando reporte PDF...")
        progress_bar.progress(60)
        
        filename = f"social_media_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        generate_simple_pdf(filename)
        
        progress_bar.progress(80)
        status_text.text("✅ Preparando descarga...")
        
        # Leer el archivo generado
        with open(filename, "rb") as f:
            pdf_data = f.read()
        
        progress_bar.progress(100)
        status_text.text("🎉 ¡Reporte generado exitosamente!")
        
        # Mostrar success message
        st.markdown("""
        <div class="success-box">
            <h3>✅ ¡Éxito!</h3>
            <p>Tu reporte ha sido generado correctamente. Haz clic en el botón de abajo para descargarlo.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botón de descarga
        st.download_button(
            label="📥 DESCARGAR REPORTE PDF",
            data=pdf_data,
            file_name=filename,
            mime="application/pdf",
            use_container_width=True
        )
        
        # Información adicional
        col_info1, col_info2, col_info3 = st.columns(3)
        with col_info1:
            st.info(f"📁 **Tamaño:** {len(pdf_data) / 1024:.1f} KB")
        with col_info2:
            st.info(f"📅 **Fecha:** {datetime.now().strftime('%d/%m/%Y')}")
        with col_info3:
            st.info(f"⏰ **Hora:** {datetime.now().strftime('%H:%M:%S')}")
        
        # Limpiar archivo temporal (opcional)
        try:
            os.remove(filename)
        except:
            pass
            
    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        
        st.error(f"❌ **Error al generar el reporte:** {str(e)}")
        
        with st.expander("🔍 Ver detalles del error"):
            st.code(str(e))
            st.markdown("""
            ### 💡 Soluciones posibles:
            
            1. **Verifica la conexión a la base de datos**
               - Comprueba que las credenciales en `DB_CONFIG` sean correctas
               - Asegúrate de que el servidor de BD esté accesible
            
            2. **Verifica que la tabla exista**
               - La tabla `social_media.social_media` debe existir
               - Debe contener datos válidos
            
            3. **Revisa las librerías instaladas**
               ```bash
               pip install reportlab psycopg2-binary matplotlib
               ```
            """)

# Footer con información adicional
st.markdown("---")
st.markdown("""
### 📚 ¿Cómo usar esta aplicación?

1. **Haz clic** en el botón "GENERAR Y DESCARGAR PDF"
2. **Espera** mientras se genera el reporte (10-15 segundos)
3. **Descarga** el PDF cuando esté listo
4. **Abre** el archivo PDF para ver el análisis completo

### ⚙️ Configuración técnica

El reporte se genera utilizando:
- **ReportLab** para crear el PDF
- **Matplotlib** para gráficos
- **PostgreSQL** como fuente de datos
- **Streamlit** como interfaz web

### 🛟 ¿Necesitas ayuda?

Si encuentras problemas:
- Verifica que las credenciales de la BD sean correctas
- Asegúrate de tener todas las dependencias instaladas
- Revisa que la tabla `social_media.social_media` exista
""")

# Estado de la aplicación (en sidebar)
with st.sidebar:
    st.divider()
    st.caption(f"🕐 Última actualización: {datetime.now().strftime('%H:%M:%S')}")
    if st.button("🔄 Refrescar página"):
        st.rerun()