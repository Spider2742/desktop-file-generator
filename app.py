from flask import Flask, request, send_file
import os

app = Flask(__name__, static_folder='build')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        exec = request.form['exec']
        icon = request.form['icon']
        terminal = request.form['terminal']
        categories = request.form.getlist('categories')

        categories_string = ""
        for category in categories:
            if category == "1":
                categories_string += "Game;"
            elif category == "2":
                categories_string += "Application;"
            elif category == "3":
                categories_string += "Utility;"
            elif category == "4":
                categories_string += "Education;"
            elif category == "5":
                categories_string += "Settings;"
            elif category == "6":
                categories_string += "Other;"

        desktop_file_content = f"""
[Desktop Entry]
Version=1.0
Name={name}
Comment={comment}
Exec={exec}
Icon={icon}
Terminal={terminal}
Type=Application
Categories={categories_string}
"""

        with open('temp.desktop', 'w') as f:
            f.write(desktop_file_content)

        return send_file('temp.desktop', as_attachment=True, download_name=f'{name}.desktop')

    return '''
        <form action="" method="post">
            <label for="name">Name:</label><br>
            <input type="text" id="name" name="name"><br>
            <label for="comment">Comment:</label><br>
            <input type="text" id="comment" name="comment"><br>
            <label for="exec">Executable path:</label><br>
            <input type="text" id="exec" name="exec"><br>
            <label for="icon">Icon path:</label><br>
            <input type="text" id="icon" name="icon"><br>
            <label for="terminal">Open in terminal:</label><br>
            <input type="radio" id="true" name="terminal" value="true">
            <label for="true">True</label><br>
            <input type="radio" id="false" name="terminal" value="false">
            <label for="false">False</label><br>
            <label for="categories">Categories:</label><br>
            <input type="checkbox" id="1" name="categories" value="1">
            <label for="1">Game</label><br>
            <input type="checkbox" id="2" name="categories" value="2">
            <label for="2">Application</label><br>
            <input type="checkbox" id="3" name="categories" value="3">
            <label for="3">Utility</label><br>
            <input type="checkbox" id="4" name="categories" value="4">
            <label for="4">Education</label><br>
            <input type="checkbox" id="5" name="categories" value="5">
            <label for="5">Settings</label><br>
            <input type="checkbox" id="6" name="categories" value="6">
            <label for="6">Other</label><br>
            <input type="submit" value="Create .desktop file">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)