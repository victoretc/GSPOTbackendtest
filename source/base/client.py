import allure
import requests

from requests import Response
from typing import Dict, Optional, Any, Tuple


class Requests:
    @staticmethod
    @allure.step("GET request to {url}")
    def get(
            url: str,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        return requests.get(
            url=url,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
        )

    @staticmethod
    @allure.step("POST request to {url}")
    def post(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        return requests.post(
            url=url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
        )

    @staticmethod
    @allure.step("PATCH request to {url}")
    def patch(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        return requests.patch(
            url=url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
        )

    @staticmethod
    @allure.step("PUT request to {url}")
    def put(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        return requests.put(
            url=url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
        )

    @staticmethod
    @allure.step("DELETE request to {url}")
    def delete(
            url: str,
            data: str = None,
            json: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            headers: Optional[Dict[str, str]] = None,
            cookies: Optional[Dict[str, str]] = None,
            auth: Optional[Tuple[str, str]] = None
    ) -> Response:
        return requests.delete(
            url=url,
            data=data,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            auth=auth,
        )
