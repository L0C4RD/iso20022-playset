# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BatchInformation2
from . import EntryTransaction15

class EntryDetails14(base_types._BaseFieldType):

	__slots__ = ["_Btch", "_TxDtls"]
	@property
	def Btch(self):
		return self._Btch

	@Btch.setter
	def Btch(self, value):
		self._Btch = value if value is not None else base_types.UninitialisedField(self, 'Btch', BatchInformation2, False)

	@Btch.deleter
	def Btch(self):
		del self._Btch
		self._Btch = base_types.UninitialisedField(self, 'Btch', BatchInformation2, False)

	@property
	def TxDtls(self):
		return self._TxDtls

	@TxDtls.setter
	def TxDtls(self, value):
		self._TxDtls = value if value is not None else base_types.UninitialisedField(self, 'TxDtls', EntryTransaction15, True)

	@TxDtls.deleter
	def TxDtls(self):
		del self._TxDtls
		self._TxDtls = base_types.UninitialisedField(self, 'TxDtls', EntryTransaction15, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Btch', type=BatchInformation2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TxDtls', type=EntryTransaction15, min=0, max=None, mutex_group=None, array=True),
	))