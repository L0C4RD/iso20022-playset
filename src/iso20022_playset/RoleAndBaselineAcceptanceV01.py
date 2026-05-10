from . import base_types
import MessageIdentification1
import SimpleIdentificationInformation

class RoleAndBaselineAcceptanceV01(base_types._BaseFieldType):

	__slots__ = ["_TxId", "_AccptncId", "_RltdMsgRef"]
	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if type(value) != auto else self.make_default("TxId")

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = None

	@property
	def AccptncId(self):
		return self._AccptncId

	@AccptncId.setter
	def AccptncId(self, value):
		self._AccptncId = value if type(value) != auto else self.make_default("AccptncId")

	@AccptncId.deleter
	def AccptncId(self):
		del self._AccptncId
		self._AccptncId = None

	@property
	def RltdMsgRef(self):
		return self._RltdMsgRef

	@RltdMsgRef.setter
	def RltdMsgRef(self, value):
		self._RltdMsgRef = value if type(value) != auto else self.make_default("RltdMsgRef")

	@RltdMsgRef.deleter
	def RltdMsgRef(self):
		del self._RltdMsgRef
		self._RltdMsgRef = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TxId', type=SimpleIdentificationInformation, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptncId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RltdMsgRef', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))

