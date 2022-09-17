from django.shortcuts import render

def Form_Interface(request):
    return render(request,'FormInterface.html')

def Submit_Form(request):
  name = request.GET['yourname']
  email = request.GET['youremail']
  contact = request.GET['contact']
  fathername = request.GET['fathername']
  address = request.GET['address']
  residance = request.GET['residance']
  dob = request.GET['dob']
  lang = request.GET['lang']
  gb = request.GET['gb']
  gm = request.GET['gm']
  gp = request.GET['gp']
  gs = request.GET['gs']
  tb = request.GET['tb']
  tm = request.GET['tm']
  tp = request.GET['tp']
  ts = request.GET['ts']
  tvb = request.GET['tvb']
  tvm = request.GET['tvm']
  tvp = request.GET['tvp']
  tvs = request.GET['tvs']
  projetcs = request.GET['projects']
  skills = request.GET['skills']
  achievements = request.GET['achievements']
  return render(request, 'CV.html', {'name':name, 'email':email,'contact':contact,'dob' : dob, 'lang' : lang, 'address' : address, 'fathername' : fathername, 'residance' : residance,'gp':gp,'gs':gs,'gm':gm,'gb':gb,'tb':tb,'tp':tp,'tm':tm,'ts':ts,'tvb':tvb,'tvm':tvm,'tvp':tvp,'tvs':tvs,'projetcs' : projetcs, 'skills' : skills, 'achievements' : achievements})