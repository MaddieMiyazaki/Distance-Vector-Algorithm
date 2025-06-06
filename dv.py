from flask import Flask,request, render_template
from algorithm_func import DV,nodes_list,list_to_tuple,repopulate

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/tables',methods=['GET','POST'])
def tables():
    if request.method == "POST":

        input_list = request.form.getlist("dynamic_input")
        populate_links=repopulate(input_list)

        directed=request.form.get('directed')
        input_tuples=list_to_tuple(input_list,directed)

        initial=DV(input_tuples)[0]
        answer=DV(input_tuples)[1:]
        node_list=nodes_list(input_tuples)

        return render_template("tables.html",populate_links=populate_links,directed=directed,table_headers=node_list,initial=initial,answer=answer,zip=zip,len=len)
    return render_template('index.html')

# for running locally
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)