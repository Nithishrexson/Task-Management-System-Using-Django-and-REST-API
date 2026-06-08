from django.shortcuts import render,redirect
import requests
import json

# Create your views here.

def home(request):
    api = 'http://127.0.0.1:8000/api/tasks/'
    resp = requests.get(url = api)
    print(resp.json())
    py_data = resp.json()
    return render(request,'home.html',{'data':py_data})

def add(request):
    api = 'http://127.0.0.1:8000/api/tasks/'
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']

        # print(title_data,desc_data)
        py_data = {
            'title':title_data,
            'desc' : desc_data
        }
        json_data = json.dumps(py_data)
        # print(json_data)
        # print(type(json_data))

        resp = requests.post(url = api,data = json_data)
        # print(resp)
        return redirect('home')
    return render(request,'add.html')

def complete(request):
    return render(request,'complete.html')

def trash(request):
    return render(request,'trash.html')

def support(request):
    return render(request,'support.html')


def update(request,pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    resp = requests.get(url =api)
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']
        py_data = {
            'title' : title_data,
            'desc' : desc_data,
        }
        json_data = json.dumps(py_data)
        resp = requests.put(url = api , data = json_data)
        
        return redirect(home)
    return render(request,'update.html',{'data':resp.json()})


def delete(request,pk):
    api = f'http://127.0.0.1:8000/api/task/{pk}'
    resp = requests.delete(url=api)
    return redirect('home')



about_page = [


{
    'id': 1,

    'title': 'About Our To-Do Management System',

    'desc': 'Welcome to our Task Management System, a modern web application designed to help users organize and manage daily tasks efficiently. The platform allows users to create, update, and delete tasks through a simple and user-friendly interface. By providing an organized workflow, our system helps users stay productive and manage their activities effectively.'
},

{
    'id': 2,

    'title': 'About The Developer',

    'desc': 'Hello, I’m Nithish Rexson, an MCA graduate and aspiring Python Full Stack Developer with a strong interest in Django web development and modern web technologies. I developed this To-Do Management System as a practical project to strengthen my skills in Python, Django, API integration, frontend development, and database management. Through this project, I gained hands-on experience in building and connecting frontend and backend applications.'
},

{
    'id': 3,

    'title': 'Our Mission',

    'desc': 'Our mission is to provide a simple and efficient task management platform that helps users organize their daily activities and improve productivity. We aim to create a clean and intuitive user experience while utilizing modern web development practices and technologies.'
},

{
    'id': 4,

    'title': 'Features We Provide',

    'desc': 'Our Task Management System provides essential task management features including task creation, task updating, task deletion, user authentication, and API-based communication between frontend and backend applications. The system is designed to offer smooth navigation, organized task management, and an attractive user interface.'
},

{
    'id': 5,

    'title': 'Why Choose Our Platform',

    'desc': 'Our platform is built using Django, Python, HTML, CSS, and API integration techniques to deliver reliable performance and an easy-to-use experience. We focus on simplicity, efficiency, and scalability while continuously improving the application through modern development practices and user-centered design.'
}


]


def about(request):

    return render(
        request,
        'about.html',
        {'about_page': about_page}
    )





support_page = [


{
    'id': 1,

    'title': 'Customer Support',

    'desc': 'Our support team is committed to helping users resolve any issues related to task management, account access, and application functionality. We strive to provide timely assistance and ensure a smooth user experience throughout the platform.'
},

{
    'id': 2,

    'title': 'Technical Assistance',

    'desc': 'If you experience technical issues such as login problems, task synchronization errors, page loading issues, or unexpected application behavior, our technical support resources are available to help identify and resolve the problem efficiently.'
},

{
    'id': 3,

    'title': 'Frequently Asked Questions',

    'desc': 'Users can find answers to common questions regarding account management, task creation, task updates, task deletion, and application usage. Our goal is to make the platform easy to understand and use for all users.'
},

{
    'id': 4,

    'title': 'Feedback and Suggestions',

    'desc': 'We value user feedback and continuously work to improve the platform. Users are encouraged to share suggestions, feature requests, and ideas that can help enhance the overall functionality and user experience of the application.'
},

{
    'id': 5,

    'title': 'Our Commitment',

    'desc': 'We are dedicated to providing a reliable, secure, and user-friendly task management platform. Our team continuously monitors and improves the application to ensure stability, performance, and a positive experience for all users.'
}


]



def support(request):

    return render(
        request,
        'support.html',
        {'support_page': support_page}
    )
