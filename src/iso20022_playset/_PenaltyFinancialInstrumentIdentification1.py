# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ClassificationType1Choice
from . import ForeignExchangeRate3
from . import PenaltyRate1
from . import PriceInformation25
from . import SecurityIdentification19
from . import TrueFalseIndicator

class PenaltyFinancialInstrumentIdentification1(base_types._BaseFieldType):

	__slots__ = ["_ClssfctnTp", "_FXData", "_Id", "_Lqdty", "_PricData", "_SbjtToPnlties", "_SctiesPnltyRateData"]
	@property
	def ClssfctnTp(self):
		return self._ClssfctnTp

	@ClssfctnTp.setter
	def ClssfctnTp(self, value):
		self._ClssfctnTp = value if value is not None else base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType1Choice, False)

	@ClssfctnTp.deleter
	def ClssfctnTp(self):
		del self._ClssfctnTp
		self._ClssfctnTp = base_types.UninitialisedField(self, 'ClssfctnTp', ClassificationType1Choice, False)

	@property
	def FXData(self):
		return self._FXData

	@FXData.setter
	def FXData(self, value):
		self._FXData = value if value is not None else base_types.UninitialisedField(self, 'FXData', ForeignExchangeRate3, True)

	@FXData.deleter
	def FXData(self):
		del self._FXData
		self._FXData = base_types.UninitialisedField(self, 'FXData', ForeignExchangeRate3, True)

	@property
	def Id(self):
		return self._Id

	@Id.setter
	def Id(self, value):
		self._Id = value if value is not None else base_types.UninitialisedField(self, 'Id', SecurityIdentification19, False)

	@Id.deleter
	def Id(self):
		del self._Id
		self._Id = base_types.UninitialisedField(self, 'Id', SecurityIdentification19, False)

	@property
	def Lqdty(self):
		return self._Lqdty

	@Lqdty.setter
	def Lqdty(self, value):
		self._Lqdty = value if value is not None else base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@Lqdty.deleter
	def Lqdty(self):
		del self._Lqdty
		self._Lqdty = base_types.UninitialisedField(self, 'Lqdty', TrueFalseIndicator, False)

	@property
	def PricData(self):
		return self._PricData

	@PricData.setter
	def PricData(self, value):
		self._PricData = value if value is not None else base_types.UninitialisedField(self, 'PricData', PriceInformation25, False)

	@PricData.deleter
	def PricData(self):
		del self._PricData
		self._PricData = base_types.UninitialisedField(self, 'PricData', PriceInformation25, False)

	@property
	def SbjtToPnlties(self):
		return self._SbjtToPnlties

	@SbjtToPnlties.setter
	def SbjtToPnlties(self, value):
		self._SbjtToPnlties = value if value is not None else base_types.UninitialisedField(self, 'SbjtToPnlties', TrueFalseIndicator, False)

	@SbjtToPnlties.deleter
	def SbjtToPnlties(self):
		del self._SbjtToPnlties
		self._SbjtToPnlties = base_types.UninitialisedField(self, 'SbjtToPnlties', TrueFalseIndicator, False)

	@property
	def SctiesPnltyRateData(self):
		return self._SctiesPnltyRateData

	@SctiesPnltyRateData.setter
	def SctiesPnltyRateData(self, value):
		self._SctiesPnltyRateData = value if value is not None else base_types.UninitialisedField(self, 'SctiesPnltyRateData', PenaltyRate1, False)

	@SctiesPnltyRateData.deleter
	def SctiesPnltyRateData(self):
		del self._SctiesPnltyRateData
		self._SctiesPnltyRateData = base_types.UninitialisedField(self, 'SctiesPnltyRateData', PenaltyRate1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ClssfctnTp', type=ClassificationType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FXData', type=ForeignExchangeRate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Id', type=SecurityIdentification19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lqdty', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricData', type=PriceInformation25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SbjtToPnlties', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesPnltyRateData', type=PenaltyRate1, min=0, max=1, mutex_group=None, array=False),
	))