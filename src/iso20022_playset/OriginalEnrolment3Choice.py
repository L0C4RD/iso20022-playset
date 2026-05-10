from . import base_types
from .Party53Choice import Party53Choice
from .CreditorEnrolment5 import CreditorEnrolment5

class OriginalEnrolment3Choice(base_types._BaseFieldType):

	__slots__ = ["_OrgnlEnrlmntData", "_OrgnlCdtrId"]
	@property
	def OrgnlEnrlmntData(self):
		return self._OrgnlEnrlmntData

	@OrgnlEnrlmntData.setter
	def OrgnlEnrlmntData(self, value):
		self._OrgnlEnrlmntData = value if type(value) != base_types.auto else self.make_default("OrgnlEnrlmntData")

	@OrgnlEnrlmntData.deleter
	def OrgnlEnrlmntData(self):
		del self._OrgnlEnrlmntData
		self._OrgnlEnrlmntData = None

	@property
	def OrgnlCdtrId(self):
		return self._OrgnlCdtrId

	@OrgnlCdtrId.setter
	def OrgnlCdtrId(self, value):
		self._OrgnlCdtrId = value if type(value) != base_types.auto else self.make_default("OrgnlCdtrId")

	@OrgnlCdtrId.deleter
	def OrgnlCdtrId(self):
		del self._OrgnlCdtrId
		self._OrgnlCdtrId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlEnrlmntData', type=CreditorEnrolment5, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='OrgnlCdtrId', type=Party53Choice, min=0, max=1, mutex_group=1, array=False),
	))

