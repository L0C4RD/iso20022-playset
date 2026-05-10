import base_types
import Max35Text
import SupplementaryData1
import YesNoIndicator

class InformationRequestStatusChangeNotificationV01(base_types._BaseFieldType):

	__slots__ = ["_SplmtryData", "_CnfdtltySts", "_OrgnlBizQry"]
	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if type(value) != auto else self.make_default("SplmtryData")

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = None

	@property
	def CnfdtltySts(self):
		return self._CnfdtltySts

	@CnfdtltySts.setter
	def CnfdtltySts(self, value):
		self._CnfdtltySts = value if type(value) != auto else self.make_default("CnfdtltySts")

	@CnfdtltySts.deleter
	def CnfdtltySts(self):
		del self._CnfdtltySts
		self._CnfdtltySts = None

	@property
	def OrgnlBizQry(self):
		return self._OrgnlBizQry

	@OrgnlBizQry.setter
	def OrgnlBizQry(self, value):
		self._OrgnlBizQry = value if type(value) != auto else self.make_default("OrgnlBizQry")

	@OrgnlBizQry.deleter
	def OrgnlBizQry(self):
		del self._OrgnlBizQry
		self._OrgnlBizQry = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CnfdtltySts', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrgnlBizQry', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
	))

