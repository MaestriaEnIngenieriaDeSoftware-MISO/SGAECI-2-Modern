from marshmallow import Schema, ValidationError

def map_externo_to_dto(request_body: dict, schema: Schema) -> Schema:
    """
    Maps the request body to the data transfer object.

    :param request_body: The request body.
    :param schema: The schema to use.
    :return: The mapped data.
    """
    dto = schema()
    errors = dto.validate(request_body)
    if errors:
        raise ValidationError(errors)
    return dto.load(request_body)