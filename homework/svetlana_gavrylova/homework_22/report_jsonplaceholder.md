# Load Testing Report

## Tool

Locust

## API Under Test

https://jsonplaceholder.typicode.com

## Test Parameters

- Endpoints: `/posts`, `/posts/{id}`, `/posts?userId=1`
- Methods: GET, POST, PUT, DELETE
- Total requests: 3996
- Failures: 0 (0%)

## Task Distribution (weights)

| Task                   | Method        | Endpoint        | Weight |
|------------------------|---------------|-----------------|--------|
| Get all posts          | GET           | /posts          | 3      |
| Get single post        | GET           | /posts/{id}     | 5      |
| Get posts by user      | GET           | /posts?userId=1 | 2      |
| Create and delete post | POST + DELETE | /posts          | 1      |
| Update post            | PUT           | /posts/{id}     | 1      |

## Response Time Percentiles (ms)

| Method         | Endpoint        | 50%    | 75%     | 90%     | 95%     | 99%     | Max     | # Reqs   |
|----------------|-----------------|--------|---------|---------|---------|---------|---------|----------|
| GET            | /posts          | 39     | 41      | 44      | 110     | 120     | 130     | 902      |
| GET            | /posts/{id}     | 39-40  | 40-42   | 42-120  | 110-130 | 110-130 | 130     | ~1500    |
| GET            | /posts?userId=1 | 39     | 40      | 44      | 110     | 120     | 150     | 631      |
| POST           | /posts          | 100    | 110     | 160     | 180     | 190     | 310     | 308      |
| DELETE         | /posts/101      | 100    | 110     | 140     | 170     | 190     | 200     | 306      |
| PUT            | /posts/{id}     | 110    | 140-240 | 230-240 | 240     | 240-310 | 340     | ~350     |
| **Aggregated** |                 | **40** | **99**  | **110** | **130** | **240** | **340** | **3996** |

## Conclusions

1. **GET requests** are the fastest (~39-40 ms median). Read operations require minimal server resources.
2. **POST and DELETE** are ~2.5x slower (~100 ms median). Write operations expectedly take more time.
3. **PUT** is the slowest method (~110-240 ms median) with the highest response time variance.
4. **0% failure rate** — the API handles the load stably.
5. **Aggregated 95th percentile is 130 ms** — 95% of all requests complete within 130 ms, which is a good result.