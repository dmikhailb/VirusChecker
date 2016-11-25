from flask import Flask, request, jsonify, make_response, abort
from flask.ext.uploads import UploadSet, configure_uploads, ALL
import pyclamd
import os

cd = pyclamd.ClamdAgnostic()

app = Flask(__name__)
files = UploadSet('files', ALL)
app.config['UPLOADED_FILES_DEST'] = 'to_scan'
configure_uploads(app, files) 


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'file upload error'}), 400)



@app.route('/scanner/api/v1.0/file-scanner', methods = ['GET', 'POST'])
def file_scanner():
	if request.method == 'POST' and 'file_to_scan' in request.files:
		file_name = files.save(request.files['file_to_scan'])		
		test_results = cd.scan_file('/home/ubuntu/virus_scanner_v2/FlaskVirusChecker/to_scan/'+file_name)
		if test_results:
			os.remove('to_scan/'+file_name)
			return jsonify({"results" : test_results})

		else:
			os.remove('to_scan/'+file_name)
			return jsonify({"results" : "no viruses detected in file "+file_name})

	else:
		abort(400)	

if __name__ == '__main__':
    app.run(debug=True)
