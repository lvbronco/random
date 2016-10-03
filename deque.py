from collections import deque

# void maxSlidingWindow(int A[], int n, int w, int B[]) {
#   deque<int> Q;
#   for (int i = 0; i < w; i++) {
#     while (!Q.empty() && A[i] >= A[Q.back()])
#       Q.pop_back();
#     Q.push_back(i);
#   }
#   for (int i = w; i < n; i++) {
#     B[i-w] = A[Q.front()];
#     while (!Q.empty() && A[i] >= A[Q.back()])
#       Q.pop_back();
#     while (!Q.empty() && Q.front() <= i-w)
#       Q.pop_front();
#     Q.push_back(i);
#   }
#   B[n-w] = A[Q.front()];
# }

def maxSlidingWindow(a, w):
  n = len(a)
  b = [None]*(n-w+1)
  q = deque()
  for i in range(w):
    while len(q) > 0 and a[i] >= a[q[-1]]:
      q.pop()
    q.append(i)
    print "{0}: {1}".format(i, q)

  for i in range(w, n):
    temp = i-w
    b[temp] = a[q[0]]
    while len(q) > 0 and a[i] >= a[q[-1]]:
      q.pop()
    while len(q) > 0 and q[0] <= temp:
      q.popleft()
    q.append(i)
    print "{0}: {1}".format(i, q)

  b[n-w] = a[q[0]]
  return b

# int main()
# {
#     int arr[] = {12, 1, 78, 90, 57, 89, 56};
#     int n = sizeof(arr)/sizeof(arr[0]);
#     int k = 3;
#     printKMax(arr, n, k);
#     return 0;
# }

a = [12, 1, 78, 90, 57, 89, 56, 32, 55, 1, 45, 103]
w = 3
print a
print maxSlidingWindow(a, w)
