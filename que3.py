# Instagram Reel Engagement Tracker

views = int(input("Enter number of views: "))
likes = int(input("Enter number of likes: "))
comments = int(input("Enter number of comments: "))

engagement_rate = ((likes + comments) / views) * 100

print("\n----- Performance Audit Report -----")
print("Views:", views)
print("Likes:", likes)
print("Comments:", comments)
print("Engagement Rate:", engagement_rate, "%")