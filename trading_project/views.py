from django.http import JsonResponse

# Health check view
def health_check(request):
    try:
        # Check if the database is accessible by running a simple query
        SomeModel.objects.exists()
        db_status = "Database is connected"
    except Exception as e:
        db_status = f"Database connection error: {str(e)}"
    
    return JsonResponse({
        'status': 'OK',
        'message': 'Django backend is reachable.',
        'db_status': db_status,
    })