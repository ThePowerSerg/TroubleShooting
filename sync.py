import requests
import time

# Read contents from site 
def download_site(url, session):
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

# Loop through the list of sites and pass URL and session information
def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    # Create a list of 160 URLs
    sites = ["https://www.jython.org", "http://olympus.realpython.org/dice",] * 80
    # Set start time before site download
    start_time = time.time()
    # Call download function
    download_all_sites(sites)
    # Calculate time elapsed 
    duration = time.time() - start_time
    # print out execution details
    print(f"Downloaded {len(sites)} in {duration} seconds")