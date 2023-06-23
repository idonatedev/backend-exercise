# iDonate Backend Exercise

## Overview

- There is a Flask app defined in `backend/web.py` and mounted at `/`.
- There is a FastAPI app defined in `backend/api.py` and mounted at `/api`, with Swagger docs at `/api/docs`.
- The database is SQLite, models are defined in `backend/models.py` and sample data has been loaded.
- Requirements are defined in `requirements.txt` and can be installed with pip.
- `./run_dev.sh` will run the app in development mode on **port 8000**, with auto-reloading enabled.
- `./run_dev.py` can also be used to start the app directly for e.g. an external debugger.

## Tasks

The tasks do not have to be completed in order and it is not expected for all tasks to be completed.

You may use whatever reference materials, search engines, or other information sources as you see fit.

### Flask Tasks

- Access the app from your browser and verify that the "Charity List" view is working.
- Update the "Charity List" view to include the Charity name and a link to the "Charity Detail" view for each charity.
- Implement the "Charity Detail" view - this view should display the charity's name, description, and a list of
  donations made to that charity. Include the Donor's name for each donation.
- Add aggregated data for "donation_count" and "total_donation_amount" to the "Charity Detail" view.
- Add search-by-name functionality to the "Charity List" view.
- Implement the ability to create a new Charity via a simple web form.
- Implement a "Donor List" view that displays a list of donors in the database by name, with a link to a "
  Donor Detail" view for each donor.
- Implement the "Donor Detail" view, which should display the donor's name, email, and a list of
  donations made by that donor - as well as which Charity and Campaign each donation was made to.
- Add aggregated data for "donation_count" and "total_donation_amount" to the "Donor Detail" view.
- Add REST endpoints with JSON output for "Charity List" and/or "Donor List".

### FastAPI Tasks

- Implement a simple FastAPI Dependency that wraps a database session object to use in the following endpoints.
- Implement an endpoint that returns a list of donors in the database for a given Charity, filterable by Date Range.
    - Include (or explain how you would include) aggregated data for "donation_count" and "total_donation_amount" for
      each donor.
- Implement an endpoint that returns a list of donations in the database, sorted by created_at, filterable by Charity
  ID, Donor ID, Campaign ID and/or Date Range.
- Implement an endpoint that returns details for a specific Donation (by ID). Include Donor, Charity and Campaign
  details in the output.
