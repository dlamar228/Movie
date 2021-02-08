class Video{
    static param_s;
    static param_f;
    static param_t;
    static player;	

    static InitSelectsSerial(){

        jQuery("#replace").replaceWith(
            `<div class="row mb-5 pb-4">
                <div class="col-12">
                    <select class="selectpicker" data-size="5" id = "lang">
                    </select>
                    <select class="selectpicker" data-size="5" id = "voice">
                    </select>
                    <select class="selectpicker" data-size="5" id = "season">
                    </select>
                    <select class="selectpicker" data-size="5" id = "serie">
                    </select>
                </div>
            </div>`);

        for(var lang of Video.GetLangs()){
            Video.addOption($('#lang'),lang,lang)
        }
        for(var voice of Video.GetVoices()){
            Video.addOption($('#voice'),voice,voice)
        }
        for(var season of Video.GetSeasons()){
            Video.addOption($('#season'),'Season '+season,season)
        }

        for(var serie of Video.GetSeries()){
            Video.addOption($('#serie'),'Serie '+serie,serie)
        }

        
        $('.selectpicker').selectpicker();

        $('#lang').on('change', function(e){Video.ChangeLang()});
        $('#voice').on('change', function(e){Video.ChangeVoice()});
        $('#season').on('change', function(e){Video.ChangeSeason()});
        $('#serie').on('change', function(e){Video.ChangeSerie()});

        Video.ChangeSerie()
    };
    static ChangeLang(){
        Video.UpdateSelector('voice',Video.GetVoices(),'');
        Video.ChangeVoice();
    };
    static ChangeVoice(){
        Video.UpdateSelector('season',Video.GetSeasons(),'Season ');
        Video.ChangeSeason();
    };
    static ChangeSeason(){
        Video.UpdateSelector('serie',Video.GetSeries(),'Serie ');
        Video.ChangeSerie();
    };
    static ChangeSerie(){
        $('.selectpicker').selectpicker();   
        var key  = Video.GetSelectValue('serie')
        var serie = Video.param_s[Video.GetSelectValue('lang')][Video.GetSelectValue('voice')][Video.GetSelectValue('season')][key];
        var sources = []
        for(var q of Object.keys(serie)){
            sources.push(
                {
                    src: serie[q],
                    type: 'video/mp4',
                    size: q,
                }
            )
        }
        Video.LoadVideo(sources);
    };
    static UpdateSelector(name,values,text = ''){
        var obj = $("#"+name);
        obj.find('option').remove();

        for(var value of values){
            Video.addOption(obj,text+value,value);
        }

        obj.selectpicker('refresh');
    }
    static GetSeries(){
        return Object.keys(Video.param_s[Video.GetSelectValue('lang')][Video.GetSelectValue('voice')][Video.GetSelectValue('season')]);
    };
    static GetSeasons(){
        return Object.keys(Video.param_s[Video.GetSelectValue('lang')][Video.GetSelectValue('voice')]);
    };
    static GetVoices(){
        return Object.keys(Video.param_s[Video.GetSelectValue('lang')]);
    };
    static GetLangs(){
        return Object.keys(Video.param_s);
    };
    static GetSelectValue(name){
        var e = document.getElementById(name);  
        var selected_value = e.options[e.selectedIndex].value;
        return selected_value;
    };
    static addOption($select, text, value = null) {
        var $opt = $('<option />', {text: text});
        if (value === null) {
          value = text.toLowerCase().replace(/\s+/g, '-');
        }
        $opt.attr('value', value);
        $select.append($opt);
        $select.selectpicker('refresh');
    };
    static LoadVideo(sources_){
        var source = {
            type: 'video',
            title: 'Test video',
            sources: sources_,
        };

        Video.player.source = source;
    };
    static InitVideo(plyr,ps,pf,pt){
        Video.player = plyr;

        if(ps.length != 0 ){
            Video.param_s = JSON.parse(ps);
            Video.InitSelectsSerial()
        }
        if(pf.length != 0 ){
            Video.param_f = JSON.parse(pf);
        }
        if(pt.length != 0 ){
            Video.param_t = JSON.parse(pt);
        }
    }
}