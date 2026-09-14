import time

def demonstrate_performance_footprints():
    """Döngülerin performans üzerindeki izlerini gösterir."""
    print("--- Performans İzleri (Performance Footprints) ---")
    iterations = 1_000_000

    # For döngüsü ile performans izi
    start_time = time.perf_counter()
    data_for = []
    for i in range(iterations):
        data_for.append(i * 2) # Basit bir işlem
    end_time = time.perf_counter()
    # Döngünün sistemde bıraktığı performans izi
    print(f"For döngüsü ile {iterations} işlem: {end_time - start_time:.4f} saniye")

    # While döngüsü ile performans izi
    start_time = time.perf_counter()
    data_while = []
    i = 0
    while i < iterations:
        data_while.append(i * 2) # Basit bir işlem
        i += 1
    end_time = time.perf_counter()
    # Döngünün sistemde bıraktığı performans izi
    print(f"While döngüsü ile {iterations} işlem: {end_time - start_time:.4f} saniye")

    print("\nFarklı döngü türleri ve içindeki işlemler, sisteminizde farklı performans izleri bırakır.")

def demonstrate_data_integrity_footprints():
    """Döngülerin veri bütünlüğü ve uygulama durumu üzerindeki izlerini gösterir."""
    print("\n--- Veri Bütünlüğü ve Durum İzleri (Data Integrity and State Footprints) ---")

    original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Başlangıçtaki sayılar: {original_numbers}") # Döngü öncesi veri durumu

    # Döngü, verileri filtreleyip dönüştürerek yeni bir 'ayak izi' bırakır
    processed_numbers = []
    for num in original_numbers:
        if num % 2 == 0: # Çift sayıları kontrol et
            processed_numbers.append(num * 10) # Çift sayıları dönüştür
        else:
            processed_numbers.append(num) # Tek sayıları olduğu gibi bırak

    # Döngü sonrası verinin yeni durumu, döngünün bıraktığı iz
    print(f"Döngü sonrası işlenmiş sayılar: {processed_numbers}")

    # Başka bir örnek: Paylaşılan bir sayacı değiştirme
    global_counter = 0
    print(f"\nDöngü öncesi global_counter: {global_counter}") # Döngü öncesi global durum

    for _ in range(5):
        global_counter += 1 # Döngü, paylaşılan bir durumu değiştirir
    # Döngü sonrası global durum, döngünün bıraktığı iz
    print(f"Döngü sonrası global_counter: {global_counter}")

    print("\nDöngüler, verilerinizi ve uygulamanızın durumunu kalıcı olarak değiştirerek izler bırakır.")

# Ana çalışma bloğu
if __name__ == "__main__":
    demonstrate_performance_footprints()
    demonstrate_data_integrity_footprints()
    print("\nBu örnek, döngülerin kodunuzda bıraktığı performans ve veri izlerini göstermektedir.")
