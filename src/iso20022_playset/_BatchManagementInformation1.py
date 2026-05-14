# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max140Binary import Max140Binary
from ._Max15NumericText import Max15NumericText
from ._Max35Text import Max35Text

class BatchManagementInformation1(base_types._BaseFieldType):

	__slots__ = ["_BtchId", "_ColltnId", "_MsgChcksmInptVal", "_MsgSeqNb"]
	@property
	def BtchId(self):
		return self._BtchId

	@BtchId.setter
	def BtchId(self, value):
		self._BtchId = value if type(value) != base_types.auto else self.make_default("BtchId")

	@BtchId.deleter
	def BtchId(self):
		del self._BtchId
		self._BtchId = None

	@property
	def ColltnId(self):
		return self._ColltnId

	@ColltnId.setter
	def ColltnId(self, value):
		self._ColltnId = value if type(value) != base_types.auto else self.make_default("ColltnId")

	@ColltnId.deleter
	def ColltnId(self):
		del self._ColltnId
		self._ColltnId = None

	@property
	def MsgChcksmInptVal(self):
		return self._MsgChcksmInptVal

	@MsgChcksmInptVal.setter
	def MsgChcksmInptVal(self, value):
		self._MsgChcksmInptVal = value if type(value) != base_types.auto else self.make_default("MsgChcksmInptVal")

	@MsgChcksmInptVal.deleter
	def MsgChcksmInptVal(self):
		del self._MsgChcksmInptVal
		self._MsgChcksmInptVal = None

	@property
	def MsgSeqNb(self):
		return self._MsgSeqNb

	@MsgSeqNb.setter
	def MsgSeqNb(self, value):
		self._MsgSeqNb = value if type(value) != base_types.auto else self.make_default("MsgSeqNb")

	@MsgSeqNb.deleter
	def MsgSeqNb(self):
		del self._MsgSeqNb
		self._MsgSeqNb = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BtchId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ColltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgChcksmInptVal', type=Max140Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgSeqNb', type=Max15NumericText, min=0, max=1, mutex_group=None, array=False),
	))