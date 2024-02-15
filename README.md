# Gemini Pro Vision and Gemini Pro Test

Code to test Gemini Pro Vision and Gemini Pro (text only model that supports chat history)

### Steps to get it work

1. Create the file [api_keys.json](./api_keys.json)
1. Put this content into it
    ```json
    {
        "Google-Generative-Language" : "YOUR_API_KEY"
    }
    ```
1. [Get an API key](https://makersuite.google.com/app/apikey)
1. Replace `YOUR_API_KEY` with your API key
1. (For gemini-pro-vision) Replace image.jpg with your image (if you want to use a png image, change the path in `main.py`)

### Sample Output for given image in gemini-vision-pro

```
1. Two containers of food
2. A bowl of soy sauce
3. A bowl of sesame seeds
4. A pair of chopsticks

No
```

### Sample Output for given prompt in gemini-pro

```
1. Water
2. Milk
3. Honey
4. Olive oil
5. Coconut oil
6. Maple syrup
7. Aloe vera juice
8. Lemon juice
9. Apple cider vinegar
10. Green tea
--------------------------------------------------------------------------------
1. Water
2. Milk
3. Honey
4. Maple syrup
5. Aloe vera juice
6. Lemon juice
7. Apple cider vinegar
8. Green tea
```
