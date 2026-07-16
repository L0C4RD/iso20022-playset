# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import IndividualPerson41
from . import Max35Text
from . import Proxy12
from . import SafekeepingAccount19
from . import SpecificInstructionRequest4
from . import VoteDetails6
from . import YesNoIndicator

class Instruction8(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_MtgAttndee", "_Prxy", "_ReqdExctnDt", "_SnglInstrId", "_SpcfcInstrReq", "_VoteDtls", "_VoteExctnConf"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SafekeepingAccount19, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SafekeepingAccount19, False)

	@property
	def MtgAttndee(self):
		return self._MtgAttndee

	@MtgAttndee.setter
	def MtgAttndee(self, value):
		self._MtgAttndee = value if value is not None else base_types.UninitialisedField(self, 'MtgAttndee', IndividualPerson41, True)

	@MtgAttndee.deleter
	def MtgAttndee(self):
		del self._MtgAttndee
		self._MtgAttndee = base_types.UninitialisedField(self, 'MtgAttndee', IndividualPerson41, True)

	@property
	def Prxy(self):
		return self._Prxy

	@Prxy.setter
	def Prxy(self, value):
		self._Prxy = value if value is not None else base_types.UninitialisedField(self, 'Prxy', Proxy12, False)

	@Prxy.deleter
	def Prxy(self):
		del self._Prxy
		self._Prxy = base_types.UninitialisedField(self, 'Prxy', Proxy12, False)

	@property
	def ReqdExctnDt(self):
		return self._ReqdExctnDt

	@ReqdExctnDt.setter
	def ReqdExctnDt(self, value):
		self._ReqdExctnDt = value if value is not None else base_types.UninitialisedField(self, 'ReqdExctnDt', ISODateTime, False)

	@ReqdExctnDt.deleter
	def ReqdExctnDt(self):
		del self._ReqdExctnDt
		self._ReqdExctnDt = base_types.UninitialisedField(self, 'ReqdExctnDt', ISODateTime, False)

	@property
	def SnglInstrId(self):
		return self._SnglInstrId

	@SnglInstrId.setter
	def SnglInstrId(self, value):
		self._SnglInstrId = value if value is not None else base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@SnglInstrId.deleter
	def SnglInstrId(self):
		del self._SnglInstrId
		self._SnglInstrId = base_types.UninitialisedField(self, 'SnglInstrId', Max35Text, False)

	@property
	def SpcfcInstrReq(self):
		return self._SpcfcInstrReq

	@SpcfcInstrReq.setter
	def SpcfcInstrReq(self, value):
		self._SpcfcInstrReq = value if value is not None else base_types.UninitialisedField(self, 'SpcfcInstrReq', SpecificInstructionRequest4, False)

	@SpcfcInstrReq.deleter
	def SpcfcInstrReq(self):
		del self._SpcfcInstrReq
		self._SpcfcInstrReq = base_types.UninitialisedField(self, 'SpcfcInstrReq', SpecificInstructionRequest4, False)

	@property
	def VoteDtls(self):
		return self._VoteDtls

	@VoteDtls.setter
	def VoteDtls(self, value):
		self._VoteDtls = value if value is not None else base_types.UninitialisedField(self, 'VoteDtls', VoteDetails6, False)

	@VoteDtls.deleter
	def VoteDtls(self):
		del self._VoteDtls
		self._VoteDtls = base_types.UninitialisedField(self, 'VoteDtls', VoteDetails6, False)

	@property
	def VoteExctnConf(self):
		return self._VoteExctnConf

	@VoteExctnConf.setter
	def VoteExctnConf(self, value):
		self._VoteExctnConf = value if value is not None else base_types.UninitialisedField(self, 'VoteExctnConf', YesNoIndicator, False)

	@VoteExctnConf.deleter
	def VoteExctnConf(self):
		del self._VoteExctnConf
		self._VoteExctnConf = base_types.UninitialisedField(self, 'VoteExctnConf', YesNoIndicator, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SafekeepingAccount19, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MtgAttndee', type=IndividualPerson41, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Prxy', type=Proxy12, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqdExctnDt', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SnglInstrId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SpcfcInstrReq', type=SpecificInstructionRequest4, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteDtls', type=VoteDetails6, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VoteExctnConf', type=YesNoIndicator, min=1, max=1, mutex_group=None, array=False),
	))