class CodeEditor {
    constructor() {
        this.editors = new Map();
        this.themes = {
            'dark': 'material-darker',
            'light': 'default',
            'cosmic': 'cosmic-night'
        };
    }
    
    initEditor(language, elementId) {
        const editor = CodeMirror(document.getElementById(elementId), {
            mode: language,
            theme: this.themes['cosmic'],
            lineNumbers: true,
            autoCloseBrackets: true,
            matchBrackets: true,
            lint: true,
            gutters: ["CodeMirror-lint-markers"],
            extraKeys: {
                "Ctrl-Space": "autocomplete",
                "Ctrl-/": "toggleComment"
            }
        });
        
        this.editors.set(language, editor);
        return editor;
    }
    
    addAIAssist(editor) {
        editor.setOption('hintOptions', {
            hint: function(editor) {
                const cursor = editor.getCursor();
                const token = editor.getTokenAt(cursor);
                
                // AI-подсказки на основе контекста
                return {
                    list: [
                        'function', 'return', 'const', 'let', 'var',
                        'if', 'else', 'for', 'while', 'switch'
                    ],
                    from: CodeMirror.Pos(cursor.line, token.start),
                    to: CodeMirror.Pos(cursor.line, token.end)
                };
            }
        });
    }
}