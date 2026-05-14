# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._GenericIdentification30 import GenericIdentification30
from ._ValidityPeriodType1Code import ValidityPeriodType1Code

class ValidityPeriod1Choice(base_types._BaseFieldType):

	__slots__ = ["_Prtry", "_VldtyPrdCd"]
	@property
	def Prtry(self):
		return self._Prtry

	@Prtry.setter
	def Prtry(self, value):
		self._Prtry = value if type(value) != base_types.auto else self.make_default("Prtry")

	@Prtry.deleter
	def Prtry(self):
		del self._Prtry
		self._Prtry = None

	@property
	def VldtyPrdCd(self):
		return self._VldtyPrdCd

	@VldtyPrdCd.setter
	def VldtyPrdCd(self, value):
		self._VldtyPrdCd = value if type(value) != base_types.auto else self.make_default("VldtyPrdCd")

	@VldtyPrdCd.deleter
	def VldtyPrdCd(self):
		del self._VldtyPrdCd
		self._VldtyPrdCd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prtry', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='VldtyPrdCd', type=ValidityPeriodType1Code, min=0, max=1, mutex_group=1, array=False),
	))