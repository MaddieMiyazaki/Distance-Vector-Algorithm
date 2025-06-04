from flask import Flask,request, render_template
from algorithm_func import DV,nodes_list,list_to_tuple

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/tables',methods=['GET','POST'])
def tables():
    initial = ''
    node_list = ''
    answer=''
    if request.method == "POST":
        input_list = request.form.getlist("dynamic_input")
        directed=request.form.get('directed')
        input_tuples=list_to_tuple(input_list,directed)
        print(input_tuples)

        initial=DV(input_tuples)[0]
        answer=DV(input_tuples)[1:]
        node_list=nodes_list(input_tuples)

    return render_template("tables.html",table_headers=node_list,initial=initial,answer=answer,zip=zip,len=len)


if __name__ == '__main__':
    app.run(debug=True)