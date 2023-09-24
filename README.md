# T-GPT Backend

## Summary

**T-GPT** is a website that gives people from countries where chat gpt is not available, **instant and free access** to questions and answers. **Simply** type in a question and get an instant response from the chat gpt. Find the answers you need quickly and easily!

**THIS IS COSUMING ONLY BY THE OFFICIAL PAGE OF T-GPT**.

**THIS BACKEND DOCUMENTATION IS BEING SHOWN TO ALL THE CUSTOMER WITH EDUCATIONAL OBJETIVES**.

## API Reference

### Auth

#### Get Access

```http
    POST /auth/get-access
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `key` | `string` | **Required**. Secret key. |
| `engine` | `string` | **Required**. GPT engine. |
| `provideer` | `string` | **Required**. Provideer of the access. |
| `jwt_algorithm` | `string` | **Required**. JSON web token algorithm. |

All in ***application/json***.

### Chat

#### Get Answer

```http
    POST /chat/get-answer
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `question` | `string` | **Required**. Question will ask to ChatGPT. |

All in ***application/json***.
