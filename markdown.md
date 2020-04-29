## image alignment
required CSS:

```
img[src*='#left'] {
    float: left;
}
img[src*='#right'] {
    float: right;
}
img[src*='#center'] {
    display: block;
    margin: auto;
}
```

Usage:

```
![my image](/img/myImage.jpg#left)
![my image](/img/myImage.jpg#right)
![my image](/img/myImage.jpg#center)
```

