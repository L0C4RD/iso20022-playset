# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification81
from . import IndividualPerson30

class IndividualPersonIdentification2Choice(base_types._BaseFieldType):

	__slots__ = ["_IdNb", "_PrsnNm"]
	@property
	def IdNb(self):
		return self._IdNb

	@IdNb.setter
	def IdNb(self, value):
		self._IdNb = value if value is not None else base_types.UninitialisedField(self, 'IdNb', GenericIdentification81, False)

	@IdNb.deleter
	def IdNb(self):
		del self._IdNb
		self._IdNb = base_types.UninitialisedField(self, 'IdNb', GenericIdentification81, False)

	@property
	def PrsnNm(self):
		return self._PrsnNm

	@PrsnNm.setter
	def PrsnNm(self, value):
		self._PrsnNm = value if value is not None else base_types.UninitialisedField(self, 'PrsnNm', IndividualPerson30, False)

	@PrsnNm.deleter
	def PrsnNm(self):
		del self._PrsnNm
		self._PrsnNm = base_types.UninitialisedField(self, 'PrsnNm', IndividualPerson30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='IdNb', type=GenericIdentification81, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrsnNm', type=IndividualPerson30, min=0, max=1, mutex_group=1, array=False),
	))