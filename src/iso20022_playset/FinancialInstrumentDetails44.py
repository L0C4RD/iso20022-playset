from . import base_types
import FinancialInstrumentAttributes119
import IntraPositionDetails63
import SecurityIdentification20

class FinancialInstrumentDetails44(base_types._BaseFieldType):

	__slots__ = ["_FinInstrmId", "_SubBal", "_FinInstrmAttrbts"]
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

	@property
	def SubBal(self):
		return self._SubBal

	@SubBal.setter
	def SubBal(self, value):
		self._SubBal = value if type(value) != auto else self.make_default("SubBal")

	@SubBal.deleter
	def SubBal(self):
		del self._SubBal
		self._SubBal = None

	@property
	def FinInstrmAttrbts(self):
		return self._FinInstrmAttrbts

	@FinInstrmAttrbts.setter
	def FinInstrmAttrbts(self, value):
		self._FinInstrmAttrbts = value if type(value) != auto else self.make_default("FinInstrmAttrbts")

	@FinInstrmAttrbts.deleter
	def FinInstrmAttrbts(self):
		del self._FinInstrmAttrbts
		self._FinInstrmAttrbts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubBal', type=IntraPositionDetails63, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FinInstrmAttrbts', type=FinancialInstrumentAttributes119, min=0, max=1, mutex_group=None, array=False),
	))

