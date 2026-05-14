# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._ISODateTime import ISODateTime
from ._ProprietaryDate3 import ProprietaryDate3

class TransactionDates3(base_types._BaseFieldType):

	__slots__ = ["_AccptncDtTm", "_EndDt", "_IntrBkSttlmDt", "_Prtry", "_StartDt", "_TradActvtyCtrctlSttlmDt", "_TradDt", "_TxDtTm"]
	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if type(value) != base_types.auto else self.make_default("AccptncDtTm")

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = None

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if type(value) != base_types.auto else self.make_default("EndDt")

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = None

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if type(value) != base_types.auto else self.make_default("IntrBkSttlmDt")

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = None

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if type(value) != base_types.auto else self.make_default("StartDt")

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = None

	@property
	def TradActvtyCtrctlSttlmDt(self):
		return self._TradActvtyCtrctlSttlmDt

	@TradActvtyCtrctlSttlmDt.setter
	def TradActvtyCtrctlSttlmDt(self, value):
		self._TradActvtyCtrctlSttlmDt = value if type(value) != base_types.auto else self.make_default("TradActvtyCtrctlSttlmDt")

	@TradActvtyCtrctlSttlmDt.deleter
	def TradActvtyCtrctlSttlmDt(self):
		del self._TradActvtyCtrctlSttlmDt
		self._TradActvtyCtrctlSttlmDt = None

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if type(value) != base_types.auto else self.make_default("TradDt")

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = None

	@property
	def TxDtTm(self):
		return self._TxDtTm

	@TxDtTm.setter
	def TxDtTm(self, value):
		self._TxDtTm = value if type(value) != base_types.auto else self.make_default("TxDtTm")

	@TxDtTm.deleter
	def TxDtTm(self):
		del self._TxDtTm
		self._TxDtTm = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptncDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntrBkSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prtry', type=ProprietaryDate3, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StartDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradActvtyCtrctlSttlmDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))