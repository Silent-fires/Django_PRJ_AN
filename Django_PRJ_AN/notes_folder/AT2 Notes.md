# Assessment Development Notes

This document outlines the recommended project structure and the expected functionality for your application. Use this as a guide when developing your solution.

## 1. Recommended Project Structure

The following is a suggested layout for your Django project.

```text
project/
│
├── ml/
│   └── predict.py
│   └── train.py
│
├── classifier/
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   └── templates/
│       └── classifier/
│
├── api/
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
│
└── logs/
    └── predictions.log
```

### ML/ – Machine Learning

Contains the code responsible for loading and interacting with your machine learning model.

- **predict.py** – Contains the code used by the main application to generate predictions using the loaded ML model.
- **train.py** – Train the model and creates the relevant .pk1 file.

### Classifier/ – Main Web Application

Contains the main Django application and its associated functionality.

- **models.py** – Defines the classes that represent your application's data structures. These models will be used to store information in the database.
- **views.py** – Contains the views responsible for handling user requests and returning the appropriate responses.

  Reference: [Django REST Framework – Views](https://www.django-rest-framework.org/api-guide/views/)

- **serializers.py** – Defines serializers used to convert data between Python objects and formats suitable for transferring data, such as JSON.

  Reference: [Django REST Framework – Serializers](https://www.django-rest-framework.org/api-guide/serializers/)

- **forms.py** – Contains form definitions used to collect and validate user input.

  Reference: [Django – Working with Forms](https://docs.djangoproject.com/en/6.1/topics/forms/)

- **templates/classifier/** – Contains the HTML templates used to render the application's web pages.
- **urls.py** – Configures the URL routes for the application and determines which view should handle each request.
- **admin.py** – Configures how your application models are managed through the Django administration panel.

  Reference: [Django – The Admin Site](https://docs.djangoproject.com/en/6.1/ref/contrib/admin/)

  *Hint: Look at the `@admin.register` decorator.*

### API/ – Application Programming Interface

Contains the endpoints that allow external applications or services to interact with your application.

Unlike the main classifier application, API endpoints should generally return data in a format such as JSON rather than rendering HTML templates or forms.

- **views.py** – Contains the API views responsible for processing incoming requests and returning responses.
- **serializers.py** – Defines serializers used to convert data into and out of formats suitable for API communication.
- **urls.py** – Defines the API routes and maps each URL to its corresponding view.

  For example, a request to `/api/predict/` should be directed to the appropriate view defined in `api/views.py`.

---

## 2. Required Functionality

The following functionality is what I would like to see implemented as part of your assessment.

### A. Classifier Application

Your main classifier application should contain **two views**:

1. **Prediction Input View**
   - Provides an interface for the user to submit information for a prediction.
   - Accepts and validates the user's input.
   - Initiates the prediction process.

2. **Prediction Results View**
   - Displays the results of previously generated predictions.
   - Should be an informational view rather than another input form.
   - Retrieves and displays prediction information stored in the database.

**Important:** Your application will need to store prediction results.

I recommend using the Django ORM with SQLite to manage and persist your prediction data.

### B. API

Implement an API endpoint for generating predictions.

**Prediction Endpoint**

- Accepts two arguments:
  - `text` – The input text to be classified.
  - `model_id` – Identifies which machine learning model should be used.
- Passes the supplied information to the appropriate prediction functionality.
- Returns the predicted result in JSON format.

**Optional: Performance Endpoint**

You may also implement an additional API endpoint that returns performance information about your machine learning model(s).

This could include relevant model performance metrics.

### C. Django Admin

Leverage Django's built-in administration panel, accessible through:

```text
/admin/
```

Extend the admin functionality to allow an administrator to manually add a prediction result.

Requirements:

- Register your prediction model with the Django admin site.
- Allow an administrator to manually create a new prediction record.
- Ensure the manually created record uses the same database model and structure as predictions generated through the application.

This means that manually entered predictions and automatically generated predictions should be stored consistently.

### D. Logging

Every prediction generated by the application should also be recorded in a log file.

**Requirements:**

- Create a `logs/` directory.
- Store prediction logs in a file called `predictions.log`.
- Each prediction should generate a corresponding log entry.

Suggested location:

```text
logs/predictions.log
```

Consider recording useful information such as:
- Date and time of the prediction.
- Input text (where appropriate).
- Model ID used.
- Predicted result.

You should use Python's built-in `logging` module rather than manually writing to the file.

### E. GitHub – Version Control

Use GitHub to demonstrate the development process of your application.

I would like to see commits at **crucial development checkpoints**, rather than a single commit containing the entire completed project.

Examples of appropriate commit points:

1. Initial Django project and application setup.
2. Database models implemented.
3. Machine learning model loading and prediction functionality implemented.
4. Classifier input and results views implemented.
5. API endpoints implemented.
6. Django admin functionality implemented.
7. Logging implemented.
8. Final testing and refinements.

Commit messages should clearly describe the changes being introduced.

---

## 3. Final Assessment Checklist

Use the following checklist to make sure you have covered the expected functionality.

### Main Application
- [ ] Prediction input view implemented.
- [ ] Prediction results view implemented.
- [ ] User input validated.
- [ ] Prediction results stored in the database.
- [ ] Django ORM used for database operations.

### API
- [ ] Prediction API endpoint implemented.
- [ ] Accepts `text` and `model_id`.
- [ ] Returns prediction results as JSON.
- [ ] Optional performance endpoint implemented (if attempted).

### Django Admin
- [ ] Prediction model registered with Django admin.
- [ ] Administrator can manually add prediction records.
- [ ] Manually created records use the same database model as generated predictions.

### Logging
- [ ] `logs/` directory created.
- [ ] `predictions.log` file created.
- [ ] Each prediction generates a log entry.

### GitHub
- [ ] Project maintained in a GitHub repository.
- [ ] Commits made at important development checkpoints.
- [ ] Commit messages clearly describe the changes.

---

**Final Advice:** Focus on building the application in manageable stages. Get the basic Django application working first, then introduce the machine learning functionality, API, administration features and logging. Remember to commit your work regularly as you progress.