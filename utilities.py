import os
import gzip
import shutil

def recursive_unzip(in_dir):
    for root, dirs, files in os.walk(in_dir):
        path = root.split(os.sep)
        #print((len(path) - 1) * '---', os.path.basename(root))
        for f in files:
            if f.endswith(".gz"):
                print("/".join(path) + "/" + f)

                full_path = "/".join(path) + "/" + f

                inF = gzip.GzipFile(full_path, 'rb')
                s = inF.read()
                inF.close()

                os.remove(full_path)

                out_path = "".join(list(full_path)[:-3])
                print(out_path)
                outF = open(out_path, 'wb')
                outF.write(s)
                outF.close()

    return

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)

def recursive_copy(pattern, in_dir, out_dir):
    count = 0
    for root, dirs, files in os.walk(in_dir):
        path = root.split(os.sep)
        #print((len(path) - 1) * '---', os.path.basename(root))
        for f in files:
            print(f)
            if pattern in f and "data" in f:
                print("/".join(path) + "/" + f)

                full_path = "/".join(path) + "/" + f

                dst = out_dir + "/" + str(count) + "_" + str(full_path.split("/")[-1])
                count += 1
                print(dst)

                shutil.copy2(full_path, dst)

    return

# recursive_unzip("data/")
recursive_copy("accelerometer", "data/", "final/")