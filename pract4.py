import os
import time
import multiprocessing
from PIL import Image

def process_image(args):
    input_path, output_path = args
    img = Image.open(input_path)
    img = img.rotate(90, expand=True)
    img = img.resize((800, 600), Image.LANCZOS)
    img = img.convert('L')
    img.save(output_path, 'JPEG')
    return True

def sequential_processing(input_files, output_dir):
    tasks = [(input_files[i], os.path.join(output_dir, f"out_{i}.jpg")) for i in range(len(input_files))]
    
    start = time.time()
    for task in tasks:
        process_image(task)
    return time.time() - start

def parallel_processing(input_files, output_dir):
    tasks = [(input_files[i], os.path.join(output_dir, f"out_{i}.jpg")) for i in range(len(input_files))]
    
    start = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(process_image, tasks)
    return time.time() - start

def create_test_images(num_images=10):
    os.makedirs("test_images", exist_ok=True)
    for i in range(num_images):
        img = Image.new('RGB', (1920, 1080), color=(i*25%255, i*50%255, i*75%255))
        img.save(f"test_images/img_{i}.jpg")

def main():
    create_test_images(20)
    os.makedirs("processed", exist_ok=True)
    
    input_files = [os.path.join("test_images", f) for f in os.listdir("test_images") if f.endswith(".jpg")]
    input_files.sort()
    
    print(f"Обработка {len(input_files)} изображений")
    
    seq_time = sequential_processing(input_files, "processed")
    print(f"Последовательно: {seq_time:.4f} сек")
    
    for f in os.listdir("processed"):
        os.remove(os.path.join("processed", f))
    
    par_time = parallel_processing(input_files, "processed")
    print(f"Параллельно: {par_time:.4f} сек")
    print(f"Ускорение: {seq_time/par_time:.2f}x")

if __name__ == "__main__":
    main()