import CustomVision
import Scraping
import SoupScrape
from scrapy.crawler import CrawlerProcess


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # Souptest = SoupScrape
    #
    # Souptest.soupscrape('https://www.redbubble.com/shop/?query=usf&ref=search_box')
    VisionAPI = CustomVision.Endpoint_class

    # VisionAPI.Azure_endpoint(VisionAPI, "https://www.tampabay.com/resizer//epkcE3ukhuWVMC_WVjNjFB9utZc=/900x506/smart/filters:format(webP)/arc-anglerfish-arc2-prod-tbt.s3.amazonaws.com/public/TMYBMGWIHQI6TGNIIBWI6S7HAY.jpg")
    CrawlTest = Scraping.LinkSpider

    process = CrawlerProcess()
    process.crawl(CrawlTest)
    process.start()
    print(CrawlTest.ret_links)

    links = CrawlTest.ret_links
    print(len(links))
    count = 0
    # for link in links:
    #     VisionAPI.Azure_endpoint(VisionAPI,link,count)
    #     count = count + 1




#     prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
#     predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
#
#     with open(os.path.join(base_image_location, "Test/test_image.jpg"), "rb") as image_contents:
#         results = predictor.classify_image(
#             ProjectID, ModelName, image_contents.read())
#
#         # Display the results.
#         for prediction in results.predictions:
#             print("\t" + prediction.tag_name +
#                   ": {0:.2f}%".format(prediction.probability * 100))
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/