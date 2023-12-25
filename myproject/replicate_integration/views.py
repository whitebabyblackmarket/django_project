import replicate
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_face_swap(request):
    print("Request received")
    if request.method == 'POST':
        fs = FileSystemStorage()

        source_image = request.FILES.get('source_image')
        target_image = request.FILES.get('target_image')
        source_image_url = request.POST.get('source_image_url', '')
        target_image_url = request.POST.get('target_image_url', '')
        prompt = request.POST.get('prompt', '')
        negative_prompt = request.POST.get('negative_prompt', '')

        if source_image and not source_image_url:
            source_filename = fs.save(source_image.name, source_image)
            source_image_url = fs.url(source_filename)

        if target_image and not target_image_url:
            target_filename = fs.save(target_image.name, target_image)
            target_image_url = fs.url(target_filename)

        if not source_image_url or not target_image_url:
            print("Source or target image not provided")
            return JsonResponse({'error': 'Source or target image not provided'}, status=400)

        num_inference_steps = int(request.POST.get('num_inference_steps', 4))

        input_data = {
            "source_image": source_image_url,
            "target_image": target_image_url,
            "prompt": prompt,
            "negative_prompt": negative_prompt,
            "num_inference_steps": num_inference_steps,
            "num_images_per_prompt": 1
        }

        model = "yan-ops/face_swap:1c128bbaa2b685bcee5378b39d079a2c52de358a54d6e432f5dc3d61689e9de3"

        try:
            result = replicate.run(model, input=input_data)
            print("API Call Successful:", result)

            if 'image' in result:
                return JsonResponse({'image_url': result['image']})
            else:
                print("No image key in result:", result)
                return JsonResponse({'error': 'No image key in result'}, status=500)
        except Exception as e:
            print("Error during API call:", e)
            return JsonResponse({'error': str(e)}, status=500)
    else:
        print("Non-POST request received")
        return HttpResponse(status=405)  # Method Not Allowed





