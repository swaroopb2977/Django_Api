# Django API Employee Mangement System: [Django API]
- Description: This Django API project focuses on managing companies and employees with various features and customizations.
  It utilizes Django Rest Framework (DRF) to create a RESTful API for handling these entities.
- Technologies: Python , Django REST frameworks.

### Key Features:
   ### 1.Modular Architecture:
       Utilizes a modular architecture with a dedicated api app for handling APIs separately.
  
   ### 2.Company Model and Serializer:
      Implements a Company model and a corresponding serializer for managing company information.
  
   ### 3.CRUD Operations with ViewSet:
      Provides CRUD (Create, Read, Update, Delete) operations for companies via a CompanyViewSet using Django Rest Framework's ViewSet.
  
   ### 4.Endpoint Routing with DefaultRouter:
      Sets up URL routing efficiently using DRF's DefaultRouter to map endpoints to ViewSets.
  
   ### 5.Employee Management:
      Integrates an Employee model and establishes a relationship with the Company model for managing employees within companies.
  
   ### 6.Custom API (@action):
      Offers a custom API action to retrieve employees based on specific categories or criteria.
  
   ### 7.ReadOnly Configuration:
      Configures certain API endpoints to be read-only for enhanced security or designated functionalities.
  
   ### 8.Browsable API Disablement:
      Disables the browsable API in production for security purposes, limiting direct interaction through the browser.
  
  ### 9.Django Admin Customization:
      Customizes the Django Admin module for more intuitive and efficient management of companies and employees..
