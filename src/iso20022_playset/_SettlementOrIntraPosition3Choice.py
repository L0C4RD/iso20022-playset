# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import IntraPosition6
from . import TransactionDetails126

class SettlementOrIntraPosition3Choice(base_types._BaseFieldType):

	__slots__ = ["_IntraPosMvmnt", "_SttlmTx"]
	@property
	def IntraPosMvmnt(self):
		return self._IntraPosMvmnt

	@IntraPosMvmnt.setter
	def IntraPosMvmnt(self, value):
		self._IntraPosMvmnt = value if value is not None else base_types.UninitialisedField(self, 'IntraPosMvmnt', IntraPosition6, False)

	@IntraPosMvmnt.deleter
	def IntraPosMvmnt(self):
		del self._IntraPosMvmnt
		self._IntraPosMvmnt = base_types.UninitialisedField(self, 'IntraPosMvmnt', IntraPosition6, False)

	@property
	def SttlmTx(self):
		return self._SttlmTx

	@SttlmTx.setter
	def SttlmTx(self, value):
		self._SttlmTx = value if value is not None else base_types.UninitialisedField(self, 'SttlmTx', TransactionDetails126, False)

	@SttlmTx.deleter
	def SttlmTx(self):
		del self._SttlmTx
		self._SttlmTx = base_types.UninitialisedField(self, 'SttlmTx', TransactionDetails126, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IntraPosMvmnt', type=IntraPosition6, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='SttlmTx', type=TransactionDetails126, min=0, max=1, mutex_group=1, array=False),
	))