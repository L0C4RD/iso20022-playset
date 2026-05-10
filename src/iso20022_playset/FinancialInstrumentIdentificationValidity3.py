from . import base_types
import ISODate
import SecurityIdentification39

class FinancialInstrumentIdentificationValidity3(base_types._BaseFieldType):

	__slots__ = ["_ISINVldFr", "_FinInstrmId"]
	@property
	def ISINVldFr(self):
		return self._ISINVldFr

	@ISINVldFr.setter
	def ISINVldFr(self, value):
		self._ISINVldFr = value if type(value) != auto else self.make_default("ISINVldFr")

	@ISINVldFr.deleter
	def ISINVldFr(self):
		del self._ISINVldFr
		self._ISINVldFr = None

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
		base_types.FieldEntry(name='ISINVldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FinInstrmId', type=SecurityIdentification39, min=0, max=1, mutex_group=None, array=False),
	))

