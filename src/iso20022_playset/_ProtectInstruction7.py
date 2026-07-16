# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import ProtectTransactionType3Code
from . import RestrictedFINMax15Text

class ProtectInstruction7(base_types._BaseFieldType):

	__slots__ = ["_PrtctDt", "_TxId", "_TxTp"]
	@property
	def PrtctDt(self):
		return self._PrtctDt

	@PrtctDt.setter
	def PrtctDt(self, value):
		self._PrtctDt = value if value is not None else base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@PrtctDt.deleter
	def PrtctDt(self):
		del self._PrtctDt
		self._PrtctDt = base_types.UninitialisedField(self, 'PrtctDt', ISODate, False)

	@property
	def TxId(self):
		return self._TxId

	@TxId.setter
	def TxId(self, value):
		self._TxId = value if value is not None else base_types.UninitialisedField(self, 'TxId', RestrictedFINMax15Text, False)

	@TxId.deleter
	def TxId(self):
		del self._TxId
		self._TxId = base_types.UninitialisedField(self, 'TxId', RestrictedFINMax15Text, False)

	@property
	def TxTp(self):
		return self._TxTp

	@TxTp.setter
	def TxTp(self, value):
		self._TxTp = value if value is not None else base_types.UninitialisedField(self, 'TxTp', ProtectTransactionType3Code, False)

	@TxTp.deleter
	def TxTp(self):
		del self._TxTp
		self._TxTp = base_types.UninitialisedField(self, 'TxTp', ProtectTransactionType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrtctDt', type=ISODate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxId', type=RestrictedFINMax15Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxTp', type=ProtectTransactionType3Code, min=1, max=1, mutex_group=None, array=False),
	))