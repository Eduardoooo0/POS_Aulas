let botao = document.getElementById('botao_cadastrar')
let div = document.getElementById('form_cadastro')
let fechar = document.getElementById('fechar')
div.style.display = 'none'
botao.addEventListener('click', () =>{
    div.style.display = 'block'
})

fechar.addEventListener('click',()=>{
    div.style.display = 'none'
})


function atualizarTabela(){
    $.ajax({
        url:'http://127.0.0.1:8000/tarefas',
        method:'GET',
        dataType: 'json',
        success: function(tarefas){
            const $tbody = $('#tbtarefas tbody');
            $tbody.empty();

            tarefas.forEach(tarefa =>{
                $tbody.append(`
                <tr>
                    <td>${tarefa.id}</td>
                    <td>${tarefa.titulo}</td>
                    <td>${tarefa.descricao}</td>
                    <td>${tarefa.concluido}</td>
                </tr>`
            )})
        },
        error:function(err){
            console.error('Erro:',err);
        }
    })
}
$(document).ready(function(){
    setInterval(atualizarTabela,1000);
})