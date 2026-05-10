from . import base_types
from .Max35Text import Max35Text
from .StatusReportContent14 import StatusReportContent14
from .HostStatus1 import HostStatus1

class DiagnosisResponse7(base_types._BaseFieldType):

	__slots__ = ["_POISts", "_HstSts", "_LggdSaleId"]
	@property
	def POISts(self):
		return self._POISts

	@POISts.setter
	def POISts(self, value):
		self._POISts = value if type(value) != base_types.auto else self.make_default("POISts")

	@POISts.deleter
	def POISts(self):
		del self._POISts
		self._POISts = None

	@property
	def HstSts(self):
		return self._HstSts

	@HstSts.setter
	def HstSts(self, value):
		self._HstSts = value if type(value) != base_types.auto else self.make_default("HstSts")

	@HstSts.deleter
	def HstSts(self):
		del self._HstSts
		self._HstSts = None

	@property
	def LggdSaleId(self):
		return self._LggdSaleId

	@LggdSaleId.setter
	def LggdSaleId(self, value):
		self._LggdSaleId = value if type(value) != base_types.auto else self.make_default("LggdSaleId")

	@LggdSaleId.deleter
	def LggdSaleId(self):
		del self._LggdSaleId
		self._LggdSaleId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='POISts', type=StatusReportContent14, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='HstSts', type=HostStatus1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='LggdSaleId', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
	))

