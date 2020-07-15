import ipywidgets as widgets
from IPython.display import display, HTML
button = widgets.Button(description="Submit Solution")
name_box = widgets.Text(value='', description='Name:')
email_box = widgets.Text(value='', description='Email:')

js = """
<script>
alert('asdf');
function findCellsByTag(tagName) {
     return Jupyter.notebook.get_cells().filter(
         ({metadata: {tags}}) => tags && tags.includes(tagName));
     }
</script>
"""
display(HTML(js))

def on_clicked(b):
    name = name_box.value
    email = email_box.value
    print(name, email)
    js = """
    <script>
console.log('here');
var submit_cell = findCellsByTag('code')[0];
var text = submit_cell.get_text();
alert(text);
</script>
"""
    display(HTML(js))
    
button.on_click(on_clicked)
display(name_box, email_box, button)
