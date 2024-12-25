 
import typer 
from my_pack import module7, module8, module9 
 
app = typer.Typer() 
 
@app.command() 
def process(file_path: str): 
    Обработка файла. 
    data = module7.process_file(file_path) 
    typer.echo(f"Data from file: {data}") 
