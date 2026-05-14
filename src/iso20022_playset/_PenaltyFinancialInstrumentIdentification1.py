from . import base_types
from ._ClassificationType1Choice import ClassificationType1Choice
from ._ForeignExchangeRate3 import ForeignExchangeRate3
from ._PenaltyRate1 import PenaltyRate1
from ._PriceInformation25 import PriceInformation25
from ._SecurityIdentification19 import SecurityIdentification19
from ._TrueFalseIndicator import TrueFalseIndicator

class PenaltyFinancialInstrumentIdentification1(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_FXData", "_Id", "_Lqdty", "_PricData", "_SbjtToPnlties", "_SctiesPnltyRateData"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if type(value) != base_types.auto else self.make_default("ClssfctnTp")

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = None

	@property
	def FXData(self):
		return self._FXData

	@FXData.setter
	def FXData(self, value):
		self._FXData = value if type(value) != base_types.auto else self.make_default("FXData")

	@FXData.deleter
	def FXData(self):
		del self._FXData
		self._FXData = None

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if type(value) != base_types.auto else self.make_default("Id")

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = None

	@property
	def Lqdty(self):
		return self._Lqdty

	@Lqdty.setter
	def Lqdty(self, value):
		self._Lqdty = value if type(value) != base_types.auto else self.make_default("Lqdty")

	@Lqdty.deleter
	def Lqdty(self):
		del self._Lqdty
		self._Lqdty = None

	@property
	def PricData(self):
		return self._PricData

	@PricData.setter
	def PricData(self, value):
		self._PricData = value if type(value) != base_types.auto else self.make_default("PricData")

	@PricData.deleter
	def PricData(self):
		del self._PricData
		self._PricData = None

	@property
	def SbjtToPnlties(self):
		return self._SbjtToPnlties

	@SbjtToPnlties.setter
	def SbjtToPnlties(self, value):
		self._SbjtToPnlties = value if type(value) != base_types.auto else self.make_default("SbjtToPnlties")

	@SbjtToPnlties.deleter
	def SbjtToPnlties(self):
		del self._SbjtToPnlties
		self._SbjtToPnlties = None

	@property
	def SctiesPnltyRateData(self):
		return self._SctiesPnltyRateData

	@SctiesPnltyRateData.setter
	def SctiesPnltyRateData(self, value):
		self._SctiesPnltyRateData = value if type(value) != base_types.auto else self.make_default("SctiesPnltyRateData")

	@SctiesPnltyRateData.deleter
	def SctiesPnltyRateData(self):
		del self._SctiesPnltyRateData
		self._SctiesPnltyRateData = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXData', type=ForeignExchangeRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricData', type=PriceInformation25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtToPnlties', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesPnltyRateData', type=PenaltyRate1, min=0, max=1, mutex_group=None, array=False),
	))

