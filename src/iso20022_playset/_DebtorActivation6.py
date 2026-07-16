# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ContractReference1
from . import DateAndDateTime2Choice
from . import DocumentFormat2Choice
from . import Max140Text
from . import Max35Text
from . import Party53Choice
from . import RTPPartyIdentification2

class DebtorActivation6(base_types._BaseFieldType):

	__slots__ = ["_ActvtnReqDlvryPty", "_Cdtr", "_CstmrId", "_CtrctFrmtTp", "_CtrctRef", "_Dbtr", "_DbtrActvtnId", "_DbtrSolPrvdr", "_DdctdActvtnCd", "_DispNm", "_EndDt", "_StartDt", "_UltmtCdtr", "_UltmtDbtr"]
	@property
	def ActvtnReqDlvryPty(self):
		return self._ActvtnReqDlvryPty

	@ActvtnReqDlvryPty.setter
	def ActvtnReqDlvryPty(self, value):
		self._ActvtnReqDlvryPty = value if value is not None else base_types.UninitialisedField(self, 'ActvtnReqDlvryPty', RTPPartyIdentification2, False)

	@ActvtnReqDlvryPty.deleter
	def ActvtnReqDlvryPty(self):
		del self._ActvtnReqDlvryPty
		self._ActvtnReqDlvryPty = base_types.UninitialisedField(self, 'ActvtnReqDlvryPty', RTPPartyIdentification2, False)

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if value is not None else base_types.UninitialisedField(self, 'Cdtr', RTPPartyIdentification2, False)

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = base_types.UninitialisedField(self, 'Cdtr', RTPPartyIdentification2, False)

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if value is not None else base_types.UninitialisedField(self, 'CstmrId', Party53Choice, True)

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = base_types.UninitialisedField(self, 'CstmrId', Party53Choice, True)

	@property
	def CtrctFrmtTp(self):
		return self._CtrctFrmtTp

	@CtrctFrmtTp.setter
	def CtrctFrmtTp(self, value):
		self._CtrctFrmtTp = value if value is not None else base_types.UninitialisedField(self, 'CtrctFrmtTp', DocumentFormat2Choice, True)

	@CtrctFrmtTp.deleter
	def CtrctFrmtTp(self):
		del self._CtrctFrmtTp
		self._CtrctFrmtTp = base_types.UninitialisedField(self, 'CtrctFrmtTp', DocumentFormat2Choice, True)

	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if value is not None else base_types.UninitialisedField(self, 'CtrctRef', ContractReference1, True)

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = base_types.UninitialisedField(self, 'CtrctRef', ContractReference1, True)

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if value is not None else base_types.UninitialisedField(self, 'Dbtr', RTPPartyIdentification2, False)

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = base_types.UninitialisedField(self, 'Dbtr', RTPPartyIdentification2, False)

	@property
	def DbtrActvtnId(self):
		return self._DbtrActvtnId

	@DbtrActvtnId.setter
	def DbtrActvtnId(self, value):
		self._DbtrActvtnId = value if value is not None else base_types.UninitialisedField(self, 'DbtrActvtnId', Max35Text, False)

	@DbtrActvtnId.deleter
	def DbtrActvtnId(self):
		del self._DbtrActvtnId
		self._DbtrActvtnId = base_types.UninitialisedField(self, 'DbtrActvtnId', Max35Text, False)

	@property
	def DbtrSolPrvdr(self):
		return self._DbtrSolPrvdr

	@DbtrSolPrvdr.setter
	def DbtrSolPrvdr(self, value):
		self._DbtrSolPrvdr = value if value is not None else base_types.UninitialisedField(self, 'DbtrSolPrvdr', RTPPartyIdentification2, False)

	@DbtrSolPrvdr.deleter
	def DbtrSolPrvdr(self):
		del self._DbtrSolPrvdr
		self._DbtrSolPrvdr = base_types.UninitialisedField(self, 'DbtrSolPrvdr', RTPPartyIdentification2, False)

	@property
	def DdctdActvtnCd(self):
		return self._DdctdActvtnCd

	@DdctdActvtnCd.setter
	def DdctdActvtnCd(self, value):
		self._DdctdActvtnCd = value if value is not None else base_types.UninitialisedField(self, 'DdctdActvtnCd', Max35Text, False)

	@DdctdActvtnCd.deleter
	def DdctdActvtnCd(self):
		del self._DdctdActvtnCd
		self._DdctdActvtnCd = base_types.UninitialisedField(self, 'DdctdActvtnCd', Max35Text, False)

	@property
	def DispNm(self):
		return self._DispNm

	@DispNm.setter
	def DispNm(self, value):
		self._DispNm = value if value is not None else base_types.UninitialisedField(self, 'DispNm', Max140Text, False)

	@DispNm.deleter
	def DispNm(self):
		del self._DispNm
		self._DispNm = base_types.UninitialisedField(self, 'DispNm', Max140Text, False)

	@property
	def EndDt(self):
		return self._EndDt

	@EndDt.setter
	def EndDt(self, value):
		self._EndDt = value if value is not None else base_types.UninitialisedField(self, 'EndDt', DateAndDateTime2Choice, False)

	@EndDt.deleter
	def EndDt(self):
		del self._EndDt
		self._EndDt = base_types.UninitialisedField(self, 'EndDt', DateAndDateTime2Choice, False)

	@property
	def StartDt(self):
		return self._StartDt

	@StartDt.setter
	def StartDt(self, value):
		self._StartDt = value if value is not None else base_types.UninitialisedField(self, 'StartDt', DateAndDateTime2Choice, False)

	@StartDt.deleter
	def StartDt(self):
		del self._StartDt
		self._StartDt = base_types.UninitialisedField(self, 'StartDt', DateAndDateTime2Choice, False)

	@property
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtCdtr', RTPPartyIdentification2, False)

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = base_types.UninitialisedField(self, 'UltmtCdtr', RTPPartyIdentification2, False)

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if value is not None else base_types.UninitialisedField(self, 'UltmtDbtr', RTPPartyIdentification2, False)

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = base_types.UninitialisedField(self, 'UltmtDbtr', RTPPartyIdentification2, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ActvtnReqDlvryPty', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Cdtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CstmrId', type=Party53Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctFrmtTp', type=DocumentFormat2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CtrctRef', type=ContractReference1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Dbtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrActvtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DbtrSolPrvdr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DdctdActvtnCd', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DispNm', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='EndDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StartDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtCdtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UltmtDbtr', type=RTPPartyIdentification2, min=0, max=1, mutex_group=None, array=False),
	))