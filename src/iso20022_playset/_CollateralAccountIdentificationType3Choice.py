# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CollateralAccountType1Code
from . import GenericIdentification36

class CollateralAccountIdentificationType3Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_Tp"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification36, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification36, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', CollateralAccountType1Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', CollateralAccountType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification36, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='Tp', type=CollateralAccountType1Code, min=0, max=1, mutex_group=1, array=False),
	))