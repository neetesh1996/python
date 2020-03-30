from flask import Flask, render_template

app = Flask(__name__)
@app.route('/plot/')
def plot():
    from pandas_datareader import data
    import datetime
    from bokeh.plotting import figure,show, output_file
    from bokeh.embed import components
    from bokeh.resources import CDN


    start=datetime.datetime(2020,1,1)
    end=datetime.datetime(2020,3,24)

    df=data.DataReader(name="GOOG",data_source="yahoo",start=start,end=end)
    # type(df)
    # df

    # date_incease=df.index[df.Close > df.Open]
    # date_decrease=df.index[df.Close < df.Open]
    def inc_dec(c,o):
        if c > o:
            value="Incraese"
        elif c < o:
            value="Decrease"
        else :
            value="Equal"
        return value
    df["Status"]=[inc_dec(c,o) for c, o in zip(df.Close,df.Open)]
    df["Middle"]=(df.Open+df.Close)/2
    df["Height"]=abs(df.Open-df.Close)

    p=figure(x_axis_type='datetime', width=1000, height=300  ) #responsive=True, sizing_mode="scale_width"

    p.title.text = 'Candlestick Chart'
    p.grid.grid_line_alpha=0.5
    # type(p.title)
    hours_12=12*60*60*1000

    p.segment(df.index, df.High, df.index, df.Low, color="black")
    p.rect(df.index[df.Status=="Incraese"], df.Middle[df.Status=="Incraese"],
        hours_12,df.Height[df.Status=="Incraese"] ,fill_color="#CCFFFF",
        line_color="black")
    p.rect(df.index[df.Status=="Decrease"], df.Middle[df.Status=="Decrease"],
        hours_12,df.Height[df.Status=="Decrease"],fill_color="#FF3333",
        line_color="black")
    script1, div1=components(p)

    cdn_js=CDN.js_files[0]
    cdn_css=CDN.css_files
    # output_file('CS.html')
    # show(p)
    return render_template("plot.html",
    script1=script1,
    div1=div1,
    cdn_js=cdn_js,
    cdn_css=cdn_css,
    )
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True) 