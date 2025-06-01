from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "QA Manual em Ambiente Ágil – Visão Geral", ln=True, align="C")
        self.ln(5)

    def chapter_title(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(2)

    def chapter_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, body)
        self.ln()

content = {
    "1. Como funciona o dia a dia de um QA manual": """...""",
    "2. Como é o ciclo de vida de um bug": """...""",
    "3. Casos de Teste (Passo a Passo)": """...""",
    "4. Cenários de Teste (Formato BDD)": """..."""
}

pdf = PDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

for title, body in content.items():
    pdf.chapter_title(title)
    pdf.chapter_body(body)

pdf.output("docs/QA_Manual_Agil.pdf")
