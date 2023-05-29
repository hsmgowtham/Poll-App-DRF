def get_formatted_response(
    status, message, data={}, total_count=0, filtered_count=0, page=None
):
    """
    - Created custom method to manage DRF/REST API response with generic response format
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