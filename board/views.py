from django.shortcuts import render, redirect

# Create your views here.
from board.models import Board


def home(request):
    return render(request, "home.html")

def board(request):
    rsBoard = Board.objects.all()
    return render(request, "board_list.html", {
        'rsBoard': rsBoard
    })

def board_write(request):
    return render(request, "board_write.html",)

def board_insert(request):
    btitle = request.GET['b_title']
    bnote = request.GET['b_note']
    bwriter = request.GET['b_writer']

    if btitle != "":
        rows = Board.objects.create(b_title=btitle, b_note=bnote, b_writer=bwriter)
        return redirect('/board')
    else:
        return redirect('/board_write')

def board_view(request):
    bno = request.GET['b_no']
    rsDetail = Board.objects.filter(b_no=bno)

    return render(request, "board_view.html", {
        'rsDetail': rsDetail
    })

