import os
import time
import matplotlib.pyplot as plt

file_list = ['big_text.txt', 'MARBLES.bmp', 'RAY.bmp']
zip_file_name = 'file.zip'

if __name__ == "__main__":
    levels = list(range(10))
    real_time = []
    archive_size = []

    size_before_compression = 0
    for f in file_list:
        size_before_compression += os.path.getsize(f)
    print(f"Original size = {str(size_before_compression)} bytes")

    # run commands
    for level in levels:
        files = ' '.join(str(f) for f in file_list)
        command = 'zip -{} {} {}'.format(level, zip_file_name, files)

        t_ = time.time()
        os.system(command)
        t = time.time() - t_
        size_after_compression = os.path.getsize(zip_file_name)
        real_time.append(t)
        archive_size.append(size_after_compression)

    # remove zip file
    os.remove(zip_file_name)

    # plot figure
    fix, axs = plt.subplots(2)

    axs[0].plot(levels, real_time, 'bo-')
    axs[1].plot(levels, archive_size, 'ro-')

    axs[0].set_xticks(levels)
    axs[1].set_xticks(levels)

    axs[0].grid(True, which='both')
    axs[1].grid(True, which='both')

    axs[0].set_xlabel('Compression level')
    axs[1].set_xlabel('Compression level')

    axs[0].set_ylabel('Time [ms]')
    axs[1].set_ylabel('Archive size [byte]')

    plt.savefig('task4_3.png')





