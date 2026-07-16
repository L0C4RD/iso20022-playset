# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification179
from . import UTIIdentifier

class UniqueTransactionIdentifier1Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_UnqTxIdr"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification179, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification179, False)

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
		base_types.FieldEntry(name='Prtry', type=GenericIdentification179, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='UnqTxIdr', type=UTIIdentifier, min=0, max=1, mutex_group=1, array=False),
	))