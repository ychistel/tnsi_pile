import os
from sphinx.util.fileutil import copy_asset

from docutils import nodes,utils
from docutils.parsers.rst import Directive,directives
from sphinx.util.docutils import SphinxDirective

class PyScriptDirective(SphinxDirective):
    has_content = True
    option_spec = {
        'file': directives.path,
        'title': directives.unchanged,  # Adding the logo option
        'class': directives.class_option,  # Accepts a class option
        'height': directives.unchanged,  # Adding the height option
    }

    def run(self):
        if 'file' in self.options:
            file_path = os.path.normpath(self.options['file'])
            source_dir = os.path.dirname(os.path.abspath(self.state.document.current_source))
            #source = os.path.normpath(os.path.join(source_dir,self.options['file']))
            #source = utils.relative_path(None, source)
            full_path = os.path.abspath(os.path.join(source_dir, file_path))
            try:
                with open(full_path, 'r') as f:
                    code = f.read()
            except Exception as e:
                return [nodes.error(None, nodes.paragraph(text=f'Failed to read file: {e}'))]
        else:
            code = '\n'.join(self.content)

        div_id = f"pyscript-editor-{self.env.new_serialno('pyscript')}"
        editor_height = self.options.get('height', '40px')  # Default height

        # Create a container for the editor and output
        container = nodes.container()
        editeur = nodes.container()
        editeur['classes'].append('pyscript-editeur')

        # Create the title div with logo if the logo option is provided
        title_html = ''
        if 'title' in self.options:
            title_text = self.options['title']
            title_html = f'''
                <h3 id="{div_id}-title" class="pyscript-title">{title_text}</h3>
            '''
        title_div = nodes.raw('', title_html, format='html')

        if 'class' in self.options:
            custom_class = ' '.join(self.options.get('class', []))
            container_class = f'pyscript-container {custom_class}'
            container['classes'].append(container_class)
        else:
            container['classes'].append('pyscript-container')

        # Create the editor div
        editor_div = nodes.raw('', f'<textarea id="{div_id}" class="pyscript-editor" style="height: {editor_height};">{code}</textarea>', format='html')

        # Create the output div
        output_div = nodes.raw('', f'<div id="{div_id}-output" class="pyscript-output"></div>', format='html')

        # Les boutons en html et le logo python
        buttons_html = f'''
            <div id="{div_id}-buttons" class="pyscript-button">
            <div id="{div_id}-logo" class="pyscript-logo">
                <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/files/python-logo-only.svg" alt="Python Logo" class="python-logo"/>
            </div>
            <button id="{div_id}-run-button" onclick="runPyScript(\'{div_id}\')">Run</button>
            <button id="{div_id}-clear-editor-button" onclick="clearEditor(\'{div_id}\')">Clear Editor</button>
            <button id="{div_id}-clear-output-button" onclick="clearOutput(\'{div_id}\')">Clear Output</button>
            <button id="{div_id}-downloadCode-button" onclick="downloadCode(\'{div_id}\')">Save</button>
            <button id="{div_id}-increaseEditorHeight" onclick="increaseEditorHeight(\'{div_id}\')"> Lines + </button>
            <button id="{div_id}-decreaseEditorHeight" onclick="decreaseEditorHeight(\'{div_id}\')"> Lines - </button>
            </div>
        '''

        # Création du pied du bloc éditeur
        foot_div = nodes.raw('', f'<div id="{div_id}-foot" class="pyscript-foot"></div>', format='html')
        
        # Create the buttons div
        buttons_div = nodes.raw('', buttons_html, format='html')

        # Ajout des 4 parties du bloc editeur
        editeur.append(buttons_div)
        editeur.append(editor_div)
        editeur.append(output_div)
        editeur.append(foot_div)

        # Add the title, editor, buttons, and output divs to the container
        if title_html:
            container += title_div
        container += editeur

        return [container]

def add_pyscript_assets(app):
    static_path = os.path.join(os.path.dirname(__file__), '_static')
    for asset in ['css/codemirror.min.css','css/pyscript.css','mode/python/python.min.js', 'js/codemirror.min.js','js/pyscript.js']:
        copy_asset(os.path.join(static_path, asset), os.path.join(app.outdir, '_static/sphinx_pyscript'))

    #app.add_css_file('sphinx_pyscript/codemirror.min.css')
    #app.add_js_file('sphinx_pyscript/codemirror.min.js')
    #app.add_js_file('sphinx_pyscript/python.min.js')
    app.add_css_file('sphinx_pyscript/pyscript.css')
    app.add_js_file('sphinx_pyscript/pyscript.js')

def setup(app):
    app.add_directive("pyscript", PyScriptDirective)
    app.add_js_file("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.js")
    app.add_js_file("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/mode/python/python.min.js")
    app.add_css_file("https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.65.5/codemirror.min.css")
    app.add_js_file("https://cdn.jsdelivr.net/pyodide/v0.26.1/full/pyodide.js")
    #app.add_js_file("js/pyscript.js")  # Include the external JavaScript file
    app.connect('builder-inited', add_pyscript_assets)
