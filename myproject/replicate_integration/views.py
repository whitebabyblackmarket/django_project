import os
import replicate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'replicate_integration/index.html')

def index(request):
    return render(request, 'frontend/index.html')

@csrf_exempt
def run_stable_diffusion(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt', 'a vision of paradise. unreal engine')
        height = int(request.POST.get('height', 768))
        width = int(request.POST.get('width', 768))
        negative_prompt = request.POST.get('negative_prompt', '')
        num_outputs = int(request.POST.get('num_outputs', 1))
        num_inference_steps = int(request.POST.get('num_inference_steps', 50))
        guidance_scale = float(request.POST.get('guidance_scale', 7.5))
        scheduler = request.POST.get('scheduler', 'DPMSolverMultistep')
        seed = request.POST.get('seed', 0)  # Default to 0 for random seed

        image = request.FILES.get('image')
        if image:
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_file_url = fs.url(filename)

            # Add the path of the uploaded file to your API input
            image_path = os.path.join(settings.MEDIA_ROOT, filename)
            # Now use `image_path` as the input to your API

        model = "stability-ai/stable-diffusion:ac732df83cea7fff18b8472768c88ad041fa750ff7682a21affe81863cbe77e4"
        result = replicate.run(
            model,
            input={
                "prompt": prompt,
                "height": height,
                "width": width,
                "negative_prompt": negative_prompt,
                "num_outputs": num_outputs,
                "num_inference_steps": num_inference_steps,
                "guidance_scale": guidance_scale,
                "scheduler": scheduler,
                "seed": seed
            }
        )

        return JsonResponse({'image_url': result[0]})
    else:
        return render(request, 'replicate_integration/index.html')
