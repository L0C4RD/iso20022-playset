# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FinancialInstrumentQuantity1Choice
from . import Max35Text
from . import Number
from . import YesNoIndicator

class BuyIn3(base_types._BaseFieldType):

	__slots__ = ["_BuyInNtfctnId", "_CvrdQty", "_InitlQty", "_NbOfDays", "_ReqForDelyInd", "_UcvrdQty"]
	@property
	def BuyInNtfctnId(self):
		return self._BuyInNtfctnId

	@BuyInNtfctnId.setter
	def BuyInNtfctnId(self, value):
		self._BuyInNtfctnId = value if value is not None else base_types.UninitialisedField(self, 'BuyInNtfctnId', Max35Text, False)

	@BuyInNtfctnId.deleter
	def BuyInNtfctnId(self):
		del self._BuyInNtfctnId
		self._BuyInNtfctnId = base_types.UninitialisedField(self, 'BuyInNtfctnId', Max35Text, False)

	@property
	def CvrdQty(self):
		return self._CvrdQty

	@CvrdQty.setter
	def CvrdQty(self, value):
		self._CvrdQty = value if value is not None else base_types.UninitialisedField(self, 'CvrdQty', FinancialInstrumentQuantity1Choice, False)

	@CvrdQty.deleter
	def CvrdQty(self):
		del self._CvrdQty
		self._CvrdQty = base_types.UninitialisedField(self, 'CvrdQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def InitlQty(self):
		return self._InitlQty

	@InitlQty.setter
	def InitlQty(self, value):
		self._InitlQty = value if value is not None else base_types.UninitialisedField(self, 'InitlQty', FinancialInstrumentQuantity1Choice, False)

	@InitlQty.deleter
	def InitlQty(self):
		del self._InitlQty
		self._InitlQty = base_types.UninitialisedField(self, 'InitlQty', FinancialInstrumentQuantity1Choice, False)

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if value is not None else base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = base_types.UninitialisedField(self, 'NbOfDays', Number, False)

	@property
	def ReqForDelyInd(self):
		return self._ReqForDelyInd

	@ReqForDelyInd.setter
	def ReqForDelyInd(self, value):
		self._ReqForDelyInd = value if value is not None else base_types.UninitialisedField(self, 'ReqForDelyInd', YesNoIndicator, False)

	@ReqForDelyInd.deleter
	def ReqForDelyInd(self):
		del self._ReqForDelyInd
		self._ReqForDelyInd = base_types.UninitialisedField(self, 'ReqForDelyInd', YesNoIndicator, False)

	@property
	def UcvrdQty(self):
		return self._UcvrdQty

	@UcvrdQty.setter
	def UcvrdQty(self, value):
		self._UcvrdQty = value if value is not None else base_types.UninitialisedField(self, 'UcvrdQty', FinancialInstrumentQuantity1Choice, False)

	@UcvrdQty.deleter
	def UcvrdQty(self):
		del self._UcvrdQty
		self._UcvrdQty = base_types.UninitialisedField(self, 'UcvrdQty', FinancialInstrumentQuantity1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BuyInNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CvrdQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForDelyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcvrdQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))