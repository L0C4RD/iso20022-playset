# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import UTIIdentifier

class UniqueTransactionIdentifier3(base_types._BaseFieldType):

	__slots__ = ["_PrrUnqTxIdr", "_UnqTxIdr"]
	@property
	def PrrUnqTxIdr(self):
		return self._PrrUnqTxIdr

	@PrrUnqTxIdr.setter
	def PrrUnqTxIdr(self, value):
		self._PrrUnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'PrrUnqTxIdr', UTIIdentifier, True)

	@PrrUnqTxIdr.deleter
	def PrrUnqTxIdr(self):
		del self._PrrUnqTxIdr
		self._PrrUnqTxIdr = base_types.UninitialisedField(self, 'PrrUnqTxIdr', UTIIdentifier, True)

	@property
	def UnqTxIdr(self):
		return self._UnqTxIdr

	@UnqTxIdr.setter
	def UnqTxIdr(self, value):
		self._UnqTxIdr = value if value is not None else base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	@UnqTxIdr.deleter
	def UnqTxIdr(self):
		del self._UnqTxIdr
		self._UnqTxIdr = base_types.UninitialisedField(self, 'UnqTxIdr', UTIIdentifier, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='PrrUnqTxIdr', type=UTIIdentifier, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=1, max=1, mutex_group=None, array=False),
	))