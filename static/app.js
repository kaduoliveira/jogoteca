$('form input[type="file"]').change(event => {
    let arquivos = event,files;
    if (arquivos.length === 0) {
    }  else {
        if (arquivos[0].type == 'image/jpeg') {
        $('img').remove();
        let imagem = $('<imag class="img-responsive">');
        $('figure').prepend(imagem);
        } else {
            alert('Formato não suportado')
        }
    }
});