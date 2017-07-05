from scipy import io
import json

def save_json(filename, py_dict):

    with open(filename, 'w') as f:
        json.dump(py_dict, f)

def mat2json(mat_file, json_file):
    a = io.loadmat(mat_file, variable_names=None, mat_dtype=True)
    y = a["data"]["y"][0, 0][0]
    x = a["data"]["x"][0, 0][0]
    names = a["data"]["names"][0,0]
    names = [str(name.replace(" ", "")) for name in names]
    orbit = {}
    for i in range(len(x)):
        orbit[names[i]] = [float(x[i]/1000.), float(y[i]/1000.)]
    #print(orbit)
    save_json(json_file, orbit)
    
    

if __name__ == "__main__":
    mat2json(mat_file="2017-05-03-004109_terrific_exponential_gain_at_6GeV.mat", json_file="expon_gain.json")
   