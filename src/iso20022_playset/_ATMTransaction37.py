# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ATMCommand7 import ATMCommand7
from ._Action7 import Action7
from ._Max10000Binary import Max10000Binary
from ._Max35Text import Max35Text
from ._ResponseType12 import ResponseType12
from ._TransactionIdentifier3 import TransactionIdentifier3
from ._TrueFalseIndicator import TrueFalseIndicator

class ATMTransaction37(base_types._BaseFieldType):

	__slots__ = ["_Actn", "_Cmd", "_CmpltnReqrd", "_ICCRltdData", "_RcncltnId", "_TxId", "_TxRspn"]
	@property
	def Actn(self):
		return self._Actn

	@Actn.setter
	def Actn(self, value):
		self._Actn = value if type(value) != base_types.auto else self.make_default("Actn")

	@Actn.deleter
	def Actn(self):
		del self._Actn
		self._Actn = None

	@property
	def Cmd(self):
		return self._Cmd

	@Cmd.setter
	def Cmd(self, value):
		self._Cmd = value if type(value) != base_types.auto else self.make_default("Cmd")

	@Cmd.deleter
	def Cmd(self):
		del self._Cmd
		self._Cmd = None

	@property
	def CmpltnReqrd(self):
		return self._CmpltnReqrd

	@CmpltnReqrd.setter
	def CmpltnReqrd(self, value):
		self._CmpltnReqrd = value if type(value) != base_types.auto else self.make_default("CmpltnReqrd")

	@CmpltnReqrd.deleter
	def CmpltnReqrd(self):
		del self._CmpltnReqrd
		self._CmpltnReqrd = None

	@property
	def ICCRltdData(self):
		return self._ICCRltdData

	@ICCRltdData.setter
	def ICCRltdData(self, value):
		self._ICCRltdData = value if type(value) != base_types.auto else self.make_default("ICCRltdData")

	@ICCRltdData.deleter
	def ICCRltdData(self):
		del self._ICCRltdData
		self._ICCRltdData = None

	@property
	def RcncltnId(self):
		return self._RcncltnId

	@RcncltnId.setter
	def RcncltnId(self, value):
		self._RcncltnId = value if type(value) != base_types.auto else self.make_default("RcncltnId")

	@RcncltnId.deleter
	def RcncltnId(self):
		del self._RcncltnId
		self._RcncltnId = None

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != base_types.auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def TxRspn(self):
		return self._TxRspn

	@TxRspn.setter
	def TxRspn(self, value):
		self._TxRspn = value if type(value) != base_types.auto else self.make_default("TxRspn")

	@TxRspn.deleter
	def TxRspn(self):
		del self._TxRspn
		self._TxRspn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Actn', type=Action7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Cmd', type=ATMCommand7, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='CmpltnReqrd', type=TrueFalseIndicator, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ICCRltdData', type=Max10000Binary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=TransactionIdentifier3, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxRspn', type=ResponseType12, min=1, max=1, mutex_group=None, array=False),
	))