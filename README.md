# Task Overview
You are working on a FastAPI-based user management service that uses Pydantic schemas to validate user profile data. Users can create profiles and later update them using dedicated endpoints, with proper request body validation enforced for fields such as email. Recently, users have been unable to update their email address through the profile update endpoint, encountering validation errors for valid email inputs, while all other fields and flows (like creation) work as expected.

# Guidance
- Focus on the distinction between schema validations used during creation and update operations.
- Investigate how your update endpoint and its request body validation behave versus your profile creation logic.
- Consider Pydantic and FastAPI conventions for handling optional/required fields and types, especially for email validation.
- Maintain robust validation for all fields, including the email field, on both creation and update endpoints.

# Objectives
- Diagnose and fix the root cause preventing valid email addresses from being accepted during profile updates.
- Ensure the profile update endpoint allows standard, validated email addresses to be updated successfully.
- Confirm that all profile flows (creation and update) continue to rigorously validate emails and other fields as appropriate.

# How to Verify
- Confirm that submitting a valid email address to the profile update endpoint is accepted and updates the record.
- Test updating other profile fields and creating new profiles to ensure all validation remains consistent.
- Ensure invalid email addresses are still rejected on both creation and update.
- Validation errors should be coherent and only raised for genuinely invalid input.