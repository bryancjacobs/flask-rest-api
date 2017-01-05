class Survey(object):

    def __init__(self, survey_id, survey_code, question_id, question_handle, question_short_code, scale_id, scale_handle, answer_id, answer_handle, answer_weight, answer_data_type, value, question_text, answer_text):
        self.survey_id = survey_id
        self.survey_code = survey_code
        self.question_id = question_id
        self.question_handle = question_handle
        self.question_short_code = question_short_code
        self.scale_id = scale_id
        self.scale_handle = scale_handle
        self.answer_id = answer_id
        self.answer_handle = answer_handle
        self.answer_weight = answer_weight
        self.answer_data_type = answer_data_type
        self.value = value
        self.question_text = question_text
        self.answer_text = answer_text
