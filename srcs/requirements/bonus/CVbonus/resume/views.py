from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import template

def resume(request):
    return HttpResponse("""<html>
    <head> 
        <title> Khubieva Zukhra </title>
    </head>
    <style>
        ul{
            color: gray;
        }
        table{
            border-collapse: collapse;
        }
        th{
            width: 150px;
            padding: 0;
            border:1px solid rgb(1, 81, 255);
        }
        td{
            width: 150px;
            padding: 0;
            border:1px solid rgb(0, 81, 255);
        }
    </style>
    <body>
        <h1> CV Khubieva Zukhra </h1>
        <p align=right> <font face="Segoe Print", size=3, color=black> &#128205; Kazan</font> </p>
        <p align=right> <font face="Segoe Print", size=3, color=black> &#128231; mskeleto@student.21-school.ru </font> </p>
        <p align=right> <font face="Segoe Print", size=3, color=black> &#128222; +7 212 12-1212121 </font> </p>
        <p align=center> <font face="Segoe Print", size=3, color=black> Analitycs intern </font> </p>
        
        <h3>Skills</h3>
        <table>
            <tr>
                <th> Programming Languages </th>
                <th> Level </th>
            </tr>
            <tr>
                <td>Python</td>
                <td>&#9733;&#9733;&#9733;&#9733;&#9733;</td>
            </tr>
            <tr>
                <td>C++</td>
                <td style="border-bottom-color: #424242"> &#9733;&#9733;&#9733;&#9733;&#9734;</td>
            </tr>
            <tr>
                <td style="border-right-color: #424242">C</td>
                <td style="border-color: #424242" >&#9733;&#9733;&#9733;&#9733;&#9733;</td>
            </tr>
        </table>

        <h3> Work Expirience </h3>
        <ul style="color: black">
            <li> Minion C Programmer - School21</li>
            <ul>
                <li> Kazan, Russia</li>
                <li> 2020-2022</li>
            </ul>
        </ul>

        <h3>Education</h3>
        <ol>
            <li> Bachelor in Infocom Technologies and Communication Systems</li>
            <ul>
	            <li> Kazan National Research Technical University
named after A. N. Tupolev - KAI</li>
                <li> Kazan, Russia</li>
                <li> 2020 - 2021 </li>
            </ul>
            <li> Bachelor in IT and Computer Science</li>
            <ul>
	            <li> Kazan State Power Engineering University</li>
                <li> Kazan, Russia</li>
                <li> 2019 - 2020 </li>
            </ul>
            <li> Bachelor in Applied Informatics</li>
            <ul>
	            <li> North-Caucasus Federal University</li>
                <li> Stavropol, Russia</li>
                <li> 2017 - 2019 </li>
            </ul>
        </ol>
    </body>
</html>""")


