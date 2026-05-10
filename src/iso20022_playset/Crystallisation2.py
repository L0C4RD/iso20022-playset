import base_types
import ActiveCurrencyAnd13DecimalAmount
import Max35Text
import AdditionalInformation15
import DecimalNumber

class Crystallisation2(base_types._BaseFieldType):

	__slots__ = ["_UcrstllsdAmt", "_TrchId", "_CrstllsdAmt", "_AddtlInf", "_UcrstllsdUnitsNb", "_CrstllsdUnitsNb"]
	@property
	def UcrstllsdAmt(self):
		return self._UcrstllsdAmt

	@UcrstllsdAmt.setter
	def UcrstllsdAmt(self, value):
		self._UcrstllsdAmt = value if type(value) != auto else self.make_default("UcrstllsdAmt")

	@UcrstllsdAmt.deleter
	def UcrstllsdAmt(self):
		del self._UcrstllsdAmt
		self._UcrstllsdAmt = None

	@property
	def TrchId(self):
		return self._TrchId

	@TrchId.setter
	def TrchId(self, value):
		self._TrchId = value if type(value) != auto else self.make_default("TrchId")

	@TrchId.deleter
	def TrchId(self):
		del self._TrchId
		self._TrchId = None

	@property
	def CrstllsdAmt(self):
		return self._CrstllsdAmt

	@CrstllsdAmt.setter
	def CrstllsdAmt(self, value):
		self._CrstllsdAmt = value if type(value) != auto else self.make_default("CrstllsdAmt")

	@CrstllsdAmt.deleter
	def CrstllsdAmt(self):
		del self._CrstllsdAmt
		self._CrstllsdAmt = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def UcrstllsdUnitsNb(self):
		return self._UcrstllsdUnitsNb

	@UcrstllsdUnitsNb.setter
	def UcrstllsdUnitsNb(self, value):
		self._UcrstllsdUnitsNb = value if type(value) != auto else self.make_default("UcrstllsdUnitsNb")

	@UcrstllsdUnitsNb.deleter
	def UcrstllsdUnitsNb(self):
		del self._UcrstllsdUnitsNb
		self._UcrstllsdUnitsNb = None

	@property
	def CrstllsdUnitsNb(self):
		return self._CrstllsdUnitsNb

	@CrstllsdUnitsNb.setter
	def CrstllsdUnitsNb(self, value):
		self._CrstllsdUnitsNb = value if type(value) != auto else self.make_default("CrstllsdUnitsNb")

	@CrstllsdUnitsNb.deleter
	def CrstllsdUnitsNb(self):
		del self._CrstllsdUnitsNb
		self._CrstllsdUnitsNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='UcrstllsdAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrchId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllsdAmt', type=ActiveCurrencyAnd13DecimalAmount, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UcrstllsdUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CrstllsdUnitsNb', type=DecimalNumber, min=0, max=1, mutex_group=None, array=False),
	))

