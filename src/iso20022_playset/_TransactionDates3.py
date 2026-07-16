# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ISODateTime
from . import ProprietaryDate3

class TransactionDates3(base_types._BaseFieldType):

	__slots__ = ["_AccptncDtTm", "_EndDt", "_IntrBkSttlmDt", "_Prtry", "_StartDt", "_TradActvtyCtrctlSttlmDt", "_TradDt", "_TxDtTm"]
	@property
	def AccptncDtTm(self):
		return self._AccptncDtTm

	@AccptncDtTm.setter
	def AccptncDtTm(self, value):
		self._AccptncDtTm = value if value is not None else base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@AccptncDtTm.deleter
	def AccptncDtTm(self):
		del self._AccptncDtTm
		self._AccptncDtTm = base_types.UninitialisedField(self, 'AccptncDtTm', ISODateTime, False)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', ISODate, False)

	@property
	def IntrBkSttlmDt(self):
		return self._IntrBkSttlmDt

	@IntrBkSttlmDt.setter
	def IntrBkSttlmDt(self, value):
		self._IntrBkSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@IntrBkSttlmDt.deleter
	def IntrBkSttlmDt(self):
		del self._IntrBkSttlmDt
		self._IntrBkSttlmDt = base_types.UninitialisedField(self, 'IntrBkSttlmDt', ISODate, False)

	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', ProprietaryDate3, True)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', ProprietaryDate3, True)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', ISODate, False)

	@property
	def TradActvtyCtrctlSttlmDt(self):
		return self._TradActvtyCtrctlSttlmDt

	@TradActvtyCtrctlSttlmDt.setter
	def TradActvtyCtrctlSttlmDt(self, value):
		self._TradActvtyCtrctlSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'TradActvtyCtrctlSttlmDt', ISODate, False)

	@TradActvtyCtrctlSttlmDt.deleter
	def TradActvtyCtrctlSttlmDt(self):
		del self._TradActvtyCtrctlSttlmDt
		self._TradActvtyCtrctlSttlmDt = base_types.UninitialisedField(self, 'TradActvtyCtrctlSttlmDt', ISODate, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', ISODate, False)

	@property
	def TxDtTm(self):
		return self._TxDtTm

	@TxDtTm.setter
	def TxDtTm(self, value):
		self._TxDtTm = value if value is not None else base_types.UninitialisedField(self, 'TxDtTm', ISODateTime, False)

	@TxDtTm.deleter
	def TxDtTm(self):
		del self._TxDtTm
		self._TxDtTm = base_types.UninitialisedField(self, 'TxDtTm', ISODateTime, False)

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