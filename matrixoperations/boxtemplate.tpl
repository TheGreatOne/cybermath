<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Matrix Calculator</title>
<style type="text/css">
td.a {
    border: 1px dotted #777;
}
html {
  background-color: #FFD;
}
div {
  border-radius: 25px;
  border: 1px solid #888;
  padding-left: 15px;
  background-color: #DDE;
  text-align: left;
}
body {
  text-align: center;
}
</style>
</head>
<body>
<div>
%A_C = str(len(A))
%A_R = str(len(A[0]))
%if B == None:
%    b = int(A_R) * int(A_C) + 1
    <form id="form">
        First Matrix ("A"):
        <br>Rows:<input name="A Rows" type="text" value="{{A_R}}" tabindex={{b+1}} />
        Columns:<input name="A Columns" type="text" value="{{A_C}}" tabindex={{b+2}} />
        <button form="form" formmethod="post" formaction="/mam/tr" tabindex={{b+8}}>Transpose A</button>
        <br>
        Second Matrix ("B"):
        <br>Rows:<input name="B Rows" type="text" tabindex={{b+3}} />
        Columns:<input name="B Columns" type="text" tabindex={{b+4}} />
        <br>
        <button form="form" formmethod="post" formaction="/mam/me" tabindex={{b+5}}>Multiply</button>
        <button form="form" formmethod="post" formaction="/mam/ad" tabindex={{b+6}}>Add</button>
        <button form="form" formmethod="post" formaction="/mam/su" tabindex={{b+7}}>Subtract</button>
    </form><hr>A Values: <br><form method="POST" action="/{{operation}}/{{A_R}}/{{A_C}}">
%    i = 1
%    for x in range(int(A_R)):
%        for y in range(int(A_C)):
            <input name="A{{y}}{{x}}" type="text" value="{{A[y][x]}}" tabindex={{i}} />
%            i += 1
%        end
        <br>
%    end
    <input type="submit" tabindex={{i}} /></form>
%else:
%    B_C = str(len(B))
%    B_R = str(len(B[0]))
%    b = (int(A_R) * int(A_C)) + (int(B_R) * int(B_C)) + 1
    <form id="form">
        First Matrix ("A"):
        <br>Rows:<input name="A Rows" type="text" value="{{A_R}}" tabindex={{b+1}} />
        Columns:<input name="A Columns" type="text" value="{{A_C}}" tabindex={{b+2}} />
        <button form="form" formmethod="post" formaction="/mam/tr" tabindex={{b+8}}>Transpose A</button>
        <br>
        Second Matrix ("B"):
        <br>Rows:<input name="B Rows" type="text" value="{{B_R}}" tabindex={{b+3}} />
        Columns:<input name="B Columns" type="text" value="{{B_C}}" tabindex={{b+4}} />
        <br>
        <button form="form" formmethod="post" formaction="/mam/me" tabindex={{b+5}}>Multiply</button>
        <button form="form" formmethod="post" formaction="/mam/ad" tabindex={{b+6}}>Add</button>
        <button form="form" formmethod="post" formaction="/mam/su" tabindex={{b+7}}>Subtract</button>
    </form><hr>A Values: <br><form method="POST" action="/{{operation}}/{{A_R }}/{{A_C}}/{{B_R}}/{{B_C}}">
%    i = 1
%    for x in range(int(A_R)):
%        for y in range(int(A_C)):
            <input name="A{{y}}{{x}}" type="text" value="{{A[y][x]}}" tabindex={{i}} />
%            i += 1
%        end
%    end
    <br>
    B Values: <br>
%    for x in range(int(B_R)):
%        for y in range(int(B_C)):
            <input name="B{{y}}{{x}}" type="text" value="{{B[y][x]}}" tabindex={{i}} />
%            i += 1
%        end
        <br>
%    end
    <input type="submit" tabindex={{i}} /></form>
%end
<hr><table>
%for i in range(len(a)):
    <tr>
%    for o in a[i]:
        <td class="a">{{o}}</td>
%    end
    </tr>
%end
</table>

<hr>
<a href="/mm"><button>Go Back To Beginning</button></a></div>
<footer>
<a href="http://validator.w3.org/check/referer">
<strong> HTML </strong> Valid! </a>
<a href="http://jigsaw.w3.org/css-validator/check/referer?profile=css3">
<strong> CSS </strong> Valid! </a>
</footer>
</body></html>
