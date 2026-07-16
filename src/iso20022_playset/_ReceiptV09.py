# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import MessageHeader9
from . import Receipt7
from . import SupplementaryData1

class ReceiptV09(base_types._BaseFieldType):

	__slots__ = ["_MsgHdr", "_RctDtls", "_SplmtryData"]
	@property
	def MsgHdr(self):
		return self._MsgHdr

	@MsgHdr.setter
	def MsgHdr(self, value):
		self._MsgHdr = value if value is not None else base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

	@MsgHdr.deleter
	def MsgHdr(self):
		del self._MsgHdr
		self._MsgHdr = base_types.UninitialisedField(self, 'MsgHdr', MessageHeader9, False)

	@property
	def RctDtls(self):
		return self._RctDtls

	@RctDtls.setter
	def RctDtls(self, value):
		self._RctDtls = value if value is not None else base_types.UninitialisedField(self, 'RctDtls', Receipt7, True)

	@RctDtls.deleter
	def RctDtls(self):
		del self._RctDtls
		self._RctDtls = base_types.UninitialisedField(self, 'RctDtls', Receipt7, True)

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
		base_types.FieldEntry(name='MsgHdr', type=MessageHeader9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RctDtls', type=Receipt7, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='SplmtryData', type=SupplementaryData1, min=0, max=None, mutex_group=None, array=True),
	))