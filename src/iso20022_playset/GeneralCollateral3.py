from . import base_types
import FinancialInstrument59
import ISINOct2015Identifier

class GeneralCollateral3(base_types._BaseFieldType):

	__slots__ = ["_ElgblFinInstrmId", "_FinInstrmId"]
	@property
	def ElgblFinInstrmId(self):
		return self._ElgblFinInstrmId

	@ElgblFinInstrmId.setter
	def ElgblFinInstrmId(self, value):
		self._ElgblFinInstrmId = value if type(value) != auto else self.make_default("ElgblFinInstrmId")

	@ElgblFinInstrmId.deleter
	def ElgblFinInstrmId(self):
		del self._ElgblFinInstrmId
		self._ElgblFinInstrmId = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ElgblFinInstrmId', type=ISINOct2015Identifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=FinancialInstrument59, min=0, max=None, mutex_group=None, array=True),
	))

