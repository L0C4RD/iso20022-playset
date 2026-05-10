from . import base_types
from ._Max35Text import Max35Text

class MaintenanceIdentificationAssociation1(base_types._BaseFieldType):

	__slots__ = ["_MstrTMId", "_TMId"]
	@property
	def MstrTMId(self):
		return self._MstrTMId

	@MstrTMId.setter
	def MstrTMId(self, value):
		self._MstrTMId = value if type(value) != base_types.auto else self.make_default("MstrTMId")

	@MstrTMId.deleter
	def MstrTMId(self):
		del self._MstrTMId
		self._MstrTMId = None

	@property
	def TMId(self):
		return self._TMId

	@TMId.setter
	def TMId(self, value):
		self._TMId = value if type(value) != base_types.auto else self.make_default("TMId")

	@TMId.deleter
	def TMId(self):
		del self._TMId
		self._TMId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MstrTMId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

