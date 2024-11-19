from pypdf import PdfReader

class SplitService:
    def split_pages(pages,start_page:int,count:int):
        end_page = min(len(pages),start_page - 1 + count)

        writer = PdfWriter()