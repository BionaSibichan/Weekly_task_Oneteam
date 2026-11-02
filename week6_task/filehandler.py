import pickle

def read_log_file(filename):
    try:
        f = open(filename,"r")
        lines = f.readlines()
        f.close()
        return lines
    except FileNotFoundError:
        print("Error: could not find file",filename)
        return []
    except Exception as e:
        print("something went wrong while reading file:",e)
        return []

def write_invalid_records(filename,records):
    try:
        f = open(filename,"w")
        for line in records:
            if not line.endswith("\n"):
                line = line+"\n"
            f.write(line)
        f.close()
    except Exception as e:
        print("error while writing invalid records:",e)

def save_pickle(filename,data):
    try:
        f = open(filename,"wb")
        pickle.dump(data,f)
        f.close()
    except Exception as e:
        print("error while saving pickle file:",e)

def load_pickle(filename):
    try:
        f = open(filename,"rb")
        data = pickle.load(f)
        f.close()
        return data
    except FileNotFoundError:
        print("Error: pickle file not found")
        return []
    except Exception as e:
        print("error while loading pickle file:",e)
        return []