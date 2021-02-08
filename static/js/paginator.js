class Index {
 
    static initPaginator() {
        document.body.querySelectorAll('div.tm-paging,.d-flex > a')
                .forEach( link => link.addEventListener('click', Index.pagination_link_clickHandler) );

        document.body.querySelector('#genre').querySelectorAll('ul > li > a')
                .forEach( link => link.addEventListener('click', Index.filter_link_clickHandler) );

        document.body.querySelector('#year').querySelectorAll('ul > li > a')
                .forEach( link => link.addEventListener('click', Index.filter_link_clickHandler) );

        document.body.querySelector('#country').querySelectorAll('ul > li > a')
                .forEach( link => link.addEventListener('click', Index.filter_link_clickHandler) );

        document.body.querySelector('#filter').addEventListener('click', Index.filter_run_link_clickHandler);
    };
    static get_list(objects){
        var list = [];
        for (var obj of objects ){  
            if(obj.classList.contains('active')){
                list.push(obj.id);
            }         
        }
        return list
    };
    static filter_activate(objects,list){
        for (var obj of objects){  
            if(list.indexOf( obj.id ) != -1 ){
                obj.classList.add('active');
            }
        }
    };
    static get_json_list_genre(){
        return JSON.stringify(Index.get_list(document.querySelector('#genre').querySelectorAll('ul > li > a')));
    };
    static get_json_list_year(){
        return JSON.stringify(Index.get_list(document.querySelector('#year').querySelectorAll('ul > li > a')));
    };
    static get_json_list_country(){
        return JSON.stringify(Index.get_list(document.querySelector('#country').querySelectorAll('ul > li > a')));
    };
    static filter_link_clickHandler(event){
        event.preventDefault();
        if($(this).hasClass('active')) {
            $(this).toggleClass('active',false);
        } else {
            $(this).toggleClass('active',true);
        }
    };  
    static filter_run_link_clickHandler(event){
        event.preventDefault();

        let path = event.target.href;
        let page = 1;

        Index.ajax_request(path,page);
        
    }; 
    static pagination_link_clickHandler(event){
        event.preventDefault();

        let path = event.target.href;
        let page = getURLParameter(path,"page");


        Index.ajax_request(path,page);
    
    };  
    static ajax_request(path,page){
        if (typeof page !== 'undefined') {
            
            let genre = Index.get_json_list_genre();
            let year = Index.get_json_list_year();
            let countres = Index.get_json_list_country();

            jQuery.ajax({
                url: '',
                headers:{"X-CSRFToken": getCookie('csrftoken')},
                type: 'POST',
                dataType: 'json',
                data: {
                    'page': page,
                    'genres':genre,
                    'countres': countres,
                    'years': year,
                    
                 }, 
                    
                success : function (json) {
                    window.history.pushState({route: path}, "EVILEG", path);
                    jQuery("#main").replaceWith(json.movie_list); 
                    Index.initPaginator();

                    Index.filter_activate(document.body.querySelector('#genre').querySelectorAll('ul > li > a') , json.genres); 

                    Index.filter_activate(document.body.querySelector('#year').querySelectorAll('ul > li > a') , json.years);

                    Index.filter_activate(document.body.querySelector('#country').querySelectorAll('ul > li > a') , json.countres);
                }
            });
            document.getElementById("movie-block").scrollIntoView();
        }
    };
}

function getURLParameter(sUrl, sParam) {
    let sPageURL = sUrl.substring(sUrl.indexOf('?') + 1);
    let sURLVariables = sPageURL.split('&');
    for (let i = 0; i < sURLVariables.length; i++) {
        let sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam) {
            return sParameterName[1];
        }
    }
} 

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

Index.initPaginator();