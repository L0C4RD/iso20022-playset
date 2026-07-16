# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification1
from . import MessageHeader1
from . import SecuritiesReturnCriteria1
from . import SecuritiesSearchCriteria4
from . import SupplementaryData1

class SecurityQueryV01(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_ReqTp", "_SchCrit", "_SmlSetRtrCrit", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader1, False)

	@property
	def ReqTp(self):
		return self._ReqTp

	@ReqTp.setter
	def ReqTp(self, value):
		self._ReqTp = value if value is not None else base_types.UninitialisedField(self, 'ReqTp', GenericIdentification1, False)

	@ReqTp.deleter
	def ReqTp(self):
		del self._ReqTp
		self._ReqTp = base_types.UninitialisedField(self, 'ReqTp', GenericIdentification1, False)

	@property
	def SchCrit(self):
		return self._SchCrit

	@SchCrit.setter
	def SchCrit(self, value):
		self._SchCrit = value if value is not None else base_types.UninitialisedField(self, 'SchCrit', SecuritiesSearchCriteria4, False)

	@SchCrit.deleter
	def SchCrit(self):
		del self._SchCrit
		self._SchCrit = base_types.UninitialisedField(self, 'SchCrit', SecuritiesSearchCriteria4, False)

	@property
	def SmlSetRtrCrit(self):
		return self._SmlSetRtrCrit

	@SmlSetRtrCrit.setter
	def SmlSetRtrCrit(self, value):
		self._SmlSetRtrCrit = value if value is not None else base_types.UninitialisedField(self, 'SmlSetRtrCrit', SecuritiesReturnCriteria1, False)

	@SmlSetRtrCrit.deleter
	def SmlSetRtrCrit(self):
		del self._SmlSetRtrCrit
		self._SmlSetRtrCrit = base_types.UninitialisedField(self, 'SmlSetRtrCrit', SecuritiesReturnCriteria1, False)

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

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ReqTp', type=GenericIdentification1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SchCrit', type=SecuritiesSearchCriteria4, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SmlSetRtrCrit', type=SecuritiesReturnCriteria1, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))