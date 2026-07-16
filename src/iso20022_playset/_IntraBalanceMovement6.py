# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Amount2Choice
from . import CashSubBalanceTypeAndQuantityBreakdown3
from . import DateAndDateTime2Choice
from . import GenericIdentification37
from . import ISODateTime
from . import Linkages57
from . import Max350Text
from . import PriorityNumeric4Choice
from . import SupplementaryData1
from . import SystemPartyIdentification8

class IntraBalanceMovement6(base_types._BaseFieldType):

	__slots__ = ["_BalFr", "_BalTo", "_CreDtTm", "_CshSubBalId", "_FctvSttlmDt", "_InstrPrcgAddtlDtls", "_IntnddSttlmDt", "_Lnkgs", "_MsgOrgtr", "_PrevslySttldAmt", "_Prty", "_RmngSttlmAmt", "_SplmtryData", "_StsDt", "_SttldAmt", "_SttlmAmt"]
	@property
	def BalFr(self):
		return self._BalFr

	@BalFr.setter
	def BalFr(self, value):
		self._BalFr = value if value is not None else base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@BalFr.deleter
	def BalFr(self):
		del self._BalFr
		self._BalFr = base_types.UninitialisedField(self, 'BalFr', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def BalTo(self):
		return self._BalTo

	@BalTo.setter
	def BalTo(self, value):
		self._BalTo = value if value is not None else base_types.UninitialisedField(self, 'BalTo', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@BalTo.deleter
	def BalTo(self):
		del self._BalTo
		self._BalTo = base_types.UninitialisedField(self, 'BalTo', CashSubBalanceTypeAndQuantityBreakdown3, False)

	@property
	def CreDtTm(self):
		return self._CreDtTm

	@CreDtTm.setter
	def CreDtTm(self, value):
		self._CreDtTm = value if value is not None else base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@CreDtTm.deleter
	def CreDtTm(self):
		del self._CreDtTm
		self._CreDtTm = base_types.UninitialisedField(self, 'CreDtTm', ISODateTime, False)

	@property
	def CshSubBalId(self):
		return self._CshSubBalId

	@CshSubBalId.setter
	def CshSubBalId(self, value):
		self._CshSubBalId = value if value is not None else base_types.UninitialisedField(self, 'CshSubBalId', GenericIdentification37, False)

	@CshSubBalId.deleter
	def CshSubBalId(self):
		del self._CshSubBalId
		self._CshSubBalId = base_types.UninitialisedField(self, 'CshSubBalId', GenericIdentification37, False)

	@property
	def FctvSttlmDt(self):
		return self._FctvSttlmDt

	@FctvSttlmDt.setter
	def FctvSttlmDt(self, value):
		self._FctvSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@FctvSttlmDt.deleter
	def FctvSttlmDt(self):
		del self._FctvSttlmDt
		self._FctvSttlmDt = base_types.UninitialisedField(self, 'FctvSttlmDt', DateAndDateTime2Choice, False)

	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', Max350Text, False)

	@property
	def IntnddSttlmDt(self):
		return self._IntnddSttlmDt

	@IntnddSttlmDt.setter
	def IntnddSttlmDt(self, value):
		self._IntnddSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTime2Choice, False)

	@IntnddSttlmDt.deleter
	def IntnddSttlmDt(self):
		del self._IntnddSttlmDt
		self._IntnddSttlmDt = base_types.UninitialisedField(self, 'IntnddSttlmDt', DateAndDateTime2Choice, False)

	@property
	def Lnkgs(self):
		return self._Lnkgs

	@Lnkgs.setter
	def Lnkgs(self, value):
		self._Lnkgs = value if value is not None else base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@Lnkgs.deleter
	def Lnkgs(self):
		del self._Lnkgs
		self._Lnkgs = base_types.UninitialisedField(self, 'Lnkgs', Linkages57, True)

	@property
	def MsgOrgtr(self):
		return self._MsgOrgtr

	@MsgOrgtr.setter
	def MsgOrgtr(self, value):
		self._MsgOrgtr = value if value is not None else base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

	@MsgOrgtr.deleter
	def MsgOrgtr(self):
		del self._MsgOrgtr
		self._MsgOrgtr = base_types.UninitialisedField(self, 'MsgOrgtr', SystemPartyIdentification8, False)

	@property
	def PrevslySttldAmt(self):
		return self._PrevslySttldAmt

	@PrevslySttldAmt.setter
	def PrevslySttldAmt(self, value):
		self._PrevslySttldAmt = value if value is not None else base_types.UninitialisedField(self, 'PrevslySttldAmt', Amount2Choice, False)

	@PrevslySttldAmt.deleter
	def PrevslySttldAmt(self):
		del self._PrevslySttldAmt
		self._PrevslySttldAmt = base_types.UninitialisedField(self, 'PrevslySttldAmt', Amount2Choice, False)

	@property
	def Prty(self):
		return self._Prty

	@Prty.setter
	def Prty(self, value):
		self._Prty = value if value is not None else base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@Prty.deleter
	def Prty(self):
		del self._Prty
		self._Prty = base_types.UninitialisedField(self, 'Prty', PriorityNumeric4Choice, False)

	@property
	def RmngSttlmAmt(self):
		return self._RmngSttlmAmt

	@RmngSttlmAmt.setter
	def RmngSttlmAmt(self, value):
		self._RmngSttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'RmngSttlmAmt', Amount2Choice, False)

	@RmngSttlmAmt.deleter
	def RmngSttlmAmt(self):
		del self._RmngSttlmAmt
		self._RmngSttlmAmt = base_types.UninitialisedField(self, 'RmngSttlmAmt', Amount2Choice, False)

	@property
	def SplmtryData(self):
		return self._SplmtryData

	@SplmtryData.setter
	def SplmtryData(self, value):
		self._SplmtryData = value if value is not None else base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@SplmtryData.deleter
	def SplmtryData(self):
		del self._SplmtryData
		self._SplmtryData = base_types.UninitialisedField(self, 'SplmtryData', SupplementaryData1, True)

	@property
	def StsDt(self):
		return self._StsDt

	@StsDt.setter
	def StsDt(self, value):
		self._StsDt = value if value is not None else base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@StsDt.deleter
	def StsDt(self):
		del self._StsDt
		self._StsDt = base_types.UninitialisedField(self, 'StsDt', ISODateTime, False)

	@property
	def SttldAmt(self):
		return self._SttldAmt

	@SttldAmt.setter
	def SttldAmt(self, value):
		self._SttldAmt = value if value is not None else base_types.UninitialisedField(self, 'SttldAmt', Amount2Choice, False)

	@SttldAmt.deleter
	def SttldAmt(self):
		del self._SttldAmt
		self._SttldAmt = base_types.UninitialisedField(self, 'SttldAmt', Amount2Choice, False)

	@property
	def SttlmAmt(self):
		return self._SttlmAmt

	@SttlmAmt.setter
	def SttlmAmt(self, value):
		self._SttlmAmt = value if value is not None else base_types.UninitialisedField(self, 'SttlmAmt', Amount2Choice, False)

	@SttlmAmt.deleter
	def SttlmAmt(self):
		del self._SttlmAmt
		self._SttlmAmt = base_types.UninitialisedField(self, 'SttlmAmt', Amount2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BalFr', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='BalTo', type=CashSubBalanceTypeAndQuantityBreakdown3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CreDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CshSubBalId', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='FctvSttlmDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IntnddSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lnkgs', type=Linkages57, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='MsgOrgtr', type=SystemPartyIdentification8, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PrevslySttldAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prty', type=PriorityNumeric4Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RmngSttlmAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='StsDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttldAmt', type=Amount2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SttlmAmt', type=Amount2Choice, min=1, max=1, mutex_group=None, array=False),
	))