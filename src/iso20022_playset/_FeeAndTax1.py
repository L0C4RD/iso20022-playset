# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Fee1 import Fee1
from ._Max35Text import Max35Text
from ._Tax30 import Tax30

class FeeAndTax1(base_types._BaseFieldType):

	__slots__ = ["_ComrclAgrmtRef", "_IndvFee", "_IndvTax"]
	@property
	def ComrclAgrmtRef(self):
		return self._ComrclAgrmtRef

	@ComrclAgrmtRef.setter
	def ComrclAgrmtRef(self, value):
		self._ComrclAgrmtRef = value if type(value) != base_types.auto else self.make_default("ComrclAgrmtRef")

	@ComrclAgrmtRef.deleter
	def ComrclAgrmtRef(self):
		del self._ComrclAgrmtRef
		self._ComrclAgrmtRef = None

	@property
	def IndvFee(self):
		return self._IndvFee

	@IndvFee.setter
	def IndvFee(self, value):
		self._IndvFee = value if type(value) != base_types.auto else self.make_default("IndvFee")

	@IndvFee.deleter
	def IndvFee(self):
		del self._IndvFee
		self._IndvFee = None

	@property
	def IndvTax(self):
		return self._IndvTax

	@IndvTax.setter
	def IndvTax(self, value):
		self._IndvTax = value if type(value) != base_types.auto else self.make_default("IndvTax")

	@IndvTax.deleter
	def IndvTax(self):
		del self._IndvTax
		self._IndvTax = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='ComrclAgrmtRef', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='IndvFee', type=Fee1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='IndvTax', type=Tax30, min=0, max=None, mutex_group=None, array=True),
	))