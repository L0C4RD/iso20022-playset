from . import base_types
from ._InvestigationRequestAction1 import InvestigationRequestAction1
from ._InvestigationServiceLevel1Choice import InvestigationServiceLevel1Choice
from ._InvestigationSubType1Choice import InvestigationSubType1Choice
from ._InvestigationType1Choice import InvestigationType1Choice
from ._Max35Text import Max35Text
from ._Party40Choice import Party40Choice
from ._UUIDv4Identifier import UUIDv4Identifier
from ._UnderlyingData13Choice import UnderlyingData13Choice
from ._UnderlyingInvestigationInstrument1Choice import UnderlyingInvestigationInstrument1Choice

class InvestigationRequest51(base_types._BaseFieldType):

	__slots__ = ["_EIR", "_InvstgtnSubTp", "_InvstgtnTp", "_MsgId", "_ReqActn", "_ReqOrgtr", "_Rqstr", "_RqstrInvstgtnId", "_Rspndr", "_RspndrInvstgtnId", "_SvcLvl", "_Undrlyg", "_UndrlygInstrm", "_XpctdRspndr"]
	@property
	def EIR(self):
		return self._EIR

	@EIR.setter
	def EIR(self, value):
		self._EIR = value if type(value) != base_types.auto else self.make_default("EIR")

	@EIR.deleter
	def EIR(self):
		del self._EIR
		self._EIR = None

	@property
	def InvstgtnSubTp(self):
		return self._InvstgtnSubTp

	@InvstgtnSubTp.setter
	def InvstgtnSubTp(self, value):
		self._InvstgtnSubTp = value if type(value) != base_types.auto else self.make_default("InvstgtnSubTp")

	@InvstgtnSubTp.deleter
	def InvstgtnSubTp(self):
		del self._InvstgtnSubTp
		self._InvstgtnSubTp = None

	@property
	def InvstgtnTp(self):
		return self._InvstgtnTp

	@InvstgtnTp.setter
	def InvstgtnTp(self, value):
		self._InvstgtnTp = value if type(value) != base_types.auto else self.make_default("InvstgtnTp")

	@InvstgtnTp.deleter
	def InvstgtnTp(self):
		del self._InvstgtnTp
		self._InvstgtnTp = None

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if type(value) != base_types.auto else self.make_default("MsgId")

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = None

	@property
	def ReqActn(self):
		return self._ReqActn

	@ReqActn.setter
	def ReqActn(self, value):
		self._ReqActn = value if type(value) != base_types.auto else self.make_default("ReqActn")

	@ReqActn.deleter
	def ReqActn(self):
		del self._ReqActn
		self._ReqActn = None

	@property
	def ReqOrgtr(self):
		return self._ReqOrgtr

	@ReqOrgtr.setter
	def ReqOrgtr(self, value):
		self._ReqOrgtr = value if type(value) != base_types.auto else self.make_default("ReqOrgtr")

	@ReqOrgtr.deleter
	def ReqOrgtr(self):
		del self._ReqOrgtr
		self._ReqOrgtr = None

	@property
	def Rqstr(self):
		return self._Rqstr

	@Rqstr.setter
	def Rqstr(self, value):
		self._Rqstr = value if type(value) != base_types.auto else self.make_default("Rqstr")

	@Rqstr.deleter
	def Rqstr(self):
		del self._Rqstr
		self._Rqstr = None

	@property
	def RqstrInvstgtnId(self):
		return self._RqstrInvstgtnId

	@RqstrInvstgtnId.setter
	def RqstrInvstgtnId(self, value):
		self._RqstrInvstgtnId = value if type(value) != base_types.auto else self.make_default("RqstrInvstgtnId")

	@RqstrInvstgtnId.deleter
	def RqstrInvstgtnId(self):
		del self._RqstrInvstgtnId
		self._RqstrInvstgtnId = None

	@property
	def Rspndr(self):
		return self._Rspndr

	@Rspndr.setter
	def Rspndr(self, value):
		self._Rspndr = value if type(value) != base_types.auto else self.make_default("Rspndr")

	@Rspndr.deleter
	def Rspndr(self):
		del self._Rspndr
		self._Rspndr = None

	@property
	def RspndrInvstgtnId(self):
		return self._RspndrInvstgtnId

	@RspndrInvstgtnId.setter
	def RspndrInvstgtnId(self, value):
		self._RspndrInvstgtnId = value if type(value) != base_types.auto else self.make_default("RspndrInvstgtnId")

	@RspndrInvstgtnId.deleter
	def RspndrInvstgtnId(self):
		del self._RspndrInvstgtnId
		self._RspndrInvstgtnId = None

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if type(value) != base_types.auto else self.make_default("SvcLvl")

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = None

	@property
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if type(value) != base_types.auto else self.make_default("Undrlyg")

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = None

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if type(value) != base_types.auto else self.make_default("UndrlygInstrm")

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = None

	@property
	def XpctdRspndr(self):
		return self._XpctdRspndr

	@XpctdRspndr.setter
	def XpctdRspndr(self, value):
		self._XpctdRspndr = value if type(value) != base_types.auto else self.make_default("XpctdRspndr")

	@XpctdRspndr.deleter
	def XpctdRspndr(self):
		del self._XpctdRspndr
		self._XpctdRspndr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EIR', type=UUIDv4Identifier, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnSubTp', type=InvestigationSubType1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='InvstgtnTp', type=InvestigationType1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqActn', type=InvestigationRequestAction1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqOrgtr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rqstr', type=Party40Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RqstrInvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rspndr', type=Party40Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RspndrInvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SvcLvl', type=InvestigationServiceLevel1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Undrlyg', type=UnderlyingData13Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygInstrm', type=UnderlyingInvestigationInstrument1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XpctdRspndr', type=Party40Choice, min=0, max=1, mutex_group=None, array=False),
	))

