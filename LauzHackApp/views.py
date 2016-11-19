from django.shortcuts import render


def index(request):
	return render(request, 'LauzHackApp/chooseYourType.html', {})
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
def pickVideo(request):
    return render(request, 'LauzHackApp/pickVideo', {})    

def pickChannel(request):
    return render(request, 'LauzHackApp/pickChannel',{})


def youWatch(request):
	context = {}

	v = request.POST["videoLink"]
	
	context["video_link"] = ("https://www.youtube.com/embed/" + v.split("=")[1] + "?rel=0")

	return render(request, 'LauzHackApp/youWatch.html', context)

def youAre(request):



    return render(request, 'LauzHackApp/youAre.html', {})