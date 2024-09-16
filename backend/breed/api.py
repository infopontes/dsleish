from ninja import Router

router = Router()


@router.get("/list_breed")
def list_breed(request):
    '''
        http://localhost:8000/api/breed/list_breed
    '''
    return {"message": "Hello from App Breed"}
