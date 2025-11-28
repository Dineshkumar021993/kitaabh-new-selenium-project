import logging

from testlink import TestLinkHelper, TestlinkAPIClient


def update_execution_status(test_case_name, test_result, test_note='Test note'):
    DEVKEY = '61d7a5645cc64f946ec9d9d2acb95abc'
    URL = "http://localhost/testlink/testlink/lib/api/xmlrpc/v1/xmlrpc.php"

    # Initialize the TestLink API client
    # tl_helper = TestLinkHelper(server_url=URL, devKey=DEVKEY)
    # api = tl_helper.connect(TestlinkAPIClient)
    api = TestlinkAPIClient(URL, DEVKEY)

    # Define parameters
    test_plan = "kitaab Test plan"
    test_project = "KITAAB Testing create Ledgers for all groups"
    build = "kitaab 0.0.53.exe"
    try:
        test_plan_id = api.getTestPlanByName(test_project, test_plan)[0]['id']
        response = api.reportTCResult(
            testcasename=test_case_name,
            testplanid=test_plan_id,
            buildname=build,
            notes=test_note,
            status=test_result
        )
        print(response)
    except Exception as e:
        # Log the error
        logging.error(f"Failed to update execution status for '{test_case_name}': {str(e)}")
        # Optionally raise the exception again if needed
        raise





