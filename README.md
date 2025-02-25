git clone https://github.com/lucas-vallery/vision.git
git submodule init
git submodule update

## On Linux machine
python3 -m venv env
source env/bin/activate
pip install -r ./yolov5/requirements.txt

## On Windows machine
python3 -m venv env
.\env\Scripts\activate
pip install -r ./yolov5/requirements.txt