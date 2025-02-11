// once I thought I should scrape the tesla locations from https://www.tesla.com/findus/list
// and use BeautifulSoup to scrape the data
// but then found the api when I found the api then I use JavaScript to fetch the data
// and save it to a file

const fetchTeslaLocations = async () => {
  const url = "https://www.tesla.com/cua-api/tesla-locations";
  const headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
  };
  try {
    const response = await fetch(url, { headers });
    return await response.json();
  } catch (error) {
    console.error("Error fetching data:", error);
    return null;
  }
};

const saveToFile = (data) => {
  const fs = require("fs");
  const path = require("path");

  const filePath = path.join(__dirname, "tesla_locations.json");
  fs.writeFileSync(filePath, JSON.stringify(data, null, 4));
  console.log("Data saved to tesla_locations.json");
};

const main = async () => {
  const data = await fetchTeslaLocations();
  if (data) {
    await saveToFile(data);
  }
};

main();
