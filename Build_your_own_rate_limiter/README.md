### Step Zero[​](https://codingchallenges.fyi/challenges/challenge-rate-limiter#step-zero "Direct link to Step Zero")

In most programming languages (Fortran and COBOL are exceptions) we index arrays from the element zero onwards because arrays are represented as a pointer to the beginning and an offset from that beginning - i.e. if you're familiar with C then `array[index]` is equivalent to `*(array + index)`.

As usually, I'll leave you to setup your IDE / editor of choice and programming language of choice. Once you're set up, let's proceed to Step 1.

You might also want to download and install [Postman](https://www.postman.com/) for the later parts of the challenge. If not you can use curl.

### Step 1[​](https://codingchallenges.fyi/challenges/challenge-rate-limiter#step-1 "Direct link to Step 1")

In this step your goal is to implement a simple API you we can use for testing. For this challenge I'd like you to create two endpoints: `/limited` and `/unlimited`.

You can have them return anything you want, for my examples I've had them return some text, here is my test to check they work, you should do something similar:

```
% curl http://127.0.0.1:8080/unlimitedUnlimited! Let's Go!% curl http://127.0.0.1:8080/limitedLimited, don't over use me!
```

### Step 2[​](https://codingchallenges.fyi/challenges/challenge-rate-limiter#step-2 "Direct link to Step 2")

In this step your goal is to implement the token bucket algorithm for rate limiting. The token bucket algorithm works like this:

- There is a 'bucket' that has capacity for N tokens. Usually this is a bucket per user or IP address.
- Every time period a new token is added to the bucket, if the bucket is full the token is discarded.
- When a request arrives and the bucket contains tokens, the request is handled and a token is removed from the bucket.
- When a request arrives and the bucket is empty, the request is declined.

For this step, implement this strategy such that the bucket is per IP address, has a capacity of 10 tokens with new tokens added at a rate of 1 token per second.

When a request is rejected you should return the HTTP status code of 429 - Too Many Requests.

Once you have implemented that you can use Postman to test it. There is a blog post that introduces the performance testing abilities of Postman and explains how to set it up [here](https://blog.postman.com/postman-api-performance-testing/).

I configured a test to hit the limited API endpoint with 10 Virtual Users, as you can see that results in no errors initially, (the bucket had ten tokens, then after a second 90% of the requests fail as there are 10 users trying to access the API, but only one token being added per second.
