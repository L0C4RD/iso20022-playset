from . import base_types
from ._Max35Text import Max35Text
from ._SupplementaryData1 import SupplementaryData1
from ._YesNoIndicator import YesNoIndicator

class InformationRequestStatusChangeNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_CnfdtltySts", "_OrgnlBizQry", "_SplmtryData"]
	@property
	def CnfdtltySts(self):
		return self._CnfdtltySts

	@CnfdtltySts.setter
	def CnfdtltySts(self, value):
		self._CnfdtltySts = value if type(value) != base_types.auto else self.make_default("CnfdtltySts")

	@CnfdtltySts.deleter
	def CnfdtltySts(self):
		del self._CnfdtltySts
		self._CnfdtltySts = None

	@property
	def OrgnlBizQry(self):
		return self._OrgnlBizQry

	@OrgnlBizQry.setter
	def OrgnlBizQry(self, value):
		self._OrgnlBizQry = value if type(value) != base_types.auto else self.make_default("OrgnlBizQry")

	@OrgnlBizQry.deleter
	def OrgnlBizQry(self):
		del self._OrgnlBizQry
		self._OrgnlBizQry = None

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != base_types.auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CnfdtltySts', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizQry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))

