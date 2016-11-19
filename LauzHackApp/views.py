from django.shortcuts import render

def index(request):
	return render(request, 'LauzHackApp/seeThroughMe.html')
'''
if request.method == 'POST':
        if 'url' in request.POST:
            url = request.POST['url']
            videos = Video.objects.filter(url=url).all()
            if len(videos) > 0:
                video = videos[0]
            else:
                # Call to Youtube API
                # length = ...
                video = Video(url, length)
                video.save()

            return render(request, 'video.html')
            '''
def youWatch(request):
	return render(request, 'LauzHackApp/youWatch.html')