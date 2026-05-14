# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._ISODate import ISODate
from ._Max70Text import Max70Text
from ._PaymentMeans1 import PaymentMeans1

class Instalment2(base_types._BaseFieldType):

	__slots__ = ["_Amt", "_PmtDueDt", "_PmtInstrm", "_SeqId"]
	@property
	def Amt(self):
		return self._Amt

	@Amt.setter
	def Amt(self, value):
		self._Amt = value if type(value) != base_types.auto else self.make_default("Amt")

	@Amt.deleter
	def Amt(self):
		del self._Amt
		self._Amt = None

	@property
	def PmtDueDt(self):
		return self._PmtDueDt

	@PmtDueDt.setter
	def PmtDueDt(self, value):
		self._PmtDueDt = value if type(value) != base_types.auto else self.make_default("PmtDueDt")

	@PmtDueDt.deleter
	def PmtDueDt(self):
		del self._PmtDueDt
		self._PmtDueDt = None

	@property
	def PmtInstrm(self):
		return self._PmtInstrm

	@PmtInstrm.setter
	def PmtInstrm(self, value):
		self._PmtInstrm = value if type(value) != base_types.auto else self.make_default("PmtInstrm")

	@PmtInstrm.deleter
	def PmtInstrm(self):
		del self._PmtInstrm
		self._PmtInstrm = None

	@property
	def SeqId(self):
		return self._SeqId

	@SeqId.setter
	def SeqId(self, value):
		self._SeqId = value if type(value) != base_types.auto else self.make_default("SeqId")

	@SeqId.deleter
	def SeqId(self):
		del self._SeqId
		self._SeqId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Amt', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtDueDt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PmtInstrm', type=PaymentMeans1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SeqId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
	))