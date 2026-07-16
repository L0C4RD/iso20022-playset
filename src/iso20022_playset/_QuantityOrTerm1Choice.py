# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import QuantityTerm1
from . import Schedule10

class QuantityOrTerm1Choice(base_types._BaseFieldType):

	__slots__ = ["_SchdlPrd", "_Term"]
	@property
	def SchdlPrd(self):
		return self._SchdlPrd

	@SchdlPrd.setter
	def SchdlPrd(self, value):
		self._SchdlPrd = value if value is not None else base_types.UninitialisedField(self, 'SchdlPrd', Schedule10, True)

	@SchdlPrd.deleter
	def SchdlPrd(self):
		del self._SchdlPrd
		self._SchdlPrd = base_types.UninitialisedField(self, 'SchdlPrd', Schedule10, True)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', QuantityTerm1, False)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', QuantityTerm1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='SchdlPrd', type=Schedule10, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='Term', type=QuantityTerm1, min=0, max=1, mutex_group=1, array=False),
	))