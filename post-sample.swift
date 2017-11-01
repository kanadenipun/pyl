import Foundation

let headers = [
  "content-type": "application/json",
  "cache-control": "no-cache",
  "postman-token": "8d8fdaee-aa6f-6a2c-8b9f-e5d169865572"
]
let parameters = ["data": ["$", "$", "I Solemnly swear,", "$", "I am upto No Good :D", "$", "$", "$"]] as [String : Any]

let postData = JSONSerialization.data(withJSONObject: parameters, options: [])

let request = NSMutableURLRequest(url: NSURL(string: "https://api.mlab.com/api/1/databases/krpyl/collections/queue?apiKey=")! as URL,
                                        cachePolicy: .useProtocolCachePolicy,
                                    timeoutInterval: 10.0)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = postData as Data

let session = URLSession.shared
let dataTask = session.dataTask(with: request as URLRequest, completionHandler: { (data, response, error) -> Void in
  if (error != nil) {
    print(error)
  } else {
    let httpResponse = response as? HTTPURLResponse
    print(httpResponse)
  }
})

dataTask.resume()
