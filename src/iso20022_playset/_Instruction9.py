from . import base_types
from ._ISODateTime import ISODateTime
from ._IndividualPerson41 import IndividualPerson41
from ._Max35Text import Max35Text
from ._PartyIdentification338 import PartyIdentification338
from ._Proxy12 import Proxy12
from ._SafekeepingAccount20 import SafekeepingAccount20
from ._SpecificInstructionRequest4 import SpecificInstructionRequest4
from ._VoteDetails7 import VoteDetails7
from ._YesNoIndicator import YesNoIndicator

class Instruction9(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_AddtlDsclsrInf", "_MtgAttndee", "_Prxy", "_ReqdExctnDt", "_SnglInstrId", "_SpcfcInstrReq", "_VoteDtls", "_VoteExctnConf"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def AddtlDsclsrInf(self):
		return self._AddtlDsclsrInf

	@AddtlDsclsrInf.setter
	def AddtlDsclsrInf(self, value):
		self._AddtlDsclsrInf = value if type(value) != base_types.auto else self.make_default("AddtlDsclsrInf")

	@AddtlDsclsrInf.deleter
	def AddtlDsclsrInf(self):
		del self._AddtlDsclsrInf
		self._AddtlDsclsrInf = None

	@property
	def MtgAttndee(self):
		return self._MtgAttndee

	@MtgAttndee.setter
	def MtgAttndee(self, value):
		self._MtgAttndee = value if type(value) != base_types.auto else self.make_default("MtgAttndee")

	@MtgAttndee.deleter
	def MtgAttndee(self):
		del self._MtgAttndee
		self._MtgAttndee = None

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if type(value) != base_types.auto else self.make_default("Prxy")

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = None

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if type(value) != base_types.auto else self.make_default("ReqdExctnDt")

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = None

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if type(value) != base_types.auto else self.make_default("SnglInstrId")

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = None

	@property
	def SpcfcInstrReq(self):
		return self._SpcfcInstrReq

	@SpcfcInstrReq.setter
	def SpcfcInstrReq(self, value):
		self._SpcfcInstrReq = value if type(value) != base_types.auto else self.make_default("SpcfcInstrReq")

	@SpcfcInstrReq.deleter
	def SpcfcInstrReq(self):
		del self._SpcfcInstrReq
		self._SpcfcInstrReq = None

	@property
	def VoteDtls(self):
		return self._VoteDtls

	@VoteDtls.setter
	def VoteDtls(self, value):
		self._VoteDtls = value if type(value) != base_types.auto else self.make_default("VoteDtls")

	@VoteDtls.deleter
	def VoteDtls(self):
		del self._VoteDtls
		self._VoteDtls = None

	@property
	def VoteExctnConf(self):
		return self._VoteExctnConf

	@VoteExctnConf.setter
	def VoteExctnConf(self, value):
		self._VoteExctnConf = value if type(value) != base_types.auto else self.make_default("VoteExctnConf")

	@VoteExctnConf.deleter
	def VoteExctnConf(self):
		del self._VoteExctnConf
		self._VoteExctnConf = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount20, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlDsclsrInf', type=PartyIdentification338, min=0, max=250, mutex_group=None, array=True),
		base_types.FieldEntry(name='MtgAttndee', type=IndividualPerson41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prxy', type=Proxy12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpcfcInstrReq', type=SpecificInstructionRequest4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteDtls', type=VoteDetails7, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteExctnConf', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))

