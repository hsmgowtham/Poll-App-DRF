def get_formatted_response(
    status, message, data={}, total_count=0, filtered_count=0, page=None
):
    """
    - Created custom method to manage DRF/REST API response with generic response format
    - Suppose if we changing the format then front-end side having clashes to manage UI response
    - So created 3 payloads as response
    """
    response = {
        "status": status,
        "message": message,
        "data": data,
        "total_count": total_count,
        "filtered_count": filtered_count,
    }
    if page:
        response["next"] = page.get("next")
        response["previous"] = page.get("previous")
        response["page_range"] = page.get("page_range")
        response["per_page"] = page.get("per_page")
    return response