# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Operation1Code
from . import Term1

class AmountOrPercentageRange1(base_types._BaseFieldType):

	__slots__ = ["_Opr", "_Term"]
	@property
	def Opr(self):
		return self._Opr

	@Opr.setter
	def Opr(self, value):
		self._Opr = value if value is not None else base_types.UninitialisedField(self, 'Opr', Operation1Code, False)

	@Opr.deleter
	def Opr(self):
		del self._Opr
		self._Opr = base_types.UninitialisedField(self, 'Opr', Operation1Code, False)

	@property
	def Term(self):
		return self._Term

	@Term.setter
	def Term(self, value):
		self._Term = value if value is not None else base_types.UninitialisedField(self, 'Term', Term1, True)

	@Term.deleter
	def Term(self):
		del self._Term
		self._Term = base_types.UninitialisedField(self, 'Term', Term1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Opr', type=Operation1Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Term', type=Term1, min=0, max=10, mutex_group=None, array=True),
	))