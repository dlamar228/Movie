         '''def save(self, *args, **kwargs):
         url = self.movie.url

        path = 'media\\movies\\'+url+'\\video'
        
        if not os.path.exists(path + '\\'+self.language) : 
            path = create_folder(path,self.language)
        if not os.path.exists(path + '\\'+str(self.quality)):
            path = create_folder(path,str(self.quality))
        if not os.path.exists(path + '\\'+self.voice_acting):
            path = create_folder(path,self.voice_acting)
        if not os.path.exists(path + '\\season_' + str(self.season)):
            path = create_folder(path,'season_' + str(self.season)) 

        super(Season, self).save(*args, **kwargs)

    def get_all_url(self):
        result = {}
        movie = self.movie.url
        path = os.path.join('media\\movies',movie.url,'video',self.language,str(self.quality),self.voice_acting,'season_' + str(self.season)) + '\\'

        for i in range(1, self.episodes + 1):
            result[i] = path + movie.name + '_' + \
            'season_' + str(self.season) + '_' + \
            'episode_' + str(i) + '_' + \
            self.language + '_' + \
            str(self.quality) + '_'+ \
            self.voice_acting + '.mp4' 

        return 1 '''
     
     
     ''' def save(self, *args, **kwargs):
        url = self.movie.url
        path = 'media\\movies\\'+url+'\\video'
        if not os.path.exists(path + '\\'+self.language) :
            path = create_folder(path,self.language)
        if not os.path.exists( path + '\\'+str(self.quality)):
            path = create_folder(path,str(self.quality))
        if not os.path.exists(path + '\\'+self.voice_acting):
            path = create_folder(path,self.voice_acting)
        if not os.path.exists( path + '\\trailer'):
            path = create_folder(path,'trailer')
                
        super(Trailer, self).save(*args, **kwargs)

    def get_url(self):
        movie = self.movie.url

        path = os.path.join('media\\movies',movie.url,'video',self.language,str(self.quality),self.voice_acting,'trailer') + '\\'

        result = path  + movie.name + '_' + \
            'trailer_' + \
            self.language + '_' + \
            str(self.quality) + '_'+ \
            self.voice_acting + '.mp4' 

        return self.video.url '''   
    
    '''def save(self, *args, **kwargs):
        url = self.movie.url

        path = 'media\\movies\\'+url+'\\video'

        if not os.path.exists(path + '\\'+self.language) : 
            path = create_folder(path,self.language)
        if not os.path.exists( path + '\\'+str(self.quality)):
            path = create_folder(path,str(self.quality))
        if not os.path.exists(path + '\\'+self.voice_acting):
            path = create_folder(path,self.voice_acting)
        if not os.path.exists( path + '\\film'):
            path = create_folder(path,'film')

        super(Film, self).save(*args, **kwargs)

    def get_url(self):
        movie = self.movie.url

        path = os.path.join('media\\movies',movie.url,'video',self.language,str(self.quality),self.voice_acting,'film') + '\\'

        result = path  + movie.name + '_' + \
            'film_' + \
            self.language + '_' + \
            str(self.quality) + '_'+ \
            self.voice_acting + '.mp4'
        return self.video.url '''