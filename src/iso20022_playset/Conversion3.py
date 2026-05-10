from . import base_types
import FinancialInstrumentIdentification5
import AdditionalInformation15

class Conversion3(base_types._BaseFieldType):

	__slots__ = ["_OrgnlScty", "_AddtlInf"]
	@property
	def OrgnlScty(self):
		return self._OrgnlScty

	@OrgnlScty.setter
	def OrgnlScty(self, value):
		self._OrgnlScty = value if type(value) != auto else self.make_default("OrgnlScty")

	@OrgnlScty.deleter
	def OrgnlScty(self):
		del self._OrgnlScty
		self._OrgnlScty = None

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='OrgnlScty', type=FinancialInstrumentIdentification5, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
	))

