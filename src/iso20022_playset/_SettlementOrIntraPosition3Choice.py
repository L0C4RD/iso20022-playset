from . import base_types
from ._IntraPosition6 import IntraPosition6
from ._TransactionDetails126 import TransactionDetails126

class SettlementOrIntraPosition3Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmnt", "_SttlmTx"]
	@property
	def IntraPosMvmnt(self):
		return self._IntraPosMvmnt

	@IntraPosMvmnt.setter
	def IntraPosMvmnt(self, value):
		self._IntraPosMvmnt = value if type(value) != base_types.auto else self.make_default("IntraPosMvmnt")

	@IntraPosMvmnt.deleter
	def IntraPosMvmnt(self):
		del self._IntraPosMvmnt
		self._IntraPosMvmnt = None

	@property
	def SttlmTx(self):
		return self._SttlmTx

	@SttlmTx.setter
	def SttlmTx(self, value):
		self._SttlmTx = value if type(value) != base_types.auto else self.make_default("SttlmTx")

	@SttlmTx.deleter
	def SttlmTx(self):
		del self._SttlmTx
		self._SttlmTx = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmnt', type=IntraPosition6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmTx', type=TransactionDetails126, min=0, max=1, mutex_group=1, array=False),
	))

