# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import GenericIdentification30
from . import ValidityPeriodType1Code

class ValidityPeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_VldtyPrdCd"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if value is not None else base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = base_types.UninitialisedField(self, 'Prtry', GenericIdentification30, False)

	@property
	def VldtyPrdCd(self):
		return self._VldtyPrdCd

	@VldtyPrdCd.setter
	def VldtyPrdCd(self, value):
		self._VldtyPrdCd = value if value is not None else base_types.UninitialisedField(self, 'VldtyPrdCd', ValidityPeriodType1Code, False)

	@VldtyPrdCd.deleter
	def VldtyPrdCd(self):
		del self._VldtyPrdCd
		self._VldtyPrdCd = base_types.UninitialisedField(self, 'VldtyPrdCd', ValidityPeriodType1Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VldtyPrdCd', type=ValidityPeriodType1Code, min=0, max=1, mutex_group=1, array=False),
	))