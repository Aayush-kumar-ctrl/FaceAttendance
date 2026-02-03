# FaceAttendance

FaceAttendance is a lightweight face-recognition-based attendance system. It detects faces from a camera or video, recognizes registered users, and records attendance automatically. The project is suitable for classrooms, small offices, or prototype demonstrations.

## Features
- Real-time face detection and recognition
- Record attendance with timestamp
- Add and manage registered users (face data)
- Save attendance logs (CSV or database)
- Configurable camera / video input

## Tech stack
- Python 3.8+
- OpenCV
- face_recognition (dlib-based) or alternative ML models
- NumPy, pandas
- Optional: Flask / FastAPI for a web UI (if included)

## Repository structure (example)
- data/               # folder for face images and datasets
- models/             # trained encodings or model weights
- src/                # main application source code
- utils/              # helper scripts (image preprocessing, I/O)
- attendance.csv      # output attendance log (or DB)
- requirements.txt    # Python dependencies
- README.md           # this file

> If your repository layout differs, update the structure above to match.

## Prerequisites
- Python 3.8 or later
- pip
- A webcam (or recorded video file) for testing
- (Optional) GPU and appropriate drivers if using heavy models

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/Aayush-kumar-ctrl/FaceAttendance.git
   cd FaceAttendance
   ```

2. Create a virtual environment and activate it:
   - Linux/macOS:
     ```
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```
     python -m venv venv
     venv\Scripts\Activate.ps1
     ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

If `requirements.txt` is missing, common dependencies include:
```
opencv-python
face_recognition
numpy
pandas
dlib
```
(Adjust versions per your project requirements.)

## Usage

1. Prepare dataset
   - Create a folder (e.g., `data/`) with subfolders or images for each person.
   - Name images clearly (e.g., `alice_01.jpg`, `bob_01.jpg`) or organize by person folder.

2. Generate face encodings (if applicable)
   ```
   python src/encode_faces.py --dataset data/ --encodings models/encodings.pickle
   ```
   Adjust script and flags to match the repository tooling.

3. Run the real-time attendance app
   ```
   python src/run_attendance.py --encodings models/encodings.pickle --output attendance.csv
   ```
   Replace script names and flags as appropriate.

4. Check `attendance.csv` for recorded entries:
   - Columns: `name`, `timestamp`, `status` (present / recognized), etc.

## Configuration
- Camera index: change the camera source (0 for default webcam)
- Recognition thresholds: adjust face distance or confidence threshold in config
- Output: change CSV path or set up a database (SQLite/Postgres) if desired

## Troubleshooting
- Low recognition rate: ensure good lighting, clear frontal faces, and enough training images per person.
- dlib/face_recognition install issues: follow official installation guides for your platform; on some systems you may need to install system libraries or use a prebuilt wheel.

## Tests
If you have tests, run them with:
```
pytest
```
(or the appropriate test runner configured for this repository)

## Contribution
Contributions are welcome. Suggested workflow:
1. Fork the repo
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Make changes and add tests
4. Open a pull request describing the changes

Please follow any project-specific contribution guidelines if present.

## License
Add your license here (e.g., MIT, Apache-2.0). If you don't have one yet, consider adding an open-source license to clarify usage rights.

## Author / Maintainer
Aayush-kumar-ctrl

## Contact
Open an issue or PR in this repository for questions, bug reports, or feature requests.
