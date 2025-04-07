from flask import Flask, render_template, request, jsonify, session
from app.forms import ReleaseForm, TrackForm

from app import app


@app.route("/upload", methods=["GET", "POST"])
def index():
    release_form = ReleaseForm()
    track_form = TrackForm()

    # Проверяем, если в сессии уже есть список треков, то используем его
    if 'track_list' not in session:
        session['track_list'] = []

    if request.method == "POST":
        # Сохраняем данные релиза или другие действия
        pass

    return render_template("upload.html", release_form=release_form, track_form=track_form, track_list=session['track_list'])


@app.route("/add_track", methods=["POST"])
def add_track():
    form = TrackForm()
    if form.validate_on_submit():
        track_data = {
            "title": form.track_title.data,
            "version": form.version.data,
            "artists": form.artists.data,
            "composer": form.composer.data,
            "authors": form.authors.data,
            "explicit": form.explicit.data
        }

        # Добавляем новый трек в список для текущей сессии
        if 'track_list' not in session:
            session['track_list'] = []
        session['track_list'].append(track_data)

        # Сохраняем изменения в сессии
        session.modified = True

        return jsonify({"status": "success", "track": track_data})
    return jsonify({"status": "error", "errors": form.errors})