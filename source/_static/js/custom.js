// custom.js

document.addEventListener("DOMContentLoaded", function() {
    if (!window.pyscriptLoaded) {
        var script = document.createElement('script');
        //script.src = "../_statict/sphinx_codemirror/pyscript.js";
        script.src = "https://pyscript.net/latest/pyscript.js";
        script.onload = function() {
            window.pyscriptLoaded = true;
            initializeCodeMirrors();
            initializePyScript();
        };
        document.head.appendChild(script);
    } else {
        initializeCodeMirrors();
        initializePyScript();
    }

    function initializeCodeMirrors() {
        document.querySelectorAll('.codemirror-container').forEach((container) => {
            const textarea = container.querySelector('textarea');
            const editor = CodeMirror.fromTextArea(textarea, {
                lineNumbers: true,
                mode: "python",
                theme: "default",
                indentUnit: 4  // Spécifie le nombre d'espaces pour l'indentation
            });
            container.editor = editor;
        });
    }

    function initializePyScript() {
        document.querySelectorAll('.pyscript-container').forEach((container) => {
            const runButton = container.querySelector('.run-button');
            const outputDiv = container.querySelector('.output');
            runButton.addEventListener('click', () => {
                const code = container.querySelector('.codemirror-container').editor.getValue();
                const pyscriptTag = document.createElement('py-script');
                pyscriptTag.innerHTML = code;
                outputDiv.innerHTML = ''; // Clear previous output
                outputDiv.appendChild(pyscriptTag);
            });
        });
    }
});
