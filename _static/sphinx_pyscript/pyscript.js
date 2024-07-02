let pyodideReady = false;
let pyodide = null;
let editors = {};

async function loadPyodideAndPackages(){
    pyodide = await loadPyodide({
        indexURL: "https://cdn.jsdelivr.net/pyodide/v0.26.1/full/"
    });
    await pyodide.loadPackage(['micropip']);
    pyodideReady = true;
}

loadPyodideAndPackages();

async function runPyScript(id) {
    if (!pyodideReady) {
        alert("Pyodide is still loading. Please wait.");
        return;
    }

    let editor = editors[id];
    if (!editor) {
        console.error("CodeMirror editor not found for ID:", id);
        return;
    }

    let output = document.getElementById(id + '-output');
    let code = editor.getValue();

    output.innerHTML = '';

    try {
        let result = await pyodide.runPythonAsync(`
import sys
from io import StringIO

output = StringIO()
sys.stdout = output
sys.stderr = output

code = '''${code}'''

exception_occurred = False
assertion_failed = False

try:
    exec(code)
except AssertionError as ae:
    exception_occurred = True
    assertion_failed = True
    print(f"AssertionError: {ae}")
except Exception as e:
    exception_occurred = True
    print(f"Error: {e}")

sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__

output_value = output.getvalue()
output_value
        `);

        let formattedResult = formatOutput(result !== undefined ? result : 'No output');
        output.innerHTML = formattedResult;
    } catch (err) {
        output.innerHTML = '<span class="error">Error: ' + escapeHtml(err.toString()) + '</span>';
    }
}

// Fonction pour échapper les caractères HTML spéciaux
function escapeHtml(text) {
    return text.replace(/&/g, '&amp;')
               .replace(/</g, '&lt;')
               .replace(/>/g, '&gt;')
               .replace(/"/g, '&quot;')
               .replace(/'/g, '&#039;');
}

// Fonction pour formater la sortie avec des balises HTML et des classes CSS
function formatOutput(output) {

    // Échapper les caractères HTML spéciaux
    let escapedOutput = escapeHtml(output);

    // Ajouter des balises HTML avec des classes CSS pour les erreurs, avertissements et résultats
    let formattedOutput = escapedOutput
        .split('\n')
        .map(line => {
            if (line.startsWith("Bravo!")) {
                return `<span class="success">${line}</span>`;
            } else if (line.startsWith("AssertionError: ")) {
                return `<span class="assertion-error">${line}</span>`;
            } else if (line.startsWith("Error: ")) {
                return `<span class="error">${line}</span>`;
            } else if (line.startsWith("Warning: ")) {
                return `<span class="warning">${line}</span>`;
            } else if (line.startsWith("Result: ")) {
                return `<span class="result">${line}</span>`;
            } else {
                return `<span class="line">${line}</span>`;
            }
        })
        .join('<br>');

    return formattedOutput;
}

function clearEditor(editorId) {
    const editor = editors[editorId];
    //const output = document.getElementById(`${editorId}-output`);
    editor.setValue('');
    //output.textContent = '';
}

function clearOutput(editorId) {
    //const editor = codeEditors[editorId];
    const output = document.getElementById(`${editorId}-output`);
    //editor.setValue('');
    output.textContent = '';
}

function downloadCode(editorId) {
    const editor = editors[editorId];
    const code = editor.getValue();

    const blob = new Blob([code], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.style.display = 'none';
    a.href = url;
    a.download = 'script.py';
    document.body.appendChild(a);

    a.click();

    // Clean up
    setTimeout(() => {
        document.body.removeChild(a);
        window.URL.revokeObjectURL(url);
    }, 0);
}

function increaseEditorHeight(editorId) {
    const editor = editors[editorId];
    const currentHeight = editor.getWrapperElement().style.height;
    const newHeight = parseInt(currentHeight, 10) + 50;  // Augmenter la hauteur par exemple de 50 pixels
    editor.setSize(null, newHeight);
}

function decreaseEditorHeight(editorId) {
    const editor = editors[editorId];
    const currentHeight = editor.getWrapperElement().style.height;
    const newHeight = parseInt(currentHeight, 10) - 50;  // Réduire la hauteur par exemple de 50 pixels
    if (newHeight >= 40) {  // Limiter la hauteur minimale (par exemple 50 pixels)
        editor.setSize(null, newHeight);
    }
}

function tailleCaracteres(textEditor){
    // Sélectionnez l'élément dont vous voulez connaître la taille de police
    const element = document.getElementById(textEditor);
    // Utilisez window.getComputedStyle pour obtenir les styles calculés
    const styles = window.getComputedStyle(element);
    // Récupérez la taille de police à partir des styles calculés
    const fontSize = styles.getPropertyValue('font-size');
    return fontSize.split('px')[0]
}
// Initialize CodeMirror on all textareas after the document is ready
document.addEventListener('DOMContentLoaded', (event) => {
    
    function initializeEditor(editorId, code, height) {
        const textarea = document.getElementById(editorId);
        const editor = CodeMirror.fromTextArea(textarea, {
            mode: 'python',
            lineNumbers: true,
            indentUnit: 4,
        });
        editor.setValue(code);
        const heightDefault = height.split('px')[0];
        var lineHeight = tailleCaracteres(editorId) * 2;
        // recherche de la hauteur de l'éditeur si vide ou complété
        var nbLignes = editor.lineCount();
        var heightOfLines = nbLignes * lineHeight;
        var height = Math.max(heightDefault, heightOfLines ) ;
        editor.setSize(null, height);  // Set the height of the editor
        editors[editorId] = editor;
    }

    // Expose the functions to the global scope
    window.runPyScript = runPyScript;
    window.clearEditor = clearEditor;
    window.clearOutput = clearOutput;

    // Initialize editors for each textarea
    document.querySelectorAll('textarea[id^="pyscript-editor-"]').forEach(textarea => {
        const code = textarea.textContent || textarea.value;
        const height = textarea.style.height || '50px';  // Get the specified height or use default
        initializeEditor(textarea.id, code, height);
    });
});
