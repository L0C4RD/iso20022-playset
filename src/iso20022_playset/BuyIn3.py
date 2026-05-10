import base_types
import Max35Text
import FinancialInstrumentQuantity1Choice
import Number
import YesNoIndicator

class BuyIn3(base_types._BaseFieldType):

	__slots__ = ["_CvrdQty", "_ReqForDelyInd", "_UcvrdQty", "_BuyInNtfctnId", "_NbOfDays", "_InitlQty"]
	@property
	def CvrdQty(self):
		return self._CvrdQty

	@CvrdQty.setter
	def CvrdQty(self, value):
		self._CvrdQty = value if type(value) != auto else self.make_default("CvrdQty")

	@CvrdQty.deleter
	def CvrdQty(self):
		del self._CvrdQty
		self._CvrdQty = None

	@property
	def ReqForDelyInd(self):
		return self._ReqForDelyInd

	@ReqForDelyInd.setter
	def ReqForDelyInd(self, value):
		self._ReqForDelyInd = value if type(value) != auto else self.make_default("ReqForDelyInd")

	@ReqForDelyInd.deleter
	def ReqForDelyInd(self):
		del self._ReqForDelyInd
		self._ReqForDelyInd = None

	@property
	def UcvrdQty(self):
		return self._UcvrdQty

	@UcvrdQty.setter
	def UcvrdQty(self, value):
		self._UcvrdQty = value if type(value) != auto else self.make_default("UcvrdQty")

	@UcvrdQty.deleter
	def UcvrdQty(self):
		del self._UcvrdQty
		self._UcvrdQty = None

	@property
	def BuyInNtfctnId(self):
		return self._BuyInNtfctnId

	@BuyInNtfctnId.setter
	def BuyInNtfctnId(self, value):
		self._BuyInNtfctnId = value if type(value) != auto else self.make_default("BuyInNtfctnId")

	@BuyInNtfctnId.deleter
	def BuyInNtfctnId(self):
		del self._BuyInNtfctnId
		self._BuyInNtfctnId = None

	@property
	def NbOfDays(self):
		return self._NbOfDays

	@NbOfDays.setter
	def NbOfDays(self, value):
		self._NbOfDays = value if type(value) != auto else self.make_default("NbOfDays")

	@NbOfDays.deleter
	def NbOfDays(self):
		del self._NbOfDays
		self._NbOfDays = None

	@property
	def InitlQty(self):
		return self._InitlQty

	@InitlQty.setter
	def InitlQty(self, value):
		self._InitlQty = value if type(value) != auto else self.make_default("InitlQty")

	@InitlQty.deleter
	def InitlQty(self):
		del self._InitlQty
		self._InitlQty = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CvrdQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqForDelyInd', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UcvrdQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BuyInNtfctnId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDays', type=Number, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InitlQty', type=FinancialInstrumentQuantity1Choice, min=1, max=1, mutex_group=None, array=False),
	))

