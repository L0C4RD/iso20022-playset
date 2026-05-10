from . import base_types
from ._Max350Text import Max350Text

class CorporateActionNarrative2(base_types._BaseFieldType):

	__slots__ = ["_AddtlTxt", "_DclrtnDtls", "_InfConds", "_InfToCmplyWth", "_RegnDtls", "_TaxtnConds"]
	@property
	def AddtlTxt(self):
		return self._AddtlTxt

	@AddtlTxt.setter
	def AddtlTxt(self, value):
		self._AddtlTxt = value if type(value) != base_types.auto else self.make_default("AddtlTxt")

	@AddtlTxt.deleter
	def AddtlTxt(self):
		del self._AddtlTxt
		self._AddtlTxt = None

	@property
	def DclrtnDtls(self):
		return self._DclrtnDtls

	@DclrtnDtls.setter
	def DclrtnDtls(self, value):
		self._DclrtnDtls = value if type(value) != base_types.auto else self.make_default("DclrtnDtls")

	@DclrtnDtls.deleter
	def DclrtnDtls(self):
		del self._DclrtnDtls
		self._DclrtnDtls = None

	@property
	def InfConds(self):
		return self._InfConds

	@InfConds.setter
	def InfConds(self, value):
		self._InfConds = value if type(value) != base_types.auto else self.make_default("InfConds")

	@InfConds.deleter
	def InfConds(self):
		del self._InfConds
		self._InfConds = None

	@property
	def InfToCmplyWth(self):
		return self._InfToCmplyWth

	@InfToCmplyWth.setter
	def InfToCmplyWth(self, value):
		self._InfToCmplyWth = value if type(value) != base_types.auto else self.make_default("InfToCmplyWth")

	@InfToCmplyWth.deleter
	def InfToCmplyWth(self):
		del self._InfToCmplyWth
		self._InfToCmplyWth = None

	@property
	def RegnDtls(self):
		return self._RegnDtls

	@RegnDtls.setter
	def RegnDtls(self, value):
		self._RegnDtls = value if type(value) != base_types.auto else self.make_default("RegnDtls")

	@RegnDtls.deleter
	def RegnDtls(self):
		del self._RegnDtls
		self._RegnDtls = None

	@property
	def TaxtnConds(self):
		return self._TaxtnConds

	@TaxtnConds.setter
	def TaxtnConds(self, value):
		self._TaxtnConds = value if type(value) != base_types.auto else self.make_default("TaxtnConds")

	@TaxtnConds.deleter
	def TaxtnConds(self):
		del self._TaxtnConds
		self._TaxtnConds = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlTxt', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DclrtnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InfToCmplyWth', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxtnConds', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
	))

