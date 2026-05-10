from . import base_types
from ._Reason2 import Reason2
from ._SimpleIdentificationInformation import SimpleIdentificationInformation
from ._MessageIdentification1 import MessageIdentification1

class RoleAndBaselineRejectionV01(base_types._BaseFieldType):

	__slots__ = ["_RjctnId", "_RltdMsgRef", "_TxId", "_RjctnRsn"]
	@property
	def RjctnId(self):
		return self._RjctnId

	@RjctnId.setter
	def RjctnId(self, value):
		self._RjctnId = value if type(value) != base_types.auto else self.make_default("RjctnId")

	@RjctnId.deleter
	def RjctnId(self):
		del self._RjctnId
		self._RjctnId = None

	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if type(value) != base_types.auto else self.make_default("RltdMsgRef")

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = None

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
	def RjctnRsn(self):
		return self._RjctnRsn

	@RjctnRsn.setter
	def RjctnRsn(self, value):
		self._RjctnRsn = value if type(value) != base_types.auto else self.make_default("RjctnRsn")

	@RjctnRsn.deleter
	def RjctnRsn(self):
		del self._RjctnRsn
		self._RjctnRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RjctnId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctnRsn', type=Reason2, min=0, max=1, mutex_group=None, array=False),
	))

