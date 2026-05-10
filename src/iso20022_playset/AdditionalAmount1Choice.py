import base_types
import ActiveOrHistoricCurrencyAndAmount

class AdditionalAmount1Choice(base_types._BaseFieldType):

	__slots__ = ["_RsltgCshOut", "_AddtlCshIn"]
	@property
	def RsltgCshOut(self):
		return self._RsltgCshOut

	@RsltgCshOut.setter
	def RsltgCshOut(self, value):
		self._RsltgCshOut = value if type(value) != auto else self.make_default("RsltgCshOut")

	@RsltgCshOut.deleter
	def RsltgCshOut(self):
		del self._RsltgCshOut
		self._RsltgCshOut = None

	@property
	def AddtlCshIn(self):
		return self._AddtlCshIn

	@AddtlCshIn.setter
	def AddtlCshIn(self, value):
		self._AddtlCshIn = value if type(value) != auto else self.make_default("AddtlCshIn")

	@AddtlCshIn.deleter
	def AddtlCshIn(self):
		del self._AddtlCshIn
		self._AddtlCshIn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RsltgCshOut', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='AddtlCshIn', type=ActiveOrHistoricCurrencyAndAmount, min=0, max=1, mutex_group=1, array=False),
	))

