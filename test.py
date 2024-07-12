import re

html = """
<div class="detail__body itp_bodycontent_wrapper">
  <div class="detail__body-text itp_bodycontent">
    <!-- S:Table of Content -->
    <!-- E:Table of Content -->
    <strong> Jakarta </strong>
    -
    <p>
      Indeks Harga Saham Gabungan (IHSG) pada pembukaan perdagangan pagi ini
      bergerak di zona hijau. Indeks naik 7 poin atau 0,10% ke level 7.277.
    </p>
    <p>
      Mengutip data RTI, Rabu (10/7/2024), IHSG bergerak pada level tertingginya
      di 7.310 dan terendah di 7.272. Volume saham yang diperdagangkan di awal
      pembukaan mencapai 6 miliar, dengan turnover Rp 1,2 triliun serta
      frekuensi sebanyak 150 ribu kali.
    </p>
    <p>
      Sebanyak 217 saham bergerak naik, 174 saham bergerak turun, dan 182 saham
      belum bergerak dengan market cap tercatat mencapai Rp 12.453 triliun.
    </p>
    <!--s:parallaxindetail-->
    <div class="clearfix"></div>
    <style>
      @import url("https://awscdnstatic.detik.net.id/live/_rmbassets/scrollpage/scrollpage.css");
    </style>
    <div
      class="parallaxindetail scrollpage"
      style="height: 650px; background-color: #f8f8f8"
    >
      <p
        class="para_caption"
        style="
          display: block;
          font-size: 9px;
          color: rgba(0, 0, 0, 0.55);
          position: relative;
          margin: 5px;
          text-align: center;
          left: 0px;
          right: 0px;
          letter-spacing: 0.7px;
        "
      >
        ADVERTISEMENT
      </p>
      <div class="ads-scrollpage-container">
        <div
          class="ads-scrollpage-height"
          style="height: 600px; width: 100%; margin: auto"
        >
          <div class="ads-scrollpage-box">
            <div class="ads-scrollpage-top" style="top: 91px">
              <div class="ads-scrollpage-banner">
                <!-- /4905536/detik_desktop/finance/parallax_detail -->
                <div
                  id="div-gpt-ad-1618601354128-0"
                  style="min-width: 300px; min-height: 250px"
                >
                  <script>
                    googletag.cmd.push(function () {
                      googletag.display("div-gpt-ad-1618601354128-0");
                    });
                  </script>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <p
        class="para_caption"
        style="
          display: block;
          font-size: 9px;
          color: rgba(0, 0, 0, 0.55);
          position: relative;
          margin: 8px;
          text-align: center;
          left: 0px;
          right: 0px;
          letter-spacing: 0.7px;
        "
      >
        SCROLL TO CONTINUE WITH CONTENT
      </p>
    </div>
    <!--e:parallaxindetail-->
    <p>
      Mengutip hasil riset Mega Capital Sekuritas dan Investasiku, pada
      perdagangan hari ini bakal dipengaruhi oleh sentimen global yakni,
      iInvestor Menanti Komentar Lanjutan Powell. Bursa AS ditutup variatif,
      indeks S&amp;P 500 dan Nasdaq sempat mencetak rekor harga tertinggi. Pada
      pertemuan Komite Perbankan DPD AS (Senate Banking Committee), Ketua The
      Fed Jerome Powell memberikan komentar yang cenderung netral.
    </p>
    <p>
      Pasalnya Powell mengakui perkembangan yang signifikan pada pasar tenaga
      kerja AS dan status ekonomi AS tidak lagi overheated,
      <br />
      namun ia ingin melihat perkembangan data inflasi yang lebih baik. Powell
      turut memperingati bahwa risiko bukan hanya pada inflasi, melainkan ada
      pada ketepatan dalam menahan atau memangkas suku bunga agar tidak merusak
      perekonomian AS.
    </p>
    <!--s:static_detail-->
    <div class="clearfix"></div>
    <div
      class="staticdetail_container"
      style="
        position: relative;
        width: 100%;
        height: 330px;
        background-color: #f8f8f8;
        align-content: center;
        margin: 0px auto 20px;
      "
    >
      <span
        class="para_caption"
        style="
          display: block;
          font-size: 9px;
          color: rgba(0, 0, 0, 0.55);
          position: relative;
          padding: 8px;
          text-align: center;
          left: 0px;
          right: 0px;
          letter-spacing: 0.7px;
          top: 0;
        "
      >
        ADVERTISEMENT
      </span>
      <div
        class="staticdetail_ads"
        style="
          width: 100%;
          height: 300px;
          position: relative;
          text-align: center;
        "
      >
        <!-- /4905536/detik_desktop/finance/static_detail -->
        <div
          id="div-gpt-ad-1709715464819-0"
          style="min-width: 400px; min-height: 250px"
        >
          <script>
            googletag.cmd.push(function () {
              googletag.display("div-gpt-ad-1709715464819-0");
            });
          </script>
        </div>
      </div>
    </div>
    <!--e:static_detail-->
    <p>
      Bursa Asia kompak melanjutkan penguatan, hal ini ditopang oleh ekspektasi
      kenaikan inflasi Tiongkok periode Juni yang akan rilis Rabu pagi ini. Hari
      ini pelaku pasar akan kembali mencermati komentar Powell pada pertemuan
      Komite Jasa Keuangan DPR AS (House Financial Services Committee), rilis
      inflasi Tiongkok, dan cadangan minyak mentah mingguan AS.
    </p>
    <p>
      Sementara di bursa domestik, sejalan dengan penguatan di bursa regional
      Asia, IHSG menguat 0.26% ke level 7269, sebelumnya
      <br />
      IHSG bahkan sempat menyentuh level tertinggi harian di 7302. Investor
      asing konsisten melanjutkan akumulasi net buy harian sebesar Rp 166 miliar
      di pasar reguler, dengan 5 saham yang paling banyak dibeli yaitu BBCA,
      BBRI, BMRI, AMMN, dan ADRO.
    </p>
    <p>
      Sentimen positif turut menjadi penopang penguatan IHSG yaitu rilis data
      penjualan mobil yang naik 2.28% MoM di bulan Juni dan penjualan ritel
      bulan Mei yang naik 2.1% YoY, membaik dari bulan sebelumnya yang
      terkontraksi 2.7% YoY. Kenaikan penjualan ritel bulan Mei menjadi kenaikan
      yang ke 4 di tahun ini, didukung oleh program bantuan langsung tunai dari
      pemerintah.
    </p>
    <p>
      Secara sektoral, penguatan IHSG ditopang oleh sektor keuangan dan
      industrial yang menguat masing-masing 1.44% dan 1.10%. Sebaliknya, aksi
      jual justru terjadi pada sektor kesehatan yang melemah 1.28%.
    </p>
    <strong> (rrd/rir) </strong>
    <div class="detail__body-tag mgt-16">
      <div class="nav">
        <a
          class="nav__item"
          dtr-act="tag"
          dtr-evt="tag"
          dtr-idx=" 1"
          dtr-sec=""
          dtr-ttl="ihsg"
          href="https://www.detik.com/tag/ihsg/"
          onclick="_pt(this)"
        >
          ihsg
        </a>
        <a
          class="nav__item"
          dtr-act="tag"
          dtr-evt="tag"
          dtr-idx=" 2"
          dtr-sec=""
          dtr-ttl="saham"
          href="https://www.detik.com/tag/saham/"
          onclick="_pt(this)"
        >
          saham
        </a>
      </div>
    </div>
  </div>
  <!-- S:skyscraper -->
  <style>
    .skybanner {
      width: 160px;
    }
  </style>
  <div class="skybanner">
    <div class="sticky">
      <div class="skybanner_container">
        <!-- /4905536/detik_desktop/finance/skyscrapper -->
        <div id="div-gpt-ad-1610072077615-0">
          <script>
            googletag.cmd.push(function () {
              googletag.display("div-gpt-ad-1610072077615-0");
            });
          </script>
        </div>
      </div>
    </div>
  </div>
  <!-- E:skyscraper -->
</div>
"""

# Define the regex pattern
pattern = re.compile(r'<p>(.*?)</p>', re.DOTALL)

# Find all matches
matches = pattern.findall(html)

# Clean up the matches to remove any additional HTML tags within the paragraphs
cleaned_matches = [re.sub(r'<.*?>', '', match).strip() for match in matches]

# Print the cleaned matches
for match in cleaned_matches:
    print(match)