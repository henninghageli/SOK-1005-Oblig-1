import numpy as np
import requests
import matplotlib.pyplot as plt

class TempPlotter:
    def __init__(self):
        self.urls = {
            "lower_troposphere": "https://www.nsstc.uah.edu/data/msu/v6.0/tlt/uahncdc_lt_6.0.txt",
            "mid_troposphere": "https://www.nsstc.uah.edu/data/msu/v6.0/tmt/uahncdc_mt_6.0.txt",
            "tropopause": "https://www.nsstc.uah.edu/data/msu/v6.0/ttp/uahncdc_tp_6.0.txt",
            "lower_stratosphere": "https://www.nsstc.uah.edu/data/msu/v6.0/tls/uahncdc_ls_6.0.txt"
        }
        self.lower_troposphere = self._get_global_temp(self.urls["lower_troposphere"])
        self.mid_troposphere = self._get_global_temp(self.urls["mid_troposphere"])
        self.tropopause = self._get_global_temp(self.urls["tropopause"])
        self.lower_stratosphere = self._get_global_temp(self.urls["lower_stratosphere"])

    def _get_global_temp(self, url):
        response = requests.get(url)
        data = response.text.split("\n")[1:]
        data = [line.strip() for line in data]
        data = [line.split() for line in data if line and line[0].isdigit()]
        data = [float(line[2]) for line in data]
        return data
    
    def _moving_average(self, data, window_size=12):
        return np.convolve(data, np.ones(window_size)/window_size, mode="valid")
    
    def plot(self):
        lt_ma = self._moving_average(self.lower_troposphere)
        mt_ma = self._moving_average(self.mid_troposphere)
        tp_ma = self._moving_average(self.tropopause)
        ls_ma = self._moving_average(self.lower_stratosphere)

        avg_ma = (lt_ma + mt_ma + tp_ma + ls_ma) / 4

        plt.figure(figsize=(10, 6))
        plt.plot(lt_ma, label="Lower Troposphere")
        plt.plot(mt_ma, label="Mid Troposphere")
        plt.plot(tp_ma, label="Tropopause")
        plt.plot(ls_ma, label="Lower Stratosphere")
        plt.plot(avg_ma, label="Average", linestyle="--", linewidth=2)

        plt.xlabel("Year")
        plt.ylabel("Temperature Anomaly (°C)")
        plt.title("12-Month Moving Average of Global Temperature Anomalies")
        plt.xticks(np.arange(0, len(avg_ma) + 12, 12), np.arange(1979, 2025), rotation=90)
        plt.legend()
        plt.grid(True)
        plt.show()
    
def main():
    tp = TempPlotter()
    tp.plot()

if __name__ == "__main__":
    main()
