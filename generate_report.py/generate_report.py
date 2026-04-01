import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import io
from datetime import datetime
from connection import db_pass

#configuração do banco de dados para conexão

db_user = "postgres"
db_senha = quote_plus(db_pass)
db_host = "localhost"
db_port = "5432"
db_name = "postgres"


engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_senha}@{db_host}:{db_port}/{db_name}')

#query para consumir os dados do banco PostgreSQL 
query = """
    SELECT
        c.dia_inic_vigenc_conv::date as ano,
        SUM(e.vl_repasse_conv) as val_repasse
    FROM 
        execucao_financeira e
    INNER JOIN 
        convenios c ON e.id_proposta::bigint = c.id_proposta
    GROUP BY   
        ano
    ORDER BY
        ano
    ;
"""

#Conexão
df = pd.read_sql(query, engine)
df['ano'] = pd.to_datetime(df['ano']).dt.year
df_grouped = df.groupby('ano', as_index=False)['val_repasse'].sum()

print(df.dtypes)
print(df.head)

plt.clf()
plt.close('all')

#Plot
anos = df_grouped['ano']
valores = df_grouped['val_repasse']
bar_width = 0.6


plt.figure(figsize=(10,6))
bars = plt.bar(anos, valores, width= bar_width, color = 'royalblue', edgecolor='black')
plt.title('Evolução Anual dos Repasses')
plt.xlabel('Ano')
plt.ylabel('Valor Repassado (R$)')
plt.yticks([])
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
for bar, valor in zip(bars, valores):
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura,
        f'R${valor:,.0f}',
        ha='center',
        va='bottom',
        fontsize=7,
    )
plt.tight_layout()



buf = io.BytesIO()
plot_file='grafico_relatorio.png'
plt.savefig(plot_file, format='png')



# Montando PDF 
class PDF(FPDF):
    def header(self):

        # Logo
        logo_path = "C:/Users/lucio/Downloads/facilit_tecnologia_logo.jpg"
        self.image(logo_path, x=10, y=8, w=33)
        
        # Título
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'Relatório de Evolução dos Repasses', 0, 1, 'C')
        self.ln(10)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Página {self.page_no()}', 0 , 0, 'C')
    
    def add_observations(self, observations): 
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 8, observations)

pdf = PDF()
pdf.add_page()

# Adicionando Gráfico
pdf.image(plot_file, x=30, y=40, w=150)
pdf.ln(110)

# Observações
observations = (
    "Observações:\n"
    "- Este relatório demonstra os valores anuais dos repasses extraídos diretamente do banco de dados principal.\n"
    "- Use este relatório para monitoramento gerencial e tomadas de decisão."
)
pdf.add_observations(observations)

# Timestamp
now = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'C:/Teste técnico BI/generate_report.py/relatorio_evolucao_repasses_{now}.pdf'

pdf.output(filename)
print(f'Relatório gerado automaticamente e salvo como {filename[:30]}')

