# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max140Text
from . import Max35Text

class ATMCommandIdentification1(base_types._BaseFieldType):

	__slots__ = ["_Orgn", "_Prcr", "_Ref"]
	@property
	def Orgn(self):
		return self._Orgn

	@Orgn.setter
	def Orgn(self, value):
		self._Orgn = value if value is not None else base_types.UninitialisedField(self, 'Orgn', Max35Text, False)

	@Orgn.deleter
	def Orgn(self):
		del self._Orgn
		self._Orgn = base_types.UninitialisedField(self, 'Orgn', Max35Text, False)

	@property
	def Prcr(self):
		return self._Prcr

	@Prcr.setter
	def Prcr(self, value):
		self._Prcr = value if value is not None else base_types.UninitialisedField(self, 'Prcr', Max140Text, False)

	@Prcr.deleter
	def Prcr(self):
		del self._Prcr
		self._Prcr = base_types.UninitialisedField(self, 'Prcr', Max140Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Orgn', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Prcr', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))