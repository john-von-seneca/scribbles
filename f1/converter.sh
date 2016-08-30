echo $2
jupyter nbconvert --stdout --to html "$1/$2.ipynb" > "$1/$2.html"
sed s/.ipynb/.html/ "$1/$2.html" -i
