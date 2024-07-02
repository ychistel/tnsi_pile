function initializeCodeMirror() {
    const editorElements = document.querySelectorAll('editor');
    editorElements.forEach(element => {
        const editor = CodeMirror.fromTextArea(element, {
            mode: 'python',
            lineNumbers: true,
            theme: "default"
        });
        element.nextElementSibling.addEventListener('click', () => {
            runCode(editor, element.nextElementSibling.nextElementSibling);
        });
    });
}

async function runCode(editor, outputElement) {
    const code = editor.getValue();
    const pyodide = await loadPyodide();
    try {
        let output = await pyodide.runPythonAsync(code);
        outputElement.textContent = output;
    } catch (error) {
        outputElement.textContent = error;
    }
}

// Vérifiez la disponibilité de CodeMirror et initialisez les éditeurs
document.addEventListener('DOMContentLoaded', function () {
    function checkCodeMirror() {
        if (typeof CodeMirror !== 'undefined') {
            initializeCodeMirror();
        } else {
            setTimeout(checkCodeMirror, 50);
        }
    }
    checkCodeMirror();
});
