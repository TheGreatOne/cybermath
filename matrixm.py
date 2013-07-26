from bottle import route, run, request, post, redirect, template



@route("/invalid")
def invalid():
    return '''<html><head><title>Matrix Calculator</title></head><body>Invalid matrixies! <a href="mm"><button>Go Back To Beginning</button></a><footer>
    <a href="http://validator.w3.org/check/referer">
    <strong> HTML </strong> Valid! </a>
    <a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
    <strong> CSS </strong> Valid! </a>
    </footer></body></html>'''


@route("/mm")
def mm():
    return '''<html><head><title>Matrix Calculator</title></head><body><form id="form">
            First Matrix ("A"):
            <br>Rows:<input name="A Rows" type="text" tabindex=1 />
            Columns:<input name="A Columns" type="text" tabindex=2 />
            <button form="form" formmethod="post" formaction="/mam/tr" tabindex=8>Transpose A</button>
            <br>
            Second Matrix ("B"):
            <br>Rows:<input name="B Rows" type="text" tabindex=3 />
            Columns:<input name="B Columns" type="text" tabindex=4 />
            <br>
            <button form="form" formmethod="post" formaction="/mam/me" tabindex=5>Multiply</button>
            <button form="form" formmethod="post" formaction="/mam/ad" tabindex=6>Add</button>
            <button form="form" formmethod="post" formaction="/mam/su" tabindex=7>Subtract</button>
          </form><footer>
          <a href="http://validator.w3.org/check/referer">
          <strong> HTML </strong> Valid! </a>
          <a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
          <strong> CSS </strong> Valid! </a>
          </footer></body></html>'''


@post("/mam/<operation>")
def mam(operation):
    A_R = request.forms.get('A Rows')
    A_C = request.forms.get('A Columns')
    if operation == "tr":
        b = int(A_R) * int(A_C) + 1
        a = '''<form id="form">
            First Matrix ("A"):
            <br>Rows:<input name="A Rows" type="text" value="''' + A_R + '''" tabindex=''' + str(b+1) + ''' />
            Columns:<input name="A Columns" type="text" value="''' + A_C + '''" tabindex=''' + str(b+2) + ''' />
            <button form="form" formmethod="post" formaction="/mam/tr" tabindex=''' + str(b+8) + '''>Transpose A</button>
            <br>
            Second Matrix ("B"):
            <br>Rows:<input name="B Rows" type="text" tabindex=''' + str(b+3) + ''' />
            Columns:<input name="B Columns" type="text" tabindex=''' + str(b+4) + ''' />
            <br>
            <button form="form" formmethod="post" formaction="/mam/me" tabindex=''' + str(b+5) + '''>Multiply</button>
            <button form="form" formmethod="post" formaction="/mam/ad" tabindex=''' + str(b+6) + '''>Add</button>
            <button form="form" formmethod="post" formaction="/mam/su" tabindex=''' + str(b+7) + '''>Subtract</button>
          </form><hr>A Values: <br><form method="POST" action="/''' + operation + '/' + A_R + "/" + A_C + '">'
        i = 1
        for x in range(int(A_R)):
            for y in range(int(A_C)):
                a += '''<input name="A''' + str(y) + str(x) + '''" type="text" tabindex=''' + str(i) + ''' />'''
                i += 1
        a = a + "<br>"
        a += '''<input type="submit" tabindex=''' + str(i) + ''' /></form>'''
    else:
        B_R = request.forms.get('B Rows')
        B_C = request.forms.get('B Columns')
        if (A_C != B_R) and ((B_C != '1') or (B_R != '1')) and (operation == "me"):
            redirect("/invalid")
        if ((operation == "ad") or (operation == "su")) and ((A_R != B_R) or (A_C != B_C)):
            redirect("/invalid")
        b = (int(A_R) * int(A_C)) + (int(B_R) * int(B_C)) + 1
        a = '''<form id="form">
                First Matrix ("A"):
                <br>Rows:<input name="A Rows" type="text" value="''' + A_R + '''" tabindex=''' + str(b+1) + ''' />
                Columns:<input name="A Columns" type="text" value="''' + A_C + '''" tabindex=''' + str(b+2) + ''' />
                <button form="form" formmethod="post" formaction="/mam/tr" tabindex=''' + str(b+8) + '''>Transpose A</button>
                <br>
                Second Matrix ("B"):
                <br>Rows:<input name="B Rows" type="text" value="''' + B_R + '''" tabindex=''' + str(b+3) + ''' />
                Columns:<input name="B Columns" type="text" value="''' + B_C + '''" tabindex=''' + str(b+4) + ''' />
                <br>
                <button form="form" formmethod="post" formaction="/mam/me" tabindex=''' + str(b+5) + '''>Multiply</button>
                <button form="form" formmethod="post" formaction="/mam/ad" tabindex=''' + str(b+6) + '''>Add</button>
                <button form="form" formmethod="post" formaction="/mam/su" tabindex=''' + str(b+7) + '''>Subtract</button>
              </form><hr>A Values: <br><form method="POST" action="/''' + operation + '/' + A_R + "/" + A_C + "/" + B_R + "/" + B_C + '">'
        i = 1
        for x in range(int(A_R)):
            for y in range(int(A_C)):
                a += '''<input name="A''' + str(y) + str(x) + '''" type="text" tabindex=''' + str(i) + ''' />'''
                i += 1
            a = a + "<br>"
        a = a + "B Values: <br>"
        for x in range(int(B_R)):
            for y in range(int(B_C)):
                a += '''<input name="B''' + str(y) + str(x) + '''" type="text" tabindex=''' + str(i) + ''' />'''
                i += 1
            a = a + "<br>"
        a += '<input type="submit" tabindex=' + str(i) + ' /></form>'
    return '''<html><head><title>Matrix Calculator</title></head><body>''' + a + '''<footer>
            <a href="http://validator.w3.org/check/referer">
            <strong> HTML </strong> Valid! </a>
            <a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
            <strong> CSS </strong> Valid! </a>
            </footer></body></html>'''


@post("/tr/<A_R>/<A_C>")
def tr(A_R, A_C):
    A = []
    for r in range(int(A_C)):
        A.append([])
        for c in range(int(A_R)):
            a = request.forms.get("A" + str(r) + str(c))
            if float(a) == float(a) // 1:
                A[r].append(int(a))
            else:
                A[r].append(float(a))
    b = []
    for r in range(int(A_C)):
        b.append([])
        for c in range(int(A_R)):
            b[r].append(A[r][c])
    return template("boxtemplate", a=A, A=b, B=None, operation="tr")


@post("/ad/<A_R>/<A_C>/<B_R>/<B_C>")
def ad(A_R, A_C, B_R, B_C):
    A = []
    C = []
    for r in range(int(A_C)):
        A.append([])
        for c in range(int(A_R)):
            a = request.forms.get("A" + str(r) + str(c))
            if float(a) == float(a) // 1:
                A[r].append(int(a))
            else:
                A[r].append(float(a))
        C.append(A[r][:])
    B = []
    for r in range(int(B_C)):
        B.append([])
        for c in range(int(B_R)):
            a = request.forms.get("B" + str(r) + str(c))
            if float(a) == float(a) // 1:
                B[r].append(int(a))
            else:
                B[r].append(float(a))
    for r in range(int(A_C)):
        for c in range(int(A_R)):
            A[r][c] += B[r][c]
    return template("boxtemplate", a=A, A=C, B=B, operation="ad")


@post("/su/<A_R>/<A_C>/<B_R>/<B_C>")
def su(A_R, A_C, B_R, B_C):
    A = []
    C = []
    for r in range(int(A_C)):
        A.append([])
        for c in range(int(A_R)):
            a = request.forms.get("A" + str(r) + str(c))
            if float(a) == float(a) // 1:
                A[r].append(int(a))
            else:
                A[r].append(float(a))
        C.append(A[r][:])
    B = []
    for r in range(int(B_C)):
        B.append([])
        for c in range(int(B_R)):
            a = request.forms.get("B" + str(r) + str(c))
            if float(a) == float(a) // 1:
                B[r].append(int(a))
            else:
                B[r].append(float(a))
    for r in range(int(A_C)):
        for c in range(int(A_R)):
            A[r][c] -= B[r][c]
    return template("boxtemplate", a=A, A=C, B=B, operation="su")


@post("/me/<A_R>/<A_C>/<B_R>/<B_C>")
def me(A_R, A_C, B_R, B_C):
    mat = []
    A = []
    C = []
    for r in range(int(A_C)):
        A.append([])
        for c in range(int(A_R)):
            a = request.forms.get("A" + str(r) + str(c))
            if float(a) == float(a) // 1:
                A[r].append(int(a))
            else:
                A[r].append(float(a))
        C.append(A[r][:])
    B = []
    for r in range(int(B_C)):
        B.append([])
        for c in range(int(B_R)):
            a = request.forms.get("B" + str(r) + str(c))
            if float(a) == float(a) // 1:
                B[r].append(int(a))
            else:
                B[r].append(float(a))
    if B_R == '1' and B_C == '1':
        for r in range(int(A_C)):
            for c in range(int(A_R)):
                A[r][c] *= B[0][0]
    else:
        for ar in range(int(A_R)):
            mat.append([])
            for bc in range(int(B_C)):
                mat[ar].append([])
                a = 0
                for ac in range(int(A_C)):
                    a += A[ac][ar] * B[bc][ac]
                mat[ar][bc] = a
        A = mat
    return template("boxtemplate", a=A, A=C, B=B, operation="me")

run(server='gae')