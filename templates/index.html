from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        comment = request.form['comment']
        exec = request.form['exec']
        terminal = request.form['terminal']

        desktop_file_content = f"""
[Desktop Entry]
# Created by desktopfilecreator.com
Type=Application
Version=1.0
Name={name}
Comment={comment}
Path=
Exec={exec}
Terminal={terminal}
"""

        local_install_command = f"echo -e \"{desktop_file_content}\" > ~/.local/share/applications/{name}.desktop"
        system_install_command = f"echo -e \"{desktop_file_content}\" > /usr/local/share/applications/{name}.desktop"

        return render_template('install.html', name=name, comment=comment, exec=exec, terminal=terminal, desktop_file_content=desktop_file_content, local_install_command=local_install_command, system_install_command=system_install_command)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)