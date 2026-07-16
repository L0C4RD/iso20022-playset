# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationRequestAction1
from . import InvestigationServiceLevel1Choice
from . import InvestigationSubType1Choice
from . import InvestigationType1Choice
from . import Max35Text
from . import Party40Choice
from . import UUIDv4Identifier
from . import UnderlyingData13Choice
from . import UnderlyingInvestigationInstrument1Choice

class InvestigationRequest51(base_types._BaseFieldType):

	__slots__ = ["_EIR", "_InvstgtnSubTp", "_InvstgtnTp", "_MsgId", "_ReqActn", "_ReqOrgtr", "_Rqstr", "_RqstrInvstgtnId", "_Rspndr", "_RspndrInvstgtnId", "_SvcLvl", "_Undrlyg", "_UndrlygInstrm", "_XpctdRspndr"]
	@property
	def EIR(self):
		return self._EIR

	@EIR.setter
	def EIR(self, value):
		self._EIR = value if value is not None else base_types.UninitialisedField(self, 'EIR', UUIDv4Identifier, False)

	@EIR.deleter
	def EIR(self):
		del self._EIR
		self._EIR = base_types.UninitialisedField(self, 'EIR', UUIDv4Identifier, False)

	@property
	def InvstgtnSubTp(self):
		return self._InvstgtnSubTp

	@InvstgtnSubTp.setter
	def InvstgtnSubTp(self, value):
		self._InvstgtnSubTp = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnSubTp', InvestigationSubType1Choice, False)

	@InvstgtnSubTp.deleter
	def InvstgtnSubTp(self):
		del self._InvstgtnSubTp
		self._InvstgtnSubTp = base_types.UninitialisedField(self, 'InvstgtnSubTp', InvestigationSubType1Choice, False)

	@property
	def InvstgtnTp(self):
		return self._InvstgtnTp

	@InvstgtnTp.setter
	def InvstgtnTp(self, value):
		self._InvstgtnTp = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnTp', InvestigationType1Choice, False)

	@InvstgtnTp.deleter
	def InvstgtnTp(self):
		del self._InvstgtnTp
		self._InvstgtnTp = base_types.UninitialisedField(self, 'InvstgtnTp', InvestigationType1Choice, False)

	@property
	def MsgId(self):
		return self._MsgId

	@MsgId.setter
	def MsgId(self, value):
		self._MsgId = value if value is not None else base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@MsgId.deleter
	def MsgId(self):
		del self._MsgId
		self._MsgId = base_types.UninitialisedField(self, 'MsgId', Max35Text, False)

	@property
	def ReqActn(self):
		return self._ReqActn

	@ReqActn.setter
	def ReqActn(self, value):
		self._ReqActn = value if value is not None else base_types.UninitialisedField(self, 'ReqActn', InvestigationRequestAction1, False)

	@ReqActn.deleter
	def ReqActn(self):
		del self._ReqActn
		self._ReqActn = base_types.UninitialisedField(self, 'ReqActn', InvestigationRequestAction1, False)

	@property
	def ReqOrgtr(self):
		return self._ReqOrgtr

	@ReqOrgtr.setter
	def ReqOrgtr(self, value):
		self._ReqOrgtr = value if value is not None else base_types.UninitialisedField(self, 'ReqOrgtr', Party40Choice, False)

	@ReqOrgtr.deleter
	def ReqOrgtr(self):
		del self._ReqOrgtr
		self._ReqOrgtr = base_types.UninitialisedField(self, 'ReqOrgtr', Party40Choice, False)

	@property
	def Rqstr(self):
		return self._Rqstr

	@Rqstr.setter
	def Rqstr(self, value):
		self._Rqstr = value if value is not None else base_types.UninitialisedField(self, 'Rqstr', Party40Choice, False)

	@Rqstr.deleter
	def Rqstr(self):
		del self._Rqstr
		self._Rqstr = base_types.UninitialisedField(self, 'Rqstr', Party40Choice, False)

	@property
	def RqstrInvstgtnId(self):
		return self._RqstrInvstgtnId

	@RqstrInvstgtnId.setter
	def RqstrInvstgtnId(self, value):
		self._RqstrInvstgtnId = value if value is not None else base_types.UninitialisedField(self, 'RqstrInvstgtnId', Max35Text, False)

	@RqstrInvstgtnId.deleter
	def RqstrInvstgtnId(self):
		del self._RqstrInvstgtnId
		self._RqstrInvstgtnId = base_types.UninitialisedField(self, 'RqstrInvstgtnId', Max35Text, False)

	@property
	def Rspndr(self):
		return self._Rspndr

	@Rspndr.setter
	def Rspndr(self, value):
		self._Rspndr = value if value is not None else base_types.UninitialisedField(self, 'Rspndr', Party40Choice, False)

	@Rspndr.deleter
	def Rspndr(self):
		del self._Rspndr
		self._Rspndr = base_types.UninitialisedField(self, 'Rspndr', Party40Choice, False)

	@property
	def RspndrInvstgtnId(self):
		return self._RspndrInvstgtnId

	@RspndrInvstgtnId.setter
	def RspndrInvstgtnId(self, value):
		self._RspndrInvstgtnId = value if value is not None else base_types.UninitialisedField(self, 'RspndrInvstgtnId', Max35Text, False)

	@RspndrInvstgtnId.deleter
	def RspndrInvstgtnId(self):
		del self._RspndrInvstgtnId
		self._RspndrInvstgtnId = base_types.UninitialisedField(self, 'RspndrInvstgtnId', Max35Text, False)

	@property
	def SvcLvl(self):
		return self._SvcLvl

	@SvcLvl.setter
	def SvcLvl(self, value):
		self._SvcLvl = value if value is not None else base_types.UninitialisedField(self, 'SvcLvl', InvestigationServiceLevel1Choice, True)

	@SvcLvl.deleter
	def SvcLvl(self):
		del self._SvcLvl
		self._SvcLvl = base_types.UninitialisedField(self, 'SvcLvl', InvestigationServiceLevel1Choice, True)

	@property
	def Undrlyg(self):
		return self._Undrlyg

	@Undrlyg.setter
	def Undrlyg(self, value):
		self._Undrlyg = value if value is not None else base_types.UninitialisedField(self, 'Undrlyg', UnderlyingData13Choice, False)

	@Undrlyg.deleter
	def Undrlyg(self):
		del self._Undrlyg
		self._Undrlyg = base_types.UninitialisedField(self, 'Undrlyg', UnderlyingData13Choice, False)

	@property
	def UndrlygInstrm(self):
		return self._UndrlygInstrm

	@UndrlygInstrm.setter
	def UndrlygInstrm(self, value):
		self._UndrlygInstrm = value if value is not None else base_types.UninitialisedField(self, 'UndrlygInstrm', UnderlyingInvestigationInstrument1Choice, False)

	@UndrlygInstrm.deleter
	def UndrlygInstrm(self):
		del self._UndrlygInstrm
		self._UndrlygInstrm = base_types.UninitialisedField(self, 'UndrlygInstrm', UnderlyingInvestigationInstrument1Choice, False)

	@property
	def XpctdRspndr(self):
		return self._XpctdRspndr

	@XpctdRspndr.setter
	def XpctdRspndr(self, value):
		self._XpctdRspndr = value if value is not None else base_types.UninitialisedField(self, 'XpctdRspndr', Party40Choice, False)

	@XpctdRspndr.deleter
	def XpctdRspndr(self):
		del self._XpctdRspndr
		self._XpctdRspndr = base_types.UninitialisedField(self, 'XpctdRspndr', Party40Choice, False)

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