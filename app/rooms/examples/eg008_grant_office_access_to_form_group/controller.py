from typing import List

from docusign_rooms import (
    FormGroupsApi,
    FormGroupSummary,
    FormGroupSummaryList,
    OfficeSummary,
    OfficesApi,
    OfficeSummaryList,
)
from flask import session, request

from app.rooms import create_rooms_api_client


class Eg008Controller:
    @staticmethod
    def get_args() -> dict:
        """Get required session and request arguments"""
        return {
            "account_id": session["ds_account_id"],
            # Represents your {ACCOUNT_ID}
            "access_token": session["ds_access_token"],
            # Represents your {ACCESS_TOKEN}
            "form_group_id": request.form.get("form_group_id"),
            'office_id': request.form.get('office_id')
        }

    @staticmethod
    def get_form_groups(args) -> List[FormGroupSummary]:
        """
        1. Create an API Client with headers
        2. GET Form Groups via FormGroupsAPI
        """

        # Step 1. Create an API with headers with headers
        api_client = create_rooms_api_client(access_token=args['access_token'])

        # Step 2. GET Form Groups via FormGroupsAPI
        form_groups_api = FormGroupsApi(api_client)
        responses = form_groups_api.get_form_groups(
            account_id=args['account_id'])  # type: FormGroupSummaryList

        return responses.form_groups

    @staticmethod
    def get_offices(args) -> List[OfficeSummary]:
        """
        1. Create an API Client with headers
        2. Get Offices via OfficesAPI
        """

        # Step 1. Create an API with headers with headers
        api_client = create_rooms_api_client(args['access_token'])

        # Step 2. GET offices via OfficesAPI
        offices_api = OfficesApi(api_client=api_client)
        responses = offices_api.get_offices(
            account_id=args['account_id'])  # type: OfficeSummaryList

        return responses.office_summaries

    @staticmethod
    def worker(args):
        """

        1. Create an API client with headers
        2. Grant office access tp a form group via FormGroups API
        """

        # Step 1. Create an API client with headers
        api_client = create_rooms_api_client(access_token=args['access_token'])

        # Step 2. Grant office access tp a form group via FormGroups API
        form_groups_api = FormGroupsApi(api_client)

        form_groups_api.grant_office_access_to_form_group(
            form_group_id=args['form_group_id'], office_id=args['office_id'],
            account_id=args['account_id'])
