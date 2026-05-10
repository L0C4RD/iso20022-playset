from . import base_types
from ._CommonFinancialInstrumentAttributes11 import CommonFinancialInstrumentAttributes11
from ._FinancialInstrument97 import FinancialInstrument97
from ._SecurityIdentification39 import SecurityIdentification39

class SecurityAttributes11(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmAttrbts", "_FinInstrmId", "_FinInstrmTp"]
	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != base_types.auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	@property
	def FinInstrmId(self):
		return self._FinInstrmId

	@FinInstrmId.setter
	def FinInstrmId(self, value):
		self._FinInstrmId = value if type(value) != base_types.auto else self.make_default("FinInstrmId")

	@FinInstrmId.deleter
	def FinInstrmId(self):
		del self._FinInstrmId
		self._FinInstrmId = None

	@property
	def FinInstrmTp(self):
		return self._FinInstrmTp

	@FinInstrmTp.setter
	def FinInstrmTp(self, value):
		self._FinInstrmTp = value if type(value) != base_types.auto else self.make_default("FinInstrmTp")

	@FinInstrmTp.deleter
	def FinInstrmTp(self):
		del self._FinInstrmTp
		self._FinInstrmTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmAttrbts', type=CommonFinancialInstrumentAttributes11, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmTp', type=FinancialInstrument97, min=0, max=1, mutex_group=None, array=False),
	))

