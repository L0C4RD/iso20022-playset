import base_types
import PartyIdentification2Choice
import Max350Text
import Max256Text

class CorporateActionNarrative1(base_types._BaseFieldType):

	__slots__ = ["_InfConds", "_Offerr", "_TaxtnConds", "_AddtlTxt", "_URLAdr", "_InfToCmplyWth", "_NewCpnyNm"]
	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if type(value) != auto else self.make_default("InfConds")

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = None

	@property
	def Offerr(self):
		return self._Offerr

	@Offerr.setter
	def Offerr(self, value):
		self._Offerr = value if type(value) != auto else self.make_default("Offerr")

	@Offerr.deleter
	def Offerr(self):
		del self._Offerr
		self._Offerr = None

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if type(value) != auto else self.make_default("TaxtnConds")

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = None

	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def URLAdr(self):
		return self._URLAdr

	@URLAdr.setter
	def URLAdr(self, value):
		self._URLAdr = value if type(value) != auto else self.make_default("URLAdr")

	@URLAdr.deleter
	def URLAdr(self):
		del self._URLAdr
		self._URLAdr = None

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if type(value) != auto else self.make_default("InfToCmplyWth")

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = None

	@property
	def NewCpnyNm(self):
		return self._NewCpnyNm

	@NewCpnyNm.setter
	def NewCpnyNm(self, value):
		self._NewCpnyNm = value if type(value) != auto else self.make_default("NewCpnyNm")

	@NewCpnyNm.deleter
	def NewCpnyNm(self):
		del self._NewCpnyNm
		self._NewCpnyNm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='InfConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Offerr', type=PartyIdentification2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='URLAdr', type=Max256Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NewCpnyNm', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

