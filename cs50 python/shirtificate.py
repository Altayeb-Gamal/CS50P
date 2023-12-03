from fpdf import FPDF


def main():
    pdf = FPDF(orientation="P", format="A4")
    name = input("Name: ")
    pdf.add_page()
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.set_font("Helvetica", "B", 50)
    pdf.cell(0, 50, text="CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")
    pdf.image("shirtificate.png", x=5, y=80, w=200)
    pdf.set_font("Helvetica", "B", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(0, 180, align="C", text=f"{name} took CS50")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
