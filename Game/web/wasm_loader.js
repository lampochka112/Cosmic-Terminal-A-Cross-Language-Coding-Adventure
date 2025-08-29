// Загрузка WebAssembly модуля
async function loadWasmGame() {
    try {
        const importObject = {
            env: {
                memory: new WebAssembly.Memory({ initial: 256 }),
                table: new WebAssembly.Table({ initial: 0, element: 'anyfunc' })
            }
        };
        
        const response = await fetch('game_engine.wasm');
        const bytes = await response.arrayBuffer();
        const wasmModule = await WebAssembly.instantiate(bytes, importObject);
        
        // Экспорт функций из C++ в JavaScript
        window.gameEngine = {
            run: wasmModule.instance.exports.run,
            checkSolution: wasmModule.instance.exports.checkSolution
        };
        
    } catch (error) {
        console.error('WASM loading failed:', error);
    }
}