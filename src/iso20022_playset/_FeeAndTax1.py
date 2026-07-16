# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Fee1
from . import Max35Text
from . import Tax30

class FeeAndTax1(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_IndvFee", "_IndvTax"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if value is not None else base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = base_types.UninitialisedField(self, 'ComrclAgrmtRef', Max35Text, False)

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if value is not None else base_types.UninitialisedField(self, 'IndvFee', Fee1, True)

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = base_types.UninitialisedField(self, 'IndvFee', Fee1, True)

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if value is not None else base_types.UninitialisedField(self, 'IndvTax', Tax30, True)

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = base_types.UninitialisedField(self, 'IndvTax', Tax30, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvFee', type=Fee1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvTax', type=Tax30, min=0, max=None, mutex_group=None, array=True),
	))