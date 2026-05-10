from . import base_types
from ._ContractReference1 import ContractReference1
from ._DateAndDateTime2Choice import DateAndDateTime2Choice
from ._DocumentFormat2Choice import DocumentFormat2Choice
from ._Max140Text import Max140Text
from ._Max35Text import Max35Text
from ._Party53Choice import Party53Choice
from ._RTPPartyIdentification2 import RTPPartyIdentification2

class DebtorActivation6(base_types._BaseFieldType):

	__slots__ = ["_ActvtnReqDlvryPty", "_Cdtr", "_CstmrId", "_CtrctFrmtTp", "_CtrctRef", "_Dbtr", "_DbtrActvtnId", "_DbtrSolPrvdr", "_DdctdActvtnCd", "_DispNm", "_EndDt", "_StartDt", "_UltmtCdtr", "_UltmtDbtr"]
	@property
	def ActvtnReqDlvryPty(self):
		return self._ActvtnReqDlvryPty

	@ActvtnReqDlvryPty.setter
	def ActvtnReqDlvryPty(self, value):
		self._ActvtnReqDlvryPty = value if type(value) != base_types.auto else self.make_default("ActvtnReqDlvryPty")

	@ActvtnReqDlvryPty.deleter
	def ActvtnReqDlvryPty(self):
		del self._ActvtnReqDlvryPty
		self._ActvtnReqDlvryPty = None

	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CstmrId(self):
		return self._CstmrId

	@CstmrId.setter
	def CstmrId(self, value):
		self._CstmrId = value if type(value) != base_types.auto else self.make_default("CstmrId")

	@CstmrId.deleter
	def CstmrId(self):
		del self._CstmrId
		self._CstmrId = None

	@property
	def CtrctFrmtTp(self):
		return self._CtrctFrmtTp

	@CtrctFrmtTp.setter
	def CtrctFrmtTp(self, value):
		self._CtrctFrmtTp = value if type(value) != base_types.auto else self.make_default("CtrctFrmtTp")

	@CtrctFrmtTp.deleter
	def CtrctFrmtTp(self):
		del self._CtrctFrmtTp
		self._CtrctFrmtTp = None

	@property
	def CtrctRef(self):
		return self._CtrctRef

	@CtrctRef.setter
	def CtrctRef(self, value):
		self._CtrctRef = value if type(value) != base_types.auto else self.make_default("CtrctRef")

	@CtrctRef.deleter
	def CtrctRef(self):
		del self._CtrctRef
		self._CtrctRef = None

	@property
	def Dbtr(self):
		return self._Dbtr

	@Dbtr.setter
	def Dbtr(self, value):
		self._Dbtr = value if type(value) != base_types.auto else self.make_default("Dbtr")

	@Dbtr.deleter
	def Dbtr(self):
		del self._Dbtr
		self._Dbtr = None

	@property
	def DbtrActvtnId(self):
		return self._DbtrActvtnId

	@DbtrActvtnId.setter
	def DbtrActvtnId(self, value):
		self._DbtrActvtnId = value if type(value) != base_types.auto else self.make_default("DbtrActvtnId")

	@DbtrActvtnId.deleter
	def DbtrActvtnId(self):
		del self._DbtrActvtnId
		self._DbtrActvtnId = None

	@property
	def DbtrSolPrvdr(self):
		return self._DbtrSolPrvdr

	@DbtrSolPrvdr.setter
	def DbtrSolPrvdr(self, value):
		self._DbtrSolPrvdr = value if type(value) != base_types.auto else self.make_default("DbtrSolPrvdr")

	@DbtrSolPrvdr.deleter
	def DbtrSolPrvdr(self):
		del self._DbtrSolPrvdr
		self._DbtrSolPrvdr = None

	@property
	def DdctdActvtnCd(self):
		return self._DdctdActvtnCd

	@DdctdActvtnCd.setter
	def DdctdActvtnCd(self, value):
		self._DdctdActvtnCd = value if type(value) != base_types.auto else self.make_default("DdctdActvtnCd")

	@DdctdActvtnCd.deleter
	def DdctdActvtnCd(self):
		del self._DdctdActvtnCd
		self._DdctdActvtnCd = None

	@property
	def DispNm(self):
		return self._DispNm

	@DispNm.setter
	def DispNm(self, value):
		self._DispNm = value if type(value) != base_types.auto else self.make_default("DispNm")

	@DispNm.deleter
	def DispNm(self):
		del self._DispNm
		self._DispNm = None

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
	def UltmtCdtr(self):
		return self._UltmtCdtr

	@UltmtCdtr.setter
	def UltmtCdtr(self, value):
		self._UltmtCdtr = value if type(value) != base_types.auto else self.make_default("UltmtCdtr")

	@UltmtCdtr.deleter
	def UltmtCdtr(self):
		del self._UltmtCdtr
		self._UltmtCdtr = None

	@property
	def UltmtDbtr(self):
		return self._UltmtDbtr

	@UltmtDbtr.setter
	def UltmtDbtr(self, value):
		self._UltmtDbtr = value if type(value) != base_types.auto else self.make_default("UltmtDbtr")

	@UltmtDbtr.deleter
	def UltmtDbtr(self):
		del self._UltmtDbtr
		self._UltmtDbtr = None

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

