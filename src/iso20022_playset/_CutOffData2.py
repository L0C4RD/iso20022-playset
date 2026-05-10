from . import base_types
from ._NettingCutOff2 import NettingCutOff2
from ._PartyIdentification242Choice import PartyIdentification242Choice

class CutOffData2(base_types._BaseFieldType):

	__slots__ = ["_NetgCutOffDtls", "_PtcptId"]
	@property
	def NetgCutOffDtls(self):
		return self._NetgCutOffDtls

	@NetgCutOffDtls.setter
	def NetgCutOffDtls(self, value):
		self._NetgCutOffDtls = value if type(value) != base_types.auto else self.make_default("NetgCutOffDtls")

	@NetgCutOffDtls.deleter
	def NetgCutOffDtls(self):
		del self._NetgCutOffDtls
		self._NetgCutOffDtls = None

	@property
	def PtcptId(self):
		return self._PtcptId

	@PtcptId.setter
	def PtcptId(self, value):
		self._PtcptId = value if type(value) != base_types.auto else self.make_default("PtcptId")

	@PtcptId.deleter
	def PtcptId(self):
		del self._PtcptId
		self._PtcptId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NetgCutOffDtls', type=NettingCutOff2, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PtcptId', type=PartyIdentification242Choice, min=1, max=1, mutex_group=None, array=False),
	))

