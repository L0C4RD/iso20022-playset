# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveOrHistoricCurrencyAndAmount import ActiveOrHistoricCurrencyAndAmount
from ._ActiveOrHistoricCurrencyCode import ActiveOrHistoricCurrencyCode
from ._ISODate import ISODate

class AmountsAndValueDate4(base_types._BaseFieldType):

	__slots__ = ["_CallAmt", "_FnlSttlmDt", "_OptnSttlmCcy", "_PutAmt"]
	@property
	def CallAmt(self):
		return self._CallAmt

	@CallAmt.setter
	def CallAmt(self, value):
		self._CallAmt = value if type(value) != base_types.auto else self.make_default("CallAmt")

	@CallAmt.deleter
	def CallAmt(self):
		del self._CallAmt
		self._CallAmt = None

	@property
	def FnlSttlmDt(self):
		return self._FnlSttlmDt

	@FnlSttlmDt.setter
	def FnlSttlmDt(self, value):
		self._FnlSttlmDt = value if type(value) != base_types.auto else self.make_default("FnlSttlmDt")

	@FnlSttlmDt.deleter
	def FnlSttlmDt(self):
		del self._FnlSttlmDt
		self._FnlSttlmDt = None

	@property
	def OptnSttlmCcy(self):
		return self._OptnSttlmCcy

	@OptnSttlmCcy.setter
	def OptnSttlmCcy(self, value):
		self._OptnSttlmCcy = value if type(value) != base_types.auto else self.make_default("OptnSttlmCcy")

	@OptnSttlmCcy.deleter
	def OptnSttlmCcy(self):
		del self._OptnSttlmCcy
		self._OptnSttlmCcy = None

	@property
	def PutAmt(self):
		return self._PutAmt

	@PutAmt.setter
	def PutAmt(self, value):
		self._PutAmt = value if type(value) != base_types.auto else self.make_default("PutAmt")

	@PutAmt.deleter
	def PutAmt(self):
		del self._PutAmt
		self._PutAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='CallAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FnlSttlmDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OptnSttlmCcy', type=ActiveOrHistoricCurrencyCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PutAmt', type=ActiveOrHistoricCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))